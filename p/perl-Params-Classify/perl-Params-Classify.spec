%define dist Params-Classify
Name: perl-%dist
Version: 0.013
Release: alt3.1.1.1

Summary: Argument type classification
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-parent

%description
This module provides various type-testing functions.  These are intended
for functions that, unlike most Perl code, care what type of data they
are operating on.  For example, some functions wish to behave differently
depending on the type of their arguments (like overloaded functions
in C++).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Params
%perl_vendor_autolib/Params

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.013-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.013-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.013-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.013-alt2
- rebuilt for perl-5.16

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.013-alt1
- initial revision
