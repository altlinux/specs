%define module Encode-Detect

Name: perl-%module
Version: 1.01
Release: alt3.1.1.1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perl module that detects the encoding of data
License: MPL
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Encode/Encode-Detect-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: gcc-c++ perl-Encode-JP perl-Module-Build

%description
This module allows to determine the charset of the input data and then
decode it using the encoder of the detected charset.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Encode
%perl_vendor_autolib/Encode

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt1.2
- rebuilt for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt1.1
- rebuilt with perl 5.12

* Wed Jun 25 2008 Victor Forsyuk <force@altlinux.org> 1.01-alt1
- 1.01

* Fri May 04 2007 Victor Forsyuk <force@altlinux.org> 1.00-alt1
- Initial build.
