# SPEC file for miredo package

%def_with static

Name: miredo
Version: 1.2.6
Release: alt3.gite5f565

Summary: Teredo IPv6 tunneling through NATs

License: %gpl2plus
Group: System/Servers
URL: http://www.remlab.net/miredo

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Requires: lib%name = %version-%release

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.service

Source4: %name-server.init
Source5: %name-server.sysconfig
Source6: %name-server.service

Patch0: %name-%version-%release.patch

Patch1: %name-1.2.6-alt-fix_includes.patch
Patch2: %name-1.2.6-alt-armh.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Nov 04 2014
# optimized out: libcloog-isl4 xz
BuildRequires: glibc-devel-static libcap-devel

%description
The Teredo IPv6 tunneling protocol encapsulates IPv6 packets into
UDP/IPv4 datagrams,  to allow hosts behind  NAT devices to access
the IPv6 Internet.

Miredo  is a Teredo client (as per RFC 4380): it can provide IPv6
connectivity to a dual-stack IPv6/IPv4 host even if it is located
behind a NAT. It can also operate as a Teredo relay which
forwards IPv6 packets between the IPv6 Internet and remote
Teredo clients.


%package server
Summary: Teredo server for Teredo clients
Group: System/Servers

# NOTE: miredo-server is not linking with libmiredo
#Requires: lib%name = %version-%release

%description server
The Teredo IPv6 tunneling protocol encapsulates IPv6 packets into
UDP/IPv4 datagrams,  to allow hosts behind  NAT devices to access
the IPv6 Internet.

This package provides a Teredo server. Teredo servers help Teredo
clients  determine their  NAT configuration,  maintain their  NAT
binding, and perform hole punching when transmitting IPv6 packets
to other Teredo clients and/or Teredo relays.


%package -n lib%name
Summary: shared libraries for Miredo client
Group: System/Libraries

%description -nlib%name
The Teredo IPv6 tunneling protocol encapsulates IPv6 packets into
UDP/IPv4 datagrams,  to allow hosts behind  NAT devices to access
the IPv6 Internet.

This package contains a shared libraries for Teredo client.


%package -n lib%name-devel
Summary: development files for Miredo client shared libraries
Group: System/Libraries
Requires: lib%name = %version-%release

%description -nlib%name-devel
The Teredo IPv6 tunneling protocol encapsulates IPv6 packets into
UDP/IPv4 datagrams,  to allow hosts behind  NAT devices to access
the IPv6 Internet.

This package contains a development files for Miredo client shared
libraries.


%if_with static
%package -n lib%name-devel-static
Summary: Miredo client static libraries
Group: System/Libraries
Requires: lib%name-devel = %version-%release

%description -nlib%name-devel-static
The Teredo IPv6 tunneling protocol encapsulates IPv6 packets into
UDP/IPv4 datagrams,  to allow hosts behind  NAT devices to access
the IPv6 Internet.

This package contains a Miredo client static libraries.
%endif


%define miredo_user             _miredo
%define miredo_group            _miredo

%prep
%setup
%patch0 -p1

%patch1

%ifarch armh
%patch2
%endif

%build
%def_enable Werror

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_optflags -std=gnu99
./autogen.sh
# --localstatedir used here as a prefix for LOCALSTATEDIR/run/ directory to place PID file
%configure --enable-miredo-user %miredo_user --without-Judy --localstatedir=/
%make

%install
mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%makeinstall

%find_lang %name

mkdir -p -- %buildroot/%_initdir
install -m 0755 -- %SOURCE1 %buildroot%_initdir/%name
install -m 0755 -- %SOURCE4 %buildroot%_initdir/%name-server
mkdir -p -- %buildroot/%_sysconfdir/sysconfig
install -m 0644 -- %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m 0644 -- %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name-server

install -m 0644 -- misc/%name-server.conf %buildroot%_sysconfdir/%name/%name-server.conf

# Moving service file to the proper location
rm -rf -- %buildroot%_libdir/systemd
mkdir -p -- %buildroot%_unitdir
install -m 0644 -- %SOURCE3 %buildroot%_unitdir/%name.service
install -m 0644 -- %SOURCE6 %buildroot%_unitdir/%name-server.service

%pre
# Add the "_miredo" user
%_sbindir/groupadd -r -f %miredo_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %miredo_group -c 'Miredo daemon' \
        -s /dev/null -d /dev/null %miredo_user 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%pre server
# Add the "_miredo" user
%_sbindir/groupadd -r -f %miredo_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %miredo_group -c 'Miredo daemon' \
        -s /dev/null -d /dev/null %miredo_user 2>/dev/null ||:

%post server
%post_service %name-server

%preun server
%preun_service %name-server

%files -f %name.lang
%doc AUTHORS README THANKS TODO
%doc --no-dereference COPYING
%doc misc/miredo-server.conf

%dir %_sysconfdir/%name
%config(noreplace)  %_sysconfdir/%name/%name.conf
%config(noreplace)  %_sysconfdir/%name/client-hook
%config(noreplace)  %_sysconfdir/sysconfig/%name

%config  %_initdir/%name
%_unitdir/%name.service

%exclude %_docdir/miredo/examples/

%_bindir/teredo-mire
%_sbindir/%name
%_sbindir/%name-checkconf

%_man1dir/teredo-mire*
%_man5dir/%name.conf*
%_man8dir/%name.*
%_man8dir/%name-checkconf*

%files server
%doc AUTHORS README THANKS
%doc --no-dereference COPYING

%dir %_sysconfdir/%name
%config(noreplace)  %_sysconfdir/%name/%name-server.conf
%config(noreplace)  %_sysconfdir/sysconfig/%name-server

%config  %_initdir/%name-server
%_unitdir/%name-server.service

%_sbindir/%name-server

%_man5dir/%name-server.conf*
%_man8dir/%name-server*


%files -n lib%name
%_libdir/libteredo.so.6*
%_libdir/libtun6.so.2*
%_libexecdir/miredo/miredo-privproc

%files -n lib%name-devel
%_includedir/libteredo*
%_includedir/libtun6*
%_libdir/libteredo.so
%_libdir/libtun6.so

%if_with static
%files -n lib%name-devel-static
%_libdir/libteredo.a
%_libdir/libtun6.a
%else
%exclude %_libdir/libteredo.a
%exclude %_libdir/libtun6.a
%endif

%changelog
* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.2.6-alt3.gite5f565
- Fix build with LTO flags

* Thu Jul 01 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.2.6-alt2.gite5f565
- Restore from orphaned
- Fix systemd startup order (Closes: 38847)

* Tue Nov 04 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.6-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.5-alt2
- Fix build with gettext-tools 0.18.2.1

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1.2
- Disabled -Werror compiler flag

* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1.1
- Fixed build

* Fri Apr 20 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.5-alt1
- New version

* Fri Jan 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.4-alt1
- New version

* Fri Jun 24 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.3-alt1
- Initial build for ALT Linux Sisyphus
