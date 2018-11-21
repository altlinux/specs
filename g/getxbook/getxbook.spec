Name:    getxbook
Version: 1.2
Release: alt3

Summary: a collection of tools to download books
License: ISC License
Group:   Text tools
URL:     https://njw.me.uk/getxbook/

# Source-url: https://njw.me.uk/getxbook/getxbook-%version.tar.xz
Source: %name-%version.tar

Source1: getxbook.desktop

Patch: getxbook-openssl.patch

BuildRequires: libssl-devel

%add_optflags -Wno-error=format-truncation

%description
Online book websites are designed not around reading,
but around surveillance. It is not merely the selection of book that is recorded,
but exactly what is read, when, and for how long. Forever.
And this is linked to all other information the website holds about you
(which in the case of Google and Amazon is likely to be a great deal).

%package gui
Summary: GUI interface for collection of tools to download books
Group: Text tools
Requires: %name = %EVR
Requires: tk

%description gui
Online book websites are designed not around reading,
but around surveillance. It is not merely the selection of book that is recorded,
but exactly what is read, when, and for how long. Forever.
And this is linked to all other information the website holds about you
(which in the case of Google and Amazon is likely to be a great deal).


%prep
%setup
%patch -p1
%__subst "s|^CFLAGS =.*|CFLAGS = %optflags \\\|" config.mk

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix
install -D %SOURCE1 %buildroot%_desktopdir/getxbook.desktop

%files
%doc README LEGAL COPYING
%_bindir/getabook
%_bindir/getgbook
%_bindir/getbnbook
%_man1dir/*

%files gui
%_desktopdir/getxbook.desktop
%_bindir/getxbookgui
%_pixmapsdir/*

%changelog
* Wed Nov 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt3
- use optflags instead hardcoded flags, fix build with gcc 8 behaviour
- split gui subpackage, add desktop file

* Mon Oct 15 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- fix build with openssl 1.1

* Mon Jan 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux Sisyphus
