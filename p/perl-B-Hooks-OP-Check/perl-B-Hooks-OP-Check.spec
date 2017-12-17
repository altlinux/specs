%define _unpackaged_files_terminate_build 1
%define dist B-Hooks-OP-Check
Name: perl-%dist
Version: 0.22
Release: alt1.1

Summary: Wrap OP check callbacks
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-ExtUtils-Depends perl-Pod-Escapes perl-devel perl-parent

%description
This module provides a C api for XS modules to hook into the callbacks
of PL_check.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/B
%perl_vendor_autolib/B

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.19-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.19-alt2
- rebuilt for perl-5.16

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- initial revision
