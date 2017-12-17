%define dist Array-RefElem
Name: perl-%dist
Version: 1.00
Release: alt5.1.1.1.1

Summary: Set up array elements as aliases
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
This module gives direct access to some of the internal Perl routines
that let you store things in arrays and hashes.  The following
functions are available:

* av_store()
* av_push()
* hv_store()

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Array
%perl_vendor_autolib/Array

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt5.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt5.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt5.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt5
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt4
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.00-alt3
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt2.1
- rebuilt with perl 5.12

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 1.00-alt2
- fix directory ownership violation

* Sun Aug 03 2008 Michael Bochkaryov <misha@altlinux.ru> 1.00-alt1
- initial build for ALT Linux

