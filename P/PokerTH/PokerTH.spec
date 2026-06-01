# vim: set ft=spec: -*- rpm-spec -*-

Name: PokerTH
Version: 2.0.7
Release: alt1

Summary: Texas Hold'em poker game
Group: Games/Cards
License: AGPL-3.0+
Url: http://www.pokerth.net/
Vcs: https://github.com/pokerth/pokerth

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: use_bundled_websocketpp.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: ninja-build
BuildRequires: boost-asio-devel boost-filesystem-devel boost-program_options-devel boost-interprocess-devel gcc-c++ libgnutls-openssl-devel
%if %{defined _priority_distbranch} %{?_priority_distbranch:&& "%_priority_distbranch" != "p10" && "%_priority_distbranch" != "p11"}
BuildRequires: websocketpp-devel
%endif
BuildRequires: qt6-base-devel qt6-websockets-devel qt6-svg-devel qt6-tools-devel qt6-multimedia-devel qt6-declarative-devel

BuildRequires: zlib-devel libprotobuf-devel
BuildRequires: protobuf-compiler

Requires: %name-data = %version-%release

%define _unpackaged_files_terminate_build 1

%description
PokerTH is a poker game written in C++/Qt5. You can play the popular
"Texas Hold'em" poker variant against up to nine computer-opponents or
play network games with people all over the world.

%package data
Summary: Data files for %name
Group: Games/Cards
License: ALT-Public-Domain and GPLv2+
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
# Use bundled websocketpp on branches <= p11:
# compilation with system websocketpp is broken there.
%if %{undefined _priority_distbranch} || "%{?_priority_distbranch}" == "p10" || "%{?_priority_distbranch}" == "p11"
%patch1 -p1
%endif

%if %{defined _priority_distbranch} %{?_priority_distbranch:&& "%_priority_distbranch" != "p10" && "%_priority_distbranch" != "p11"}
# be shure that bundled websocketpp is not used
rm -r src/third_party/websocketpp/
%endif

%build
%add_optflags -fno-strict-aliasing
%cmake -DCMAKE_BUILD_TYPE:STRING=Release -G Ninja
%cmake_build --config Release --target all

# Fix QT paths in desktop files
QT_PLUGIN_PATH="$(qmake-qt6 -query QT_INSTALL_PLUGINS 2>/dev/null)"
[ -n "$QT_PLUGIN_PATH" ] || exit 1
sed -ri "s|QT_PLUGIN_PATH=[^[:blank:]]+|QT_PLUGIN_PATH=$QT_PLUGIN_PATH|" pokerth.desktop
QML_IMPORT_PATH="$(qmake-qt6 -query QT_INSTALL_QML 2>/dev/null)"
[ -n "$QML_IMPORT_PATH" ] || exit 1
sed -ri -e "s|QT_PLUGIN_PATH=[^[:blank:]]+|QT_PLUGIN_PATH=$QT_PLUGIN_PATH|" \
        -e "s|QML_IMPORT_PATH=[^[:blank:]]+|QML_IMPORT_PATH=$QML_IMPORT_PATH|" pokerth_qml.desktop

%install
%cmake_install

# remove bundled font (see ALT 25328)
rm %buildroot%_datadir/pokerth/data/fonts/DejaVuSans-Bold.ttf

%files
%_bindir/*

%files data
%_datadir/pokerth
%_desktopdir/pokerth.desktop
%_pixmapsdir/pokerth.png

%changelog
* Mon Jun 01 2026 Mikhail Efremov <sem@altlinux.org> 2.0.7-alt1
- Updated to 2.0.7.

* Tue Mar 10 2026 Mikhail Efremov <sem@altlinux.org> 2.0.6-alt1
- Handling the case when _priority_distbranch is not defined.
- Updated to 2.0.6.

* Wed Feb 25 2026 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt1
- Used bundled websocketpp on branches <= p11.
- Updated to 2.0.4.

* Thu Feb 19 2026 Mikhail Efremov <sem@altlinux.org> 2.0-alt1
- Updated to 2.0.

* Mon May 13 2024 Ivan A. Melnikov <iv@altlinux.org> 1.1.2-alt8
- NMU: fix FTBFS with new boost.

* Wed Jun 30 2021 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt7
- Fixed data package License tag.
- Don't use rpm-build-licenses.
- Cleanup BR.

* Thu Jun 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt6
- Rebuilt with boost-1.73.0.

* Mon Nov 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt5
- Rebuilt with boost-1.71.0.

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt4
- Remove bundled font (Closes: #25328).

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.2-alt3.1
- NMU: rebuilt with boost-1.67.0

* Wed May 23 2018 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt3
- Regenerate protobuf files with current protobuf.
- Fix enum entry name.

* Mon Mar 12 2018 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt2
- Fix build with boost 1.66.

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

