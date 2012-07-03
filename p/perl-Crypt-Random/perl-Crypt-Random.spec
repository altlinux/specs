%define dist Crypt-Random
Name: perl-%dist
Version: 1.25
Release: alt3

Summary: Cryptographically Secure, True Random Number Generator
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Class-Loader perl-Math-Pari perl-devel

%description
Crypt::Random is an interface module to the /dev/random device found on
most modern unix systems. It also interfaces with egd, a user space
entropy gathering daemon, available for systems where /dev/random (or
similar) devices are not available. When Math::Pari is installed,
Crypt::Random can generate random integers of arbritary size of a given
bitsize or in a specified interval.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/makerandom
%perl_vendor_privlib/Crypt

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 1.25-alt3
- rebuilt

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.25-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.25-alt2
- fix directory ownership violation

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.25-alt1
- first build for ALT Linux Sisyphus
