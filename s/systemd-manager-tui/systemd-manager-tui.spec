Name: systemd-manager-tui
Version: 2.0.2
Release: alt1
License: MIT

Summary: A program for managing systemd services through a TUI 

Group: System/Configuration/Other

Url: https://github.com/matheus-git/systemd-manager-tui
Vcs: https://github.com/matheus-git/systemd-manager-tui.git

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
* Sun Jun 15 2025 Kirill Unitsaev <fiersik@altlinux.org> 2.0.2-alt1
- Initial build
