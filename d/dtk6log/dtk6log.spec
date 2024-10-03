%def_disable clang

Name: dtk6log
Version: 0.0.1
Release: alt2

Summary: Deepin tool kit log modules

License: LGPL-2.1
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtk6log

Source: %url/archive/%version/%name-%version.tar.gz

Provides: libdtk6-log = %EVR
Obsoletes: libdtk6-log < %EVR
Provides: dtk6-log = %EVR
Obsoletes: dtk6-log < %EVR

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: cmake dqt6-base-devel libspdlog-devel
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
Requires: libdqt6-core = %_dqt6_version

%description -n lib%{name}0
Deepin tool kit log modules.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk6-log-devel = %EVR
Obsoletes: dtk6-log-devel < %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%prep
%setup

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CMAKE_PREFIX_PATH=%_dqt6_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt6_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DCMAKE_INSTALL_RPATH=%_dqt6_libdir \
  -DMKSPECS_INSTALL_DIR=%_dqt6_mkspecsdir/modules/ \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DBUILD_WITH_QT6=ON \
  -DBUILD_WITH_SYSTEMD=ON \
  #
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files -n lib%{name}0
%doc README.md LICENSE*
%_libdir/lib%name.so.0*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/dtk6/
%dir %_includedir/dtk6/DLog/
%_includedir/dtk6/DLog/*.h
%dir %_libdir/cmake/Dtk6Log/
%_libdir/cmake/Dtk6Log/*.cmake
%_pkgconfigdir/%name.pc
%_dqt6_mkspecsdir/modules/qt_lib_dtklog.pri

%changelog
* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1-alt2
- Built with separate qt6 (ALT #48138).

* Fri Aug 30 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1-alt1
- Initial build for ALT Sisyphus.
