%def_disable clang

%define sover 0

Name: dtklog
Version: 6.7.43
Release: alt1

Summary: Deepin tool kit log modules

License: LGPL-2.1-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtklog
VCS: https://github.com/linuxdeepin/dtklog

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5 rpm-macros-dqt6
BuildRequires: cmake dqt5-base-devel dqt6-base-devel libspdlog-devel

%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
Deepin tool kit log modules.

%package -n lib%name%sover
Summary: Libraries for %name
Group: System/Libraries
Requires: libdqt5-core = %_dqt5_version

%description -n lib%name%sover
Deepin tool kit log modules.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk5-log-devel = %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%package -n libdtk6log%sover
Summary: Libraries for %name
Group: System/Libraries
Requires: libdqt6-core = %_dqt6_version

%description -n libdtk6log%sover
Deepin tool kit log modules.
Libraries for dtk6log.

%package -n libdtk6log-devel
Summary: Development package for dtk6log
Group: Development/KDE and QT
Provides: dtk6-log-devel = %EVR
Obsoletes: dtk6-log-devel < %EVR

%description -n libdtk6log-devel
Header files and libraries for dtk6log.

%prep
%setup
%patch -p1

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

echo "Start DTK6 build."
%DQ6build \
  -DMKSPECS_INSTALL_DIR=%_dqt6_mkspecsdir/modules \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DDTK5=OFF \
  -DBUILD_WITH_SYSTEMD=ON \
#

echo "Start DTK5 build."
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake -B build5 \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DDTK5=ON \
  -DBUILD_WITH_SYSTEMD=ON \
  -DMKSPECS_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/modules/ \
#
cmake --build build5 -j%__nprocs

%install
%DQ6install
DESTDIR=%buildroot cmake --install build5 --verbose

%files -n lib%{name}%sover
%doc README.md LICENSE* CHANGELOG.md
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/dtk5/
%dir %_includedir/dtk5/DLog/
%_includedir/dtk5/DLog/*.h
%dir %_libdir/cmake/DtkLog/
%_libdir/cmake/DtkLog/*.cmake
%_pkgconfigdir/%name.pc
%_dqt5_archdatadir/mkspecs/modules/qt_lib_dtklog.pri

%files -n libdtk6log%sover
%doc README.md LICENSE* CHANGELOG.md
%_libdir/libdtk6log.so.%{sover}*

%files -n libdtk6log-devel
%_libdir/libdtk6log.so
%dir %_includedir/dtk6/
%dir %_includedir/dtk6/DLog/
%_includedir/dtk6/DLog/*.h
%dir %_libdir/cmake/Dtk6Log/
%_libdir/cmake/Dtk6Log/*.cmake
%_pkgconfigdir/dtk6log.pc
%_dqt6_mkspecsdir/modules/qt_lib_dtklog.pri

%changelog
* Tue Jun 09 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.43-alt1
- New version 6.7.43.

* Thu May 14 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.41-alt1
- New version 6.7.41.

* Wed Apr 15 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.39-alt1
- New version 6.7.39.
- Clarified license tag.

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.33-alt1
- New version 6.7.33.

* Thu Jan 22 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.31-alt1
- New version 6.7.31.
- Unified dtk5 and dtk6 modules.

* Fri Oct 17 2025 Leontiy Volodin <lvol@altlinux.org> 0.0.6-alt1
- New version 0.0.6.

* Tue Jul 22 2025 Leontiy Volodin <lvol@altlinux.org> 0.0.5-alt1
- New version 0.0.5.

* Thu Jan 16 2025 Leontiy Volodin <lvol@altlinux.org> 0.0.2-alt1
- New version 0.0.2.
- Added vcs tag.

* Thu Sep 12 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1-alt2
- Moved mkspecs module to dqt5's default place.

* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1-alt1
- Initial build for ALT Sisyphus.
