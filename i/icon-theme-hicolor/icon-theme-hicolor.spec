%define _name hicolor
%def_disable check

Name: icon-theme-%_name
Version: 0.18
Release: alt1

Summary: hicolor-icon-theme is the default fallback theme used by implementations of the icon theme specification.
License: GPL-2.0
Group: Graphical desktop/Other
Url: https://www.freedesktop.org/wiki/Software/icon-theme/

Vcs: https://gitlab.freedesktop.org/xdg/default-icon-theme.git

Source: https://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%version.tar.xz

BuildArch: noarch

Provides: hicolor-icon-theme

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
#  https://github.com/openSUSE/daps
%{?_enable_check:BuildRequires: daps}

%description
This is a set of directories for default fallback icons used by
implementations of the icon theme specification.

%prep
%setup -n %_name-icon-theme-%version

%build
%meson
%meson_build

%install
%meson_install

touch %buildroot%_datadir/icons/hicolor/icon-theme.cache

%check
# validate specifications in spec/
python3 validate.py

%files
%doc README* NEWS
# Exists in filesystem package
#dir %_datadir/icons/hicolor/16x16
%dir %_datadir/icons/hicolor/16x16/*
%exclude %_datadir/icons/hicolor/16x16/apps
%dir %_datadir/icons/hicolor/16x16@2
%dir %_datadir/icons/hicolor/16x16@2/*
%dir %_datadir/icons/hicolor/22x22
%dir %_datadir/icons/hicolor/22x22/*
%dir %_datadir/icons/hicolor/22x22@2
%dir %_datadir/icons/hicolor/22x22@2/*
%dir %_datadir/icons/hicolor/24x24
%dir %_datadir/icons/hicolor/24x24/*
%dir %_datadir/icons/hicolor/24x24@2
%dir %_datadir/icons/hicolor/24x24@2/*
# Exists in filesystem package
#dir %_datadir/icons/hicolor/32x32
%dir %_datadir/icons/hicolor/32x32/*
%exclude %_datadir/icons/hicolor/32x32/apps
%dir %_datadir/icons/hicolor/32x32@2
%dir %_datadir/icons/hicolor/32x32@2/*
%dir %_datadir/icons/hicolor/36x36
%dir %_datadir/icons/hicolor/36x36/*
%dir %_datadir/icons/hicolor/36x36@2
%dir %_datadir/icons/hicolor/36x36@2/*
# Exists in filesystem package
#dir %_datadir/icons/hicolor/48x48
%dir %_datadir/icons/hicolor/48x48/*
%exclude %_datadir/icons/hicolor/48x48/apps
%dir %_datadir/icons/hicolor/48x48@2
%dir %_datadir/icons/hicolor/48x48@2/*
%dir %_datadir/icons/hicolor/64x64
%dir %_datadir/icons/hicolor/64x64/*
%dir %_datadir/icons/hicolor/64x64@2
%dir %_datadir/icons/hicolor/64x64@2/*
%dir %_datadir/icons/hicolor/72x72
%dir %_datadir/icons/hicolor/72x72/*
%dir %_datadir/icons/hicolor/72x72@2
%dir %_datadir/icons/hicolor/72x72@2/*
%dir %_datadir/icons/hicolor/96x96
%dir %_datadir/icons/hicolor/96x96/*
%dir %_datadir/icons/hicolor/96x96@2
%dir %_datadir/icons/hicolor/96x96@2/*
%dir %_datadir/icons/hicolor/128x128
%dir %_datadir/icons/hicolor/128x128/*
%dir %_datadir/icons/hicolor/128x128@2
%dir %_datadir/icons/hicolor/128x128@2/*
%dir %_datadir/icons/hicolor/192x192
%dir %_datadir/icons/hicolor/192x192/*
%dir %_datadir/icons/hicolor/192x192@2
%dir %_datadir/icons/hicolor/192x192@2/*
%dir %_datadir/icons/hicolor/256x256
%dir %_datadir/icons/hicolor/256x256/*
%dir %_datadir/icons/hicolor/256x256@2
%dir %_datadir/icons/hicolor/256x256@2/*
%dir %_datadir/icons/hicolor/512x512
%dir %_datadir/icons/hicolor/512x512/*
%dir %_datadir/icons/hicolor/512x512@2
%dir %_datadir/icons/hicolor/512x512@2/*
%dir %_datadir/icons/hicolor/scalable
%dir %_datadir/icons/hicolor/scalable/*
%dir %_datadir/icons/hicolor/symbolic
%dir %_datadir/icons/hicolor/symbolic/*
%dir %_datadir/icons/hicolor/index.theme
%_datadir/icons/hicolor/icon-theme.cache
%_datadir/pkgconfig/default-icon-theme.pc

%changelog
* Mon May 27 2024 Yuri N. Sedunov <aris@altlinux.org> 0.18-alt1
- 0.18

* Mon Mar 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt2
- provides hicolor-icon-theme (ALT #38261)

* Mon Sep 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- 0.17

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Sun Dec 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt1
- 0.14

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.13-alt1
- 0.13

* Fri Mar 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- new version (0.12)

* Fri Apr 17 2009 Yuri N. Sedunov <aris@altlinux.org> 0.10-alt3
- empty icon-theme.cache added to %%files

* Tue Oct 16 2007 Alexey Rusakov <ktirf@altlinux.org> 0.10-alt2
- moving some directories to filesystem package (see ALT Bug #11302 for
  details).

* Wed Jan 24 2007 Alexey Rusakov <ktirf@altlinux.org> 0.10-alt1
- new version (0.10)

* Mon Oct 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.9-alt1
- new version (0.9)

* Thu Apr 15 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt1
- new version
- fix %%group %%license

* Thu Feb 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- First build for Sisyphus.
