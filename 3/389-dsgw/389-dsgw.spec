%define pkgname dirsrv

Summary:  389 Directory Server Gateway (dsgw)

Name:     389-dsgw
Version:  1.1.11
Release:  alt2
License:  GPLv2
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Url:      http://port389.org
# VCS:	  https://git.fedorahosted.org/git/389/dsgw.git
Group:    System/Servers

BuildRequires: 389-adminutil-devel gcc-c++ libicu-devel libsasl2-devel libicu-devel mozldap-devel
BuildRequires: perl-Mozilla-LDAP perl-CGI

Provides: fedora-ds-dsgw = %version-%release
Obsoletes: fedora-ds-dsgw < %version-%release

Source0: %name-%version-%release.tar

%description
389 Directory Server Gateway is a collection of 3 web applications
that run on top of the Administration Server used by the Directory
Server.  These 3 applications are:
* phonebook - a simple phonebook application geared towards end users,
with simple search screens and simple self-service management
* orgchart - an organization chart viewer
* gateway - a more advanced search interface that allows admins to
create and edit user entries, and allows creation of templates for
different types of user and group entries

%prep
%setup

%autoreconf

%build

# get adminutil locations
export adminutil_inc=/usr/include/libadminutil
export adminutil_lib=-L%_libdir/

# force the use of the admin server
%undefine _configure_gettext
%configure --with-admserv=/usr/share/%pkgname/html/ \
           --with-ldapsdk-inc=/usr/include/mozldap \
	   --with-ldapsdk-lib=%_libdir \
	   --with-instconfigdir=/etc/%pkgname/ \
	   --with-adminserver

%make_build

%install
%makeinstall_std

%files
%config %_sysconfdir/%pkgname/dsgw/*
%_libdir/%pkgname/dsgw-cgi-bin/*
%_datadir/%pkgname/dsgw/*
%_datadir/%pkgname/manual/en/dsgw/*
%_datadir/%pkgname/properties/dsgw/*
%_sbindir/setup-ds-dsgw

%changelog
* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.11-alt2
- Rebuild with new icu

* Tue Nov 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.11-alt1
- New version

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.9-alt1.qa1
- NMU: rebuilt with libicuuc.so.50.

* Sat May 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Fri Aug 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.6-alt2
- rebuild with icu-4.6

* Mon Nov 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Tue Jul 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Mon Oct 12 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt2
- fix build (add libicu-devel to buildreq)

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Tue Jun 02 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt3
- build with 389-adminutil instead of fedora-ds-adminutil

* Mon May 25 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt2
- rename to 389-dsgw

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1
- Initial release

