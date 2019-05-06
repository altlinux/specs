%define _name poly2tri-c
%define ver_major 0.1
%define api_ver %ver_major

Name: lib%_name
Version: %ver_major.0
Release: alt2.1

Summary: A 2D constrained Delaunay triangulation library
Group: System/Libraries
License: BSD

Url: http://code.google.com/p/%_name/
# Automatically exported from code.google.com/p/poly2tri-c
# VCS: https://github.com/Paul-Browne/poly2tri-c
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
# with gcc5 produce error: ISO C does not support '__FUNCTION__' predefined identifier
sed -i 's/-pedantic//' configure.ac
%autoreconf
%configure --disable-static
%ifarch %e2k
# lcc: "sweep.c", line 989: error: missing return statement at end of non-void function
sed -i 's,-Werror,& -Wno-error=return-type,' poly2tri-c/p2t/{sweep,common}/Makefile
%endif
%make_build

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
* Mon May 06 2019 Michael Shigorin <mike@altlinux.org> 0.1.0-alt2.1
- fixed build with lcc on e2k
- enabled parallel build
- updated source git notice (aris@)

* Mon Jul 06 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt2
- fixed build with gcc5

* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus

