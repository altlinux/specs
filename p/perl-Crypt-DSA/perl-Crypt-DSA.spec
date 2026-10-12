%define dist Crypt-DSA
Name: perl-%dist
Version: 1.24
Release: alt1

Summary: %dist - DSA signatures and key generation

License: GPL-1.0-or-later or Artistic-1.0-Perl
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/T/TI/TIMLEGGE/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Tue Jun 17 2008
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel openssl perl-Convert-PEM perl-Crypt-DES_EDE3 perl-Data-Buffer perl-File-Which perl(Convert/ASN1.pm) perl(Crypt/SysRandom.pm) perl(Digest/SHA.pm) perl(Math/BigInt.pm)

%description
Crypt::DSA is an implementation of the DSA (Digital Signature Algorithm)
signature verification system. The implementation itself is pure Perl,
although the heavy-duty mathematics underneath are provided by the
Math::Pari library.  This package provides DSA signing, signature
verification, and key generation.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/Crypt/DSA*

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1.24-alt1
- new version 1.24
- switch random source to Crypt::SysRandom (drop Crypt::URandom).
- security fixes:
  + CVE-2026-8700: replace rand() with a CSPRNG.
  + CVE-2026-8704: replace two-arg open.
  + CVE-2026-12205: generate a fresh nonce for every signature.
  + CVE-2026-14570: fix modulo bias in key generation.

* Fri Apr 04 2025 Igor Vlasenko <viy@altlinux.org> 1.19-alt1
- automated CPAN update

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Tue Dec 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt2
- fixed build with openssl 1.0.0b
  (patch from https://rt.cpan.org/Public/Bug/Display.html?id=49668)
- spec cleanup

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt1
- new version 0.14 (with rpmrb script)

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt1
- first build for ALT Linux Sisyphus
