#Module-Specific definitions
%define mod_name mod_dbi_pool
%define mod_conf A79_%mod_name
%define mod_so %mod_name.so

Summary: Provides database connection pooling services for the apache web server
Name: apache2-mod_dbi_pool
Version: 0.4.0
Release: alt1
Group: System/Servers
License: GPL
Url: http://www.outoforder.cc/projects/apache/mod_dbi_pool/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.outoforder.cc/downloads/mod_dbi_pool/%mod_name-%version.tar.bz2
Source1: %mod_conf.conf
Source2: %mod_conf.load
Patch: mod_dbi_pool-0.4.0-module.diff

# Automatically added by buildreq on Mon Feb 09 2009
BuildRequires: apache2-devel gcc-c++ libdbi-devel

%description
mod_dbi_pool provides database connection pooling services for other Apache
Modules. Using libdbi it allows other modules to have a dynamic pool of
database connections for many common SQL Servers, including mSQL, MySQL,
PostgreSQL, Oracle, SQLite and FreeTDS (MSSQL/Sybase).

%package devel
Summary: Development files for %mod_name
Group: Development/C

%description devel
mod_dbi_pool provides database connection pooling services for other Apache
Modules. Using libdbi it allows other modules to have a dynamic pool of
database connections for many common SQL Servers, including mSQL, MySQL,
PostgreSQL, Oracle, SQLite and FreeTDS (MSSQL/Sybase).

This package contains headers for %mod_name.

%prep
%setup -q -n %mod_name-%version
%patch0 -p1

# stupid libtool...
%__subst "s|libmod_dbi_pool|mod_dbi_pool|g" src/Makefile*

# lib64 fixes
find . -maxdepth 1 -type f| xargs %__subst "s|/lib\b|/%_lib|g"

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
%configure --with-apxs=%_sbindir/apxs2

%make_build

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
mkdir -p %buildroot%_includedir/apache2/
install -m 644 src/.libs/%mod_name.so %buildroot%apache2_moduledir/%mod_name.so
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %buildroot%apache2_mods_available

install -m0644 include/mod_dbi_pool.h %buildroot%_includedir/apache2/

%files
%doc LICENSE
%apache2_mods_available/*.load
%config %apache2_mods_available/*.conf
%apache2_moduledir/*.so

%files devel
%_includedir/apache2/*.h

%changelog
* Mon Feb 09 2009 Boris Savelev <boris@altlinux.org> 0.4.0-alt1
- initial build for Sisyphus from Mandriva

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-5mdv2009.0
+ Revision: 234919
- rebuild

* Thu Jun 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-4mdv2009.0
+ Revision: 215565
- fix rebuild
- hard code %%{_localstatedir}/lib to ease backports

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.4.0-3mdv2008.1
+ Revision: 135820
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-3mdv2008.0
+ Revision: 82552
- rebuild

* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdv2007.1
+ Revision: 140664
- rebuild

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2007.0
+ Revision: 79400
- Import apache-mod_dbi_pool

* Wed Aug 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdv2007.0
- initial Mandriva package

