%define _unpackaged_files_terminate_build 1
%def_without docs

%define sover 5
%define sover_compose 0
%define sover_qt 3
%define libappstream libappstream%sover
%define libappstream_compose libappstream-compose%sover_compose
%define libappstreamqt5 libappstreamqt5_%sover_qt
%define libappstreamqt6 libappstreamqt6_%sover_qt

Name:    appstream
Version: 1.0.2
Release: alt1.1

Summary: Utilities to generate, maintain and access the AppStream Xapian database
# library; LGPLv2+, tools: GPLv2+
License: GPL-2.0+ and LGPL-2.0+
Group:   System/Configuration/Packaging

Url:     http://www.freedesktop.org/wiki/Distributions/AppStream/
# VCS:   https://github.com/ximion/appstream
Source:  appstream-%version.tar
Patch1: alt-qt5.patch

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: ctest
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: gperf
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: libcurl-devel
BuildRequires: liblmdb-devel
BuildRequires: libprotobuf-lite-devel
BuildRequires: libstemmer-devel
BuildRequires: libxapian-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: ninja-build
BuildRequires: protobuf-compiler
%if_with docs
BuildRequires: daps
%endif
BuildRequires: qt6-base-devel qt6-tools
BuildRequires: qt5-base-devel qt5-tools
BuildRequires: xmlto
BuildRequires: gtk-doc
BuildRequires: libsoup-devel
BuildRequires: /proc
BuildRequires: libxmlb-devel
BuildRequires: libsystemd-devel
BuildRequires: libcairo-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libgdk-pixbuf-gir-devel
BuildRequires: libpango-devel
BuildRequires: librsvg-devel
BuildRequires: libzstd-devel
BuildRequires: gi-docgen

#Requires: appstream-data

%description
AppStream-Core makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%package compose
Summary: Executable for generating AppStream data
Group:   System/Configuration/Packaging

%description compose
%summary.

%package -n %libappstream_compose
Summary: Library for generating AppStream data
Group: System/Libraries
Provides: libappstream-compose = %EVR
Obsoletes: libappstream-compose < %EVR
%description -n %libappstream_compose
%summary.

%package -n libappstream-compose-gir
Summary: GObject introspection for libappstream-compose
Group: System/Libraries
Conflicts: libappstream-compose < %version-%release
Requires: %libappstream_compose

%description -n libappstream-compose-gir
%summary.

%package -n libappstream-gir
Summary: GObject introspection for libappstream
Group: System/Libraries
Conflicts: libappstream < %version-%release
Requires: %libappstream

%description -n libappstream-gir
%summary.

%package -n libappstream-compose-devel
Summary: Development files for %name
Group: Development/C
Requires: libappstream-compose-gir

%description -n libappstream-compose-devel
%summary.

%package -n %libappstream
Summary: Library to access AppStream services
Group: System/Libraries

%description -n %libappstream
%summary.

%package -n libappstream-devel
Summary: Development files for %name
Group: Development/C
Requires: %name
Requires: libappstream-gir
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n libappstream-devel
%summary.

%package -n %libappstreamqt5
Summary: Qt bindings for %name
Group: System/Libraries
Requires: %name
Provides: %name-qt = %EVR
Obsoletes: %name-qt < %EVR

%description -n %libappstreamqt5
%summary.

%package -n %libappstreamqt6
Summary: Qt bindings for %name
Group: System/Libraries
Requires: %name

%description -n %libappstreamqt6
%summary.

%package -n libappstream-qt-devel
Summary: Development files for %name-qt bindings
Group: Development/KDE and QT
Provides: %name-qt-devel = %EVR
Obsoletes: %name-qt-devel < %EVR

%description -n libappstream-qt-devel
%summary.

%package -n libappstream-qt6-devel
Summary: Development files for %name-qt bindings
Group: Development/KDE and QT

%description -n libappstream-qt6-devel
%summary.

%package doc
Summary: Documenation for development using %name
Group: Development/Documentation
BuildArch: noarch

%description doc
%summary.

%prep
%setup
%patch1 -p1 -b .qt
%ifarch %e2k
# workaround for EDG frontend
sed -i "s|g_autofree gchar \*\*|g_autofree_edg(gchar*)|" qt/pool.cpp
sed -i "s|g_autofree gchar \*|g_autofree_edg(gchar)|" qt/spdx.cpp
sed -i "s/-Werror=shadow/-Wno-error=shadow/" meson.build
%endif
# prepare qt5 build
cp -ar qt/cmake/AppStreamQt{,6}Config.cmake.in
cp -ar qt/cmake/AppStreamQt{,6}ConfigVersion.cmake.in
cat qt/cmake/AppStreamQt5Config.cmake.in >qt/cmake/AppStreamQtConfig.cmake.in
cat qt/cmake/AppStreamQt5ConfigVersion.cmake.in >qt/cmake/AppStreamQtConfigVersion.cmake.in
sed -i 's|libAppStreamQt|libAppStreamQt6|g' qt/cmake/AppStreamQt6Config.cmake.in
cp -ar qt qt5
sed -i 's|qt-versions|qt-versions5|' qt5/meson.build

