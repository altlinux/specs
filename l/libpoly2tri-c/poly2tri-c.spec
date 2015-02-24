%define _name poly2tri-c
%define ver_major 0.1
%define api_ver %ver_major

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A 2D constrained Delaunay triangulation library
Group: System/Libraries
License: BSD
Url: http://code.google.com/p/%_name/
#VCS: https://code.google.com/p/poly2tri-c/
Source: %_name-%version.tar

BuildRequires: glib2-devel >= 2.28

%description
Poly2Tri-C: A library for generating, refining and rendering
2-Dimensional Constrained Delaunay Triangulations

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for %name.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-static
%make

%install
%makeinstall_std

%files
%_bindir/p2tc
%_libdir/%name-%api_ver.so.*
%doc LICENSE* README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name.pc

%changelog
* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus

