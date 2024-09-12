%def_disable clang

Name: dtklog
Version: 0.0.1
Release: alt2

Summary: Deepin tool kit log modules

License: LGPL-2.1
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtklog

Source: %url/archive/%version/%name-%version.tar.gz

Provides: libdtk5-log = %EVR
Obsoletes: libdtk5-log < %EVR
Provides: dtk5-log = %EVR
Obsoletes: dtk5-log < %EVR

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt5
BuildRequires: cmake dqt5-base-devel libspdlog-devel
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
Deepin tool kit log modules.

%package -n lib%{name}0
Summary: Libraries for %name
Group: System/Libraries
Requires: libdqt5-core = %_dqt5_version

%description -n lib%{name}0
Deepin tool kit log modules.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk5-log-devel = %EVR
Obsoletes: dtk5-log-devel < %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%prep
%setup

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DBUILD_WITH_SYSTEMD=ON \
  -DMKSPECS_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/modules/ \
  #
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files -n lib%{name}0
%doc README.md LICENSE*
%_libdir/lib%name.so.0*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/dtk5/
%dir %_includedir/dtk5/DLog/
%_includedir/dtk5/DLog/*.h
%dir %_libdir/cmake/DtkLog/
%_libdir/cmake/DtkLog/*.cmake
%_pkgconfigdir/%name.pc
%_dqt5_archdatadir/mkspecs/modules/qt_lib_dtklog.pri

%changelog
* Thu Sep 12 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1-alt2
- Moved mkspecs module to dqt5's default place.

* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1-alt1
- Initial build for ALT Sisyphus.
