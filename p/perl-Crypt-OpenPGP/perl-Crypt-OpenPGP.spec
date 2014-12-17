BuildRequires: perl-podlators
%define _unpackaged_files_terminate_build 1
%define dist Crypt-OpenPGP
Name: perl-%dist
Version: 1.08
Release: alt1

Summary: Pure-Perl OpenPGP-compatible PGP implementation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SR/SROMANOV/Crypt-OpenPGP-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Jan 25 2011
BuildRequires: openssl perl-Crypt-Blowfish perl-Crypt-CAST5_PP perl-Crypt-DES_EDE3 perl-Crypt-DSA perl-Crypt-IDEA perl-Crypt-RIPEMD160 perl-Crypt-RSA perl-Crypt-Rijndael perl-Crypt-Twofish perl-File-HomeDir perl-Filter perl-Math-BigInt-GMP perl-Module-Install perl-libwww perl(Test/Exception.pm) perl(Term/ReadKey.pm)

%description
Crypt::OpenPGP is a pure-Perl implementation of the OpenPGP standard.
In addition to support for the standard itself, Crypt::OpenPGP claims
compatibility with many other PGP implementations, both those that support
the standard and those that preceded it.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %name


%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Crypt

%files scripts
%_bindir/*
#_man1dir/*


%changelog
* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Wed Dec 18 2013 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt2
- fixed build (RT#81442)

* Tue Jan 25 2011 Alexey Tourbin <at@altlinux.ru> 1.06-alt1
- 1.05 -> 1.06

* Fri Apr 09 2010 Victor Forsiuk <force@altlinux.org> 1.04-alt1
- 1.04

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.03-alt3
- fix directory ownership violation

* Tue Jan 23 2007 Vitaly Lipatov <lav@altlinux.ru> 1.03-alt2
- cleanup spec

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.03-alt1
- first build for ALT Linux Sisyphus
