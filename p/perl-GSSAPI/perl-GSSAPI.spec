%define dist GSSAPI
Name: perl-%dist
Version: 0.28
Release: alt2

Summary: Perl extension providing access to the GSSAPIv2 library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: libkrb5-devel perl-Test-Pod

%description
This module gives access to the routines of the GSSAPI library,
as described in rfc2743 and rfc2744 and implemented by the
Kerberos-1.2 distribution from MIT.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/GSSAPI*
%perl_vendor_autolib/GSSAPI

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.28-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.26-alt1.1
- rebuilt with perl 5.12

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.26-alt1
- new version
- fixed build

* Mon Jun 11 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.24-alt1
- first build for ALT Linux Sisyphus

