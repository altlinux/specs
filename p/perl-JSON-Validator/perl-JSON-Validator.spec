%define _unpackaged_files_terminate_build 1

Name: perl-JSON-Validator
Version: 3.17
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
%perl_vendorlib/JSON*
%doc Changes README.md

%changelog
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
