%define _libexecdir %_prefix/libexec

%def_disable clang
%def_without docs

Name: dtk6core
Version: 6.0.11
Release: alt1

Summary: Deepin tool kit core modules

License: LGPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtk6core

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

Provides: libdtk6-core = %EVR
Obsoletes: libdtk6-core < %EVR
Provides: dtk6-core = %EVR
Obsoletes: dtk6-core < %EVR

BuildRequires(pre): rpm-build-ninja deepin-desktop-base rpm-macros-qt6
BuildRequires: cmake qt6-base-devel libsystemd-devel dtk6-common-devel libuchardet-devel libspdlog-devel
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif
%if_with docs
BuildRequires: qt6-base-doc
%endif

%description
Deepin tool kit core modules.

%package -n lib%{name}6
Summary: Libraries for %name
Group: System/Libraries
Requires: libqt6-core = %_qt6_version

%description -n lib%{name}6
Deepin tool kit core modules.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk6-core-devel = %EVR
Obsoletes: dtk6-core-devel < %EVR
Requires: %name = %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%if_with docs
%package doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch
Provides: dtk6-core-doc = %EVR
Obsoletes: dtk6-core-doc < %EVR

%description doc
This package provides %name documantation.
%endif

%prep
%setup
%patch -p1

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export PATH=%_qt6_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DDTK_VERSION=%version \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DD_DSG_APP_DATA_FALLBACK=/var/dsg/appdata \
  -DBUILD_WITH_SYSTEMD=ON \
%if_without docs
  -DBUILD_DOCS=OFF \
%endif
  -DMKSPECS_INSTALL_DIR=%_qt6_archdatadir/mkspecs/modules/ \
  #
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE
%dir %_libexecdir/dtk6
%dir %_libexecdir/dtk6/DCore/
%_libexecdir/dtk6/DCore/bin/

%files -n lib%{name}6
%_libdir/lib%name.so.6*

%files -n lib%name-devel
%doc docs/Specification.md
%_libdir/lib%name.so
%dir %_includedir/dtk6/
%_includedir/dtk6/DCore/
%_qt6_archdatadir/mkspecs/modules/qt_lib_dtkcore.pri
%_qt6_archdatadir/mkspecs/features/dtk_install_dconfig.prf
%_libdir/cmake/Dtk6Core/
%_libdir/cmake/Dtk6CMake/
%_libdir/cmake/Dtk6Tools/
%_libdir/cmake/Dtk6DConfig/
%_pkgconfigdir/dtk6core.pc

%if_with docs
%files doc
%_qt6_datadir/doc/dtk6core.qch
%endif

%changelog
* Mon Apr 22 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.11-alt1
- New version 6.0.11.

* Tue Apr 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.9-alt1
- Initial build for ALT Sisyphus.
