#Module-Specific definitions
%define mod_name mod_vdbh
%define mod_conf 21_%mod_name
%define mod_so %mod_name

Summary: A Virtual Database Hosting DSO module for the apache web server
Name: apache2-mod_vdbh
Version: 1.0.3
Release: alt1.1
Group: System/Servers
License: GPL
Url: http://www.synthemesc.com/mod_vdbh/
Packager: Boris Savelev <boris@altlinux.org>

Source: %mod_name-%version.tar.bz2
Source1: %mod_conf.conf
Source2: %mod_conf.load

# Automatically added by buildreq on Mon Feb 09 2009
BuildRequires: apache2-devel libMySQL-devel

%description
mod_vdbh is an Apache Web Server module allowing mass virtual
hosting without the need for file based configuration. The virtual
host paths are translated from a MySQL database at request time,
thus the configuration can be changed without having to restart
Apache Web Server.

%prep
%setup -q -n %mod_name-%version

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
%_sbindir/apxs2 -DHAVE_STDDEF_H -I%_includedir/mysql -L%_libdir -Wl,-lmysqlclient -c mod_vdbh.c

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
install -m 644 .libs/%mod_name.so %buildroot%apache2_moduledir/%mod_name.so
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %buildroot%apache2_mods_available

%files
%doc AUTHORS README TODO
%apache2_mods_available/*.load
%config %apache2_mods_available/*.conf
%apache2_moduledir/*.so

%changelog
* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Mon Feb 09 2009 Boris Savelev <boris@altlinux.org> 1.0.3-alt1
- initial build for Sisyphus from Mandriva

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-9mdv2009.0
+ Revision: 235119
- rebuild

* Thu Jun 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-8mdv2009.0
+ Revision: 215663
- fix rebuild
- fix buildroot

* Fri Mar 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-7mdv2008.1
+ Revision: 181958
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-6mdv2008.0
+ Revision: 82692
- rebuild

* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-5mdv2007.1
+ Revision: 140769
- rebuild

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-4mdv2007.0
+ Revision: 79539
- Import apache-mod_vdbh

* Tue Sep 05 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-1mdv2007.0
- rebuilt against MySQL-5.0.24a-1mdv2007.0 due to ABI changes

* Mon Aug 07 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-3mdv2007.0
- rebuild

* Sun Dec 18 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-2mdk
- rebuilt against apache-2.2.0

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.3-1mdk
- rebuilt against MySQL-5.0.15
- fix versioning

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.54_1.0.3-2mdk
- fix deps

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.54_1.0.3-1mdk
- rename the package
- the conf.d directory is renamed to modules.d
- use new rpm-4.4.x pre,post magic

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.53_1.0.3-4mdk
- use the %%mkrel macro

* Mon Feb 28 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.53_1.0.3-3mdk
- fix %%post and %%postun to prevent double restarts
- fix bug #6574

* Wed Feb 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.53_1.0.3-2mdk
- spec file cleanups, remove the ADVX-build stuff

* Tue Feb 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.53_1.0.3-1mdk
- rebuilt for apache 2.0.53

* Tue Jan 25 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.52_1.0.3-2mdk
- rebuilt against MySQL-4.1.x system libs
- nuke redundant deps

* Wed Sep 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.52_1.0.3-1mdk
- built for apache 2.0.52

* Fri Sep 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.51_1.0.3-1mdk
- built for apache 2.0.51

* Tue Jul 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.50_1.0.3-1mdk
- built for apache 2.0.50
- remove redundant provides

* Tue Jun 15 2004 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.0.49_1.0.3-1mdk
- built for apache 2.0.49

