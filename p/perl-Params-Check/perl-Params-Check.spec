%define dist Params-Check
Name: perl-%dist
Version: 0.32
Release: alt1

Summary: A generic input parsing/checking mechanism.
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/Params-Check-0.32.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Feb 26 2011
BuildRequires: perl-Locale-Maketext-Simple perl-devel

%description
Params::Check is a generic input parsing/checking mechanism.  It allows
for generic input checking and validating using a powerfull templating
system, providing default values and so on.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Params

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- 0.26 -> 0.28

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.26-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.26-alt2
- fix directory ownership violation

* Mon Jun 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.26-alt1
- new version 0.26 (with rpmrb script)

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.23-alt1
- first build for ALT Linux Sisyphus
