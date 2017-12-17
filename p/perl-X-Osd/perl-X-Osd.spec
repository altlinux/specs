%define dist X-Osd
Name: perl-%dist
Version: 0.7
Release: alt4.1.1.1.1

Summary: Perl extension to the X On Screen Display library (xosd)
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libxosd-devel perl-devel xvfb-run

%description
XOSD displays text on your screen, sounds simple right? The difference
is it is unmanaged and shaped, so it appears transparent. This gives the
effect of an On Screen Display, like your TV/VCR etc..
It currently supports 3 type of writes, string for simple text, printf
formatted text, slider and percentage display.

%prep
%setup -q -n %dist-%version

%ifndef _build_display
%def_without test
%endif

%build
%perl_vendor_build

xvfb-run -a make test

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/X
%perl_vendor_autolib/X

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.7-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.7-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.7-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.7-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.7-alt2.2
- rebuilt with perl-5.14
- enabled tests using Xvfb

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7-alt2.1
- rebuilt with perl 5.12

* Mon Jun 30 2008 Grigory Milev <week@altlinux.ru> 0.7-alt2
- fix build requires

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.7-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sat Apr 17 2004 Grigory Milev <week@altlinux.ru> 0.7-alt1
- Initial build for ALT Linux.
