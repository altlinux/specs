%define _unpackaged_files_terminate_build 1
%define dist Clone
Name: perl-%dist
Version: 0.39
Release: alt1.1

Summary: Recursively copy Perl datatypes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/G/GA/GARU/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
This module provides a clone() method which makes recursive
copies of nested hash, array, scalar and reference types,
including tied variables and objects.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/Clone*
%perl_vendor_autolib/Clone*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1.1
- rebuild with new perl 5.22.0

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1.1
- rebuild with new perl 5.20.1

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.31-alt4
- rebuilt for perl-5.16

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 0.31-alt3
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.31-alt2
- rebuilt as plain src.rpm

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.31-alt1.1
- rebuilt for perl-5.12

* Tue Mar 10 2009 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.28 -> 0.31

* Wed Mar 05 2008 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- 0.27 -> 0.28

* Thu Jul 26 2007 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- 0.22 -> 0.27
- Clone.pm: replaced DynaLoader with XSLoader, removed AutoLoader

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.20 -> 0.22

* Thu Jul 06 2006 Alexey Tourbin <at@altlinux.ru> 0.20-alt1
- 0.18 -> 0.20

* Tue Sep 06 2005 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- initial revision (for PPI) (also for Class::DBI)
