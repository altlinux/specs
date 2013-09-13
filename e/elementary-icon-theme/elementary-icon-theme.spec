Name: elementary-icon-theme
Version: 3.2
Release: alt1

Summary: simple and appealing Tango-styled icon theme
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/elementaryicons

Source0: elementaryicons.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

#Build-Depends: debhelper (>= 7.0.50~),
#               icon-naming-utils

#Depends: ${misc:Depends},
#         gnome-icon-theme-full,
#         hicolor-icon-theme
#Suggests: notify-osd-icons-elementary

%description
The official elementary icons are designed to be simple and appealing.

These icons are the inspiration behind Ubuntu's default Humanity icon
theme.

%prep
%setup -q -n elementaryicons

%build

%install
mkdir -p %buildroot%_datadir/icons/elementary/
cp -pr * %buildroot%_datadir/icons/elementary/

%files
%doc AUTHORS CONTRIBUTORS
%_datadir/icons/elementary
%exclude %_datadir/icons/elementary/AUTHORS
%exclude %_datadir/icons/elementary/CONTRIBUTORS
%exclude %_datadir/icons/elementary/COPYING

%changelog
* Fri Sep 13 2013 Igor Zubkov <icesik@altlinux.org> 3.2-alt1
- 3.1 -> 3.2 (bzr -r1136)

* Mon Sep 09 2013 Igor Zubkov <icesik@altlinux.org> 3.1-alt1
- build for Sisyphus


