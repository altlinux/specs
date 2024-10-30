%define _unpackaged_files_terminate_build 1

Name: gitu
Version: 0.26.0
Release: alt1

Summary: A terminal user interface for Git
License: MIT
Group: Development/Tools
Url: https://crates.io/crates/gitu
Vcs: https://github.com/altsem/gitu

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo

%description
%summary. Inspired by Magit, and launched straight from the terminal.

%prep
%setup -a 1
install -D %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%doc README.md CHANGELOG.md
%_bindir/%name

%changelog
* Wed Oct 30 2024 Vladislav Glinkin <smasher@altlinux.org> 0.26.0-alt1
- Initial build for ALT

