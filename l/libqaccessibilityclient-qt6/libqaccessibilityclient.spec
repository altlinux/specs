%define bname qaccessibilityclient
Name: lib%bname-qt6
Version: 0.6.0
Release: alt1

Group: System/Libraries
Summary: This library is used when writing accessibility clients
License: LGPL-3.0
Url: https://invent.kde.org/libraries/libqaccessibilityclient

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: extra-cmake-modules
BuildRequires: cmake qt6-base-devel

%description
%summary.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: libqaccessibilityclient-devel
Conflicts: libqaccessibilityclient-qt5-devel
%description devel
%summary.

%prep
%setup
#exclude tests and examples from build
sed -i '/add_subdirectory.*tests\|add_subdirectory.*examples/d' ./CMakeLists.txt

%build
%cmake \
    -DQT_MAJOR_VERSION=6 \
    #
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSES/* README*
%_libdir/%{name}.so.0
%_libdir/%{name}.so.*
%_datadir/qlogging-categories6/*.*categories

%files devel
%_includedir/QAccessibilityClient6/
%_libdir/cmake/QAccessibilityClient6/
%_libdir/lib*.so

%changelog
* Mon Jul 01 2024 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Mon Dec 25 2017 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt2
- track library soname

* Fri Aug 25 2017 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1
- Initial build
