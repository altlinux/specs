Name:    getxbook
Version: 1.2
Release: alt2

Summary: a collection of tools to download books
License: ISC License
Group:   File tools
URL:     https://njw.me.uk/getxbook/

# Source-url: https://njw.me.uk/getxbook/getxbook-%version.tar.xz
Source: %name-%version.tar

Patch: getxbook-openssl.patch

BuildRequires: libssl-devel

%description
Online book websites are designed not around reading,
but around surveillance. It is not merely the selection of book that is recorded,
but exactly what is read, when, and for how long. Forever.
And this is linked to all other information the website holds about you
(which in the case of Google and Amazon is likely to be a great deal).

%prep
%setup
%patch -p1

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc LEGAL COPYING
%_bindir/getabook
%_bindir/getgbook
%_bindir/getbnbook
%_bindir/getxbookgui
%_man1dir/*
%_pixmapsdir/*

%changelog
* Mon Oct 15 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- fix build with openssl 1.1

* Mon Jan 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- initial build for ALT Linux Sisyphus
