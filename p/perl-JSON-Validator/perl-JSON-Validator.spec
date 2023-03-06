%define _unpackaged_files_terminate_build 1

Name: perl-JSON-Validator
Version: 5.14
Release: alt1
Summary: Validate data against a JSON schema
License: Artistic 2.0
Group: Development/Perl
Url: https://github.com/mojolicious/json-validator.git
Source0: http://www.cpan.org/authors/id/J/JH/JHTHORSEN/JSON-Validator-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  perl(ExtUtils/MakeMaker.pm) perl(Test/Deep.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Mojo/Base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Mojo/Base.pm)
BuildRequires:  perl(Mojo/File.pm)
BuildRequires:  perl(Mojo/JSON.pm)
BuildRequires:  perl(Mojo/JSON/Pointer.pm)
BuildRequires:  perl(Mojo/Loader.pm)
BuildRequires:  perl(Mojo/URL.pm)
BuildRequires:  perl(Mojo/UserAgent.pm)
BuildRequires:  perl(Mojo/Util.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Term/ANSIColor.pm)
BuildRequires:  perl(Tie/Hash.pm)
BuildRequires:  perl(Time/Local.pm)
BuildRequires:  perl(Data/Validate/Domain.pm)
BuildRequires:  perl(Data/Validate/IP.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(Mojolicious/Lite.pm)
BuildRequires:  perl(Net/IDN/Encode.pm)
BuildRequires:  perl(Test/Mojo.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Net/IDN/Encode.pm)
BuildRequires:  perl(Net/IDN/Encode.pm)
BuildRequires:  perl(YAML/XS.pm)
BuildRequires:  perl(lib.pm)

Requires:       perl(Mojolicious.pm)

%description
JSON::Validator is a data structure validation library based around JSON
Schema. This module can be used directly with a JSON schema or you can use
the elegant DSL schema-builder JSON::Validator::joi to define the schema
programmatically.

%prep
%setup -q -n JSON-Validator-%{version}
rm -f t/invalid-ref.t
%build
%perl_vendor_build

%install
%perl_vendor_install
%_fixperms $RPM_BUILD_ROOT/*

%files
%doc Changes CONTRIBUTING.md
%perl_vendorlib/JSON*
%doc Changes

%changelog
* Mon Mar 06 2023 Igor Vlasenko <viy@altlinux.org> 5.14-alt1
- automated CPAN update

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 5.13-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 5.13-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 5.12-alt1
- automated CPAN update

* Wed Aug 31 2022 Igor Vlasenko <viy@altlinux.org> 5.11-alt1
- automated CPAN update

* Thu Aug 18 2022 Igor Vlasenko <viy@altlinux.org> 5.10-alt1
- automated CPAN update

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 5.08-alt1
- automated CPAN update

* Sat Jan 08 2022 Igor Vlasenko <viy@altlinux.org> 5.05-alt1
- automated CPAN update

* Wed Dec 15 2021 Igor Vlasenko <viy@altlinux.org> 5.04-alt1
- automated CPAN update

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 5.03-alt1
- automated CPAN update

* Mon Oct 11 2021 Igor Vlasenko <viy@altlinux.org> 5.02-alt1
- automated CPAN update

* Tue Oct 05 2021 Igor Vlasenko <viy@altlinux.org> 5.01-alt1
- automated CPAN update

* Fri Sep 17 2021 Igor Vlasenko <viy@altlinux.org> 4.24-alt1
- automated CPAN update

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.org> 4.23-alt1
- automated CPAN update

* Sun Jul 11 2021 Igor Vlasenko <viy@altlinux.org> 4.21-alt1
- automated CPAN update

* Sat Jun 19 2021 Igor Vlasenko <viy@altlinux.org> 4.20-alt1
- automated CPAN update

* Thu Jun 17 2021 Igor Vlasenko <viy@altlinux.org> 4.18-alt1
- automated CPAN update

* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 4.17-alt1
- automated CPAN update

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 4.16-alt1
- automated CPAN update

* Wed Feb 24 2021 Igor Vlasenko <viy@altlinux.org> 4.14-alt1
- automated CPAN update

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 4.13-alt1
- automated CPAN update

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 4.12-alt1
- automated CPAN update

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 4.10-alt1
- automated CPAN update

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 4.05-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 4.04-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 4.02-alt1
- automated CPAN update

* Sat Jul 04 2020 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 4.00-alt1
- automated CPAN update

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 3.25-alt1
- automated CPAN update

* Tue Mar 03 2020 Igor Vlasenko <viy@altlinux.ru> 3.24-alt1
- automated CPAN update

* Thu Feb 20 2020 Igor Vlasenko <viy@altlinux.ru> 3.23-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 3.20-alt1
- automated CPAN update

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 3.17-alt1
- automated CPAN update

* Thu Oct 31 2019 Igor Vlasenko <viy@altlinux.ru> 3.16-alt1
- automated CPAN update

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 3.15-alt1
- automated CPAN update

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.14-alt1
- automated CPAN update

* Sun May 12 2019 Igor Vlasenko <viy@altlinux.ru> 3.11-alt1
- automated CPAN update

* Thu Apr 11 2019 Igor Vlasenko <viy@altlinux.ru> 3.08-alt1
- automated CPAN update

* Tue Apr 02 2019 Alexandr Antonov <aas@altlinux.org> 3.06-alt1
- initial build for ALT
