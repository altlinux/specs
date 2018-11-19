%define _unpackaged_files_terminate_build 1

Name:           perl-URI-db
Version:        0.19
Release:        alt1
Summary:        Perl support for database URIs
License:        GPL+ or Artistic
Group: 		Development/Perl
URL:            https://metacpan.org/release/URI-db/
Source:        	%name-%version.tar
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
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README README.md
%perl_vendorlib/URI*

%changelog
* Tue Nov 20 2018 Alexandr Antonov <aas@altlinux.org> 0.19-alt1
- initial build for ALT
