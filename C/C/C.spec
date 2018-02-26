Name: C
Version: 0.06
Release: alt0.1

Summary: C - a pseudo interpreter of the C programming language

License: GPL
Group: Development/C
Url: http://labs.cybozu.co.jp/blog/kazuhoatwork/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://labs.cybozu.co.jp/blog/kazuho/archives/c/%name-%version.tar.bz2

# Automatically added by buildreq on Fri Feb 03 2006
BuildRequires: help2man

%description
C - a pseudo interpreter of the C programming language.

%prep
%setup -q

%build

%configure

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS ChangeLog README
%_bindir/*
%_man1dir/*


%changelog
* Sat Jul 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt0.1
- new version 0.06 (with rpmrb script)

* Fri Feb 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt0.1
- initial build for ALT Linux Sisyphus

