%define _unpackaged_files_terminate_build 1
%define dist Email-Address
Name: perl-%dist
Version: 1.913
Release: alt1

Summary: RFC 2822 Address Parsing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl(Capture/Tiny.pm)

%description
This class implements a complete RFC 2822 parser that locates email
addresses in strings and returns a list of Email::Address objects
found. Alternatley you may construct objects manually. The goal
of this software is to be correct, and very very fast.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email*

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1.913-alt1
- automated CPAN update

* Tue Jan 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.912-alt1
- automated CPAN update

* Wed Dec 26 2018 Igor Vlasenko <viy@altlinux.ru> 1.911-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.909-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.908-alt1
- automated CPAN update

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.907-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.905-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.903-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.901-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.900-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.898-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.896-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.892-alt1
- 1.889 -> 1.892

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1.889-alt1
- 1.887 -> 1.889

* Wed Apr 18 2007 Alexey Tourbin <at@altlinux.ru> 1.887-alt1
- 1.884 -> 1.887

* Thu Feb 22 2007 Alexey Tourbin <at@altlinux.ru> 1.884-alt1
- 1.85 -> 1.884 (closes #10404)

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.85-alt1
- initial revision
