%define _unpackaged_files_terminate_build 1

Name: skrooge
Version: 26.4.0
Release: alt1
Summary: A personal finances manager, powered by KDE
License: %gpl2plus
Group: Office
URL: http://skrooge.org/
Packager: Andrey Cherepanov <cas@altlinux.org> 

Source: %name-%version.tar.xz
Source1:%name.po

ExcludeArch: ppc64le armh %ix86

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: grantlee5-devel
BuildRequires: kf6-karchive-devel
BuildRequires: kf6-kauth-devel
BuildRequires: kf6-kbookmarks-devel
BuildRequires: kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kdoctools-devel-static
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifications-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: kf6-kparts-devel
BuildRequires: kf6-krunner-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-ktexttemplate-devel
BuildRequires: kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel
BuildRequires: kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel
BuildRequires: kf6-sonnet-devel
BuildRequires: libofx-devel
#BuildRequires: libqca-qt6-devel
BuildRequires: libsqlite3-devel
BuildRequires: libsqlcipher-devel
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel
%endif

Requires: libgrantlee_templates5
Requires: kf6-kio
Requires: libqt6-core = %_qt6_version

%description
A personal finances manager, powered by KDE.

%prep
%setup
#cp -f %SOURCE1 po/ru/skrooge.po

%build
%K6init no_altplace
%K6build -DSKG_CIPHER=OFF \
         -DQT_MAJOR_VERSION=6 \
         -DKDE_INSTALL_KXMLGUIDIR=%_K6xmlgui \
%ifarch %qt6_qtwebengine_arches
	 -DSKG_WEBENGINE=ON \
%else
	 -DSKG_WEBENGINE=OFF \
%endif
         -DSKG_BUILD_TEST=OFF

