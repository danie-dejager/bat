%define name bat
%define version 0.24.0
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
cargo build --release

%install
# Create the necessary directory structure in the buildroot
mkdir -p %{buildroot}/bin

# Copy the binary to /bin in the buildroot
strip target/release/%{name}
install -m 755 target/release/%{name} %{buildroot}/bin/

%files
# List all the files to be included in the package
/bin/%{name}

%changelog
* Wed Jan 31 2024 Danie de Jager - 0.24.0-1
- Initial RPM build
