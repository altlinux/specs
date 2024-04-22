%def_disable clang
%def_enable docs

Name: dtk6widget
Version: 6.0.11
Release: alt1

Summary: Deepin tool kit widget modules

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkwidget

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

Provides: libdtk6-widget = %EVR
Obsoletes: libdtk6-widget < %EVR

# for webp (dci) icons
Requires: qt6-imageformats

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja rpm-macros-qt6
BuildRequires: cmake doxygen dtk6-common-devel libdtk6gui-devel qt6-tools-devel libxcbutil-devel libstartup-notification-devel libXext-devel libXi-devel qt6-svg-devel libcups-devel

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package -n lib%{name}6
Summary: Libraries for %name
Group: System/Libraries
Requires: libqt6-core = %_qt6_version
Requires: libqt6-gui = %_qt6_version
Requires: libqt6-printsupport = %_qt6_version
Requires: libqt6-widgets = %_qt6_version

%description -n lib%{name}6
DtkWidget is Deepin graphical user interface for deepin desktop development.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk6-widget-devel = %EVR
Obsoletes: dtk6-widget-devel < %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%package examples
Summary: Examples for %name
Group: Development/KDE and QT
Provides: dtk6-widget-examples = %EVR
Obsoletes: dtk6-widget-examples < %EVR

%description examples
DtkWidget is Deepin graphical user interface for deepin desktop development.
Examples for %name.

%if_enabled docs
%package doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch
Provides: dtk6-widget-doc = %EVR
Obsoletes: dtk6-widget-doc < %EVR

%description doc
This package provides %name documantation.
%endif

%prep
%setup

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt6_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=None \
  -DMKSPECS_INSTALL_DIR=%_qt6_archdatadir/mkspecs/modules/ \
%if_enabled docs
  -DBUILD_DOCS=ON \
  -DQCH_INSTALL_DESTINATION=%_qt6_docdir \
%else
  -DBUILD_DOCS=OFF \
%endif
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DDTK_VERSION=%version \
  -DBUILD_PLUGINS=OFF \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE
%dir %_libdir/dtk6/
%dir %_libdir/dtk6/DWidget/
%_libdir/dtk6/DWidget/bin/
%dir %_datadir/dtk6/
%_datadir/dtk6/DWidget/

%files -n lib%{name}6
%_libdir/lib%name.so.6*

%files -n lib%name-devel
%dir %_includedir/dtk6/
%_includedir/dtk6/DWidget/
%_qt6_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/Dtk6Widget/
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%files examples
%dir %_libdir/dtk6/DWidget/
%_libdir/dtk6/DWidget/examples/

%files doc
%_qt6_docdir/dtkwidget.qch

%changelog
* Mon Apr 22 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.11-alt1
- New version 6.0.11.

* Tue Apr 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.9-alt1
- Initial build for ALT Sisyphus.
