%define _unpackaged_files_terminate_build 1

Name:           perl-URI-db
Version:        0.21
Release:        alt1
Summary:        Perl support for database URIs
License:        GPL+ or Artistic
Group: 		Development/Perl
URL:            https://metacpan.org/release/URI-db/
Source0:        	http://www.cpan.org/authors/id/D/DW/DWHEELER/URI-db-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(URI/Nested.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:	perl(Test/Spelling.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:  perl(utf8.pm)

%description
This class provides support for database URIs. They're inspired by
JDBC URIs and PostgreSQL URIs, though they're a bit more formal.
The specification for their format is documented in README.md.

%prep
%setup -q -n URI-db-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README README.md
%perl_vendorlib/URI*

%changelog
* Sun May 21 2023 Igor Vlasenko <viy@altlinux.org> 0.21-alt1
- automated CPAN update

* Wed Jun 22 2022 Igor Vlasenko <viy@altlinux.org> 0.20-alt1
- automated CPAN update

* Tue Nov 20 2018 Alexandr Antonov <aas@altlinux.org> 0.19-alt1
- initial build for ALT
