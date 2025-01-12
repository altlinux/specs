Name: prboom-plus
Version: 2.6.66
Release: alt1

Summary: Doom - classic 3D shoot-em-up game
Group: Games/Arcade
URL: http://prboom-plus.sourceforge.net/
License: GPLv2

Source0: %name-%version.tar.gz

Patch0: gcc14.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake dumb-devel gcc-c++ libSDL2-devel libfluidsynth-devel libmad-devel libpcre-devel

%description
Doom is the classic 3D shoot-em-up game. It must have been one of the best
selling games ever; it totally outclassed any  3D world games that preceded
it, with amazing speed, flexibility, and outstanding gameplay. The specs to
the game were released, and thousands of extra levels were written by fans of
the game; even today new levels are written for Doom faster then any one person
could play them.

%prep
%setup
%patch0 -p0

%build
pushd prboom2
%cmake -DDOOMWADDIR=%{_datadir}/doom
%cmake_build

%install
pushd prboom2
%cmake_install

%files
%_bindir/*
%_datadir/prboom-plus/*
%_man5dir/*
%_man6dir/*
%_docdir/*

%changelog
* Sun Jan 12 2025 Grigory Ustinov <grenka@altlinux.org> 2.6.66-alt1
- Build new version.

* Tue Mar 30 2021 Grigory Ustinov <grenka@altlinux.org> 2.5.1.3-alt2
- Fixed FTBFS with -fcommon.
- Fixed license tag.

* Fri Oct 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1.3-alt1.1
- Rebuilt with libpng15

* Thu Apr 12 2012 Igor Zubkov <icesik@altlinux.org> 2.5.1.3-alt1
- 2.5.0.6 -> 2.5.1.3

* Tue Dec 29 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.6-alt1
- 2.5.0.5 -> 2.5.0.6

* Wed Dec 16 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.5-alt1
- 2.5.0.4 -> 2.5.0.5

* Fri Oct 16 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.4-alt1
- 2.5.0.3 -> 2.5.0.4

* Tue Aug 04 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.3-alt2
- own doc dir

* Fri Jul 31 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.3-alt1
- 2.5.0.1 -> 2.5.0.3

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 2.5.0.1-alt1
- 2.4.8.2 -> 2.5.0.1

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 2.4.8.2-alt1
- 2.4.6.1 -> 2.4.8.2
- buildreq

* Mon Oct 02 2006 Igor Zubkov <icesik@altlinux.org> 2.4.6.1-alt1
- 2.4.3.1 -> 2.4.6.1
- buildreq

* Mon Aug 14 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.3.1-alt1
- Initial build for Sisyphus

* Mon Aug 14 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.5-alt1
- 2.4.4 -> 2.4.5

* Tue Aug 01 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Tue Jul 25 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.3-alt1
- 2.4.3
- remove COPYING (GPL v2) from package

* Mon Jul 17 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.2-alt1
- 2.4.2 

* Mon Apr 10 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.1-alt1
- 2.4.1
- buildreq

* Tue Apr 04 2006 Igor Zubkov <icesik@altlinux.ru> 2.4.0-alt1
- 2.4.0
- buildreq

* Mon Nov 07 2005 Igor Zubkov <icesik@altlinux.ru> 2.2.6-alt1
- Initial build for Sisyphus
