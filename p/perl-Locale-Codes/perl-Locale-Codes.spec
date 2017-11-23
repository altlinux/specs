%define _unpackaged_files_terminate_build 1
%define dist Locale-Codes
Name: perl-%dist
Version: 3.55
Release: alt1

Summary: ISO codes for countries, languages, currencies, and scripts
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SB/SBECK/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Module-Build

%description
This package contains four Perl modules (Locale::Language,
Locale::Country, Locale::Currency, and Locale::Script) which
can be used to process ISO codes for identifying languages,
countries, scripts, and currencies & funds.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README README.first examples
%dir	%perl_vendor_privlib/Locale
	%perl_vendor_privlib/Locale/*.pm
%doc	%perl_vendor_privlib/Locale/*.pod
%dir	%perl_vendor_privlib/Locale/Codes
	%perl_vendor_privlib/Locale/Codes/*.pm
%doc	%perl_vendor_privlib/Locale/Codes/*.pod

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.55-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 3.54-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.53-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.51-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.50-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 3.42-alt1
- automated CPAN update

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 3.41-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.40-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.39-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.38-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 3.37-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 3.36-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 3.34-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 3.33-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.32-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 3.31-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 3.30-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.27-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 3.26-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 3.23-alt1
- 3.18 -> 3.23

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
