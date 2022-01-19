%define _unpackaged_files_terminate_build 1
%define bname Crypt-OpenSSL-X509
Name: perl-%bname
Version: 1.912
Release: alt1
Summary: Perl interface to OpenSSL for X509
License: Perl
Group: Development/Perl
URL: http://search.cpan.org/dist/%bname/
Source0: http://www.cpan.org/authors/id/J/JO/JONASBN/Crypt-OpenSSL-X509-%{version}.tar.gz

BuildRequires: rpm-build-perl perl-devel libssl-devel perl-Test-Pod perl(inc/Module/Install.pm) perl(Convert/ASN1.pm)

%description
Crypt::OpenSSL::X509 - Perl extension to OpenSSL's X509 API.


%prep
%setup -q -n Crypt-OpenSSL-X509-%{version}
# Remove bundled modules
rm -rf ./inc

%build
%perl_vendor_build


%install
%perl_vendor_install


%check
%make_build test


%files
%doc README Changes.md
%perl_vendor_archlib/auto/*
%perl_vendor_archlib/Crypt


%changelog
* Wed Jan 19 2022 Igor Vlasenko <viy@altlinux.org> 1.912-alt1
- automated CPAN update

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 1.910-alt1
- automated CPAN update

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 1.908-alt1
- automated CPAN update

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 1.906-alt1
- automated CPAN update

* Tue Apr 13 2021 Igor Vlasenko <viy@altlinux.org> 1.903-alt1
- automated CPAN update

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 1.902-alt1
- automated CPAN update

* Sun Nov 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.901-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 1.813-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.812-alt1.1
- rebuild with new perl 5.28.1

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.812-alt1
- automated CPAN update

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 1.811-alt1
- automated CPAN update

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.809-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.809-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.808-alt2.1
- rebuild with new perl 5.26.1

* Sun Dec 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.808-alt2
- fix for perl 5.26

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
