Name: perl-Text-Xslate
Version: 3.4.0
Release: alt1.1

Summary: Text::Xslate - Scalable template engine for Perl5
License: Perl
Group: Development/Perl

Url: %CPAN Text-Xslate
# Cloned from git://github.com/xslate/p5-Text-Xslate.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-Any-Moose perl-Data-MessagePack perl-Devel-StackTrace perl-Encode-JP perl-File-Copy-Recursive perl-Module-Install-TestTarget perl-Module-Install-XSUtil perl-Mouse perl-Template perl-Test-Requires perl-autodie perl-unicore

%description
Xslate is a template engine for Perl5 with the following features:
* Extremely fast - Up to 50~100 times faster than TT2!
* Supports multiple template syntaxes - TT2 compatible syntax,
  for example
* Easy to enhance - by importing subroutines and/or by calling
  object methods
* Safe - Escapes HTML meta characters by default

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README.md example
%_bindir/xslate
%_man1dir/xslate.1*
%perl_vendor_archlib/Text/Xslate*
%perl_vendor_autolib/Text/Xslate
%doc Changes README.md HACKING

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1.1
- rebuild with new perl 5.26.1

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.0-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.9-alt1.1
- rebuild with new perl 5.24.1

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.9-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.3.7-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 3.3.7-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.3.3-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1.1
- rebuild with new perl 5.20.1

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt1
- new version 3.2.4

* Thu Dec 12 2013 Vladimir Lettiev <crux@altlinux.ru> 3.1.0-alt1
- 2.0009 -> 3.1.0

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.0009-alt1
- 1.6001 -> 2.0009

* Tue Dec 18 2012 Vladimir Lettiev <crux@altlinux.ru> 1.6001-alt2
- Optimized build requires

* Tue Dec 18 2012 Vladimir Lettiev <crux@altlinux.ru> 1.6001-alt1
- 1.5018 -> 1.6001

* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5018-alt1
- 1.5017 -> 1.5018

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5017-alt1
- 1.5007 -> 1.5017
- built for perl-5.16

* Sun Dec 04 2011 Vladimir Lettiev <crux@altlinux.ru> 1.5007-alt2
- Buildreq Amon2 -> Amon2::Lite

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.5007-alt1
- New version 1.5007

* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 1.5003-alt1
- 1.5002 -> 1.5003
- built for perl-5.14

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 1.4001-alt1
- New version 1.4001

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.4000-alt1
- New version 1.4000

* Sat Mar 05 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0012-alt1
- New version 1.0012

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0011-alt1
- New version 1.0011

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0008-alt1
- initial build
