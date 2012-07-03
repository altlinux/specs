Name: ski
Version: 6.7
Release: alt1.1
Url: http://www.catb.org/~esr/ski/
Source0: %name-%version.tar.gz
License: GPL
Group: Games/Arcade
Summary: a hotdogging game, evade the deadly Yeti on your jet-powered skis
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

%description
Imagine you are skiing down an infinite slope, facing such hazards as
trees, ice, bare ground, and the man-eating Yeti!  Unfortunately,
you have put your jet-powered skis on backwards, so you can't see
ahead where you are going; only behind where you have been.  However,
you can turn to either side, jump or hop through the air, teleport
through hyperspace, launch nuclear ICBMs, and cast spells to call the
Fire Demon.  And since the hazards occur in patches, you can
skillfully outmaneuver them.  A fun and very silly game that proves
you don't need fancy graphical user interfaces to have a good time.

%prep
%setup

%build
make %name.6

%install
mkdir -p %buildroot%_gamesbindir %buildroot%_man6dir/
install -m755 %name %buildroot%_gamesbindir/%name.py
ln -s %name.py %buildroot%_gamesbindir/%name
install %name.6 %buildroot%_man6dir/

%files
%doc README COPYING

%_man6dir/%name.6*
%_gamesbindir/%name.py
%_gamesbindir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 6.7-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 6.7-alt1
- Autobuild version bump to 6.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5-alt1.2
- Rebuilt with python 2.6

* Sun Feb 10 2008 Grigory Batalov <bga@altlinux.ru> 6.5-alt1.1
- Rebuilt with python-2.5.

* Thu Dec 06 2007 Fr. Br. George <george@altlinux.ru> 6.5-alt1
- Initial build for ALT

* Mon Jan 12 2004 Eric S. Raymond <esr@snark.thyrsus.com> 6.5-1
- 6.4 introduced a bug into the ? and ! commands, now fixed.

* Sun Jan 11 2004 Eric S. Raymond <esr@snark.thyrsus.com> 6.4-1
- Game commands now accept numeric repeat prefixes.

* Sat Jan  3 2004 Eric S. Raymond <esr@snark.thyrsus.com> 6.3-1
- Fix bug introduced to teleport command in 6.2.

* Tue Dec 31 2003 Eric S. Raymond <esr@snark.thyrsus.com> 6.2
- Emit reset on keyboard interrupt, just in case user bails out in the
  middle af a row refresh.  Fix bug in ! command interpretation.
  Terrain key is now colorized.

* Tue Dec 30 2003 Eric S. Raymond <esr@snark.thyrsus.com> 6.1
- Python reimplementation of the original C game.

