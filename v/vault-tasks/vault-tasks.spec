Name: vault-tasks
Version: 0.13.0
Release: alt1
License: MPL-2.0

Summary: TUI Markdown Task Manager

Group: Office

Url: https://github.com/louis-thevenet/vault-tasks
Vcs: https://github.com/louis-thevenet/vault-tasks.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
%summary.
It will parse any Markdown file or vault and display the tasks it contains.

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
* Sat Aug 09 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Sun Jun 15 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.12.0-alt1
- Initial build
