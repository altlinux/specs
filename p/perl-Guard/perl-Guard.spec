%define module Guard

Name: perl-%module
Version: 1.023
Release: alt1.1.1.1.1

Summary: Safe cleanup blocks for Perl
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/Guard-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
This module implements so-called "guards". A guard is something (usually an
object) that "guards" a resource, ensuring that it is cleaned up when expected.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Guard*
%perl_vendor_autolib/Guard

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.023-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.023-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.023-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.023-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.023-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.022-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.022-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.022-alt2
- rebuilt for perl-5.14

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.022-alt1
- 1.022

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.021-alt1.1
- rebuilt with perl 5.12

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 1.021-alt1
- Initial build.
