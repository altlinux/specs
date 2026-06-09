%define rname cantor

%def_enable python3
%def_disable luajit
%ifarch %qt6_qtwebengine_arches
%def_enable qtwebengine
%else
%def_disable qtwebengine
%endif

%define cantor_sover 28
%define libcantorlibs libcantorlibs%cantor_sover
%define cantor_config_sover 0
%define libcantor_config libcantor_config%cantor_config_sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Education
Summary: KDE Frontend to Mathematical Software
Url: http://www.kde.org
License: GPL-2.0-or-later or GPL-3.0-only

%if_enabled qtwebengine
Requires: kalgebra
Requires: epstool
%endif
Provides:  kde5-cantor = %EVR
Obsoletes: kde5-cantor < %EVR

Source: %rname-%version.tar
Patch1: alt-lib-so-ver.patch
Patch2: alt-find-luajit.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-svg-devel qt6-declarative-devel qt6-tools-devel qt6-5compat-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: libcln-devel libspectre-devel libdiscount-devel libpoppler-qt6-devel
BuildRequires: libxml2-devel libxslt-devel
%{?_enable_python3:BuildRequires: python3-devel}
%{?_enable_luajit:BuildRequires: liblua5-devel libluajit-devel}
BuildRequires: analitza-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel kf6-kparts-devel kf6-kpty-devel kf6-kservice-devel kf6-ktexteditor-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-syntax-highlighting-devel

%description
Cantor is a front-end to powerful mathematics and statistics packages.
Cantor integrates them into the KDE Platform and provides a nice, worksheet-based, graphical user interface.
It supports environments for KAlgebra, Lua, Maxima, R, Sage, Octave, Python, Scilab, and Qalculate!

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kf6-filesystem
Provides:  kde5-cantor-common = %EVR
Obsoletes: kde5-cantor-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libspectre-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libcantorlibs
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libcantorlibs
%name library

%package -n %libcantor_config
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libcantor_config
%name library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

#LUA_BASE_VER=`echo "%{get_version libluajit-devel}" | sed -E 's|^([[:digit:]]+\.[[:digit:]]).*|\1|'`
#pushd src/backends/lua
#for f in *.{h,cpp} ; do
#    sed -i "s|luajit-2.0/lua.hpp|luajit-${LUA_BASE_VER}/lua.hpp|" $f
#done
#popd

%build
%if_enabled qtwebengine
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #
%endif

%install
%if_enabled qtwebengine
%K6install
%K6install_move data cantor knsrcfiles
mv %buildroot/%_K6xdgmime/cantor{,-kde6}.xml
%find_lang %name --with-kde --all-name
%else
mkdir -p %buildroot
%endif

%files
%if_enabled qtwebengine
%_K6bin/cantor*
%_K6lib/cantor_pythonbackend.so
%_K6plug/kf6/parts/*cantor*.so
%_K6plug/cantor_plugins/
%_K6data/cantor/
%_K6cfg/*.kcfg
%_K6xdgapp/org.kde.cantor.desktop
%_K6icon/*/*/apps/*.*
%_K6data/knsrcfiles/*cantor*.knsrc
%_K6xdgmime/*cantor*.xml
%_datadir/metainfo/*.xml
%endif

%if_enabled qtwebengine
%files common -f %name.lang
%doc LICENSES/*

%files devel
%_K6inc/cantor/
%_K6link/lib*.so
%_libdir/cmake/Cantor/

%files -n %libcantorlibs
%_K6lib/libcantorlibs.so.%cantor_sover
%_K6lib/libcantorlibs.so.*
%files -n %libcantor_config
%_K6lib/libcantor_config.so.%cantor_config_sover
%_K6lib/libcantor_config.so.*
%endif

%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sun Feb 08 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt2
- fix requires

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed May 28 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Feb 24 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Dec 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.11.90-alt1
- beta with KF6

* Fri Nov 08 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Tue Feb 20 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Tue Jan 30 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 23.08.4-alt2
- fix incorrect deletion of menu items (ALT #48950)

* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Mon Nov 27 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt2
- using rpm-macros-qt5-webengine

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Thu Oct 19 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Tue Jun 13 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Thu Jan 19 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Wed Sep 21 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Tue Jul 12 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Mon May 23 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Sat Mar 05 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt2
- build empty package on e2k and ppc64le

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Fri Aug 27 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Fri Jul 09 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Tue May 25 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Tue Mar 23 2021 Egor Ignatov <egori@altlinux.org> 20.12.3-alt2
- fix octave backend

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Wed Mar 10 2021 Egor Ignatov <egori@altlinux.org> 20.12.2-alt2
- Fix octave backend
  + Add epstool dependency to prevent crash on plotting
  + Add patch to use gnuplot graphics toolkit by default

* Wed Feb 17 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Dec 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Thu Oct 15 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Wed Sep 23 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Wed Aug 19 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Fri Mar 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Wed Nov 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.12.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1
- new version
- don't build lua backend

* Thu Apr 13 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2
- fix to build with luajit-2.0

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Sun Apr 03 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.12.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
