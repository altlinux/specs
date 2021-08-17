Name: PySolFC
Version: 2.12.0
Release: alt2

Summary: A collection of solitare card games

License: GPL-2.0+
Group: Games/Cards
Url: http://pysolfc.sourceforge.net

Source0: http://downloads.sourceforge.net/pysolfc/%name-%version.tar.bz2
Source1: PySol.desktop
Source2: pysol-start-script

Patch2: 06d2fd5b90c29cbfe9b938676cc85c514cbbcca1.patch

Provides: pysol = 5.%version
Requires: PySolFC-Cardsets

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

# we will use kivy
%add_python3_req_skip gtk

# never use jnius
%add_python3_req_skip jnius_never_use

%description
%name is a collection of more than 1000 solitaire card games. It is a fork
of PySol solitare. Its features include modern look and feel (uses Tile widget
set), multiple cardsets and tableau backgrounds, sound, unlimited undo, player
statistics, a hint system, demo games, a solitaire wizard, support for user
written plug-ins, an integrated HTML help browser, and lots of documentation.

%package -n python3-module-PySolFC
Summary: Supplemental python module for %name solitaire game collection
Group: Games/Cards

%description -n python3-module-PySolFC
Supplemental python module for %name solitaire game collection

%prep
%setup
%patch2 -p1
# Set correct python2 executable in shebang
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *)
# force skip jinus if it is installed
subst 's|jnius|jnius_never_use|' pysollib/init.py

%build
%python3_build

%install
%python3_install
#-O1
# install desktop file
rm %buildroot%_desktopdir/*.desktop
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

# install the startup wrapper
mv %buildroot%_bindir/pysol.py %buildroot%_datadir/%name
install -m755 %SOURCE2 %buildroot/%_bindir/pysol

%find_lang pysol

# we will use kivy
rm -rf %buildroot%python3_sitelibdir/pysollib/pysolgtk

%files -f pysol.lang
%doc AUTHORS.md README.md PKG-INFO
%dir %_datadir/%name
%_bindir/pysol
%_datadir/%name/*
#_datadir/pixmaps/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/pysol.png

%files -n python3-module-PySolFC
%python3_sitelibdir/pysollib/*
%python3_sitelibdir/*egg-info

%changelog
* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt2
- NMU: ignore pyjnius (used as sign we are running on Android)
- drop old python2 patches

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt1
- NMU: new version 2.12.0 (with rpmrb script)

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt2
- NMU: build with python3

* Sat May 30 2020 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version
- Fix License tag according to SPDX

* Thu Nov 27 2014 Fr. Br. George <george@altlinux.ru> 2.0-alt2
- Import FC patch

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1
- Rebuild with Python-2.7

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0
- Provide icons, ignore upstream desktop file

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.1
- Rebuilt with python 2.6

* Sat Sep 26 2009 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from FC

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-7
- Rebuild for Python 2.6

* Fri Apr 4 2008 Stewart Adam <s.adam@diffingo.com> 1.1-6
- Fix Source0 URL
- Add egg-info file
- Remove deprecated Encoding key from desktop file

* Sat Jan 19 2008 Stewart Adam <s.adam@diffingo.com> 1.1-5
- Rebuild

* Thu Nov 1 2007 Stewart Adam <s.adam@diffingo.com> 1.1-4
- Provides: pysol since PySolFC is almost a drop-in replacement for
  the now unmaintained pysol

* Mon Oct 22 2007 Stewart Adam <s.adam@diffingo.com> 1.1-3
- s/python-imageing-tk/python-imaging-tk/

* Fri Oct 19 2007 Stewart Adam <s.adam@diffingo.com> 1.1-2
- Add Requires: python-imageing-tk

* Sat Sep 29 2007 Stewart Adam <s.adam@diffingo.com> 1.1-1
- Initial release

