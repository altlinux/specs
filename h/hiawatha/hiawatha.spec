Name: hiawatha
Version: 10.5
Release: alt1

Summary: A secure and advanced webserver
License: GPLv2+
Group: System/Servers

Url: http://www.hiawatha-webserver.org/
Source0: http://www.hiawatha-webserver.org/files/hiawatha-%version.tar.gz
Source1: hiawatha.init
Source2: hiawatha.logrotate
Patch0: hiawatha-9.15-nobody99.patch
Patch1: hiawatha-9.15-libs-in-system-place.patch

BuildRequires(pre): cmake
# Automatically added by buildreq on Tue Feb 17 2015
# optimized out: cmake-modules libcloog-isl4 libxml2-devel pkg-config
BuildRequires: cmake libxslt-devel zlib-devel

%description
Hiawatha is an advanced and secure Web server for Unix.

It has been written with security as its main goal. It's very
secure and fast and is really easy to configure. It features
a rootjail, the ability to run CGIs under any UID/GID you want,
prevention of SQL injection and cross-site scripting, banning of
clients who try such exploits, and many other features. These
features make Hiawatha an interesting Web server for those who
need more security than what the other available Web servers
are offering.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%cmake_insource \
    -DCMAKE_INSTALL_NAME_DIR=%_libdir \
    -DLIB_INSTALL_DIR=%_libdir \
    -DCONFIG_DIR=%_sysconfdir/%name \
    -DWEBROOT_DIR=%_var/www/%name \
    -DWORK_DIR=%_localstatedir/%name \
    -DLOG_DIR=%_logdir/%name \
    -DPID_DIR=%_runtimedir \
    -DENABLE_CACHE=On \
    -DENABLE_IPV6=On \
    -DENABLE_MONITOR=On \
    -DENABLE_RPROXY=On \
    -DENABLE_TLS=On \
    -DENABLE_TOMAHAWK=On \
    -DENABLE_TOOLKIT=On \
    -DENABLE_XSLT=On \
    -DENABLE_ZLIB_SUPPORT=On \
    #
%make_build

%install
%makeinstall_std
install -d %buildroot%_logdir/hiawatha
install -pDm755 %_sourcedir/hiawatha.init %buildroot%_initdir/hiawatha
install -pDm644 %_sourcedir/hiawatha.logrotate \
	%buildroot%_logrotatedir/hiawatha

%post
%post_service hiawatha

%preun
%preun_service hiawatha

%files
%dir %_sysconfdir/hiawatha
%config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_initrddir/%name
%config(noreplace) %_logrotatedir/%name
%dir %_var/www/%name
%config(noreplace) %_var/www/%name/*
%_bindir/ssi-cgi
%_sbindir/cgi-wrapper
%_sbindir/%name
%_sbindir/wigwam
%_libdir/*.so.*
%_man1dir/*
%_logdir/%name

%changelog
* Fri Jan 27 2017 Michael Shigorin <mike@altlinux.org> 10.5-alt1
- 10.5

* Thu Oct 06 2016 Michael Shigorin <mike@altlinux.org> 10.4-alt1
- 10.4

* Wed Jun 15 2016 Michael Shigorin <mike@altlinux.org> 10.3-alt1
- 10.3

* Tue May 03 2016 Michael Shigorin <mike@altlinux.org> 10.2-alt1
- 10.2

* Fri Feb 12 2016 Michael Shigorin <mike@altlinux.org> 10.1-alt1
- new version 10.1

* Fri Nov 27 2015 Michael Shigorin <mike@altlinux.org> 10.0-alt1
- new version 10.0

* Thu Oct 29 2015 Michael Shigorin <mike@altlinux.org> 9.15-alt1
- 9.15
- updated patches

* Tue Feb 17 2015 Michael Shigorin <mike@altlinux.org> 9.12-alt1
- 9.12 (closes: #30743, #30748)
- built with mbedtls instead of polarssl, see
  https://www.hiawatha-webserver.org/weblog/86
- minor spec cleanup

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 9.0-alt1
- New version (ALT #28848)

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 7.8.2-alt1
- 7.8.2

* Wed Aug 31 2011 Victor Forsiuk <force@altlinux.org> 7.6-alt1
- 7.6

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 7.5-alt1
- 7.5

* Sat Apr 09 2011 Victor Forsiuk <force@altlinux.org> 7.4.1-alt1
- 7.4.1

* Mon Mar 28 2011 Victor Forsiuk <force@altlinux.org> 7.4-alt2
- Fix BuildRequires.

* Mon Nov 15 2010 Victor Forsiuk <force@altlinux.org> 7.4-alt1
- 7.4

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 7.3-alt1
- 7.3

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 7.1-alt1
- 7.1

* Mon Feb 15 2010 Victor Forsiuk <force@altlinux.org> 7.0-alt1
- 7.0

* Mon Dec 07 2009 Victor Forsyuk <force@altlinux.org> 6.19-alt1
- 6.19

* Wed Nov 25 2009 Victor Forsyuk <force@altlinux.org> 6.18-alt2
- Add condstop target to init-script.

* Mon Nov 16 2009 Victor Forsyuk <force@altlinux.org> 6.18-alt1
- Initial build.
