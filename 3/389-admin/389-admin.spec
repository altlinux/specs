%global pkgname		dirsrv
%global groupname	%{pkgname}.target
%def_without selinux

Summary: 389 Administration Server
Name:    389-admin
Version: 1.1.46
Release: alt1
License: GPLv2
Url:     http://port389.org/
# VCS:   https://git.fedorahosted.org/git/389/admin.git
Group:   System/Servers

BuildRequires: 389-adminutil-devel apache2-devel apache2-mod_nss gcc-c++
BuildRequires: libicu-devel libsasl2-devel perl-Mozilla-LDAP perl-CGI
BuildRequires: 389-ds-base mozldap-devel libaprutil1-devel

Requires: apache2-httpd-worker
Requires: apache2-mod_nss
Requires: 389-ds-base

Provides: fedora-ds-adminserver = %version-%release
Obsoletes: fedora-ds-adminserver < %version-%release

Packager: Andrey Cherepanov <cas@altlinux.org>

Source0: %name-%version.tar
Source1: %{pkgname}-admin

%add_perl_lib_path %_libdir/%{pkgname}/perl

%description
Administration Server for 389 Directory Server. Use setup-ds-admin.pl to
setup.

%prep
%setup

%build
export icu_lib=-L%_libdir/
export adminutil_lib=-L%_libdir/
export adminutil_inc=/usr/include/libadminutil/
%add_optflags -I%_includedir/apu-1
%undefine _configure_gettext
%configure --localstatedir=/var \
           --with-modnss-lib=%_libdir/apache2/modules/ \
           --with-httpd=%_sbindir/httpd2.worker \
	   --with-apr-config=/usr/bin/apr-1-config \
	   --with-apxs=%apache2_apxs \
           --with-openldap \
%if_with selinux
           --with-selinux \
%endif
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-systemddirsrvgroupname=%{groupname}

%make

%install
%makeinstall_std

subst 's|%_libdir/httpd|%_libdir/apache2|' %buildroot%_sysconfdir/%{pkgname}/admin-serv/*.conf
subst 's|libmodnss.so|mod_nss.so|' %buildroot%_sysconfdir/%{pkgname}/admin-serv/*.conf
subst 's|%_sysconfdir/mime.types|%_sysconfdir/httpd2/conf/mime.types|' %buildroot%_sysconfdir/%{pkgname}/admin-serv/*.conf
subst 's|LoadModule file_cache_module|#LoadModule file_cache_module|' %buildroot%_sysconfdir/%{pkgname}/admin-serv/*.conf
subst 's|HostnameLookups off|HostnameLookups on|' %buildroot%_sysconfdir/%{pkgname}/admin-serv/httpd.conf

install -pDm755 %SOURCE1 %buildroot%_initdir/%{pkgname}-admin

rm -f %buildroot%_libdir/*.so

%post
%post_service %{pkgname}-admin

%preun
%preun_service %{pkgname}-admin

%files
%doc LICENSE
%dir %_sysconfdir/%pkgname/admin-serv
%config(noreplace)%_sysconfdir/%pkgname/admin-serv/*.conf
%_initdir/%{pkgname}-admin
%_datadir/%pkgname
%config(noreplace)%_sysconfdir/sysconfig/%{pkgname}-admin
%_unitdir/%{pkgname}-admin.service
%_sbindir/*
%_libdir/*.so.*
%_libdir/%pkgname
%_man8dir/*

%changelog
* Thu Nov 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.46-alt1
- New version 1.1.46

* Thu May 12 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.43-alt1
- New version

* Tue Apr 05 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.42-alt2
- Rebuild with new apache2
- Use %%apache2_apxs for apxs2 location

* Tue Nov 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.42-alt1
- New version
- SELinux support is disabled

* Fri Mar 21 2014 Timur Aitov <timonbl4@altlinux.org> 1.1.35-alt1
- 1.1.35

* Thu Jul 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.30-alt1
- 1.1.30

* Sat May 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.29-alt1
- 1.1.29

* Tue Mar 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.28-alt1
- 1.1.28

* Sat Sep 10 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.23-alt1
- 1.1.23

* Fri Aug 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.21-alt1
- 1.1.21

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.16-alt1
- 1.1.16

* Mon Feb 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.12-alt2
- Fix build

* Mon Nov 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.12-alt1
- 1.1.12

* Wed Sep 08 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.11-alt1
- 1.1.11

* Tue Jul 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.11-alt0.rc1.1
- 1.1.11-rc1

* Mon Mar 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.11-alt0.a2.1
- 1.1.11-a2

* Wed Jan 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.10-alt1
- 1.1.10-a2

* Wed Sep 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.9-alt2
- Autoreq with fixed rpm-build-perl
- Remove unused requires

* Wed Sep 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Mon Apr 27 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.7-alt2
- build repaired

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Fri Aug 01 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1
- Fedora-DS 1.1 Final release
- Resolve bug 357501: Console/admin express: can't view log files
- Resolve bug 186280: Close potential security vulnerabilities in CGI code
- Resolve bug 370071: Fixed issues with loading CRL files.
- Resolve bug 383301: Admin Server main html page refers to dsgw, org
- Resolve bug 368481: Unable to change Admin Server log paths in Console
- Resolve bug 370071: Fixed malloc issue when importing a CRL.
- Resolve bug 400341: Be sure to only change admin user's password in change-sie-password.
- Resolve bug 411231: [Admin express] help button brings up an error page
- Resolve bug 400421: unable to restart configDS via console
- Resolve bug 407011: GIF missing on the front page for admin web ui
- Resolve bug 420751: Console admin user unable to manage users&groups
- Resolve bug 425861: Instance creation through console is broken
- Resolve bug 425849: migrate-ds-admin.pl spins at 100 cpu
- Resolve bug 426056: Unable to connect to admin express via SSL - firefox cipher issues?

* Tue Oct 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071030
- CVS snapshot 20071030
- Resolves bug 317651: Clean up setup dialog text
- patches rename

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0.20071008
- CVS snapshot 20071008

* Wed May 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt0
- Initial
