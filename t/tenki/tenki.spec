Name: tenki
Version: 1.11.0
Release: alt1
License: MIT

Summary: tty-clock with weather effect

Group: Shells

Url: https://github.com/ckaznable/tenki
Vcs: https://github.com/ckaznable/tenki.git

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
* Fri Feb 07 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.11.0-alt1
- Initial build
