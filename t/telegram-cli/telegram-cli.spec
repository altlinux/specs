Name: telegram-cli
Version: 1.3.3
Release: alt1

Summary: Private fast and open platform for instant messaging

Group: Networking/Instant messaging
License: GPLv2

Url: https://github.com/vysheng/tg
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Requires: wget

# manually removed: python3 ruby ruby-stdlibs 
# Automatically added by buildreq on Thu Sep 04 2014
# optimized out: libcloog-isl4 python3-base
BuildRequires: libconfig-devel libevent-devel lua-devel lua libreadline-devel libssl-devel zlib-devel libjansson-devel

BuildRequires: wget

BuildRequires: libtgl-devel >= 2.0.3.0

# manually removd: python3 ruby ruby-stdlibs
%description
Telegram is an Open Source messaging platform for mobile, desktop focused on privacy.

%prep
%setup

%build
# TODO: does not effect: --enable-python
%configure --enable-lua
%make_build

%install
install -D -m0755 bin/telegram-cli %buildroot%_bindir/%name
install -D -m0644 tg-server.pub %buildroot/%_sysconfdir/%name/server.pub

%files
%doc CHANGELOG README.* start-telegram-daemon
%_bindir/%name
%dir %_sysconfdir/%name/
%_sysconfdir/%name/server.pub

%changelog
* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- enw release 1.3.3, build with libtgl

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.beta.469d2338a-alt1.1
- NMU: rebuild with new lua

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new release 1.3.1

* Sat Dec 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.0.5.1-alt1
- new release 1.0.5.1

* Thu Sep 04 2014 Vitaly Lipatov <lav@altlinux.ru> 1.0.beta.469d2338a-alt1
- new build 469d2338a

* Sat Mar 29 2014 Vitaly Lipatov <lav@altlinux.ru> 0.0.beta.1dad2e8993-alt1
- new build 1dad2e8993

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.0.beta-alt1
- initial build for ALT Linux Sisyphus
