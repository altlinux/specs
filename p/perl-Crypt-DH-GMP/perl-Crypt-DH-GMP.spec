%define _unpackaged_files_terminate_build 1
%define module Crypt-DH-GMP

Name: perl-%module
Version: 0.00012
Release: alt1.1.1.1.1

Summary: Crypt::DH Using GMP Directly
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/D/DM/DMAKI/Crypt-DH-GMP-%{version}.tar.gz

# Automatically added by buildreq on Fri Mar 09 2012
BuildRequires: libgmp-devel perl-Crypt-DH perl-Devel-CheckLib perl-Math-BigInt-GMP perl-Pod-Escapes perl-Test-Requires

%description
Crypt::DH::GMP is a (somewhat) portable replacement to Crypt::DH, implemented mostly in C.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Crypt/
%perl_vendor_archlib/Crypt/

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.00012-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.00012-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.00012-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.00012-alt1.1
- rebuild with new perl 5.20.1

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.00012-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.00011-alt1
- automated CPAN update

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.00010-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.00010-alt2
- rebuilt for perl-5.16

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.00010-alt1.1
- Rebuilt with gmp 5.0.5

* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 0.00010-alt1
- Initial build.