%build
%meson -Dqt=true \
%if_with docs
	-Ddocs=true \
%else
	-Ddocs=false \
%endif
	-Dstemming=true \
	-Dcompose=true
%ifarch %e2k
export LD_LIBRARY_PATH=$(pwd)/%__builddir/src
%endif
%meson_build

%install
%meson_install
mkdir -p %buildroot%_datadir/app-info/{icons,xmls}
mkdir -p %buildroot/var/cache/app-info/{icons,xapian,xmls}
touch %buildroot/var/cache/app-info/cache.watch
rm -f %buildroot%_datadir/installed-tests/appstream/metainfo-validate.test

pushd %buildroot/%_libdir/cmake/
cp -ar AppStreamQt5 AppStreamQt
mv AppStreamQt/AppStreamQt{5,}Config.cmake
mv AppStreamQt/AppStreamQt{5,}ConfigVersion.cmake
sed -i 's|AppStreamQt5|AppStreamQt|g' AppStreamQt/AppStreamQtConfig.cmake
sed -i 's|AppStreamQt|AppStreamQt5|g' AppStreamQt/AppStreamQtConfig.cmake
popd
cp -ar %buildroot/%_includedir/AppStreamQt5 %buildroot/%_includedir/AppStreamQt
ln -s libAppStreamQt5.so %buildroot/%_libdir/libAppStreamQt.so

%find_lang %name

%check
#%%meson_test

%files -f appstream.lang
%doc AUTHORS MAINTAINERS NEWS README.md RELEASE
%config(noreplace) %_datadir/appstream/appstream.conf
%_bindir/appstreamcli
%dir %_datadir/app-info/
%dir %_datadir/app-info/icons
%dir %_datadir/app-info/xmls
%ghost %_cachedir/app-info/cache.watch
%dir %_cachedir/app-info
%dir %_cachedir/app-info/icons
%dir %_cachedir/app-info/xapian
%dir %_cachedir/app-info/xmls
%_man1dir/appstreamcli.1.*
%_datadir/gettext/its/metainfo.*
%_datadir/metainfo/org.freedesktop.appstream.cli.*.xml

%files -n %libappstream
%_libdir/libappstream.so.*
%_libdir/libappstream.so.%sover

%files -n libappstream-gir
%_libdir/girepository-1.0/AppStream-1.0.typelib

%files -n libappstream-devel
%_includedir/appstream/
%_libdir/libappstream.so
%_libdir/pkgconfig/appstream.pc
%_datadir/gir-1.0/AppStream-1.0.gir

%files -n %libappstreamqt5
%_libdir/libAppStreamQt5.so.*
%_libdir/libAppStreamQt5.so.%sover_qt
%files -n %libappstreamqt6
%_libdir/libAppStreamQt6.so.*
%_libdir/libAppStreamQt6.so.%sover_qt

%files -n libappstream-qt-devel
%_includedir/AppStreamQt/
%_includedir/AppStreamQt5/
%_libdir/cmake/AppStreamQt/
%_libdir/cmake/AppStreamQt5/
%_libdir/libAppStreamQt5.so
%_libdir/libAppStreamQt.so

%files -n libappstream-qt6-devel
%_includedir/AppStreamQt6/
%_libdir/cmake/AppStreamQt6/
%_libdir/libAppStreamQt6.so

%files doc
%_defaultdocdir/%name
%_datadir/gtk-doc/html/appstream
%_datadir/gtk-doc/html/appstream-compose

%files compose
%_libexecdir/appstreamcli-compose
%_man1dir/appstreamcli-compose.1*
%_datadir/metainfo/org.freedesktop.appstream.compose.metainfo.xml

%files -n %libappstream_compose
%_libdir/libappstream-compose.so.*
%_libdir/libappstream-compose.so.%sover_compose

%files -n libappstream-compose-gir
%_libdir/girepository-1.0/AppStreamCompose-1.0.typelib

%files -n libappstream-compose-devel
%_includedir/appstream-compose/
%_libdir/libappstream-compose.so
%_libdir/pkgconfig/appstream-compose.pc
%_datadir/gir-1.0/AppStreamCompose-1.0.gir

%changelog
* Mon May 06 2024 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1.1
- NMU: build Qt5 and Qt6 libs
- NMU: apply shared libs policy

