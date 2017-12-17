%define dist Text-CHM
Name: perl-%dist
Version: 0.01
Release: alt4.1.1.1.1

Summary: Perl module for handling Compiled HtmlHelp Files (.chm)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libchm-devel perl-devel

%description
Perl module Text::CHM  implements a (partial) support for handling
Compiled HTML Help Files (chm files for short) via CHMLib.  CHMLib
is a small library  designed for accessing MS ITSS files. The ITSS
file format is used for chm files, which have been the predominant
medium for software documentation from Microsoft.

Text::CHM  allows you  to open chm files, get their filelist,  get
the content of each file and close them.  At the moment,  no write
support is available.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README contrib*
%perl_vendor_autolib/Text
%perl_vendor_archlib/Text

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt2.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt2.1
- rebuilt with perl 5.12

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.01-alt2
- Fix typo in package summary

* Sun Jul 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.01-alt1
- First build for ALT Linux Sisyphus

* Sun Jul 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.01-alt0
- Initial build
