Name: hyprls
Version: 0.13.0
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
* Fri Mar 20 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Jan 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Sat Dec 06 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Fri Oct 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Wed May 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sat May 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

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
