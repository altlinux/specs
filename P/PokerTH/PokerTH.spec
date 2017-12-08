# vim: set ft=spec: -*- rpm-spec -*-

Name: PokerTH
Version: 1.1.2
Release: alt1

Summary: Texas Hold'em poker game
Group: Games/Cards
License: %gagpl3plus
Url: http://www.pokerth.net/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses >= 2.0.5-alt1

BuildRequires: boost-asio-devel boost-filesystem-devel boost-program_options-devel boost-interprocess-devel gcc-c++ libSDL-devel libSDL_mixer-devel libcurl-devel libdb4-devel libgnutls-openssl-devel libgsasl-devel qt5-base-devel

BuildPreReq: libgcrypt-devel zlib-devel libsqlite3-devel phonon-devel tinyxml-devel libircclient-devel libprotobuf-devel
BuildPreReq: protobuf-compiler

Requires: %name-data = %version-%release

%define _unpackaged_files_terminate_build 1

%description
PokerTH is a poker game written in C++/Qt5. You can play the popular
"Texas Hold'em" poker variant against up to nine computer-opponents or
play network games with people all over the world.

%package data
Summary: Data files for %name
Group: Games/Cards
BuildArch: noarch
Requires: %name = %version-%release

%description data
PokerTH is a poker game written in C++/Qt5. You can play the popular
"Texas Hold'em" poker variant against up to nine computer-opponents or
play network games with people all over the world.

This package contents data files for %name.

%prep
%setup
%patch -p1

%build
%add_optflags -fno-strict-aliasing
qmake-qt5 \
	QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" \
	pokerth.pro
%make_build
qmake-qt5 \
	QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" \
	pokerth_game.pro
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_bindir
install -pm755 pokerth bin/pokerth_server %buildroot%_bindir

%files
%_bindir/*

%files data
%_datadir/pokerth
%_desktopdir/pokerth.desktop
%_pixmapsdir/pokerth.png

%changelog
* Fri Dec 08 2017 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt1
- Fix build.
- Drop obsoleted patches.
- Require PokerTH in PokerTH-data subpackage.
- [1.1.2]

* Mon Aug 28 2017 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt4
- Fix build with boost-1.65.0.
- Rebuilt with boost 1.65.0.

* Mon Apr 04 2016 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt3
- Fix build: Patches from Fedora.
- Move data to separate subpackage.

* Tue Jul 14 2015 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt2
- Fix build with Qt-5.5.0.
- Use rpm-build-licenses again.

* Thu Jun 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.1-alt1.1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.1.1-alt1.1
- rebuild with boost 1.57.0

* Tue Jan 14 2014 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1
- [1.1.1]

* Tue Dec 24 2013 Mikhail Efremov <sem@altlinux.org> 1.1-alt1
- Build with Qt5.
- [1.1]

* Wed Nov 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Fixed build

* Mon Apr 08 2013 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- [1.0.1]

* Mon Jan 07 2013 Mikhail Efremov <sem@altlinux.org> 1.0-alt1
- [1.0]

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.3
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.2
- Rebuilt with Boost 1.51.0

* Mon Jul 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.1
- Rebuilt

* Tue Jun 26 2012 Mikhail Efremov <sem@altlinux.org> 0.9.5-alt1
- [0.9.5]

* Fri Apr 27 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1
- [0.9.4]

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.1
- Rebuilt with Boost 1.49.0

* Sat Feb 25 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3-alt1
- [0.9.3]

* Sun Jan 15 2012 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- [0.9.1]

* Sat Jan 07 2012 Mikhail Efremov <sem@altlinux.org> 0.9-alt1
- [0.9]

* Wed Dec 07 2011 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt3
- Rebuild with gnutls26-2.12.14.

* Fri Dec 02 2011 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt2
- Rebuilt with Boost 1.48.0.

* Fri Jul 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.1
- Rebuilt with Boost 1.47.0

* Sat Mar 26 2011 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1
- [0.8.3]

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.1
- Rebuilt with Boost 1.46.1
- Added libgcrypt-devel into BuildPreReq

* Fri Dec 17 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8.1-alt1
- [0.8.1]

* Tue Sep 28 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8-alt1
- [0.8]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.7.1-alt1
- [0.7.1]

* Tue May 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.7-alt1
- Built for Sisyphus

