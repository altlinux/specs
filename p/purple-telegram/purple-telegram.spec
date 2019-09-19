Name: purple-telegram
Version: 1.4.2
Release: alt1

Summary: Libpurple protocol plugin for Telegram support
License: GPLv2+
Group: Networking/Instant messaging
URL: https://github.com/majn/telegram-purple.git
# https://github.com/majn/tgl
# https://github.com/vysheng/tl-parser
Packager: Mikhail Kolchin <mvk@altlinux.org>

Source: %name-%version.tar

# Automatically added by buildreq on Sun Apr 24 2016
# optimized out: glib2-devel libgpg-error libgpg-error-devel pkg-config python-base python-modules
BuildRequires: libgcrypt-devel libpurple-devel libwebp-devel zlib-devel
BuildRequires: libpng-devel

%description
Adds support for Telegram to Pidgin, Adium, Finch
and other Libpurple based messengers.

%prep
%setup

%build
# Here we manually create commit.h to avoid git commands
# Thanks for glebfm@ for a nice idea
echo "#ifndef GIT_COMMIT" > commit.h
echo "#  define GIT_COMMIT \"${GIT_COMMIT}\"" >> commit.h
echo "#endif" >> commit.h

# Upstream uses hardcoded Werror flag, so we disable it here
find . -name "Makefile*" | xargs sed -i "s/-Werror //g"

%configure
%make_build

%install
%makeinstall_std

%find_lang telegram-purple

%files -f telegram-purple.lang
%doc README* CHANGELOG*
%_libdir/purple-2/telegram-purple.so
%_datadir/appdata/telegram-purple.metainfo.xml
%_pixmapsdir/pidgin/protocols/*/telegram.png

%changelog
* Thu Sep 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.2-alt1
- Build new version.

* Mon Aug 26 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.
- Updated russian localization.

* Fri Jan 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Build new version (Closes: #33384).

* Mon Apr 25 2016 Mikhail Kolchin <mvk@altlinux.org> 1.2.6-alt1
- new version

* Tue Jan 26 2016 Mikhail Kolchin <mvk@altlinux.org> 1.2.5-alt1
- initial build for ALT Linux Sisyphus
