%define _unpackaged_files_terminate_build 1

%def_with check

Name: lomiri-action-api
Version: 1.2.2
Release: alt1

Summary: Lomiri Action Qt5 API

License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-action-api

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: doxygen
BuildRequires: /usr/bin/dot
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-tools

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /usr/bin/dbus-test-runner
%endif

%description
Lomiri Common Action API (built against Qt5). Allow applications to
export actions in various forms to the Lomiri Shell.

%package -n lib%{name}-qt5
Group: System/Libraries
Summary: Lomiri Action Qt5 API

%description -n lib%{name}-qt5
Lomiri Common Action API (built against Qt5). Allow applications to
export actions in various forms to the Lomiri Shell.

%package -n lib%{name}-qt5-devel
Group: Development/C++
Summary: Lomiri Action Qt5 API - development files
Requires: lib%{name}-qt5 = %{version}-%{release}

%description -n lib%{name}-qt5-devel
Lomiri Common Action API (built against Qt5). Allow applications to
export actions in various forms to the Lomiri Shell.

This package contains development files to develop against the library.

%package -n %{name}-doc
Group: Documentation
Summary: Lomiri Action API - documentation
BuildArch: noarch

%description -n %{name}-doc
Lomiri Common Action API. Allow applications to
export actions in various forms to the Lomiri Shell.

This package contains developer documentation.

%prep
%setup
%patch -p1

%build
%cmake \
       -DGENERATE_DOCUMENTATION=ON \
       -DENABLE_QT6=OFF \
       -DENABLE_WERROR=OFF \
       -Duse_libhud2=OFF
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV

%files -n lib%{name}-qt5
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/liblomiri-action-qt.so.1
%dir %_qt5_qmldir/Lomiri/Action
%_qt5_qmldir/Lomiri/Action/liblomiri-action-qml.so
%_qt5_qmldir/Lomiri/Action/qmldir

%files -n lib%{name}-qt5-devel
%_libdir/liblomiri-action-qt.so
%dir %_includedir/lomiri-action-qt-1
%dir %_includedir/lomiri-action-qt-1/lomiri
%dir %_includedir/lomiri-action-qt-1/lomiri/action
%_includedir/lomiri-action-qt-1/lomiri/action/Action
%_includedir/lomiri-action-qt-1/lomiri/action/ActionContext
%_includedir/lomiri-action-qt-1/lomiri/action/ActionManager
%_includedir/lomiri-action-qt-1/lomiri/action/PreviewAction
%_includedir/lomiri-action-qt-1/lomiri/action/PreviewParameter
%_includedir/lomiri-action-qt-1/lomiri/action/PreviewRangeParameter
%_includedir/lomiri-action-qt-1/lomiri/action/lomiri-action-context.h
%_includedir/lomiri-action-qt-1/lomiri/action/lomiri-action-manager.h
%_includedir/lomiri-action-qt-1/lomiri/action/lomiri-action.h
%_includedir/lomiri-action-qt-1/lomiri/action/lomiri-menu-item.h
%_includedir/lomiri-action-qt-1/lomiri/action/lomiri-preview-action.h
%_includedir/lomiri-action-qt-1/lomiri/action/lomiri-preview-parameter.h
%_includedir/lomiri-action-qt-1/lomiri/action/lomiri-preview-range-parameter.h
%_pkgconfigdir/lomiri-action-qt-1.pc

%files -n %{name}-doc
%dir %_datadir/doc/lomiri-action-api
%_datadir/doc/lomiri-action-api/*

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.2-alt1
- New version 1.2.2.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- New version 1.2.1.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
