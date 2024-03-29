Name: bitlbee
Version: 3.6
Release: alt1
Group: Networking/IRC
License: GPLv2
Url: http://www.bitlbee.org
Summary: IRC gateway to IM chat networks
Source: %name-%version.tar.gz
Source1: %name.alt.init

# Automatically added by buildreq on Thu Mar 26 2020
# optimized out: glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libdbus-glib libgcrypt-devel libgpg-error libgpg-error-devel libgst-plugins1.0 libp11-kit pkg-config python-modules python2-base python3 python3-base sh4
BuildRequires: libgnutls-devel libotr-devel libpurple-devel

%description
BitlBee brings IM (instant messaging) to IRC clients. It's a great
solution for people who have an IRC client running all the time and
don't want to run an additional MSN/AIM/whatever client.

BitlBee currently supports the following IM networks/protocols:
XMPP/Jabber (including Google Talk), MSN Messenger, Yahoo! Messenger,
AIM and ICQ, and the Twitter microblogging network (plus all other
Twitter API compatible services like identi.ca and status.net).

%package devel
Group: Development/C
Summary: Development environment for %name, %summary
%description devel
%summary

%package otr
Group: Networking/Instant messaging
Summary: Off-the-record (OTR) plugin for %name
%description otr
%summary

%prep
%setup
# Hack BITLBEE_VERSION into pkgconfig
sed -i 's/\Version: $BITLBEE_VERSION/Version: %version/' configure
# Hack out root check from systemd files installer
sed -i 's/\$(shell id -u),0/0,0/' Makefile

#patch -p1

%build
PYTHON=/usr/bin/python3 ./configure \
        --prefix=%prefix \
        --bindir=%_sbindir \
        --etcdir=%_sysconfdir/%name \
        --mandir=%_mandir \
        --datadir=%_datadir/%name \
        --config=%_localstatedir/%name \
        --pcdir=%_libdir/pkgconfig \
        --plugindir=%_libdir/%name \
	--systemdsystemunitdir=%_unitdir \
        --strip=0 \
        --plugins=1 \
	--purple=1 \
	--msn=1 --jabber=1 --oscar=1 --twitter=1 --skype=0 \
	--otr=plugin
# TODO unhack trail slashes in Makefile.settings generated by configure
%make_build

# Make a reasonable config
sed -i '/^[# ]*DaemonInterface *=/aDaemonInterface = 127.0.0.1
/[^# ]*User *=/aUser = %name
' bitlbee.conf

%install
%makeinstall DESTDIR=%buildroot ETCDIR=%_sysconfdir/%name install-dev install-etc install-systemd
mkdir -p %buildroot%_localstatedir/%name
install -m 755 -D %SOURCE1  %buildroot%_initdir/%name

%pre
/usr/sbin/useradd -r -d %_localstatedir/%name -s /dev/null %name || :

%post
%post_service %name

%postun
%preun_service %name
%files
%doc doc/{AUTHORS,CHANGES,CREDITS,FAQ,README}
%doc doc/user-guide/*.xml doc/user-guide/*.txt
%doc utils
%_sbindir/%name
%_datadir/%name/
%_mandir/man?/%{name}*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%attr(0700,bitlbee,bitlbee) %dir %_localstatedir/%name
%_unitdir/%{name}*
%_initdir/%name

%files otr
%_libdir/%name/*otr*

%files devel
%doc doc/example_plugin.c
%_includedir/%name/
%_libdir/pkgconfig/%name.pc

%changelog
* Thu Jun 16 2022 Fr. Br. George <george@altlinux.org> 3.6-alt1
- Autobuild version bump to 3.6

* Thu Mar 26 2020 Fr. Br. George <george@altlinux.ru> 3.5.1-alt4
- Add libpurple support
- Remove unsupported old skype

* Thu Mar 26 2020 Fr. Br. George <george@altlinux.ru> 3.5.1-alt3
- Rebuild with GNU TLS

* Thu Jan 10 2019 Fr. Br. George <george@altlinux.ru> 3.5.1-alt2
- Provide upstream openssl 1.1 support

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 3.5.1-alt1
- Autobuild version bump to 3.5.1

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 3.4.2-alt1
- Autobuild version bump to 3.4.2

* Thu Jul 16 2015 Fr. Br. George <george@altlinux.ru> 3.4.1-alt1
- Autobuild version bump to 3.4.1
- Fix documentation files

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 3.4-alt1
- Autobuild version bump to 3.4

* Fri Jan 09 2015 L.A. Kostis <lakostis@altlinux.ru> 3.2.2-alt1.1
- Packaging fixes:
  + rename .xinetd to .alt.init as it init.d file in fact.
  + typo fixes and improvements of init.d file.

* Wed Aug 20 2014 Fr. Br. George <george@altlinux.ru> 3.2.2-alt1
- Autobuild version bump to 3.2.2
- Build with libotr 4.0+

* Tue Mar 04 2014 Fr. Br. George <george@altlinux.ru> 3.2.1-alt1
- Autobuild version bump to 3.2.1
- Fix build

* Tue Mar 04 2014 Fr. Br. George <george@altlinux.ru> 3.2-alt1
- Full two major version skip rebuild (partly from FC)

* Fri Apr 02 2010 Fr. Br. George <george@altlinux.ru> 1.2.5-alt1
- Initial build from scratch
- Chkconfig off and separate user by default
