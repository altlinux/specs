%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_without check

Name: geonames
Version: 0.3.2
Release: alt1

Summary: Parse and query the geonames database dump
License: GPL-3.0
Group: System/Libraries
Url: https://gitlab.com/ubports/development/core/geonames

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: gtk-doc

%if_with check
BuildRequires: ctest
%endif

%description
Parse and query the geonames database dump

A library for parsing and querying a local copy of the geonames.org
database.

%package -n libgeonames0
Summary: Parse and query the geonames database dump
Group: System/Libraries
Requires: libgeonames-data = %{version}-%{release}

%description -n libgeonames0
A library for parsing and querying a local copy of the geonames.org
database.

This package contains the shared libraries.

%package -n libgeonames-data
Summary: %name - data files
Group: Other
BuildArch: noarch

%description -n libgeonames-data
A library for parsing and querying a local copy of the geonames.org
database.

This package contains library data files

%package -n libgeonames-devel
Summary: %name - library development files
Group: Development/C
Requires: libgeonames0 = %{version}-%{release}

%description -n libgeonames-devel
A library for parsing and querying a local copy of the geonames.org
database.

This package contains the header and development files which are needed
to use the libgeonames library.

%prep
%setup
sed -i '/^cmake_minimum_required/d' cmake/GtkDocScanGObjWrapper.cmake

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %name --all-name

%check
%ctest -V

%files -n libgeonames0
%doc AUTHORS ChangeLog COPYING COPYING.data
%_libdir/libgeonames.so.0
%_libdir/libgeonames.so.0.3.2

%files -n libgeonames-devel
%dir %_includedir/%name
%_includedir/%name/*
%_libdir/libgeonames.so
%_libdir/pkgconfig/*.pc
%dir %_datadir/gtk-doc/html/%name
%_datadir/gtk-doc/html/%name/*

%files -n libgeonames-data -f %{name}.lang
%exclude %_datadir/locale/zh_Hant/LC_MESSAGES/%{name}.mo

%changelog
* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.3.2-alt1
- New version 0.3.2.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
