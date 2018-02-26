%define dist Crypt-RSA
Name: perl-%dist
Version: 1.99
Release: alt1

Summary: RSA public-key cryptosystem
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Convert-ASCII-Armour perl-Crypt-Blowfish perl-Crypt-Primes perl-Data-Buffer perl-Digest-MD2 perl-Digest-SHA1 perl-Sort-Versions perl-Tie-EncryptedHash perl-devel

%description
Crypt::RSA is a pure-perl, cleanroom implementation of the RSA public-key
cryptosystem. It uses Math::Pari(3), a perl interface to the blazingly
fast PARI library, for big integer arithmetic and number theoretic
computations.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Crypt

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 1.99-alt1
- 1.96 -> 1.99

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.58-alt2
- fix directory ownership violation

* Tue Jun 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.58-alt1
- new version 1.58 (with rpmrb script)

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.56-alt1
- first build for ALT Linux Sisyphus
