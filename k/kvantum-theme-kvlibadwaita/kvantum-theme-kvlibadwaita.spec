%define theme KvLibadwaita
%define themename kvlibadwaita

Name: kvantum-theme-%themename
Version: 20260223
Release: alt1
License: GPL-3.0

Summary: Libadwaita style theme for Kvantum

Group: Graphical desktop/Other

Url: https://github.com/fiersik/KvLibadwaita
Vcs: https://github.com/fiersik/KvLibadwaita.git

BuildArch: noarch
Source: %name-%version.tar

Requires: Kvantum

%description
%summary. Based on Colloid-kde.

%prep
%setup
subst "s|LibadwaitaLight|KvLibadwaita|" "src/Colors/Libadwaita Light.colors"
subst "s|LibadwaitaDark|KvLibadwaitaDark|" "src/Colors/Libadwaita Dark.colors"

%install
mkdir -p %buildroot%_datadir/Kvantum/
mkdir -p %buildroot%_datadir/color-schemes/

cp -r src/%theme %buildroot%_datadir/Kvantum/
cp "src/Colors/Libadwaita Light.colors" %buildroot%_datadir/color-schemes/KvLibadwaita.colors
cp "src/Colors/Libadwaita Dark.colors" %buildroot%_datadir/color-schemes/KvLibadwaitaDark.colors

%files
%doc README.md LICENSE
%_datadir/Kvantum/%theme
%_datadir/color-schemes/*

%changelog
* Mon Feb 23 2026 Kirill Unitsaev <fiersik@altlinux.org> 20260223-alt1
- new version 20260223 (with rpmrb script)

* Sat Aug 09 2025 Kirill Unitsaev <fiersik@altlinux.org> 20250809-alt1
- new version 20250809 (with rpmrb script)
- changed upstream url
- spec: add vcs

* Sat Aug 03 2024 Kirill Unitsaev <fiersik@altlinux.org> 20240316-alt1
- Initial build