* Mon Mar 11 2024 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version (ALT #49646).

* Thu Dec 14 2023 Andrey Cherepanov <cas@altlinux.org> 0.16.4-alt2
- Built with -Dcompose=true (ALT #48797).

* Sat Nov 11 2023 Andrey Cherepanov <cas@altlinux.org> 0.16.4-alt1
- New version.

* Wed Aug 23 2023 Andrey Cherepanov <cas@altlinux.org> 0.16.3-alt1
- New version.

* Fri Apr 28 2023 Andrey Cherepanov <cas@altlinux.org> 0.16.2-alt1
- New version.

* Mon Mar 13 2023 Michael Shigorin <mike@altlinux.org> 0.16.1-alt2
- E2K: workaround for an inadequate warning in tests (ilyakurdyukov@)
- spec cleanup according to [[ALT Packaging HOWTO]]

* Sat Feb 11 2023 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version.

* Fri Jan 27 2023 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1
- New version.

* Fri Dec 23 2022 Andrey Cherepanov <cas@altlinux.org> 0.15.6-alt1
- New version.

* Thu Nov 24 2022 Sergey V Turchin <zerg@altlinux.org> 0.15.5-alt2
- allow to build with meson-0.59

* Thu Aug 25 2022 Andrey Cherepanov <cas@altlinux.org> 0.15.5-alt1
- New version.
- Build without docs (daps failed to build according to https://github.com/openSUSE/daps/issues/676).

* Tue May 24 2022 Andrey Cherepanov <cas@altlinux.org> 0.15.4-alt1
- New version.

* Tue May 17 2022 Andrey Cherepanov <cas@altlinux.org> 0.15.3-alt1
- New version.

* Wed Feb 23 2022 Andrey Cherepanov <cas@altlinux.org> 0.15.2-alt1
- New version.

* Sat Jan 01 2022 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt1
- New version (ALT #41655).

* Sat Oct 09 2021 Andrey Cherepanov <cas@altlinux.org> 0.14.6-alt1
- New version.

* Thu Sep 16 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.14.5-alt2
- Fixes for Elbrus build.

* Wed Sep 01 2021 Andrey Cherepanov <cas@altlinux.org> 0.14.5-alt1
- New version.

* Wed Jun 23 2021 Andrey Cherepanov <cas@altlinux.org> 0.14.4-alt2
- Put libraries to separate packages with appropriate names.

* Wed Jun 23 2021 Andrey Cherepanov <cas@altlinux.org> 0.14.4-alt1
- New version.

* Tue Mar 23 2021 Alexey Appolonov <alexey@altlinux.org> 0.14.3-alt2
- Corrected package URL.

* Wed Mar 10 2021 Andrey Cherepanov <cas@altlinux.org> 0.14.3-alt1
- New version.

* Tue Mar 02 2021 Andrey Cherepanov <cas@altlinux.org> 0.14.2-alt1
- New version.

* Wed Feb 17 2021 Andrey Cherepanov <cas@altlinux.org> 0.14.1-alt1
- New version.

* Wed Feb 03 2021 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- New version.

* Tue Dec 01 2020 Andrey Cherepanov <cas@altlinux.org> 0.13.1-alt1
- New version.

* Fri Nov 20 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.11-alt2
- Do not build API documentation because both daps and publican are not build for i586.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.11-alt1
- New version.
- Use daps instead of publican for documentation build.

* Fri Jan 24 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.10-alt1
- New version.

* Mon Dec 16 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.9-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.8-alt1
- New version.

* Sun Jun 23 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.7-alt1
- New version.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.6-alt1
- New version.

* Sun Jan 27 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.5-alt1
- New version.

* Mon Dec 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.4-alt1
- New version.

* Wed Oct 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.3-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt2.qa1
- NMU: applied repocop patch

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt2
- Disable tests.

* Fri Aug 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt1
- New version.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.1-alt1
- New version.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- New version.

* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.8-alt1
- New version.

* Mon Oct 23 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.7-alt1
- New version

* Sat Oct 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.6-alt1
- New version

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.5-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.4-alt1
- New version
- Use meson and ninja-build for build
- Package development documentation

* Sun Aug 06 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.3-alt1
- New version

* Wed Jul 19 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.2-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.1-alt1.gita6f9e55
- New version

* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.6-alt1
- new version 0.10.6

* Wed Dec 21 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.4-alt1
- new version 0.10.4

* Mon Nov 07 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.3-alt1
- new version 0.10.3

* Tue Sep 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- New version 0.10.1

* Tue Aug 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- New version

* Mon May 16 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- New version

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version

* Mon Sep 14 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt1
- New version

* Mon Sep 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.3-alt1
- New version

* Tue Jun 30 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.2-alt1
- New version
- appstream-qt contains libraries only for Qt5

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt2
- Rebuild with new version of xapian-core

* Sat Feb 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version

* Sun Jan 25 2015 Andrey Cherepanov <cas@altlinux.org> 0.7.6-alt1
- New version

* Mon Dec 15 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.5-alt1
- New version

* Tue Oct 28 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Import from Fedora
- Disable tests
