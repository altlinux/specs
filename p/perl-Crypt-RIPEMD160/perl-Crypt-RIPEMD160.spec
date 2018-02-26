%define dist Crypt-RIPEMD160
Name: perl-%dist
Version: 0.05
Release: alt2

Summary: Perl extension for the RIPEMD-160 Hash function
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
The Crypt::RIPEMD160 module allows you to use the RIPEMD160
Message Digest algorithm from within Perl programs.

The module is based on the implementation from Antoon Bosselaers from
Katholieke Universiteit Leuven.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt2.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt2
- fix directory ownership violation

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- first build for ALT Linux Sisyphus
