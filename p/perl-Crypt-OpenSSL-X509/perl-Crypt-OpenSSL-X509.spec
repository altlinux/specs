%define bname Crypt-OpenSSL-X509
Name: perl-%bname
Version: 1.808
Release: alt1
Summary: Perl interface to OpenSSL for X509
License: Perl
Group: Development/Perl
URL: http://search.cpan.org/dist/%bname/
Source0: http://www.cpan.org/authors/id/J/JO/JONASBN/Crypt-OpenSSL-X509-%{version}.tar.gz

BuildRequires: rpm-build-perl perl-devel libssl-devel perl-Test-Pod

%description
Crypt::OpenSSL::X509 - Perl extension to OpenSSL's X509 API.


%prep
%setup -q -n Crypt-OpenSSL-X509-%{version}


%build
%perl_vendor_build


%install
%perl_vendor_install


%check
%make_build test


%files
%doc Changes TODO README
%perl_vendor_archlib/auto/*
%perl_vendor_archlib/Crypt


%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.808-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.807-alt1.1
- rebuild with new perl 5.24.1

* Thu Sep 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.807-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.806-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.806-alt1
- automated CPAN update

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.805-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.804-alt1.1
- rebuild with new perl 5.20.1

* Sun Mar 30 2014 Led <led@altlinux.ru> 1.804-alt1
- 1.804

* Thu Feb 27 2014 Led <led@altlinux.ru> 1.800.2-alt1
- initial build
