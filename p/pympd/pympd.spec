Name: pympd
Version: 0.08.1
Release: alt1.4.1

Summary: PyGTK frontend for Music Player Daemon.
Summary(ru_RU.UTF8): Графический (PyGtk) клиент для Music Player Daemon (MPD).
License: GPL
Group: Sound
Packager: Alexey Morsov <swi@altlinux.ru>

Url: http://%name.sourceforge.net/
Source: %name-%version.tar.bz2

#BuildArch: noarch

Requires: python-module-pygtk >= 2.6
Requires: python-module-pygnome-extras python-module-pygtk-libglade
Requires: mpd >= 0.11

BuildRequires: python-module-pygtk-devel >= 2.6
BuildRequires: libgtk+2-common-devel, libgtk+2-devel

%add_python_req_skip gnomeosd

%description
Pymp'd is a frontend for mpd in the style of rhythmbox and itunes, written in python, with pygtk. Pymp'd itself is not a music player, just a frontend.

%description -l ru_RU.UTF8
Pymp'd - это графический клиент для Music Player Daemon (MPD), сделанный в стиле Rhythmbox и iTunes.

%prep
%setup -q
%__subst 's/from pympd.modules import trayicon/from egg import trayicon/' src/plugins/trayicon.py

sed -i 's|\(CFLAGS\ \=\)|\1 -g|' src/modules/tray/Makefile

%build
###%make_build 

%install
%make_build PREFIX=%_usr DESTDIR=%buildroot
%python_build_install --prefix=%_usr --record=INSTALLED_FILES \
	--install-lib=%python_sitelibdir --optimize=2


%files -f INSTALLED_FILES
%doc README
%python_sitelibdir/%name/*.pyo
%python_sitelibdir/%name/modules/*.pyo

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.08.1-alt1.4.1
- Rebuild with Python-2.7

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.08.1-alt1.4
- Rebuilt for debuginfo

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.08.1-alt1.3
- Rebuilt with python 2.6

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.08.1-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for pympd

* Tue Feb 26 2008 Alexey Morsov <swi@altlinux.ru> 0.08.1-alt1.2
- add python-module-pygtk-libglade req.

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.08.1-alt1.1
- Rebuilt with python-2.5.

* Fri Jun 15 2007 Alexey Morsov <swi@altlinux.ru> 0.08.1-alt1
- version 0.08.1

* Thu Jan 25 2007 Alexey Morsov <swi@altlinux.ru> 0.07-alt2.1
- change packager
- change BuildArch
- fix build for x86_64
- fix build section (use Makefile for trayicon and adjust PREFIX)
- add patch for trayicon

* Wed Dec 27 2006 Alexey Rusakov <ktirf@altlinux.org> 0.07-alt2
- fixed the build architecture (thanks to damir@ for the guess).

* Sun Dec 24 2006 Alexey Rusakov <ktirf@altlinux.org> 0.07-alt1
- new version 0.07 (with rpmrb script)

* Wed Oct 19 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.05-alt1
- Initial Sisyphus package.

