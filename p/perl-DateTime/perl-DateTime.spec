%define _unpackaged_files_terminate_build 1
%def_without bootstrap
%define dist DateTime
Name: perl-%dist
Version: 1.45
Release: alt1

Summary: DateTime base objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{dist}-%{version}.tar.gz
Patch: DateTime-1.42-alt-syntax-check.patch 

# break dependency loop
Requires: perl-DateTime-TimeZone

BuildRequires: perl-DateTime-Locale perl-Math-Round perl-Module-Build perl-Test-Exception perl-Test-Warn perl-Test-Fatal perl(Test/Warnings.pm) perl(CPAN/Meta/Check.pm)

%if_with bootstrap
%define _without_test 1
%add_findreq_skiplist %perl_vendor_archlib/DateTime*
%else
BuildRequires: perl-DateTime-TimeZone
# test depandency
BuildRequires: perl(Params/Validate.pm)
%endif

%description
DateTime is a class for the representation of date/time combinations,
and is part of the Perl DateTime project.  For details on this project
please see http://datetime.perl.org.  The DateTime site has a FAQ which
may help answer many "how do I do X?" questions.  The FAQ is at
http://datetime.perl.org/faq.html.

%prep
%setup -q -n %{dist}-%{version}
%patch -p0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md CONTRIBUTING.md CREDITS leaptab.txt
%perl_vendor_archlib/DateTime*
%perl_vendor_autolib/DateTime*

%changelog
* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1
- automated CPAN update

* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt2
- unbootstrap

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1.1.1
- unbootstrap after rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1.1
- rebuild with new perl 5.24.1

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Wed Mar 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1.2
- unbootstrap

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2.1
- rebuild with new perl 5.20.1

* Wed Dec 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2
- added bootstrap support
- bootstrap build for perl-5.20.1 update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Wed Mar 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Sun Aug 25 2013 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.76-alt1
- 0.70 -> 0.76
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.70-alt2
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.70-alt1
- 0.66 -> 0.70
- rebuilt as plain src.rpm

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.66-alt1
- 0.60 -> 0.66

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.60-alt1.1
- rebuilt with perl 5.12

* Tue Jul 06 2010 Alexey Tourbin <at@altlinux.ru> 0.60-alt1
- 0.55 -> 0.60

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 0.55-alt1
- 0.53 -> 0.55

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 0.53-alt1
- 0.49 -> 0.53

* Mon May 11 2009 Alexey Tourbin <at@altlinux.ru> 0.49-alt1
- 0.47 -> 0.49

* Tue Mar 24 2009 Alexey Tourbin <at@altlinux.ru> 0.47-alt1
- 0.4401 -> 0.47
- DateTime.pm no longer requires Time/y2038.pm

* Thu Nov 06 2008 Alexey Tourbin <at@altlinux.ru> 0.44-alt1
- 0.4302 -> 0.4401
- DateTime.pm now requires Time/y2038.pm

* Thu Jun 19 2008 Alexey Tourbin <at@altlinux.ru> 0.43-alt1
- 0.42 -> 0.4302

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 0.42-alt1
- 0.37 -> 0.42

* Mon Apr 09 2007 Alexey Tourbin <at@altlinux.ru> 0.37-alt1
- 0.34 -> 0.37

* Tue Sep 05 2006 Alexey Tourbin <at@altlinux.ru> 0.34-alt1
- 0.33 -> 0.34

* Wed Aug 09 2006 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- 0.30 -> 0.33

* Wed Apr 19 2006 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- 0.29.01 -> 0.30

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.29.01-alt1
- initial revision
