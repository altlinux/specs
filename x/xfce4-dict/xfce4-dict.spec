Name: xfce4-dict
Version: 0.6.0
Release: alt3

Summary: Xfce4 Dictionary - A client program to query different dictionaries
License: %gpl2plus
Group: Graphical desktop/XFce
Packager: XFCE Team <xfce@packages.altlinux.org>
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Source: %name-%version.tar

Obsoletes: xfce4-dict-plugin < 0.5.2
Provides: xfce4-dict-plugin

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfcegui4-devel libxfce4util-devel
BuildRequires: intltool

Requires: enchant xdg-utils

%description
This program allows you to search different kinds of dictionary services
for words or phrases and shows you the result.
Currently you can query a "Dict" server(RFC 2229), any online dictionary
service by opening a web browser or search for words using a spell check
program like aspell, ispell or enchant.

xfce4-dict contains a stand-alone application called "xfce4-dict" and a
panel plugin for the Xfce panel.

%prep
%setup

%build
# Fix desktop file path for xfce4-panel >= 4.8
sed -i 's|^desktopdir = \$(datadir)/xfce4/panel-plugins|desktopdir = \$(datadir)/xfce4/panel/plugins|' \
   panel-plugin/Makefile.am

%xfce4reconf
%configure \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_bindir/xfce4-dict
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop
%_desktopdir/*.desktop
%_man1dir/*
%_iconsdir/*/*/*/*

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt3
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt2
- Rebuild with xfce4-panel-4.9.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Updated to 0.6.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.2-alt1
- new version

* Wed May 14 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.0-alt1
- new version

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.1-alt1
- new version

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.2.0-alt1
- First build for Sisyphus.

