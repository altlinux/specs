Summary: A free SOCKS v4/v5 client implementation
Name: dante
Version: 1.4.2
Release: alt1
License: BSD-type
Group: Security/Networking
Url: http://www.inet.no/dante/
Source: ftp://ftp.inet.no/pub/socks/%name-%version.tar.gz
Source1: sockd.init
Source2: pam_userdb.passwd
Source3: sockd.conf
Source4: sockd.sysconfig
Source5: sockd.pam
Source6: pam_userdb.passwd.1
Patch0:	dante-am.patch
Patch1:	dante-build.patch
Patch2:	dante-cpp.patch

# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 perl python-base
BuildRequires: flex libpam0-devel libwrap-devel db4.7-utils

%description
Dante is a free implementation of the SOCKS proxy protocol, version 4,
and version 5 (rfc1928). It can be used as a firewall between
networks. It is being developed by Inferno Nettverk A/S, a Norwegian
consulting company. Commercial support is available.

This package contains the dynamic libraries required to "socksify"
existing applications, allowing them to automatically use the SOCKS
protocol.

%package server
Summary: A free SOCKS v4/v5 server implementation
Group: Security/Networking
Requires: dante

%description server
This package contains "sockd", the SOCKS proxy daemon and its
documentation.  This is the server part of the Dante SOCKS proxy
package and allows SOCKS clients to connect through it to the external
network.

%package devel
Summary: development libraries for SOCKS
Group: Development/C
Requires: dante

%description devel
Additional libraries required to compile programs that use SOCKS.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure \
	--disable-silent-rules \
	--without-glibc-secure \
	--without-upnp
%make_build
%SOURCE2 -e -f passwd.db

%install
%makeinstall

install -D -m 0644 example/socks-simple.conf $RPM_BUILD_ROOT/%_sysconfdir/socks.conf
install -D -m 0755 %SOURCE1 $RPM_BUILD_ROOT/%_initdir/sockd
install -m755 %SOURCE2 $RPM_BUILD_ROOT/%_bindir/sockd.passwd
install -D %SOURCE6 $RPM_BUILD_ROOT/%_man1dir/sockd.passwd.1
install -m 0644 %SOURCE3 $RPM_BUILD_ROOT/%_sysconfdir/sockd.conf
install -D -m 0644 %SOURCE4 $RPM_BUILD_ROOT/%_sysconfdir/sysconfig/sockd
install -D -m 0644 %SOURCE5 $RPM_BUILD_ROOT/%_sysconfdir/pam.d/sockd
install -D passwd.db $RPM_BUILD_ROOT/%_sharedstatedir/sockd/passwd.db

%pre server
useradd -r -c "SOCKS server" -d /var/empty -s /dev/null _sockd || :

%post server
test -r %_sharedstatedir/sockd/passwd.db || sockd.passwd -r

%files
%doc BUGS CREDITS NEWS README SUPPORT doc/README* example/socks.conf example/socks-simple-withoutnameserver.conf example/sockd.conf example/socks-simple.conf
%config %_sysconfdir/socks.conf
%_libdir/libsocks.so.0.1.1
%_libdir/libsocks.so.0
%_libdir/libsocks.so
%_libdir/libdsocks.so
%_bindir/socksify
%_mandir/man1/socksify.1*
%_mandir/man5/socks.conf.5*

%files server
%config %_sysconfdir/sockd.conf
%config %_sysconfdir/sysconfig/sockd
%dir %_sharedstatedir/sockd
%config(noreplace) %_sharedstatedir/sockd/passwd.db
%_initdir/sockd
%config(noreplace) %_sysconfdir/pam.d/sockd
%_sbindir/sockd
%_bindir/sockd.passwd
%_man5dir/sockd*
%_man8dir/sockd*
%_man1dir/sockd*

%files devel
%doc INSTALL doc/rfc* doc/SOCKS4.protocol
%_libdir/libsocks.a
%_includedir/socks.h

%changelog
* Thu Apr 19 2018 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Initial build for ALT

* Tue Jul  21 2015 Karl-Andre' Skevik <karls@inet.no>
- Add glibc-devel Requires entry for librt, used by socksify.
 Noted by ealogar@gmail.com.

* Sun Feb  3 2013 Karl-Andre' Skevik <karls@inet.no>
- Add reload() and comment about pidfile creation when starting as non-root.

* Tue May 10 2011 Karl-Andre' Skevik <karls@inet.no>
- Integrate some changes from Dag Wieers spec file at:
 http://svn.rpmforge.net/svn/trunk/rpms/dante/dante.spec

* Sat Dec 19 2009 Karl-Andre' Skevik <karls@inet.no>
- Minor tweaking for fedora + add socksify manual page.

* Wed Mar 26 2003 Karl-Andre' Skevik <karls@inet.no>
- Integrated changes from spec file by <dag@wieers.com>, located
 at <URL:ftp://dag.wieers.com/home-made/dante/dante.spec>.

* Thu Oct 12 2000 Karl-Andre' Skevik <karls@inet.no>
- use of macros for directory locations/paths
- explicitly name documentation files
- run chkconfig --del before files are deleted on uninstall

* Wed Mar 10 1999 Karl-Andre' Skevik <karls@inet.no>
- Integrated into CVS
- socksify patch no longer needed

* Thu Mar 04 1999 Oren Tirosh <oren@hishome.net>
- configurable %prefix, fixed daemon init script
- added /lib/libdl.so to socksify

* Wed Mar 03 1999 Oren Tirosh <oren@hishome.net>
- First spec file for Dante
