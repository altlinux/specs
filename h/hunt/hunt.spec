%define _unpackaged_files_terminate_build 1

Name: hunt
Version: 2.0.0
Release: alt1

Summary: A highly-opinionated simplified Find command made with Rust
License: MIT
Group: File tools
Url: https://crates.io/crates/hunt
Vcs: https://github.com/LyonSyonII/hunt-rs

Source0: %name-%version.tar
Source1: vendor.tar
Source2: .cargo/config.toml
BuildRequires(pre): rpm-macros-rust
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: /proc

%description
A highly-opinionated simplified Find command made with Rust
By default it searches a file/folder in the working directory and divides
the result between exact matches and ones that only contain the query
Results will be sorted alphabetically

%prep
%setup -a 1

install -D %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name
%doc README.md LICENSE

%changelog
* Fri Aug 25 2023 Vladislav Glinkin <smasher@altlinux.org> 2.0.0-alt1
- Initial build for ALT

