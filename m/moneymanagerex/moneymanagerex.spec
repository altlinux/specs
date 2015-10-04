Name: moneymanagerex
Version: 1.2.2
Release: alt2

Summary: Simple to use financial management software
License: GPLv2
Group: Office

URL: http://www.moneymanagerex.org/

## Source-git: https://github.com/moneymanagerex/moneymanagerex.git
# Source-url: https://github.com/moneymanagerex/moneymanagerex/archive/v%version.tar.gz
Source: %name-%version.tar

AutoReq:yes,nomingw32

# manually removed: i586-libgst-plugins1.0 i586-libxcb  python3 ruby ruby-stdlibs
# Automatically added by buildreq on Thu Aug 13 2015
# optimized out: at-spi2-atk fontconfig gnu-config libat-spi2-core libcairo-gobject libgdk-pixbuf libgpg-error libgst-plugins1.0 libharfbuzz-icu libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server python3-base
BuildRequires: gcc-c++ libdb4-devel libwxGTK3.1-devel

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
%_man1dir/*
%_iconsdir/hicolor/scalable/apps/mmex.svg
%_docdir/mmex/
%_datadir/mmex/


%changelog
* Sun Oct 04 2015 Anton Midyukov <antohami@altlinux.org> 1.2.2-alt2
- Rebuilt for new gcc5 C++11 ABI.

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- initial build for ALT Linux Sisyphus
