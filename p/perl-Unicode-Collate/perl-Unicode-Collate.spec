%define dist Unicode-Collate
Name: perl-%dist
Version: 0.87
Release: alt1

Summary: Unicode Collation Algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
%setup -q -n %dist-%version
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
