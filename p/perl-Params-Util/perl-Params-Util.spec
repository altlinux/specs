%define dist Params-Util
Name: perl-%dist
Version: 1.07
Release: alt2.1.1.1.1

Summary: Simple standalone param-checking functions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-ExtUtils-CBuilder

%description
Params::Util provides a basic set of importable functions that makes
checking parameters a hell of a lot easier.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Params
%perl_vendor_autolib/Params

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.07-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.07-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.07-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt2.1
- rebuild with new perl 5.20.1

* Sun Aug 25 2013 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt2
- built for perl 5.18

* Mon Aug 27 2012 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- 1.04 -> 1.07
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- 1.03 -> 1.04
- built for perl-5.14
- rebuilt as plain src.rpm

* Tue Dec 28 2010 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.00 -> 1.03

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt1.1
- rebuilt with perl 5.12

* Mon Jun 29 2009 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- 0.38 -> 1.00

* Mon Mar 09 2009 Alexey Tourbin <at@altlinux.ru> 0.38-alt1
- 0.35 -> 0.38

* Sun Nov 23 2008 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- 0.33 -> 0.35
- noarch -> $arch, due to new XS code

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- 0.31 -> 0.33

* Sat Apr 12 2008 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.25 -> 0.31

* Sat Jun 16 2007 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- 0.17 -> 0.25

* Wed Aug 09 2006 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- 0.05 -> 0.17

* Tue Sep 06 2005 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision (for PPI)
