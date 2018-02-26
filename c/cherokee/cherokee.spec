%define shortversion %(echo %{version} | sed -e 's/\([0-9]*\.[0-9]*\)\.[0-9]*/\1/')
%define wwwroot /var/www/cherokee

# This script is not only for Linux, so we have to hide it from rpm's req finder
# to avoid generated dependency on Solaris utilities... :)
%add_findreq_skiplist %_bindir/cherokee-panic

Name: cherokee
Version: 1.2.101
Release: alt2

Summary: Flexible and Fast Webserver
License: GPLv2+
Group: System/Servers

Url: http://www.cherokee-project.com/
Source: http://www.cherokee-project.com/download/%shortversion/%version/cherokee-%version.tar.gz
Source1: cherokee.init
Source2: cherokee.logrotate

Requires: %name-data = %version-%release

# Automatically added by buildreq on Sat Jun 11 2011
BuildRequires: bzlib-devel libGeoIP-devel libavformat-devel libldap-devel libmysqlclient-devel libpam-devel libpcre-devel libssl-devel php5-fpm-fcgi python-base

%description
Cherokee is a very fast, flexible and easy to configure Web Server. It supports
the widespread technologies nowadays: FastCGI, SCGI, PHP, CGI, TLS and SSL
encrypted connections, Virtual hosts, Authentication, on the fly encoding,
Apache compatible log files, and much more.

%package data
Summary: Architecture independent data files for cherokee web server
Group: System/Servers
BuildArch: noarch

%description data
Architecture independent data files for cherokee web server.

%package devel
Summary: Development files of cherokee
Group: Development/C
Requires: %name = %version-%release

%description devel
This package holds the development files for cherokee web server.

%prep
%setup

# Quick fix naive system pcre detection
subst 's#"pcre.h"#"pcre/pcre.h"#g' configure

%build
subst 's#/log/cherokee\.#/log/cherokee/cherokee\.#' cherokee.conf.sample.pre
%configure -with-wwwroot=%wwwroot --localstatedir=/var --docdir=%_datadir/cherokee \
	--disable-static --disable-internal-pcre
# strip rpath
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std
install -d %buildroot%_logdir/cherokee
install -pDm 755 %_sourcedir/cherokee.init %buildroot%_initrddir/cherokee
install -pDm 644 %_sourcedir/cherokee.logrotate %buildroot/etc/logrotate.d/cherokee

%find_lang cherokee

%post
%post_service cherokee

%preun
%preun_service cherokee

%files -f cherokee.lang
%dir %_sysconfdir/cherokee
%config(noreplace) %_sysconfdir/cherokee/*
%config(noreplace) %_initrddir/cherokee
%config(noreplace) /etc/logrotate.d/cherokee
%_bindir/*
%_sbindir/*
%_libdir/cherokee
%_libdir/lib*.so.*
%_man1dir/*
%_logdir/cherokee
%exclude %_libdir/cherokee/*.la
%exclude %_bindir/cherokee-config

%files data
%_datadir/cherokee
%wwwroot/

%files devel
%_bindir/cherokee-config
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_datadir/aclocal/*

%changelog
* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.2.101-alt2
- Fix RPATH issue.

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.101-alt1.1
- Rebuild with Python-2.7

* Sun Oct 23 2011 Victor Forsiuk <force@altlinux.org> 1.2.101-alt1
- 1.2.101

* Sat Jun 11 2011 Victor Forsiuk <force@altlinux.org> 1.2.98-alt1
- 1.2.98

* Fri Mar 25 2011 Victor Forsiuk <force@altlinux.org> 1.2.2-alt1
- 1.2.2

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Feb 22 2011 Victor Forsiuk <force@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Feb 11 2011 Victor Forsiuk <force@altlinux.org> 1.0.20-alt1
- 1.0.20

* Wed Feb 02 2011 Victor Forsiuk <force@altlinux.org> 1.0.19-alt1
- 1.0.19

* Wed Jan 12 2011 Victor Forsiuk <force@altlinux.org> 1.0.16-alt1
- 1.0.16

* Thu Dec 30 2010 Victor Forsiuk <force@altlinux.org> 1.0.15-alt1
- 1.0.15

* Tue Dec 14 2010 Victor Forsiuk <force@altlinux.org> 1.0.14-alt1
- 1.0.14

* Mon Dec 06 2010 Victor Forsiuk <force@altlinux.org> 1.0.12-alt1
- 1.0.12

* Thu Nov 25 2010 Victor Forsiuk <force@altlinux.org> 1.0.10-alt1
- 1.0.10

* Tue Aug 17 2010 Victor Forsiuk <force@altlinux.org> 1.0.8-alt1
- 1.0.8

* Tue Aug 10 2010 Victor Forsiuk <force@altlinux.org> 1.0.7-alt1
- 1.0.7

* Mon Jul 12 2010 Victor Forsiuk <force@altlinux.org> 1.0.5-alt1
- 1.0.5

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue May 25 2010 Victor Forsiuk <force@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 0.99.44-alt1
- 0.99.44

* Fri Feb 19 2010 Victor Forsiuk <force@altlinux.org> 0.99.43-alt1
- 0.99.43

* Fri Jan 29 2010 Victor Forsyuk <force@altlinux.org> 0.99.42-alt1
- 0.99.42. This release fixes a regression introduced in previous version.
  Upgrading is strongly encouraged.

* Wed Jan 27 2010 Victor Forsyuk <force@altlinux.org> 0.99.41-alt1
- 0.99.41

* Mon Jan 11 2010 Victor Forsyuk <force@altlinux.org> 0.99.39-alt1
- 0.99.39

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 0.99.37-alt1
- 0.99.37

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 0.99.35-alt1
- 0.99.35

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.27-alt1.1
- Rebuilt with python 2.6

* Fri Nov 06 2009 Victor Forsyuk <force@altlinux.org> 0.99.27-alt1
- 0.99.27

* Sun Nov 01 2009 Victor Forsyuk <force@altlinux.org> 0.99.26-alt1
- 0.99.26

* Mon Sep 28 2009 Victor Forsyuk <force@altlinux.org> 0.99.24-alt2
- Added condstop initscript target.
- Split architecture independent data files to noarch subpackage.

* Fri Sep 18 2009 Victor Forsyuk <force@altlinux.org> 0.99.24-alt1
- Initial build.
