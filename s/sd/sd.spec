%define _unpackaged_files_terminate_build 1

Name: sd
Version: 0.7.6
Release: alt1

Summary: sd is an intuitive find & replace CLI
License: MIT
Group: Text tools
Url: https://crates.io/crates/sd
Vcs: https://github.com/chmln/sd

Source0: %name-%version.tar
Source1: vendor.tar
Source2: .cargo/config.toml

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: rust

%description
sd is an intuitive find & replace CLI

%prep
%setup -a 1

install -D %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Sat Oct 21 2023 Vladislav Glinkin <smasher@altlinux.org> 0.7.6-alt1
- Initial build for ALT

