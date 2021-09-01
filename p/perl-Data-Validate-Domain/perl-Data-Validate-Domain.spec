%define _unpackaged_files_terminate_build 1
%define bname Data-Validate-Domain
Name: perl-%bname
Version: 0.15
Release: alt1
Summary: Domain validation methods Perl module
Group: Development/Perl
License: Perl (GPL or Artistic)
URL: http://search.cpan.org/dist/%bname
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/Data-Validate-Domain-%{version}.tar.gz
BuildArch: noarch

BuildRequires: rpm-build-perl perl-devel perl(Net/Domain/TLD.pm) perl(Test2/Plugin/UTF8.pm)

%description
This module collects domain validation routines to make input validation, and
untainting easier and more readable.


%prep
%setup -q -n Data-Validate-Domain-%{version}


%build
%perl_vendor_build


%install
%perl_vendor_install


%files
%doc Changes README* CONTRIBUTING.md
%perl_vendor_privlib/*


%changelog
* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.org> 0.15-alt1
- automated CPAN update

* Thu Sep 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sun Jan 26 2014 Led <led@altlinux.ru> 0.10-alt1
- initial build
