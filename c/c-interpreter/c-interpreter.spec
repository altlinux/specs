%define oname C
Name: c-interpreter
Version: 0.06
Release: alt1

Summary: C - a pseudo interpreter of the C programming language

License: GPL
Group: Development/C
Url: http://labs.cybozu.co.jp/blog/kazuhoatwork/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://labs.cybozu.co.jp/blog/kazuho/archives/c/%oname-%version.tar

# Automatically added by buildreq on Fri Feb 03 2006
BuildRequires: help2man

Obsoletes: %oname
Provides: %oname = %version

%description
C - a pseudo interpreter of the C programming language.

%prep
%setup -n %oname-%version

%build
%configure

%install
%makeinstall_std

%files
%doc AUTHORS
%_bindir/C
%_man1dir/*


%changelog
* Wed Dec 05 2012 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- rename package to c-interpreter

* Sat Jul 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt0.1
- new version 0.06 (with rpmrb script)

* Fri Feb 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt0.1
- initial build for ALT Linux Sisyphus

