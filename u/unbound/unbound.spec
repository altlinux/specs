Name: unbound
Version: 1.4.17
Release: alt1
License: BSD
Url: http://unbound.net/
Source: %name-%version.tar
Summary: Validating, recursive, and caching DNS resolver
Group: System/Servers
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

%define _chrootdir %_localstatedir/%name
%define with_python 1

PreReq: chrooted
PreReq: lib%name = %version-%release

Provides: %name-chroot(%_chrootdir)

BuildRequires: /proc flex gcc-c++ libssl-devel libldns-devel bind-utils libldns-examples splint xxd libexpat-devel libevent-devel
%if %with_python
BuildRequires: python-devel swig
%endif

%description
Unbound is a validating, recursive, and caching DNS resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

%package control
Summary: Unbound remote server control
Group: System/Configuration/Other

%description control
Unbound-control performs remote administration on  the  unbound(8)  DNS
server.   It  reads the configuration file, contacts the unbound server
over SSL sends the command and displays the result.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
This package contains shared libraries used by %name's daemons
and clients.

%package -n lib%name-devel-static
Summary: Static library for %name
Group: System/Libraries
Obsoletes: lib%name-static

%description -n lib%name-devel-static
This package contains static libraries used by %name's daemons
and clients.

%package -n lib%name-devel
Summary: Development package that includes the %name header files
Group: Development/C
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-devel
The devel package contains the include files

%if %with_python
%package -n python-module-%name
Summary: Python modules and extensions for unbound
Group: Development/Python

%description -n python-module-%name
Python modules and extensions for unbound
%endif

%prep
%setup
rm -f ldns-src.tar.gz

%build
# configure with /var/unbound/unbound.conf so that all default chroot,
# pidfile and config file are in /var/unbound, ready for chroot jail set up.
#
# This is a build using libldns builtin version, the resulting binaries
# do not require libldns and this package does not have version dependencies.
# Could be smaller using a dependency on libldns (use --with-ldns=).
%autoreconf

%configure \
	    --with-conf-file=%_chrootdir/unbound.conf \
	    --with-username=_%name \
	    --with-libevent \
	    --with-pthreads \
%if %with_python
            --with-pythonmodule --with-pyunbound \
%endif
            --enable-sha2
%make

sed -i '/do-ip6/a	do-ip6: no' doc/example.conf
subst 's|# auto-trust-anchor-file:|auto-trust-anchor-file:|g' doc/example.conf

%install
%make DESTDIR=%buildroot install
install -d 0700 %buildroot%_localstatedir/%name
install -d 0755 %buildroot%_initdir
install -m 0755 %name.init %buildroot%_initdir/unbound
# add symbolic link from /etc/unbound.conf -> /var/unbound/unbound.conf
ln -s %_localstatedir/unbound/unbound.conf %buildroot%_sysconfdir/unbound.conf

%if %with_python
rm %buildroot%python_sitelibdir/*.la
%endif

%check
%make test

%pre
/usr/sbin/groupadd -r -f _%name
/usr/sbin/useradd -r -g _%name -d %_chrootdir -s /dev/null -n -c "Domain Name Server" _%name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc doc/README doc/CREDITS doc/LICENSE doc/FEATURES
%_initdir/%name
%attr(1775,root,_%name) %dir %_localstatedir/%name
%config(noreplace) %_localstatedir/%name/unbound.conf
%config(noreplace) %_sysconfdir/unbound.conf
%_sbindir/*
%_man1dir/*
%_man5dir/*
%_man8dir/*

%exclude %_sbindir/unbound-control
%exclude %_man8dir/unbound-control*

%files control
%_sbindir/unbound-control
%_man8dir/unbound-control*


%files -n lib%name
%_libdir/libunbound*so*
%_man3dir/*

%files -n lib%name-devel-static
%_libdir/libunbound.a

%files -n lib%name-devel
%_includedir/*

%if %with_python
%files -n python-module-%name
%python_sitelibdir/*
%doc libunbound/python/examples/*
%doc pythonmod/examples/*
%endif

%changelog
* Sun Jul 08 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.17-alt1
- 1.4.17

* Fri Feb 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.16-alt1
- 1.4.16

* Fri Dec 23 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.14-alt1
- 1.4.14
- Fix for VU#209659 CVE-2011-4528

* Thu Sep 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.13-alt1
- 1.4.13
- Add python-module-unbound subpackage

* Fri Jul 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.12-alt1
- 1.4.12

* Sun Jul 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.11-alt1
- 1.4.11

* Wed Jun 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.10-alt1
- 1.4.10
- Fix assertion failure when unbound generates an empty error reply
  in response to a query, CVE-2011-1922 VU#531342

* Sat Apr 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.9-alt1
- 1.4.9

* Mon Feb 07 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.8-alt4
- Rebuild with new libevent
- Fix init script
- Make devel subpackage noarch

* Thu Feb 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.8-alt3
- Use libevent1.4
- Fix init script

* Thu Feb 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.8-alt2
- Fix init script

* Thu Feb 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.8-alt1
- 1.4.8
- Build with libevent
- Update init for run unbound-anchor
- Enable by default auto-trust-anchor-file for DNSSEC

* Sat Nov 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.7-alt1
- 1.4.7

* Fri Aug 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.6-alt1
- 1.4.6
- Add make test and update BuildRequires

* Tue Jun 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.5-alt1
- 1.4.5

* Fri May 14 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.4-alt1
- 1.4.4

* Sun Apr 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sun Jan 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Dec 14 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed Nov 18 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.4-alt1
- 1.3.4

* Sat Aug 15 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Jun 16 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.0-alt1
- 1.3.0

* Thu Mar 26 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.1-alt1
- 1.2.1
- Build without --enable-debug

* Thu Nov 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt2
- Rename subpackage lib%name-static to lib%name-devel-static (http://www.altlinux.org/Drafts/SharedLibs)

* Mon Sep 15 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt1
- New version

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.1-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Thu Aug 07 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.1-alt1
- This version features bugfixes, a couple of fixes for looking up corner cases 
  (badly operated domains), and a cleanup of code for config file reading.

* Fri May 30 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.0-alt2
- Change owner of %_localstatedir/%name to root and add sticky bit
- Change default username to _%name

* Sun May 25 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.0-alt1
- Build for ALT
