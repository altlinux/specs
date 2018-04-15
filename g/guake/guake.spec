Name:    guake
Version: 3.2.0
Release: alt1
Summary: guake - a drop-down terminal
Summary(ru.UTF-8):guake — выпадающий эмулятор терминала

License: GPLv2+
Group:   Terminals
URL: 	 http://guake.org/
# VCS:	 https://github.com/Guake/guake.git
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: rpm-build-gir
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: libgio
BuildRequires: desktop-file-utils

Requires: dconf
Requires: dbus
Requires: notification-daemon

Patch1: guake-alt-fix-ru-l10n.patch
Patch2: guake-alt-fix-sitelibdir-path.patch
Patch3: guake-alt-add-glade-l10n.patch

BuildRequires: desktop-file-utils

%description
Guake is a drop-down terminal for Gnome Desktop Environment, so you
just need to press a key to invoke him, and press again to hide.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export PBR_VERSION="%version"
%make_build

%install
export PBR_VERSION="%version"
%makeinstall_std prefix=%_prefix
install -Dm0644 guake/data/autostart-guake.desktop %buildroot%_sysconfdir/xdg/autostart/guake.desktop

# Remove compiled gscheme
rm -f %buildroot%_datadir/glib-2.0/schemas/gschemas.compiled

%find_lang %name

%files -f %name.lang
%doc COPYING NEWS.rst README.rst
%attr(755,root,root) %_bindir/%name
%_sysconfdir/xdg/autostart/guake.desktop
%_datadir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/Guake*.egg-info
%_pixmapsdir/%name.png
%_desktopdir/*.desktop
%_datadir/glib-2.0/schemas/org.guake.gschema.xml

%changelog
* Sun Apr 15 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version.

* Thu Apr 12 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Tue Mar 27 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- New version.

* Thu Mar 22 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version.

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Tue Jan 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.12-alt1
- New version.

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

