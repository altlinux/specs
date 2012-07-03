# handle initscript style change (c) mike@ :)
Name: dante
Version: 1.2.2
Release: alt2

%define service sockd
%define srcname %name-%version

Summary: A free Socks v4/v5 client/server implementation
Summary(RU_ru.KOI8-R): Свободная реализация протокола socks (v4/v5)
License: BSD-type
Group: Networking/Other
Url: http://www.inet.no/%name/

Packager: Timur Aitov <timonbl4@altlinux.org>

Source: ftp://ftp.inet.no/pub/socks/%srcname.tar.gz

Source1: sockd.init

Patch0: %name-1.2.2-alt-libdl.patch
Patch1: %name-1.2.2-alt-pidfile.patch
Patch2: %name-1.2.2-alt-sockd.conf.patch

Requires: lib%name = %version-%release

# Automatically added by buildreq on Thu Feb 12 2004
BuildRequires: bison flex libpam-devel libwrap-devel
BuildRequires: altlinux-release

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

%package -n lib%name
Summary: A free Socks v4/v5 client implementation
Summary(RU_ru.KOI8-R): Клиент Socks v4/v5
Group: System/Libraries
Provides: libsocks

%package -n lib%name-devel
Summary: Development environment for socks
Summary(RU_ru.KOI8-R): Библиотеки для разработки приложений с поддержкой socks
Group: Development/C
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: Static libraries for socks
Summary(RU_ru.KOI8-R): Статические библиотеки для разработки socks приложений.
Group: Development/C
Requires: lib%name-devel = %version-%release

%package server
Summary: A free Socks v4/v5 server implementation
Summary(RU_ru.KOI8-R): Socks v4/v5 прокси-сервер.
Group: System/Servers

Requires(post,preun): service, chkconfig
Requires: %name = %version-%release libpam libwrap
Provides: %service

%description
Dante is a free implementation of the proxy protocols socks version 4,
socks version 5 (rfc1928) and msproxy. It can be used as a firewall
between networks. It is being developed by Inferno Nettverk A/S, a
Norwegian consulting company. Commercial support is available.

This package contains utilities and documentation required to
"socksify" existing applications to become socks clients.

%description -l ru_RU.KOI8-R
Dante - свободная реализация протокола проксирования socks версий
4 и 5 (rfc1928) и msproxy. Используеться для создания прокси
серверов с поддержкой множества протоколов на основе TCP/UDP.
Dante разработан норвежской консалтинговой компанией Inferno Nettverk A/S,
которая предоставляет услуги по коммерческой поддержке dante.

Пакет содержит утилиты и документацию необходимую для настройки
работы существующих приложений как клиентов socks ("соксифизации"
/"socksify"/).

%description -n lib%name
This package contains the dynamic libraries required to "socksify"
existing applications to become socks clients.

%description -l ru_RU.KOI8-R
Динамически загружаемые библиотеки необходимые для "соксифизации"
приложений.

%description -n lib%name-devel
This package contains libraries and header files required to compile
programs that use socks.

%description -l ru_RU.KOI8-R
Библиотеки и заголовочный файлы для разработки программ использующих
socks.

%description -n lib%name-devel-static
This package contains static libraries required to build statically linked
programs that use socks.

%description -l ru_RU.KOI8-R
Статические библиотеки для разработки программ использующих socks.

%description server
This package contains the socks proxy daemon and its documentation.
The sockd is the server part of the Dante socks proxy package and
allows socks clients to connect through it to the network.

%description -l ru_RU.KOI8-R
Socks прокси сервер и документация к нему. Серверная часть Dante -
'sockd'.

%prep
%setup -q -n %srcname

%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
echo >> acinclude.m4
%autoreconf
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure %{subst_enable static}

%make_build

%install
%makeinstall

