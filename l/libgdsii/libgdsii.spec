Name:		libgdsii
Summary:	A C++ library for working with GDSII binary data files
Version:	0.21
Release:	alt2
License:	GPLv2
URL:		https://github.com/HomerReid/libGDSII
Source:		%name-%version.tar.gz
Group:		System/Libraries

BuildRequires:	gcc-c++

%description
libGDSII is a C++ library for working with GDSII binary data files,
intended primarily for use with the computational electromagnetism codes
scuff-em and meep but sufficiently general-purpose to allow other uses
as well.

The packages consists of

* a C++ library (libGDSII) with API functions for reading, processing,
and exporting GDSII files

%package devel
Group: Development/C++
Summary: Development files for %name
%description devel
%summary

%package -n GDSIIConvert
Group:	Graphics
Summary: Reporting statistics on GDSII geometries and exporting them to other file formats
%description -n GDSIIConvert
A command-line executable code (GDSIIConvert) for reporting statistics
on GDSII geometries and exporting them to other file formats, notably
including the GMSH geometry format.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
install -D libGDSII-pkgconfig %buildroot%_pkgconfigdir/libGDSII.pc

rm -fv %buildroot%_libdir/*.a

%files
%doc README*
%_libdir/*.so.*

%files devel
%doc %_datadir/libGDSII
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n GDSIIConvert
%_bindir/*

%changelog
* Tue Oct 19 2021 Grigory Ustinov <grenka@altlinux.org> 0.21-alt2
- Removed static library.

* Mon Aug 05 2019 Fr. Br. George <george@altlinux.ru> 0.21-alt1
- Initial build for ALT

