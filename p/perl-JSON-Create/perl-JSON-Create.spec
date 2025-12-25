%define _unpackaged_files_terminate_build 1
%define module_name JSON-Create

Name: perl-JSON-Create
Version: 0.35
Release: alt1

Summary: Create JSON
License: Perl
Group: Development/Perl
Url: https://metacpan.org/release/%module_name

# Source-url: https://cpan.metacpan.org/authors/id/B/BK/BKB/%module_name-%version.tar.gz
Source: %module_name-%version.tar

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(JSON/Parse.pm)
BuildRequires: perl(Unicode/UTF8.pm)

%description
This module converts Perl data structures to JSON.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/JSON/Create.pm
%perl_vendor_archlib/JSON/Create.pod
%dir %perl_vendor_archlib/JSON/Create
%perl_vendor_archlib/JSON/Create/PP.pm
%perl_vendor_archlib/JSON/Create/Bool.pm
%perl_vendor_autolib/JSON/Create

%changelog
* Thu Dec 25 2025 Vitaly Lipatov <lav@altlinux.ru> 0.35-alt1
- initial build for ALT Sisyphus (Closes: #57040)
