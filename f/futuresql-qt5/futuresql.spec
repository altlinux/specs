%define rname futuresql
%global appname FutureSQL

%define sover 0
%define major 5
%define libfuturesql libfuturesql%{major}_%sover

Name: futuresql-qt%major
Version: 0.1.1
Release: alt1

Group: System/Libraries
License: (LGPL-2.1-only OR LGPL-3.0-only) AND BSD-2-Clause
Summary: Non-blocking database framework for Qt%major
Url: https://invent.kde.org/libraries/futuresql/

Source: %rname-%version.tar

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: pkgconfig(Qt%{major}Core)
BuildRequires: pkgconfig(Qt%{major}Sql)
BuildRequires: pkgconfig(Qt%{major}Test)
BuildRequires: qcoro%major-devel

%description
FutureSQL was in part inspired by Diesel, and provides a higher level of
abstraction than QtSql. Its features include non-blocking database access by
default, relatively boilerplate-free queries, automatic database migrations
and simple mapping to objects.  In order to make FutureSQL's use of templates
less confusing, FutureSQL uses C++20 concepts, and requires a C++20 compiler.}

%package devel
Group: Development/Databases
Summary: Development files for %appname
Requires: qt%major-base-devel
Provides: %rname-devel = %version
%description devel
Development files for %name.

%package -n %libfuturesql
Group: System/Libraries
Summary: %name library
#Requires: %name-common
Requires: kf%major-filesystem
%description -n %libfuturesql
%name library.

%prep
%setup -n %rname-%version

%build
%cmake \
    -G Ninja \
    -DBUILD_WITH_QT6:BOOL=OFF \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DBUILD_TESTING:BOOL=OFF \
    #
%cmake_build

%install
%cmake_install

%files -n %libfuturesql
%doc README.md LICENSES/*
%_libdir/lib%rname%major.so.0*

%files devel
%_includedir/%appname%major/
%_libdir/cmake/%appname%major/
%_libdir/lib*.so

%changelog
* Wed Oct 18 2023 Sergey V Turchin <zerg@altlinux.org> 0.1.1-alt1
- initial build
