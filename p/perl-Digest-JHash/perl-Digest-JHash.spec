%define dist Digest-JHash
Name: perl-%dist
Version: 0.07
Release: alt2

Summary: Perl extension for 32 bit Jenkins Hashing Algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
The "Digest::JHash" module allows you to use the fast JHash hashing algorithm
developed by Bob Jenkins from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 32-bit "message
digest" of the input in the form of an unsigned long integer.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Digest
%perl_vendor_autolib/Digest

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1.1
- rebuilt with perl 5.12

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- initial build for ALT Linux Sisyphus

