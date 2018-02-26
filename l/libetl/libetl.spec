%define oname ETL
Name: libetl
Version: 0.04.14
Release: alt1

Summary: Voria Extended Class and Template Library
Summary(ru_RU.KOI8-R): Библиотека шаблонов и классов общего назначения

License: GPL
Group: Development/C++
Url: http://www.synfig.com

Packager: Yuriy Shirokov <yushi@altlinux.org>

# git clone git://synfig.git.sourceforge.net/gitroot/synfig/synfig
Source: http://prdownloads.sf.net/synfig/%oname-%version.tar

# Automatically added by buildreq on Fri Jan 12 2007
BuildRequires: gcc-c++

%package devel
Summary: Voria Extended Class and Template Library
Group: Development/C++

%description
VoriaETL is a multiplatform class and template library
designed to complement and supplement the C++ STL.

%description devel
VoriaETL is a multiplatform class and template library
designed to complement and supplement the C++ STL.

%prep
%setup -q -n %oname-%version

%build
%autoreconf
%configure

%install
%makeinstall_std

%files devel
%_bindir/ETL-config
%_includedir/ETL/
%_pkgconfigdir/ETL.pc

%changelog
* Sat Jun 18 2011 Yuriy Shirokov <yushi@altlinux.org> 0.04.14-alt1
- new version 0.04.14

* Tue Mar 23 2010 Yuriy Shirokov <yushi@altlinux.org> 0.04.13-alt1
- new version 0.04.13

* Wed Oct 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04.12-alt1
- new version 0.04.12 (with rpmrb script)

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04.11-alt1
- new version 0.04.11 (with rpmrb script)

* Fri Oct 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.04.10-alt1
- new version 0.04.10 (with rpmrb script)

* Sun Jul 01 2007 Vitaly Lipatov <lav@altlinux.ru> 0.04.09-alt1
- new version 0.04.09 (with rpmrb script)

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.04.08-alt1
- initial build for ALT Linux Sisyphus

