Name:    guake
Version: 0.8.11
Release: alt1
Summary: guake - a drop-down terminal
Summary(ru.UTF-8):guake — выпадающий эмулятор терминала

License: GPLv2+
Group:   Terminals
URL: 	 http://guake.org/
# VCS:	 https://github.com/Guake/guake.git
Source0: %name-%version.tar

BuildRequires(pre): etersoft-build-utils libGConf-devel rpm-build-gnome python-devel rpm-build-python
BuildRequires:  glibc-devel-static intltool libgtk+2-devel python-devel python-module-pygtk-devel python-module-vte python-modules-encodings GConf
BuildRequires: desktop-file-utils

Requires: GConf
Requires: dbus
Requires: python-module-pygtk-libglade notification-daemon

Patch1: guake-fix-desktop-files.patch
BuildRequires: desktop-file-utils

%description
Guake is a drop-down terminal for Gnome Desktop Environment, so you
just need to press a key to invoke him, and press again to hide.

%prep
%setup -q
%patch1 -p1

%build
%autoreconf
%configure --disable-static --disable-schemas-install
%make_build CXXFLAGS="%{optflags}" CFLAGS="%{optflags}"

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall

rm -f %buildroot%_libdir/guake/*.la %buildroot%_iconsdir/hicolor/icon-theme.cache
install -Dm644 data/guake-autostart.desktop.in %buildroot%gnome_autostartdir/guake.desktop

%find_lang %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
  %gconf2_uninstall %name
fi

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README.rst
%config %_sysconfdir/gconf/schemas/*
%attr(755,root,root) %_bindir/*
%python_sitelibdir_noarch/%name
%_datadir/%name
%_pixmapsdir/guake
%_desktopdir/*.desktop
%_datadir/dbus-1/services/org.guake.Guake.service
%_sysconfdir/gconf/schemas/guake.schemas
%_man1dir/guake.1*
%gnome_autostartdir/guake.desktop
%_iconsdir/hicolor/*/apps/%{name}*.png

%changelog
* Mon Dec 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.8.11-alt1
- New version.

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.8.10-alt1
- New version

* Fri May 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.8.9-alt1
- New version

* Fri Dec 30 2016 Andrey Cherepanov <cas@altlinux.org> 0.8.8-alt1
- new version 0.8.8

* Fri Aug 26 2016 Andrey Cherepanov <cas@altlinux.org> 0.8.7-alt1
- new version 0.8.7

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 0.8.5-alt1
- new version 0.8.5

* Thu Apr 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt1
- New version

* Mon Oct 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.3-alt1
- New version

* Mon Aug 24 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version
- Build from upstream Git repository

* Wed Nov 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt2.1
- Fixed build

* Thu Apr 25 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.4-alt2
- Fix spec

* Thu Feb 07 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.4-alt1
- New version
- Update from fc18

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.qa2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.qa1.1
- Rebuild with Python-2.7

* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.2-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for guake
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Tue Sep 07 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.2-alt2
- Added patch: Ticket #248. The focus would change to the terminal after click on the new tab button.

* Fri Aug 13 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.2-alt1
- 0.4.2.20100801
- Added autostart guake

* Wed May 05 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Tue Jan 26 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 0.4.0-alt0.1
- initial build

