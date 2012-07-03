# vim: set ft=spec: -*- rpm-spec -*-

Name: PokerTH
Version: 0.9.5
Release: alt1.1

Summary: Texas Hold'em poker game
Group: Games/Cards
License: AGPLv3+
Url: http://www.pokerth.net/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

#BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue May 26 2009
BuildRequires: boost-asio-devel boost-filesystem-devel boost-program_options-devel boost-interprocess-devel gcc-c++ libSDL-devel libSDL_mixer-devel libcurl-devel libdb4-devel libgnutls-openssl-devel libgsasl-devel libqt4-devel

BuildPreReq: libgcrypt-devel zlib-devel libsqlite3-devel phonon-devel tinyxml-devel libircclient-devel

%description
PokerTH is a poker game written in C++/QT4. You can play the popular
"Texas Hold'em" poker variant against up to nine computer-opponents or
play network games with people all over the world.

%prep
%setup
%patch -p1

%build
qmake-qt4 \
	QMAKE_CFLAGS_RELEASE="%optflags -DBOOST_FILESYSTEM_VERSION=2" \
	QMAKE_CXXFLAGS_RELEASE="%optflags -DBOOST_FILESYSTEM_VERSION=2" \
	pokerth.pro
%make_build Makefile.pokerth_{lib,game,server}
sed -i 's|-pipe |%optflags -fno-strict-aliasing |g' Makefile*
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_bindir
install -pm755 pokerth bin/pokerth_server %buildroot%_bindir

%files
%_bindir/*
%_datadir/pokerth
%_desktopdir/pokerth.desktop
%_pixmapsdir/pokerth.png

%changelog
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

