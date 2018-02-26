#Module-Specific definitions
%define mod_name mod_vhost_dbi
%define mod_conf A80_%mod_name
%define mod_so %mod_name.so

Summary: Provides database connection pooling services for the apache web server
Name: apache2-mod_vhost_dbi
Version: 0.1.0
Release: alt1
Group: System/Servers
License: GPL
Url: http://www.outoforder.cc/projects/apache/mod_vhost_dbi/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.outoforder.cc/downloads/mod_vhost_dbi/%mod_name-%version.tar.bz2
Source1: %mod_conf.conf
Source2: %mod_conf.load
Patch: mod_vhost_dbi-0.1.0-module.diff

# Automatically added by buildreq on Tue Feb 10 2009
BuildRequires: apache2-mod_dbi_pool-devel gcc-c++ libdbi-devel

%description
mod_vhost_dbi creates virtual hosts for Apache 2.0 completely dynamically,
without the need to edit your configuration file or restart Apache if you
change a Vhost.

%prep
%setup -q -n %mod_name-%version
%patch0 -p1

# stupid libtool...
%__subst "s|libmod_vhost_dbi|mod_vhost_dbi|g" src/Makefile*

# lib64 fixes
find . -maxdepth 1 -type f| xargs %__subst "s|/lib\b|/%_lib|g"

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
%configure --with-apxs=%_sbindir/apxs2
%make

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
install -m 644 src/.libs/%mod_name.so %buildroot%apache2_moduledir/%mod_name.so
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %buildroot%apache2_mods_available

%files
%doc TODO
%apache2_mods_available/*.load
%config %apache2_mods_available/*.conf
%apache2_moduledir/*.so

%changelog
* Tue Feb 10 2009 Boris Savelev <boris@altlinux.org> 0.1.0-alt1
- initial build for Sisyphus from Mandriva

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-5mdv2009.0
+ Revision: 235121
- rebuild

* Thu Jun 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-4mdv2009.0
+ Revision: 215665
- fix rebuild
- hard code %%{_localstatedir}/lib to ease backports

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.1.0-3mdv2008.1
+ Revision: 135823
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-3mdv2008.0
+ Revision: 82695
- rebuild

* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-2mdv2007.1
+ Revision: 140771
- rebuild

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdv2007.0
+ Revision: 79543
- Import apache-mod_vhost_dbi

* Wed Aug 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-1mdv2007.0
- initial Mandriva package

