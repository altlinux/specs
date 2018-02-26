#Module-Specific definitions
%define mod_name mod_macro
%define mod_conf 30_%mod_name
%define mod_so %mod_name.so

Summary: DSO module for the apache web server
Name: apache2-mod_macro
Version: 1.1.10
Release: alt1
Group: System/Servers
License: BSD-style
Url: http://www.coelho.net/mod_macro/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.cri.ensmp.fr/~coelho/mod_macro/%mod_name-%version.tar.gz
Source1: %mod_conf.load
Source2: %mod_conf.conf

# Automatically added by buildreq on Mon Feb 09 2009
BuildRequires: apache2-devel

%description
mod_macro allows the definition and use of macros within apache
runtime configuration files. The syntax is a natural extension to
apache html-like configuration style.

%prep
%setup -q -n %mod_name-%version

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
%_sbindir/apxs2 -c mod_macro.c

%install
mkdir -p %buildroot%apache2_moduledir
mkdir -p %buildroot%apache2_mods_available
install -m 644 .libs/%mod_name.so %buildroot%apache2_moduledir/%mod_name.so
install -m 644 %SOURCE1 %buildroot%apache2_mods_available
install -m 644 %SOURCE2 %buildroot%apache2_mods_available

%files
%doc CHANGES INSTALL README mod_macro.html
%apache2_mods_available/*.load
%config %apache2_mods_available/*.conf
%apache2_moduledir/*.so

%changelog
* Mon Feb 09 2009 Boris Savelev <boris@altlinux.org> 1.1.10-alt1
- initial build for Sisyphus from Mandriva

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.10-3mdv2009.0
+ Revision: 235052
- rebuild

* Thu Jun 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.10-2mdv2009.0
+ Revision: 215606
- fix rebuild

* Sat May 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.10-1mdv2009.0
+ Revision: 205389
- 1.1.10

* Fri Mar 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.8-5mdv2008.1
+ Revision: 181802
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:1.1.8-4mdv2008.1
+ Revision: 170735
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.8-3mdv2008.0
+ Revision: 82614
- rebuild

* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.8-2mdv2007.1
+ Revision: 140718
- rebuild

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.8-1mdv2007.0
+ Revision: 79463
- Import apache-mod_macro

* Sat Aug 26 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.8-1mdv2007.0
- 1.1.8

* Mon Jul 03 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.7-1mdv2007.0
- 1.1.7
- drop the advertizing patch, better fix upstream

* Fri Dec 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.6-2mdk
- rebuilt against apache-2.2.0

* Mon Nov 28 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.6-1mdk
- fix versioning

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.54_1.1.6-2mdk
- fix deps

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.54_1.1.6-1mdk
- rename the package
- the conf.d directory is renamed to modules.d
- use new rpm-4.4.x pre,post magic

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.53_1.1.6-4mdk
- use the %%mkrel 1

* Mon Feb 28 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.53_1.1.6-3mdk
- fix %%post and %%postun to prevent double restarts
- fix bug #6574

* Wed Feb 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.53_1.1.6-2mdk
- spec file cleanups, remove the ADVX-build stuff

* Tue Feb 08 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.53_1.1.6-1mdk
- rebuilt for apache 2.0.53

* Wed Sep 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.52_1.1.6-1mdk
- built for apache 2.0.52

* Fri Sep 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.51_1.1.6-1mdk
- built for apache 2.0.51

* Wed Sep 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.50_1.1.6-1mdk
- 1.1.6

* Tue Jul 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.50_1.1.5-1mdk
- built for apache 2.0.50
- remove redundant provides

* Tue Jun 15 2004 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.0.49_1.1.5-1mdk
- built for apache 2.0.49

