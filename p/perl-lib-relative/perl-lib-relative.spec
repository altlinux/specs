%define _unpackaged_files_terminate_build 1

Name:           perl-lib-relative
Version:        1.002
Release:        alt1
Summary:        Add paths relative to the current file to @INC
License:        Artistic-2.0
Group: Development/Perl
Url:            https://metacpan.org/release/lib-relative
Source0: http://www.cpan.org/authors/id/D/DB/DBOOK/lib-relative-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)

%description
This module proposes a straightforward method for adding local directory to
@INC. It takes a path relative to the current file, absolutize it, and add
it to @INC.

%prep
%setup -q -n lib-relative-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md README
%perl_vendorlib/* 
 
%changelog
* Fri Jul 28 2023 Igor Vlasenko <viy@altlinux.org> 1.002-alt1
- automated CPAN update

* Wed Jun 22 2022 Igor Vlasenko <viy@altlinux.org> 1.001-alt1
- automated CPAN update

* Mon Mar 28 2022 Alexandr Antonov <aas@altlinux.org> 1.000-alt1
- initial build for ALT