# Set library as executable - prevent ldd from complaining
chmod 755 %buildroot%_libdir/*.so*
install -pD -m644 example/socks-simple.conf %buildroot%_sysconfdir/socks.conf
install -p  -m644 example/%service.conf     %buildroot%_sysconfdir
install -pD -m755 %SOURCE1                  %buildroot%_initdir/%service

pushd %buildroot%_libdir
	ln -s libsocks.so.*.*.* libsocks5.so
popd

mkdir -p       %buildroot%_sysconfdir/sysconfig
cat << _EOF_  >%buildroot%_sysconfdir/sysconfig/%service
# Socks proxy daemon command line options
EXTRAOPTIONS="-D"
_EOF_

%pre server
%_sbindir/groupadd -r -f %service &> /dev/null ||:
%_sbindir/useradd  -r -g %service -d /dev/null \
                   -s /dev/null -n %service &> /dev/null ||:
%_sbindir/useradd  -r -g %service -d /dev/null \
                   -s /dev/null -n no%service &> /dev/null ||:

%post server
%post_service %service

%preun server
%preun_service %service
%files -n lib%name
%_libdir/*.so.*
%_libdir/libdsocks.so

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files
%_bindir/socksify
%_man1dir/*
%_man5dir/socks.conf.*
%config(noreplace) %_sysconfdir/socks.conf
%doc               BUGS CREDITS INSTALL LICENSE NEWS README SUPPORT TODO
%doc               doc/README* doc/rfc* doc/SOCKS4.protocol example/*.conf
%doc               doc/module/*.tex  contrib/sockd-stat.awk

%files server
%_sbindir/*
%_man8dir/*
%_man5dir/%service.conf.*
%config(noreplace) %_sysconfdir/sysconfig/%service
%config(noreplace) %_sysconfdir/%service.conf
%config(noreplace) %_initdir/%service

%changelog
* Tue Dec 21 2010 Timur Aitov <timonbl4@altlinux.org> 1.2.2-alt2
- mod sockd

* Thu Oct 14 2010 Timur Aitov <timonbl4@altlinux.org> 1.2.2-alt1
- new version

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 1.1.19-alt3
- cleanup spec

* Sun Mar 23 2008 Denis Smirnov <mithraen@altlinux.ru> 1.1.19-alt2
- fix #7028
- fix #4268
- cleanup spec with rpmcs
- remove old Master initscript

* Sat Mar 10 2007 Denis Smirnov <mithraen@altlinux.ru> 1.1.19-alt1
- Update to 1.1.19

* Wed Feb 12 2004 Igor Homyakov <homyakov at altlinux dot ru> 1.1.14-alt1
- 1.1.14
- Do not package lib%name-devel-static by default
- Do not package .la files.
- Rewritten start/stop script to new rc scheme
- fix libdsock.so.0 dep (patch3)
- Cleanups

* Wed Nov 20 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.1.13-alt3
- fixed bug 0001525

* Mon Oct 14 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.1.13-alt2
- rebuild with libwrap-devel
- added pid file creation patch
- spec russian translation and cleanup
- added %_sysconfdir/sysconfig/sockd for extra command line options
- rewrite startup script for support %_sysconfdir/sysconfig/sockd
- user 'nobody' is 'nosockd' now

* Mon Jun 24 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.1.13-alt1
- 1.1.13

* Thu Jun 06 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.1.12-alt2
- fixed bug 0000954 (library missed) in spec file

* Fri Apr 15 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.1.12-alt1
- build 1.1.12
- spec cleanup

* Tue Feb 26 2002 Igor Homyakov <homyakov at altlinux dot ru> 1.1.12-alt0.1
- build 1.1.12-pre1
- strict default configuration for socks server
- some fixes in spec file

* Thu Jan  3 2002 Igor Homyakov <homyakov at altlinux dot ru> alt1
- build 1.1.11

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1.10-alt1
- Complete libification.
- Updated startup script to fit ALT service initscript policy.

* Thu Aug 2 2001 Alexey A. Morozov <morozov@novosoft.ru>
- first attempt to build an [almost] ALTLinux-compliant package
- new version (1.1.10)

* Sun Mar 18 2001 Alexandr D. Kanevskiy <kad@asplinux.ru>
- import to ASPLinux

* Tue Feb 27 2001 Tim Powers <timp@redhat.com>
- another fix to the initscript where there wasn't an [ $RETVAL -eq 0 ]

* Tue Feb  6 2001 Tim Powers <timp@redhat.com>
- fixed bug 26296 where the RETVAL in the initscript was being munged
  at build time. Using an actual file instead of cat'ing it in.

* Tue Jan 23 2001 Tim Powers <timp@redhat.com>
- fix initscripts so that it's easier to internationalize

* Thu Jan  4 2001 Tim Powers <timp@redhat.com>
- fixed bad file ownership in devel package

* Mon Dec 11 2000 Tim Powers <timp@redhat.com>
- changed the initscript a bit, added condrestart too
- quiet setup
- changed two of the groups
- added the condrestart stuff to the preun and postun sections
- using %%configure and %%makeinstall

* Thu Oct 12 2000 Karl-Andre' Skevik <karls@inet.no>
-use of macros for directory locations/paths
-explicitly name documentation files
-run chkconfig --del before files are deleted on uninstall

* Wed Mar 10 1999 Karl-Andre' Skevik <karls@inet.no>
- Integrated into CVS
- socksify patch no longer needed

* Thu Mar 04 1999 Oren Tirosh <oren@hishome.net>
- configurable %prefix, fixed daemon init script
- added /lib/libdl.so to socksify

* Wed Mar 03 1999 Oren Tirosh <oren@hishome.net>
- First spec file for Dante
