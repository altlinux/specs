%define dist Text-CHM
Name: perl-%dist
Version: 0.01
Release: alt2.2

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
