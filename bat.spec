%define name bat
%define version 0.25.0
%define release 1%{?dist}

Summary:  A cat(1) clone with wings.
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  Apache-2.0, MIT licenses found
URL:      https://github.com/sharkdp/bat
Source0:  https://github.com/sharkdp/bat/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: curl
BuildRequires: gcc

%description
A cat(1) clone with syntax highlighting and Git integration..

%prep
%setup -q -n bat-%{version}

%build
# Install Rust using curl
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release --locked

%install
# Create the necessary directory structure in the buildroot
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/usr/share/man/man1

# Copy the binary to /bin in the buildroot
strip target/release/%{name}
install -m 755 target/release/%{name} %{buildroot}/bin/
install -m 755 assets/manual/%{name}.1.in %{buildroot}/usr/share/man/man1/%{name}.1
sed -i 's/{{PROJECT_EXECUTABLE_UPPERCASE}}/BAT/g' %{buildroot}/usr/share/man/man1/%{name}.1
sed -i 's/{{PROJECT_EXECUTABLE}}/bat/g' %{buildroot}/usr/share/man/man1/%{name}.1
gzip %{buildroot}/usr/share/man/man1/%{name}.1

%files
# List all the files to be included in the package
/bin/%{name}
/usr/share/man/man1/%{name}.1.gz

%changelog
* Fri Jan 10 2025 - Danie de Jager - 0.25.0-1
- built using rustc 1.84.0
* Thu Oct 24 2024 Danie de Jager - 0.24.0-5
- built using rustc 1.82.0
* Wed Aug 7 2024 Danie de Jager - 0.24.0-4
- built using rustc 1.80.0
* Wed Jan 31 2024 Danie de Jager - 0.24.0-3
- built using rustc 1.77.2
* Wed Jan 31 2024 Danie de Jager - 0.24.0-2
- Added man document.
* Wed Jan 31 2024 Danie de Jager - 0.24.0-1
- Initial RPM build
