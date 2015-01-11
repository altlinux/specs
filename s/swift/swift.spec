Name: swift
Version: 2.0
Release: alt1.1
Summary: Swift, new friendly chat client.
License: GPLv3, BSD-simplified
Group: Networking/Instant messaging
Url: http://swift.im/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: boost-asio-devel boost-devel-headers boost-filesystem-devel boost-program_options-devel boost-signals-devel gcc-c++ libexpat-devel scons libqt4-devel zlib-devel libidn-devel libavahi-devel liblua5-devel

%description
Swift is trying to plug a hole in the XMPP client landscape, and has these aims.
- Wide platform availability.
- Doing the "Right Thing" for the user, without configuration.
- Doing the "Right Thing" with standards-compliance.
- Targeting the end-users, not the system administrators.
- Being an XMPP client - not multi-protocol.
- Concentrating on the most frequently performed tasks.
- Never interrupt the user with something that doesn't need attention.

%description -l ru_RU.UTF-8
Клиент мнгновенных сообщений "Swift"
- Расчитан для конечного пользователя.
- С лёгкой настрокой.
- Корректной поддержкой стандартов XMPP.
- Клиент, только для сетей работающих по протоколу XMPP.

%prep
%setup
%patch -p1

%install
scons allow_warnings=1 optimize=1 qt=%_qt4dir SWIFT_INSTALLDIR=%buildroot%_prefix %buildroot%_prefix

%files
%_bindir/swift-im
%_bindir/swift-open-uri
%_desktopdir/swift.desktop
%_datadir/%name/*
%_iconsdir/hicolor/128x128/apps/swift.png
%_iconsdir/hicolor/64x64/apps/swift.png
%_iconsdir/hicolor/24x24/apps/swift.png
%_iconsdir/hicolor/22x22/apps/swift.png
%_iconsdir/hicolor/scalable/apps/swift.svg
%_miconsdir/swift.png
%_niconsdir/swift.xpm

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2.0-alt1.1
- build with boost 1.57.0
  + fix includes to accomodate to changes in Boost.Optional

* Wed Apr 17 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.0-alt1
- New version

* Sat Dec 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git8c01212.1
- Rebuilt with Boost 1.52.0

* Mon Apr 30 2012 Mikhail Pluzhnikov <amike@altlinux.ru> 1.0-alt1.git8c01212
- New version from GIT
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt0.1.2
- Rebuilt with Boost 1.48.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt0.1.1
- Rebuilt with Boost 1.47.0

* Tue Apr  5  2011 Mikhail Pluzhnikov <amike@altlinux.ru> 1.0-alt0.1
- Initial build

