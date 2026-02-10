# Spec file for kcollectd package

%define _unpackaged_files_terminate_build 1

Name: kcollectd
Version: 0.12.2
Release: alt1

Summary: collectd graphing frontend for KDE
License: %gpl3plus
Group: Office
Url: https://www.antonioerusso.com/projects/kcollectd/
#URL: https://gitlab.com/aerusso/kcollectd

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

Patch1: %name-0.12.0-alt-desktop_fix.patch
Patch2: %name-0.12.1-alt-fix-build-const-correctness.patch

BuildRequires(pre): rpm-build-licenses rpm-build-xdg


# Automatically added by buildreq on Tue Feb 10 2026
# optimized out: boost-devel boost-devel-headers cmake cmake-modules docbook-dtds docbook-style-xsl gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcolorscheme-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdoctools kf6-kguiaddons-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel libX11-devel libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-printsupport libqt6-qml libqt6-svg libqt6-waylandclient libqt6-widgets libqt6-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base qt6-base-devel qt6-svg-devel sh5 shared-mime-info vulkan-headers xml-common xml-utils xorg-proto-devel
BuildRequires: appstream boost-filesystem-devel extra-cmake-modules fish gtk4-update-icon-cache kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel qt6-declarative-devel librrd-devel libssl-devel


%description
Kcollectd is a graphical KDE frontend  to collectd  that allows
to view RRD files that have been created by collectd. It allows
to easily navigate in the data with the mouse and can be used
as a chart recorder.

%prep
%setup
%patch0 -p1

%patch1
%patch2 -p1

mv -f -- COPYING COPYING.GPL3.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/COPYING) COPYING


%build
%cmake -DRRD_BASEDIR=/var/lib/collectd -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
%find_lang --with-kde %name
mv -f %buildroot/%_desktopdir/net.aerusso.kcollectd.desktop %buildroot%_desktopdir/%name.desktop


%files -f %name.lang
%doc ChangeLog AUTHORS README.md TODO
%doc --no-dereference COPYING

%_bindir/%name
%_man1dir/%{name}*
%_defaultdocdir/HTML/en/%name

%_desktopdir/%name.desktop
%_xdgmimedir/packages/%name.xml

%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/*/mimetypes/*


%changelog
* Sun Feb 08 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.12.2-alt1
- New version
  - Port to Qt6/KF6

* Sun Oct 27 2024 Ivan A. Melnikov <iv@altlinux.org> 0.12.1-alt1.2
- NMU: fix FTBFS

* Mon May 20 2024 Ivan A. Melnikov <iv@altlinux.org> 0.12.1-alt1.1
- NMU: fix building with boost 1.85.0

* Thu Oct 26 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.12.1-alt1
- New version

* Tue Aug 08 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.12.0-alt2
- Fix desktop file

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.12.0-alt1
- New version

* Sat Aug 08 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.11.99-alt1
- New version

* Tue May 19 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.11.0-alt1
- New version
- Build with QT5 (Closes: #37342)
- Switch to the new upstream

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9-alt5.1
- NMU: rebuilt with boost-1.67.0

* Tue Oct 31 2017 Sergey Y. Afonin <asy@altlinux.ru> 0.9-alt5
- Rebuilt with librrd8

* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.9-alt4
- Rebuilt with GCC 6.3

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9-alt2.qa8
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt2.1
- rebuild with boost 1.57.0

* Sun Feb 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.9-alt2
- Rebuilt with Boost 1.53.0

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.5
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.4
- Rebuilt with Boost 1.51.0

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.1
- Rebuilt with Boost 1.47.0

* Sun May 29 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.9-alt1
- Initial build for ALT Linux Sisyphus

