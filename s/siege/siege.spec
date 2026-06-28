Name: siege
Version: 4.1.7
Release: alt2

Summary: An HTTP regression testing/benchmarking utility

License: %gpl2plus
Group: Networking/WWW
Url: http://www.joedog.org/JoeDog/Siege

Packager: Sergey Alembekov <rt@altlinux.ru>

# Source-url: https://github.com/JoeDog/siege/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildRequires: gcc-c++ libssl-devel
# for mans
BuildRequires: perl-podlators

%description
Siege is a regression test and benchmark utility. It can stress test a
single URL with a user defined number of simulated users, or it can
read many URLs into memory and stress them simultaneously. The program
reports the total number of hits recorded, bytes transferred, response
time, concurrency, and return status. Siege supports HTTP/1.0 and 1.1
protocols, GET and POST directives, cookies, transaction logging, and
basic authentication. Its features are configurable on a per user
basis.

%prep
%setup

%build
# old K&R code: keep pre-C23 empty-prototype semantics under gcc 15
%add_optflags -std=gnu17
utils/bootstrap
%configure \
	--localstatedir=/var \
	--sysconfdir=/etc/siege \
	--exec_prefix= \
	--with-ssl
%make_build

%install
mkdir -p %buildroot/%_sysconfdir/siege
%makeinstall_std

%files
%doc README.md AUTHORS ChangeLog
%dir %_sysconfdir/siege/
%config(noreplace) %_sysconfdir/siege/siegerc
%config(noreplace) %_sysconfdir/siege/urls.txt
%_bindir/bombardment
%_bindir/siege
%_bindir/siege.config
%_bindir/siege2csv.pl
%_man1dir/*

%changelog
* Sun Jun 28 2026 Vitaly Lipatov <lav@altlinux.ru> 4.1.7-alt2
- fixed FTBFS with gcc 15: build with -std=gnu17 (pre-C23 prototypes)

* Sun May 25 2025 Vitaly Lipatov <lav@altlinux.ru> 4.1.7-alt1
- new version 4.1.7 (ALT bug 53848)

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.72-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Feb 17 2012 Mykola Grechukh <gns@altlinux.ru> 2.72-alt1
- update to 2.72

* Sat Feb 12 2011 Sergey Alembekov <rt@altlinux.ru> 2.70-alt1
- update to 2.70

* Thu Sep 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.68-alt2
- update to 2.68b3

* Thu Jun 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.68-alt1
- cleanup spec, replace spec hacks with patches

* Sat May 24 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.68-alt0.1
- New version 2.68b1
- URL updated

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.65-alt0.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 2.65-alt0.1
- new version 2.65 (with rpmrb script)

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 2.64-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD Team)

