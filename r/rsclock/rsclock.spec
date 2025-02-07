Name: rsclock
Version: 0.1.11
Release: alt1
License: MIT

Summary: A simple terminal clock written in Rust

Group: Shells

Url: https://github.com/valebes/rsClock
Vcs: https://github.com/valebes/rsClock.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Fri Feb 07 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.11-alt1
- Initial build