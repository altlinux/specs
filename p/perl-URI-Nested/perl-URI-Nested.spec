%define _unpackaged_files_terminate_build 1

Name:           perl-URI-Nested
Version:        0.10
Release:        alt1
Summary:        Perl support for nested URIs
License:        GPL+ or Artistic
Group: 		Development/Perl
URL:            https://metacpan.org/release/URI-Nested/
Source:		%name-%version.tar
BuildArch:      noarch

BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(URI/QueryParam.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(utf8.pm)

%description
This class provides support for nested URIs, where the scheme is a
prefix, and the remainder of the URI is another URI. Examples include
JDBC URIs and database URIs.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendorlib/URI*

%changelog
* Tue Nov 20 2018 Alexandr Antonov <aas@altlinux.org> 0.10-alt1
- initial build for ALT
