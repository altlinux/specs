%define _name CCfits

Name: libccfits
Version: 2.6
Release: alt1

Summary: A C++ interface for cfitsio
Group: System/Libraries
License: BSD
Url: https://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits

Source: https://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits/%_name-%version.tar.gz

Patch: CCfits-2.6-alt-removerpath.patch

BuildRequires: autoconf-archive gcc-c++ gcc-fortran libcfitsio-devel

%description
CCfits is an object oriented interface to the cfitsio library. It is
designed to make the capabilities of cfitsio available to programmers
working in C++.
It is written in ANSI C++ and implemented using the C++ Standard Library
with namespaces, exception handling, and member template functions.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
These are the header files and libraries needed to develop a %name
application.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains the full API documentation for %name.

%prep
%setup -n %_name-%version
%patch -p1
rm -rf html/*.pl

%build
%configure --disable-static \
	--with-cfitsio-include=%_includedir/cfitsio
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/doc/%name
cp -R html %buildroot%_datadir/doc/%name/
rm -f %buildroot%_bindir/cookbook

%files
%_libdir/*.so.*
%doc License.txt

%files devel
%_libdir/*.so
%_pkgconfigdir/%_name.pc
%_includedir/%_name/
%doc CHANGES

%files devel-doc
%_datadir/doc/%name/

%changelog
* Fri Jul 23 2021 Yuri N. Sedunov <aris@altlinux.org> 2.6-alt1
- 2.6

* Wed May 26 2021 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1.1
- rebuilt against libcfitsio.so.9

* Fri Mar 18 2016 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- 2.5

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Apr 08 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt2
- fixed build with new libcfitsio-3.280-alt1

* Fri Jan 31 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt1
- fc package adapted for Sisyphus

