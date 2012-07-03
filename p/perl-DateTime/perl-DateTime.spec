%define dist DateTime
Name: perl-%dist
Version: 0.70
Release: alt2

Summary: DateTime base objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# break dependency loop
Requires: perl-DateTime-TimeZone

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-DateTime-Locale perl-DateTime-TimeZone perl-Math-Round perl-Module-Build perl-Test-Exception perl-Test-Warn

%description
DateTime is a class for the representation of date/time combinations,
and is part of the Perl DateTime project.  For details on this project
please see http://datetime.perl.org.  The DateTime site has a FAQ which
may help answer many "how do I do X?" questions.  The FAQ is at
http://datetime.perl.org/faq.html.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/DateTime*
%perl_vendor_autolib/DateTime*

%changelog
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
