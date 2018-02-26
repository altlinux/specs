%define _name hicolor

Name: icon-theme-%_name
Version: 0.12
Release: alt1

Summary: hicolor-icon-theme is the default fallback theme used by implementations of the icon theme specification.
License: GPLv2
Group: Graphical desktop/Other
Url: http://icon-theme.freedesktop.org/wiki/HicolorTheme
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://icon-theme.freedesktop.org/releases/hicolor-icon-theme-%version.tar.gz

BuildArch: noarch

%description
This is a set of directories for default fallback icons used by implementations of the icon theme specification.

%prep
%setup -q -n %_name-icon-theme-%version

%build
%configure
%make_build

%install
%makeinstall

touch %buildroot%_datadir/icons/hicolor/icon-theme.cache

%files
%doc README ChangeLog
# Exists in filesystem package
#dir %_datadir/icons/hicolor/16x16
%dir %_datadir/icons/hicolor/16x16/*
%exclude %_datadir/icons/hicolor/16x16/apps
%dir %_datadir/icons/hicolor/22x22
%dir %_datadir/icons/hicolor/22x22/*
%dir %_datadir/icons/hicolor/24x24
%dir %_datadir/icons/hicolor/24x24/*
# Exists in filesystem package
#dir %_datadir/icons/hicolor/32x32
%dir %_datadir/icons/hicolor/32x32/*
%exclude %_datadir/icons/hicolor/32x32/apps
%dir %_datadir/icons/hicolor/36x36
%dir %_datadir/icons/hicolor/36x36/*
# Exists in filesystem package
#dir %_datadir/icons/hicolor/48x48
%dir %_datadir/icons/hicolor/48x48/*
%exclude %_datadir/icons/hicolor/48x48/apps
%dir %_datadir/icons/hicolor/64x64
%dir %_datadir/icons/hicolor/64x64/*
%dir %_datadir/icons/hicolor/72x72
%dir %_datadir/icons/hicolor/72x72/*
%dir %_datadir/icons/hicolor/96x96
%dir %_datadir/icons/hicolor/96x96/*
%dir %_datadir/icons/hicolor/128x128
%dir %_datadir/icons/hicolor/128x128/*
%dir %_datadir/icons/hicolor/192x192
%dir %_datadir/icons/hicolor/192x192/*
%dir %_datadir/icons/hicolor/256x256
%dir %_datadir/icons/hicolor/256x256/*
%dir %_datadir/icons/hicolor/scalable
%dir %_datadir/icons/hicolor/scalable/*
%dir %_datadir/icons/hicolor/index.theme
%_datadir/icons/hicolor/icon-theme.cache

%changelog
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
