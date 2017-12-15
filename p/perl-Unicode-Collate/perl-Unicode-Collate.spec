%define _unpackaged_files_terminate_build 1
%define dist Unicode-Collate
Name: perl-%dist
Version: 1.25
Release: alt1.1

Summary: Unicode Collation Algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SA/SADAHIRO/%{dist}-%{version}.tar.gz

# require Unicode::Normalize without `eval'
Patch: perl-Unicode-Collate-0.56-alt-deps.patch

# avoid rpmdb bloat
%add_findprov_skiplist */Unicode/Collate/Locale/*.pl

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Unicode-Normalize perl-devel

%description
This module implements Unicode Collation Algorithm,
as described by Unicode Technical Standard #10 (UTS #10).

%prep
%setup -q -n %{dist}-%{version}
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Unicode
%perl_vendor_autolib/Unicode

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1.1
- rebuild with new perl 5.26.1

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1.1
- rebuild with new perl 5.24.1

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1.1
- rebuild with new perl 5.20.1

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Mon Oct 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.98-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.89-alt1
- 0.87 -> 0.89
- built for perl-5.16

* Tue Dec 06 2011 Kirill Maslinsky <kirill@altlinux.org> 0.87-alt1
- 0.78 -> 0.87

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.78-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 0.72-alt1
- 0.68 -> 0.72

* Sat Dec 25 2010 Alexey Tourbin <at@altlinux.ru> 0.68-alt1
- 0.56 -> 0.68

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.56-alt1.1
- rebuilt with perl 5.12

* Tue Aug 17 2010 Alexey Tourbin <at@altlinux.ru> 0.56-alt1
- 0.53 -> 0.56

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 0.53-alt1
- 0.52 -> 0.53

* Thu Jul 06 2006 Alexey Tourbin <at@altlinux.ru> 0.52-alt1
- 0.50 -> 0.52
- allkeys.txt was bundled

* Thu May 12 2005 Alexey Tourbin <at@altlinux.ru> 0.50-alt1
- 0.40 -> 0.50
- updated allkeys.txt (Unicode 4.1.0)

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 0.40-alt1
- initial revision (split from perl-i18n)
- installed allkeys.txt from unicode.org, just as recommended
