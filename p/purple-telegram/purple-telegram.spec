Name: purple-telegram
Version: 1.2.5
Release: alt1

Summary: Adds support for Libpurple based messengers
License: GPLv3
Group: Networking/Instant messaging
URL: https://github.com/majn/telegram-purple.git
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: %name-%version.tar

# Automatically added by buildreq on Thu Jan 14 2016
# optimized out: glib2-devel libcom_err-devel libkrb5-devel pkg-config
BuildRequires: libpurple-devel libssl-devel libwebp-devel zlib-devel

%description
Adds support for Telegram to Pidgin, Adium, Finch 
and other Libpurple based messengers.

%prep
%setup

%build
%configure --disable-gcrypt
%make_build

%install
%makeinstall_std

%find_lang telegram-purple

%files -f telegram-purple.lang
%_libdir/purple-2/telegram-purple.so
%config %_sysconfdir/telegram-purple/*
%_pixmapsdir/pidgin/protocols/*/telegram.png

%changelog
* Tue Jan 26 2016 Mikhail Kolchin <mvk@altlinux.org> 1.2.5-alt1
- initial build for ALT Linux Sisyphus
