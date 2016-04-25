Name: purple-telegram
Version: 1.2.6
Release: alt1

Summary: Libpurple protocol plugin for Telegram support
License: GPLv2+
Group: Networking/Instant messaging
URL: https://github.com/majn/telegram-purple.git
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: %name-%version.tar

# Automatically added by buildreq on Sun Apr 24 2016
# optimized out: glib2-devel libgpg-error libgpg-error-devel pkg-config python-base python-modules
BuildRequires: libgcrypt-devel libpurple-devel libwebp-devel zlib-devel

%description
Adds support for Telegram to Pidgin, Adium, Finch 
and other Libpurple based messengers.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang telegram-purple

%files -f telegram-purple.lang
%doc README* CHANGELOG*
%_libdir/purple-2/telegram-purple.so
%dir %_sysconfdir/telegram-purple/
%config %_sysconfdir/telegram-purple/*
%_pixmapsdir/pidgin/protocols/*/telegram.png

%changelog
* Mon Apr 25 2016 Mikhail Kolchin <mvk@altlinux.org> 1.2.6-alt1
- new version

* Tue Jan 26 2016 Mikhail Kolchin <mvk@altlinux.org> 1.2.5-alt1
- initial build for ALT Linux Sisyphus
