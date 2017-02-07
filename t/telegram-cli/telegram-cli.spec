Name: telegram-cli
Version: 1.0.beta.469d2338a
Release: alt1.1

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
BuildRequires: libconfig-devel libevent-devel lua-devel lua libreadline-devel libssl-devel zlib-devel

BuildRequires: wget

# manually removd: python3 ruby ruby-stdlibs
%description
Telegram is an Open Source messaging platform for mobile, desktop focused on privacy.

%prep
%setup

%build
%configure
%make_build

%install
install -D -m0755 bin/telegram-cli %buildroot%_bindir/%name
install -D -m0644 tg-server.pub %buildroot/%_sysconfdir/%name/server.pub

%files
%_bindir/%name
%dir %_sysconfdir/%name/
%_sysconfdir/%name/server.pub

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.beta.469d2338a-alt1.1
- NMU: rebuild with new lua

* Thu Sep 04 2014 Vitaly Lipatov <lav@altlinux.ru> 1.0.beta.469d2338a-alt1
- new build 469d2338a

* Sat Mar 29 2014 Vitaly Lipatov <lav@altlinux.ru> 0.0.beta.1dad2e8993-alt1
- new build 1dad2e8993

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.0.beta-alt1
- initial build for ALT Linux Sisyphus
