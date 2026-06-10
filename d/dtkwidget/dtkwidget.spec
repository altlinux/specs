%define _libexecdir %_prefix/libexec

%def_disable clang
%def_enable docs

Name: dtkwidget
Version: 6.7.43
Release: alt1

Summary: Deepin tool kit widget modules

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkwidget
VCS: https://github.com/linuxdeepin/dtkwidget

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

# for webp (dci) icons
Requires: dqt5-imageformats

# Common BuildRequires.
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake doxygen dtk6-common-devel libcups-devel libxcbutil-devel libstartup-notification-devel libXext-devel libXi-devel libwayland-client-devel libwayland-client

%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
# DTK5 BuildRequires.
BuildRequires(pre): rpm-macros-dqt5
BuildRequires: libgsettings-dqt5-devel libgio-devel dqt5-svg-devel dqt5-tools-devel dqt5-x11extras-devel libdtkcore-devel libdtkgui-devel libdqt5-concurrent libdqt5-printsupport

# DTK6 BuildRequires.
BuildRequires(pre): rpm-macros-dqt6
BuildRequires: libdtk6core-devel libdtk6gui-devel dqt6-base-devel dqt6-tools-devel dqt6-svg-devel vulkan-headers libdqt6-concurrent libdqt6-printsupport

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package -n lib%{name}5
Summary: Libraries for %name
Group: System/Libraries
Provides: libdtk5-widget = %EVR
Obsoletes: libdtk5-widget < %EVR
Requires: libdqt5-core = %_dqt5_version
Requires: libdqt5-gui = %_dqt5_version
Requires: libdqt5-printsupport = %_dqt5_version
Requires: libdqt5-widgets = %_dqt5_version

%description -n lib%{name}5
DtkWidget is Deepin graphical user interface for deepin desktop development.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk5-widget-devel = %EVR
Obsoletes: dtk5-widget-devel < %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%package examples
Summary: Examples for %name
Group: Development/KDE and QT
Provides: dtk5-widget-examples = %EVR
Obsoletes: dtk5-widget-examples < %EVR

%description examples
DtkWidget is Deepin graphical user interface for deepin desktop development.
Examples for %name.

%if_enabled docs
%package doc
Summary: %name documantation
Group: Documentation
BuildArch: noarch
Provides: dtk5-widget-doc = %EVR
Obsoletes: dtk5-widget-doc < %EVR

%description doc
This package provides %name documantation.
%endif

%package -n dtk6widget
Summary: Deepin tool kit widget modules
Group: Graphical desktop/Other
Provides: libdtk6-widget = %EVR
Obsoletes: libdtk6-widget < %EVR
# for webp (dci) icons
Requires: dqt6-imageformats

%description -n dtk6widget
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package -n libdtk6widget6
Summary: Libraries for dtk6widget
Group: System/Libraries
Requires: libdqt6-core = %_dqt6_version
Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-printsupport = %_dqt6_version
Requires: libdqt6-widgets = %_dqt6_version

%description -n libdtk6widget6
DtkWidget is Deepin graphical user interface for deepin desktop development.
Libraries for dtk6widget.

%package -n libdtk6widget-devel
Summary: Development package for dtk6widget
Group: Development/KDE and QT
Provides: dtk6-widget-devel = %EVR
Obsoletes: dtk6-widget-devel < %EVR

%description -n libdtk6widget-devel
Header files and libraries for dtk6widget.

%package -n dtk6widget-examples
Summary: Examples for dtk6widget
Group: Development/KDE and QT
Provides: dtk6-widget-examples = %EVR
Obsoletes: dtk6-widget-examples < %EVR

%description -n dtk6widget-examples
DtkWidget is Deepin graphical user interface for deepin desktop development.
Examples for dtk6widget.

%prep
%setup
%patch0 -p1

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

echo "Start DTK5 build."
export PATH=%_dqt5_bindir:$PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:%_libdir/pkgconfig
%cmake -B build5 \
  -GNinja \
  -DDTK5=ON \
  -DCMAKE_PREFIX_PATH=%_dqt5_libdir/cmake \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DCMAKE_LIBRARY_PATH=%_dqt5_libdir \
  -DMKSPECS_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/modules/ \
%if_enabled docs
  -DBUILD_DOCS=ON \
  -DQCH_INSTALL_DESTINATION=%_dqt5_docdir \
%else
  -DBUILD_DOCS=OFF \
%endif
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DDTK_VERSION=%version \
  -DBUILD_PLUGINS=OFF \
#
cmake --build build5 -j%__nprocs

echo "Start DTK6 build."
%DQ6build \
  -DDTK5=OFF \
  -DMKSPECS_INSTALL_DIR=%_dqt6_mkspecsdir/modules/ \
  -DBUILD_DOCS=OFF \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DDTK_VERSION=%version \
  -DBUILD_PLUGINS=OFF \
#

%install
DESTDIR=%buildroot cmake --install build5 --verbose
%DQ6install

%files
%doc README.md LICENSE CHANGELOG.md
%dir %_datadir/dtk5/
%_datadir/dtk5/DWidget/
%dir %_libexecdir/dtk5/
%dir %_libexecdir/dtk5/DWidget/
%dir %_libexecdir/dtk5/DWidget/bin/
%_libexecdir/dtk5/DWidget/bin/dtk-svgc