%install
%K6install
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS CHANGELOG README.md
%_K6bin/*
%_K6cfg/*
%_K6lib/libskg*
%_qt6_plugindir/sqldrivers/libsk*.so
%_qt6_plugindir/sk*
%_K6xdgmime/*
%_K6xdgapp/*%name.desktop
%_iconsdir/*/*/*/*
%_K6xmlgui/*
%_K6plug/kf6/ktexttemplate/grantlee_skgfilters.so
%_K6notif/%name.notifyrc
%_datadir/%name
%_datadir/knsrcfiles/*.knsrc
%_datadir/metainfo/*.appdata.xml
%_datadir/skrooge_import_backend/*.json
%_datadir/skrooge_source/*.json

%changelog
* Wed Jun 17 2026 Andrey Cherepanov <cas@altlinux.org> 26.4.0-alt1
- New version.

* Wed Feb 04 2026 Ivan A. Melnikov <iv@altlinux.org> 26.1.20-alt2
- Build w/o qt6-webengine on architectures that don't have it
  (fixes build on riscv64).

* Sat Jan 24 2026 Andrey Cherepanov <cas@altlinux.org> 26.1.20-alt1
- New version 26.1.20.

* Wed Oct 22 2025 Andrey Cherepanov <cas@altlinux.org> 25.10.0-alt1
- New version 25.10.0.

* Mon Apr 28 2025 Andrey Cherepanov <cas@altlinux.org> 25.4.0-alt1
- New version 25.4.0.

* Sat Jan 18 2025 Andrey Cherepanov <cas@altlinux.org> 25.1.0-alt1
- New version 25.1.0.
- Build with KF6.
- Build only for x86_64 and aarch64.

* Fri Sep 27 2024 Andrey Cherepanov <cas@altlinux.org> 2.33.0-alt1
- New version 2.33.0.

* Thu Apr 11 2024 Andrey Cherepanov <cas@altlinux.org> 2.32.0-alt1
- New version 2.32.0.

* Fri Oct 13 2023 Andrey Cherepanov <cas@altlinux.org> 2.31.0-alt1
- New version 2.31.0.

* Mon Sep 04 2023 Andrey Cherepanov <cas@altlinux.org> 2.30.0-alt1
- New version 2.30.0.
- Excluded ppc64le.

* Sat Feb 25 2023 Andrey Cherepanov <cas@altlinux.org> 2.29.0-alt1
- new version 2.29.0

* Tue Nov 22 2022 Andrey Cherepanov <cas@altlinux.org> 2.28.0-alt2
- Set strict requirement of libqt5-core version (ALT #43522).

* Thu Aug 04 2022 Andrey Cherepanov <cas@altlinux.org> 2.28.0-alt1
- new version 2.28.0

* Mon Jan 31 2022 Andrey Cherepanov <cas@altlinux.org> 2.27.0-alt1
- new version 2.27.0

* Thu Jul 29 2021 Andrey Cherepanov <cas@altlinux.org> 2.26.1-alt1
- new version 2.26.1

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.25.0-alt1
- new version 2.25.0
- rebuild with rpm-build-python3

* Fri Dec 11 2020 Andrey Cherepanov <cas@altlinux.org> 2.24.6-alt1
- new version 2.24.6

* Fri Jul 24 2020 Andrey Cherepanov <cas@altlinux.org> 2.23.0-alt1
- new version 2.23.0

* Thu May 28 2020 Andrey Cherepanov <cas@altlinux.org> 2.22.1-alt2
- Complete Russian translation (thanks Olesya Gerasimenko).

* Sun Apr 12 2020 Andrey Cherepanov <cas@altlinux.org> 2.22.1-alt1
- new version 2.22.1

* Fri Dec 06 2019 Andrey Cherepanov <cas@altlinux.org> 2.21.1-alt1
- new version 2.21.1

* Thu Jul 04 2019 Andrey Cherepanov <cas@altlinux.org> 2.20.0-alt1
- new version 2.20.0

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 2.19.1-alt1
- new version 2.19.1

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 2.19.0-alt1
- new version 2.19.0

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 2.18.0-alt1
- new version 2.18.0

* Wed Dec 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.17.0-alt1
- new version 2.17.0

* Wed Nov 07 2018 Andrey Cherepanov <cas@altlinux.org> 2.16.2-alt1
- new version 2.16.2

* Sun Aug 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.15.0-alt1
- New version.

* Mon Jul 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.14.0-alt1
- new version 2.14.0

* Fri May 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.13.0-alt1
- new version 2.13.0

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 2.12.0-alt1
- new version 2.12.0

* Fri Feb 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.11.0-alt1
- new version 2.11.0

* Fri Nov 10 2017 Andrey Cherepanov <cas@altlinux.org> 2.10.5-alt1
- new version 2.10.5

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- new version 2.9.0

* Mon Jul 24 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- new version 2.8.1

* Fri Jan 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- new version 2.7.0

* Tue Jan 03 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- new version 2.6.0

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Sun Jul 24 2016 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version is based on KF5
- Build without sqlcipher support

* Mon Aug 03 2015 Andrey Cherepanov <cas@altlinux.org> 1.12.5-alt1
- New version 1.12.5
- Fix watch file for new stable version tarball

* Sun May 10 2015 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- New version 1.12.0

* Fri Nov 14 2014 Andrey Cherepanov <cas@altlinux.org> 1.10.0-alt1
- new version 1.10.0

* Thu May 15 2014 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- New version

* Thu Apr 03 2014 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt2
- Rebuild with new version of grantlee

* Sun Nov 24 2013 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- New version
- Build with libofx-0.9.9

* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- New version 1.7.1

* Tue Jan 22 2013 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version 1.4.0

* Wed Jan 18 2012 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version 1.2.0
- Add watch file

* Fri Sep 23 2011 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- New version 0.9.1

* Tue Mar 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version 0.8.0
- Return to Sisyphus

* Sat Nov 14 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.5.3-alt1
- initial build for Sisyphus
