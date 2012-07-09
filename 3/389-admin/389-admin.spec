Summary: 389 Administration Server
Name: 389-admin
Version: 1.1.30
Release: alt1
License: GPLv2
Url: http://port389.org/
Group: System/Servers
# Automatically added by buildreq on Mon Aug 17 2009
BuildRequires: 389-adminutil-devel apache2-devel apache2-mod_nss gcc-c++ libicu-devel libsasl2-devel perl-Mozilla-LDAP perl-CGI 389-ds mozldap-devel

Requires: apache2-httpd-worker
Requires: apache2-mod_nss

%add_perl_lib_path %_libdir/fedora-ds/perl

Provides: fedora-ds-adminserver = %version-%release
Obsoletes: fedora-ds-adminserver < %version-%release

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version-%release.tar

%description
Administration Server for 389 Directory Server. Use setup-ds-admin.pl to setup.

%prep
%setup
# rm -f ltmain.sh
# %autoreconf

%build
export icu_lib=-L%_libdir/
export adminutil_lib=-L%_libdir/
export adminutil_inc=/usr/include/libadminutil/

%configure --localstatedir=/var --with-modnss-lib=%_libdir/apache2/modules/ \
           --with-httpd=%_sbindir/httpd2.worker --with-apxs=%_sbindir/apxs2 \
           --with-openldap --with-selinux

%make

%install

%make_install DESTDIR=%buildroot install
%__subst 's|%_libdir/httpd|%_libdir/apache2|' %buildroot%_sysconfdir/fedora-ds/admin-serv/*.conf
%__subst 's|libmodnss.so|mod_nss.so|' %buildroot%_sysconfdir/fedora-ds/admin-serv/*.conf
%__subst 's|%_sysconfdir/mime.types|%_sysconfdir/httpd2/conf/mime.types|' %buildroot%_sysconfdir/fedora-ds/admin-serv/*.conf
%__subst 's|LoadModule file_cache_module|#LoadModule file_cache_module|' %buildroot%_sysconfdir/fedora-ds/admin-serv/*.conf
%__subst 's|HostnameLookups off|HostnameLookups on|' %buildroot%_sysconfdir/fedora-ds/admin-serv/httpd.conf

%post
%post_service fedora-ds-admin

%preun
%preun_service fedora-ds-admin

%files
%doc COPYING AUTHORS NEWS README
%_libdir/fedora-ds
%_libdir/*.so.*
%_sbindir/*
%_datadir/fedora-ds
%dir                    %_sysconfdir/fedora-ds/admin-serv
%config(noreplace)      %_sysconfdir/fedora-ds/admin-serv/*.conf
%config(noreplace)      %_sysconfdir/sysconfig/fedora-ds-admin
%_initdir/fedora-ds-admin
%_man8dir/*.gz

%changelog
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
