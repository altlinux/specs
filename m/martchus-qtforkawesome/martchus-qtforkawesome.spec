%define _unpackaged_files_terminate_build 1

Name: martchus-qtforkawesome
Version: 0.3.3
Release: alt1

Summary: Library that bundles ForkAwesome for use within Qt applications
License: GPL-2.0-or-later
Group: Development/C++
Url: https://github.com/Martchus/qtforkawesome

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: fonts-fork-awesome
BuildRequires: pkgconfig(martchus-c++utilities)
BuildRequires: pkgconfig(martchus-qtutilities)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: perl-YAML-LibYAML
BuildRequires: perl-Encode
BuildRequires: doxygen

Requires: fonts-fork-awesome

%description
%summary

%package -n libmartchus-qtforkawesome1
Summary: C++ library that conveniently enables the use of Fork Awesome in Qt
Group: System/Libraries

%description -n libmartchus-qtforkawesome1
Qt ForkAwesome is a C++ library that conveniently enables the use of Fork
Awesome in Qt applications.  Qt ForkAwesome enumerates and encodes Fork
Awesome as Qt resources, it provides an 'enum' of the icon-font definitions,
and it enables font glyphs to be used in cases where Qt requires traditional
icons.  Qt ForkAwesome uses FreeType to render, hint, and antialias
icon-fonts.

Refer to the description of fonts-fork-awesome for more information about
icon-fonts.

%package -n libmartchus-qtforkawesome-devel
Summary: library that conveniently enables the use of Fork Awesome in Qt (headers)
Group: Development/C++

%description -n libmartchus-qtforkawesome-devel
Qt ForkAwesome is a C++ library that conveniently enables the use of Fork
Awesome in Qt applications.  Qt ForkAwesome enumerates and encodes Fork
Awesome as Qt resources, it provides an 'enum' of the icon-font definitions,
and it enables font glyphs to be used in cases where Qt requires traditional
icons.  Qt ForkAwesome uses FreeType to render, hint, and antialias
icon-fonts.

Refer to the description of fonts-fork-awesome for more information about
icon-fonts.

This is the development package of libmartchus-qtforkawesome.  Please note
that, at this time, Qt ForkAwesome's ABI changes with every release.

%prep
%setup
%patch -p1

%build
%cmake \
       -DBUILD_SHARED_LIBS=ON \
       -DNAMESPACE=martchus \
       -DPACKAGE_NAMESPACE=martchus \
       -DQT_PACKAGE_PREFIX=Qt6 \
       -DFORK_AWESOME_FONT_FILE=/usr/share/fonts/ttf/fork-awesome/forkawesome-webfont.ttf \
       -DFORK_AWESOME_ICON_DEFINITIONS=/usr/share/fonts-fork-awesome/icons.yml
%cmake_build

%install
%cmake_install

%files -n libmartchus-qtforkawesome1
%doc LICENSE README.md
%_libdir/libmartchus-qtforkawesome.so.0*
%_libdir/libmartchus-qtforkawesome.so.1*
%_libdir/libmartchus-qtquickforkawesome.so.0*
%_libdir/libmartchus-qtquickforkawesome.so.1*
%_libdir/qt6/plugins/iconengines/libmartchus-qtforkawesomeiconengine.so

%files -n libmartchus-qtforkawesome-devel
%dir %_includedir/martchus-qtforkawesome
%dir %_includedir/martchus-qtforkawesome/qtforkawesome
%_includedir/martchus-qtforkawesome/qtforkawesome/global.h
%_includedir/martchus-qtforkawesome/qtforkawesome/icon.h
%_includedir/martchus-qtforkawesome/qtforkawesome/iconfwd.h
%dir %_includedir/martchus-qtforkawesome/qtforkawesome/private
%_includedir/martchus-qtforkawesome/qtforkawesome/private/icons.h
%_includedir/martchus-qtforkawesome/qtforkawesome/qtforkawesome-definitions.h
%_includedir/martchus-qtforkawesome/qtforkawesome/renderer.h
%_includedir/martchus-qtforkawesome/qtforkawesome/utils.h
%_includedir/martchus-qtforkawesome/qtforkawesome/version.h
%dir %_includedir/martchus-qtquickforkawesome
%dir %_includedir/martchus-qtquickforkawesome/qtquickforkawesome
%_includedir/martchus-qtquickforkawesome/qtquickforkawesome/global.h
%_includedir/martchus-qtquickforkawesome/qtquickforkawesome/imageprovider.h
%_includedir/martchus-qtquickforkawesome/qtquickforkawesome/qtquickforkawesome-definitions.h
%_includedir/martchus-qtquickforkawesome/qtquickforkawesome/version.h
%_libdir/libmartchus-qtforkawesome.so
%_libdir/libmartchus-qtquickforkawesome.so
%_pkgconfigdir/martchus-qtforkawesome.pc
%_pkgconfigdir/martchus-qtforkawesomeiconengine.pc
%_pkgconfigdir/martchus-qtquickforkawesome.pc
%dir %_datadir/martchus-qtforkawesome
%dir %_datadir/martchus-qtforkawesome/cmake
%_datadir/martchus-qtforkawesome/cmake/martchus-qtforkawesomeConfig.cmake
%_datadir/martchus-qtforkawesome/cmake/martchus-qtforkawesomeConfigVersion.cmake
%_datadir/martchus-qtforkawesome/cmake/martchus-qtforkawesomeTargets-*.cmake
%_datadir/martchus-qtforkawesome/cmake/martchus-qtforkawesomeTargets.cmake
%dir %_datadir/martchus-qtforkawesomeiconengine
%dir %_datadir/martchus-qtforkawesomeiconengine/cmake
%_datadir/martchus-qtforkawesomeiconengine/cmake/martchus-qtforkawesomeiconengineConfig.cmake
%_datadir/martchus-qtforkawesomeiconengine/cmake/martchus-qtforkawesomeiconengineConfigVersion.cmake
%_datadir/martchus-qtforkawesomeiconengine/cmake/martchus-qtforkawesomeiconengineTargets-*.cmake
%_datadir/martchus-qtforkawesomeiconengine/cmake/martchus-qtforkawesomeiconengineTargets.cmake
%dir %_datadir/martchus-qtquickforkawesome
%dir %_datadir/martchus-qtquickforkawesome/cmake
%_datadir/martchus-qtquickforkawesome/cmake/martchus-qtquickforkawesomeConfig.cmake
%_datadir/martchus-qtquickforkawesome/cmake/martchus-qtquickforkawesomeConfigVersion.cmake
%_datadir/martchus-qtquickforkawesome/cmake/martchus-qtquickforkawesomeTargets-*.cmake
%_datadir/martchus-qtquickforkawesome/cmake/martchus-qtquickforkawesomeTargets.cmake

%changelog
* Mon May 25 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.3-alt1
- New version 0.3.3.

* Sat Nov 22 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus
