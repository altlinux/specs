Name: moneymanagerex
Version: 1.3.3
Release: alt1

Summary: Simple to use financial management software
License: GPLv2
Group: Office

URL: http://www.moneymanagerex.org/

# Note: pack submodules to .gear/@name@-postsubmodules (as in .gear/rules)

## Source-url: https://github.com/moneymanagerex/moneymanagerex/archive/v%version.tar.gz
# Source-git: https://github.com/moneymanagerex/moneymanagerex.git
Source: %name-%version.tar

# build with system wxsqlite3
Patch: moneymanagerex-wxsqlite3.patch
Patch1: moneymanagerex-configure.patch

AutoReq:yes,nomingw32

# manually removed: i586-libgst-plugins1.0 i586-libxcb  python3 ruby ruby-stdlibs
# Automatically added by buildreq on Thu Aug 13 2015
# optimized out: at-spi2-atk fontconfig gnu-config libat-spi2-core libcairo-gobject libgdk-pixbuf libgpg-error libgst-plugins1.0 libharfbuzz-icu libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server python3-base
BuildRequires: gcc-c++ libdb4-devel libwxGTK3.1-devel libwxGTK3.1-sqlite3-devel libsqlite3-devel

%description
Simple to use financial management software
Money Manager Ex (MMEX) is a free, open-source,
cross-platform, easy-to-use personal finance software.
It primarily helps organize one's finances and keeps
track of where, when and how the money goes.
MMEX includes all the basic features that 90 percents of users
would want to see in a personal finance application.
The design goals are to concentrate on simplicity
and user friendliness - something one can use everyday.

TODO: build with external lua, ccpunit, wxsqlite3

%prep
%setup
%patch -p2
%patch1 -p2

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README.TXT README.md
%_bindir/mmex
%_desktopdir/mmex.desktop
#_man1dir/*
%_iconsdir/hicolor/scalable/apps/mmex.svg
%_docdir/mmex/
%_datadir/mmex/


%changelog
* Mon Mar 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)

* Sun Oct 04 2015 Anton Midyukov <antohami at altlinux.org> 1.2.2-alt2
- Rebuilt for new gcc5 C++11 ABI.

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- initial build for ALT Linux Sisyphus