%files -n lib%{name}5
%_libdir/lib%name.so.5*

%files -n lib%name-devel
%dir %_includedir/dtk5/
%_includedir/dtk5/DWidget/
%_dqt5_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/DtkWidget/
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%files examples
%dir %_libdir/dtk5/
%dir %_libdir/dtk5/DWidget/
%_libdir/dtk5/DWidget/examples/

%if_enabled docs
%files doc
%_dqt5_docdir/dtkwidget.qch
%endif

%files -n dtk6widget
%doc README.md LICENSE CHANGELOG.md
%dir %_datadir/dtk6/
%_datadir/dtk6/DWidget/
%dir %_libexecdir/dtk6/
%dir %_libexecdir/dtk6/DWidget/
%dir %_libexecdir/dtk6/DWidget/bin/
%_libexecdir/dtk6/DWidget/bin/dtk6-svgc

%files -n libdtk6widget6
%_libdir/libdtk6widget.so.6*

%files -n libdtk6widget-devel
%dir %_includedir/dtk6/
%_includedir/dtk6/DWidget/
%_dqt6_mkspecsdir/modules/*.pri
%_libdir/cmake/Dtk6Widget/
%_pkgconfigdir/dtk6widget.pc
%_libdir/libdtk6widget.so

%files -n dtk6widget-examples
%dir %_libdir/dtk6/
%dir %_libdir/dtk6/DWidget/
%_libdir/dtk6/DWidget/examples/

%changelog
* Tue Jun 09 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.43-alt1
- New version 6.7.43.

* Thu May 14 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.41-alt1
- New version 6.7.41.

* Wed Apr 15 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.39-alt1
- New version 6.7.39.
- Disabled docs on dtk6widget.

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.33-alt1
- New version 6.7.33.

* Mon Feb 16 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.32-alt1
- New version 6.7.32.
- Unified dtk5 and dtk6 modules.
- Built on separate libgsettings-qt (no qt5 required).

* Wed Dec 10 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.28-alt1
- New version 5.7.28.

* Fri Nov 07 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.26-alt1
- New version 5.7.26.

* Fri Oct 24 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.24-alt1
- New version 5.7.24.

* Wed Oct 15 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.23-alt1
- New version 5.7.23.

* Tue Jul 22 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.19-alt1
- New version 5.7.19.

* Thu Feb 13 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.9-alt1
- New version 5.7.9.

* Thu Jan 16 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.8-alt1
- New version 5.7.8.
- Added vcs tag.

* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.34.0.2.38e3-alt1
- New version 5.6.34-2-g38e3cc14.

* Wed May 08 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- New version 5.6.28.
- Built via separate qt5 instead system (ALT #48138).

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.26-alt1
- New version 5.6.26.

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt2
- Fixed update from libdtk5-widget.

* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt1
- New version 5.6.25.

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.23-alt2
- Required on current qt5 version.

* Fri Mar 01 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.23-alt1
- New version 5.6.23.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.22-alt1
- New version 5.6.22.

* Thu Nov 30 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.20-alt1
- New version 5.6.20.
- Cleanup BRs.
- Removed obsoleted patch.
- Fixed missing icons.
- Disabled plugins.
- Renamed subpackages:
  + libdtk5-widget -> dtkwidget.
  + dtk5-widget-devel -> libdtkwidget-devel.
  + dtk5-widget-examples -> dtkwidget-examples.
  + dtk5-widget-doc -> dtkwidget-doc.

* Fri Mar 10 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.8-alt1
- New version.

* Tue Feb 21 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.7-alt1
- New version.

* Mon Feb 13 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.5-alt1
- Fixed version.
- Applied fixed from master branch.

* Wed Jan 25 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt2.gitd2cb0fb
- Fixed missing icon on titlebar button.

* Fri Jan 20 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt1.gitd2cb0fb
- New version.
- Spec:
  + Added config subpackage.
  + Added docs switcher.
  + Fixed broken configs.
- Patches:
  + Fixed build using gcc.

* Thu Nov 24 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.0.2-alt2
- Fixed translations.

* Mon Oct 17 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.0.2-alt1
- New version.
- Upstream:
  + use cmake instead qmake.

* Wed Jun 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.46-alt1
- New version.
- Upstream:
  + fix: wayland environmental network link dialogue box click invalid.
  + fix: print preview titlebar does not follow the theme changes.
  + fix: abandoned interface update.

* Mon May 23 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.45-alt1
- New version.

* Wed May 04 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.44-alt1
- New version (5.5.44).

* Tue Mar 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.42-alt1
- New version (5.5.42).

* Tue Feb 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.37-alt1
- New version (5.5.37).

* Tue Jul 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.17.1-alt1
- New version (5.5.17.1).

* Mon Jun 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.7-alt1
- New version (5.5.7) with rpmgs script.

* Mon May 17 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- New version (5.4.20) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.16-alt1
- New version (5.4.16) with rpmgs script.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.10-alt1
- New version (5.4.10) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.4.1-alt1
- New version (5.4.1) with rpmgs script.

* Wed Oct 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0-alt1
- New version (5.3.0) with rpmgs script.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.15-alt1
- New version (5.2.2.15) with rpmgs script.

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.3-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
