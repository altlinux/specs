%define oname Sunflower
Name:    sunflower
Version: 0.5.63
Release: alt3

Summary: Small and highly customizable twin-panel file manager for Linux with support for plugins
License: GPL-3.0
Group:   Graphical desktop/GNOME
URL:     https://github.com/MeanEYE/Sunflower

Packager: Alexander Burmatov <thatman@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-chardet
BuildRequires: python3-modules-sqlite3
BuildRequires: libgtk+3-gir-devel
BuildRequires: libnotify-gir
BuildRequires: libvte3-gir-devel

BuildArch: noarch

Source:  %name-%version.tar

Patch1:  update-path-for-icon.patch
Patch2:  add-locale.patch

%description
Sunflower is a small and highly customizable twin-panel file manager for Linux
with support for plugins. It is intended to be an easy-to-use and powerful
file manager that seamlessly integrates into the GNOME desktop environment
(but not limited to). Fully compatible and native to Wayland compositors.

%prep
%setup
rm -fr ./translations/be
rm -fr ./translations/ca
rm -fr ./translations/cs_CZ
rm -fr ./translations/de_DE
rm -fr ./translations/eh_AU
rm -fr ./translations/lv
rm -fr ./translations/nl_BE
rm -fr ./translations/pl_PL
rm -fr ./translations/ru_RU
rm -fr ./translations/sv
rm -fr ./translations/tr
rm -fr ./translations/zh_TW
%patch1 -p1
%patch2 -p1

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%oname-%version.dist-info
%_datadir/%name
%_datadir/applications/%oname.desktop

%changelog
* Fri Apr 14 2023 Alexander Burmatov <thatman@altlinux.org> 0.5.63-alt3
- Remove empty translations

* Tue Apr 11 2023 Alexander Burmatov <thatman@altlinux.org> 0.5.63-alt2
- Add translations (tnx respublica@)

* Fri Mar 10 2023 Alexander Burmatov <thatman@altlinux.org> 0.5.63-alt1
- Initial build for Sisyphus
- New file manager (ALT #45433)
