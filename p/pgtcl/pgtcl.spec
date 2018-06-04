%define _unpackaged_files_terminate_build 1

Name: pgtcl
Version: 2.1.1
Release: alt1
Summary: Postgresql binding tcl lib
Group: Development/Tcl
License: BSD-like
Url: https://sourceforge.net/projects/pgtclng

Source: %name.tar
Patch1: %name-%version-alt.patch

# Automatically added by buildreq on Mon Mar 12 2007
BuildRequires: postgresql-devel tcl-devel

%description
Library for access PostgreSQL database from Tcl

%prep
%setup -q -c
%patch1 -p1

%build
%autoreconf
%configure
%make

%install
%makeinstall pkglibdir=%buildroot%_libdir/tcl
mkdir -p %buildroot%_datadir/tcl/pgtcl
mv %buildroot%_libdir/tcl/pkgIndex.tcl %buildroot%_datadir/tcl/pgtcl/
sed -i 's:\<lib\>:%_lib:g' %buildroot%_datadir/tcl/pgtcl/pkgIndex.tcl

%files
%_includedir/*.h
%_libdir/tcl/*.so
%_datadir/tcl/pgtcl

%changelog
* Wed May 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.1-alt1
- Updated to upstream version 2.1.1.

* Mon Jan 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt3
- fix build

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt2
- rebuild

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt1
- update to 1.6.2
- cleanup spec

* Mon Apr 16 2007 Denis Smirnov <mithraen@altlinux.ru> 1.6-alt3
- fix x86_64 build (thanks to at@)

* Mon Mar 12 2007 Denis Smirnov <mithraen@altlinux.ru> 1.6-alt2
- fix x86_64 build

* Mon Mar 12 2007 Denis Smirnov <mithraen@altlinux.ru> 1.6-alt1
- first build for Sisyphus
