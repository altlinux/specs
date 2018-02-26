#Module-Specific definitions
%define apache_version 2.2.6
%define mod_name mod_vhost_limit
%define mod_conf B22_%mod_name
%define mod_so %mod_name.so

Summary: Restrict the number of simultaneous connections per vhost
Name: apache2-mod_vhost_limit
Version: 0.2
Release: alt1
Group: System/Servers
License: Apache License
Url: http://apache.ivn.cl/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://apache.ivn.cl/files/source/%mod_name-%version.tgz
Source1: %mod_conf.conf
Source2: %mod_conf.load

# Automatically added by buildreq on Mon Feb 09 2009
BuildRequires: apache2-devel

%description
Restrict the number of simultaneous connections per vhost.

%prep
%setup -q -n %mod_name-%version

%build
%_sbindir/apxs2 -c %mod_name.c

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
install -m 644 .libs/%mod_name.so %buildroot%apache2_moduledir/%mod_name.so
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %buildroot%apache2_mods_available

%files
%apache2_mods_available/*.load
%config %apache2_mods_available/*.conf
%apache2_moduledir/*.so

%changelog
* Mon Feb 09 2009 Boris Savelev <boris@altlinux.org> 0.2-alt1
- initial build for Sisyphus from Mandriva

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-4mdv2009.0
+ Revision: 235123
- rebuild

* Thu Jun 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-3mdv2009.0
+ Revision: 215667
- fix rebuild
- fix buildroot

* Fri Mar 07 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2008.1
+ Revision: 181979
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdv2008.1
+ Revision: 103917
- import apache-mod_vhost_limit

* Tue Oct 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdv2008.1
- initial Mandriva package
