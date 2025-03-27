Name: hyprls
Version: 0.5.2
Release: alt1
License: MIT

Summary: A LSP server for Hyprland config files

Group: System/Configuration/Other

Url: https://github.com/hyprland-community/hyprls

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang

BuildRequires: golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup -a1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor -o hyprls cmd/hyprls/main.go

%install
install -Dpm755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Tue Mar 25 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Thu Jan 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Mon Jan 20 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.4.1-alt1
- new version 0.4.1 (with rpmrb script)

* Thu Nov 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Tue Sep 24 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- Initial build
