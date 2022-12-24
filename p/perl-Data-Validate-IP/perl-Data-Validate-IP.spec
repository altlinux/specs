%define _unpackaged_files_terminate_build 1
%define bname Data-Validate-IP
Name: perl-%bname
Version: 0.31
Release: alt1
Summary: Perl IP address validation routines
Group: Development/Perl
License: Perl (GPL or Artistic)
URL: http://search.cpan.org/dist/%bname
Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%bname-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-perl perl-devel perl(NetAddr/IP.pm) perl(Test/Requires.pm)

%description
This module collects IP address validation routines to make input validation,
and untainting easier and more readable.


%prep
%setup -q -n %bname-%version


%build
%perl_vendor_build


%install
%perl_vendor_install


%files
%doc Changes README* CONTRIBUTING.md
%perl_vendor_privlib/Data


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.31-alt1
- new version

* Wed Mar 31 2021 Igor Vlasenko <viy@altlinux.org> 0.30-alt1
- new version

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Sun Jan 26 2014 Led <led@altlinux.ru> 0.18-alt1
- initial build
