%define dist Locale-Codes
Name: perl-%dist
Version: 3.18
Release: alt1

Summary: ISO codes for countries, languages, currencies, and scripts
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SB/SBECK/Locale-Codes-3.18.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 22 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
This package contains four Perl modules (Locale::Language,
Locale::Country, Locale::Currency, and Locale::Script) which
can be used to process ISO codes for identifying languages,
countries, scripts, and currencies & funds.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog README
%dir	%perl_vendor_privlib/Locale
	%perl_vendor_privlib/Locale/*.pm
%doc	%perl_vendor_privlib/Locale/*.pod
%dir	%perl_vendor_privlib/Locale/Codes
	%perl_vendor_privlib/Locale/Codes/*.pm
%doc	%perl_vendor_privlib/Locale/Codes/*.pod

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.18-alt1
- automated CPAN update

* Fri Apr 22 2011 Alexey Tourbin <at@altlinux.ru> 3.16-alt1
- 3.15 -> 3.16

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 3.15-alt1
- 3.12 -> 3.15

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 3.12-alt1
- 3.11 -> 3.12

* Sun Apr 04 2010 Alexey Tourbin <at@altlinux.ru> 3.11-alt1
- 2.07 -> 3.11

* Fri Jul 24 2009 Alexey Tourbin <at@altlinux.ru> 2.07-alt2
- rebuilt

* Fri Dec 10 2004 Alexey Tourbin <at@altlinux.ru> 2.07-alt1
- initial revision (split perl-i18n)
