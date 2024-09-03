%define rname mpvqt
%define sover 1
%define major 6
%define libname libmpvqt%sover

Name: %rname%major
Version: 1.0.1
Release: alt1

Group: System/Libraries
Summary: Wrapper for libmpv
License: LGPL-2.1-only or LGPL-3.0-only
Url: https://invent.kde.org/libraries/mpvqt

Source0: %rname-%version.tar

BuildRequires: extra-cmake-modules
BuildRequires: libmpv-devel
BuildRequires: cmake qt6-base-devel qt6-declarative-devel

%description
MpvQt is a libmpv wrapper for Qt Quick 2/Qml.

%package -n %libname
Group: System/Libraries
Summary: %name library
#Requires: %name-common
%description -n %libname
%name library

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: libmpv-devel
%description devel
%summary.

%prep
%setup -n %rname-%version

%build
%cmake \
    -DKDE_INSTALL_INCLUDEDIR=%_includedir/MpvQt%major \
    #
%cmake_build

%install
%cmakeinstall_std

%files -n %libname
%doc LICENSES/* README*
%_libdir/libMpvQt.so.*
%_libdir/libMpvQt.so.%sover
#%_datadir/qlogging-categories6/*.*categories

%files devel
%_includedir/MpvQt%major/
%_libdir/cmake/MpvQt/
%_libdir/lib*.so

%changelog
* Tue Sep 03 2024 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- Initial build
