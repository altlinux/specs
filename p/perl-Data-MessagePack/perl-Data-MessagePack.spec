Name: perl-Data-MessagePack
Version: 1.00
Release: alt2

Summary: MessagePack serialising/deserialising
License: Perl
Group: Development/Perl

URL: %CPAN Data-MessagePack
Source: %name-%version.tar
Patch0: Data-MessagePack-1.00-Fix-building-on-Perl-without-dot-in-INC.patch

BuildRequires: perl-devel perl-Encode perl-Test-Requires

%description
This module converts Perl data structures to MessagePack and vice versa.

MessagePack is a binary-based efficient object serialization format. It
enables to exchange structured objects between many languages like JSON.
But unlike JSON, it is very fast and small.

%prep
%setup -q
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/Data/MessagePack*
%perl_vendor_autolib/Data/MessagePack

%changelog
* Sun Dec 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- patch for perl 5.26

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1.1
- rebuild with new perl 5.24.1

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- new version 0.48

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.47-alt1
- 0.46 -> 0.47

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.46-alt1
- 0.41 -> 0.46
- built for perl-5.16

* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.41-alt1
- New version 0.41

* Tue Dec 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt1
- New version 0.39

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.38-alt1
- 0.34 -> 0.38
- built for perl-5.14

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 0.34-alt1
- initial build
