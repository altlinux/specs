%define _unpackaged_files_terminate_build 1
%define module Async-Interrupt

Name: perl-%module
Version: 1.22
Release: alt1
Epoch: 1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Allow C/XS libraries to interrupt perl asynchronously  
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/M/ML/MLEHMANN/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-common-sense perl-devel

%description
This module implements asynchronous notifications that enable you to signal
running perl code from another thread, asynchronously, and sometimes even
without using a single syscall.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Async
%perl_vendor_autolib/Async

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.22-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.21-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.21-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.21-alt1.1
- rebuild with new perl 5.22.0

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.21-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1.1
- rebuild with new perl 5.20.1

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1:1.1-alt2
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1:1.1-alt1
- 1.05 -> 1.1
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt1.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1.1
- rebuilt with perl 5.12

* Fri Jun 25 2010 Victor Forsiuk <force@altlinux.org> 1.05-alt1
- 1.05

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 1.02-alt1
- Initial build.
