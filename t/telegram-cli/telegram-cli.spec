Name: telegram-cli
Version: 0.0.beta
Release: alt1

Summary: Private fast and open platform for instant messaging

Group: Networking/Instant messaging
License: GPLv2

Url: https://github.com/vysheng/tg
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Requires:	wget

BuildRequires: wget

# manually removd: python3 ruby ruby-stdlibs 
# Automatically added by buildreq on Fri Feb 07 2014
# optimized out: python3-base
BuildRequires: libconfig-devel liblua5-devel libreadline-devel libssl-devel lua5 zlib-devel

%description
Telegram is an Open Source messaging platform for mobile, desktop focused on privacy.

%prep
%setup
%configure
%make_build

%install
install -D -m0755 telegram %buildroot%_bindir/telegram
install -D -m0644 tg.pub %buildroot/etc/telegram/server.pub

%files
%_bindir/telegram
%dir %_sysconfdir/telegram/
%_sysconfdir/telegram/server.pub

%changelog
* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 0.0.beta-alt1
- initial build for ALT Linux Sisyphus
