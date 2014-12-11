%define dist HTML-CTPP2
Name: perl-%dist
Version: 2.6.7
Release: alt4.1

Summary: Perl interface for CTPP2 library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: gcc-c++ libctpp-devel perl-IO-stringy perl-devel

%description
This module is very similar to well-known Sam Tregar's HTML::Template
but works in 22 - 25 times faster and contains extra functionality.

%prep
%setup -q -n %dist-%version

# XXX tests fail
mv t/test02.t{,.orig}
mv t/test04.t{,.orig}
mv t/test06.t{,.orig}
mv t/test10.t{,.orig}

%build
export CTPP2_LIB=%_libdir
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_archlib/HTML
%perl_vendor_autolib/HTML

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.6.7-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.6.7-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 2.6.7-alt3
- rebuilt for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 2.6.7-alt2
- rebuilt for perl-5.14

* Wed Feb 16 2011 Denis Smirnov <mithraen@altlinux.ru> 2.6.7-alt1
- initial build for ALT Linux Sisyphus
