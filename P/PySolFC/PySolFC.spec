Name: PySolFC
Version: 2.0
Release: alt1.1
%setup_python_module %name
Summary: A collection of solitare card games
Group: Games/Cards
License: GPLv2+
Url: http://pysolfc.sourceforge.net
Source0: http://downloads.sourceforge.net/pysolfc/%name-%version.tar.bz2
Source1: PySol.desktop
Source2: pysol-start-script
Patch0: pysolfc-setup.py-noglade.patch

Provides: pysol = 5.%version

BuildArch: noarch
Requires: %packagename = %version

%description
%name is a collection of more than 1000 solitaire card games. It is a fork
of PySol solitare. Its features include modern look and feel (uses Tile widget
set), multiple cardsets and tableau backgrounds, sound, unlimited undo, player
statistics, a hint system, demo games, a solitaire wizard, support for user
written plug-ins, an integrated HTML help browser, and lots of documentation.

%package -n %packagename
Summary: Supplemental python module for %name solitaire game collection
Group: Games/Cards
License: GPLv2+

%description -n %packagename
Supplemental python module for %name solitaire game collection

%prep
%setup
%patch0 -p0

%build
%python_build

%install
%python_install
#-O1
# install desktop file
rm %buildroot%_desktopdir/*.desktop
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D data/images/misc/pysol01.png %buildroot%_niconsdir/%name.png
install -D data/images/misc/pysol02.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

# install the startup wrapper
mv %buildroot%_bindir/pysol.py %buildroot%_datadir/%name
install -m755 %SOURCE2 %buildroot/%_bindir/pysol

%find_lang pysol

%files -f pysol.lang
%doc README PKG-INFO COPYING
%dir %_datadir/%name
%dir %python_sitelibdir/pysollib
%exclude %_iconsdir/*.png
%_bindir/pysol
%_datadir/%name/*
%_datadir/pixmaps/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/%name.png

%files -n %packagename
%python_sitelibdir/pysollib/*
%python_sitelibdir/*egg-info

%changelog
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

