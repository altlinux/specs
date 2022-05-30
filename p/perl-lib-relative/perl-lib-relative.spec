%define _unpackaged_files_terminate_build 1

Name:           perl-lib-relative
Version:        1.000
Release:        alt1
Summary:        Add paths relative to the current file to @INC
License:        Artistic-2.0
Group: Development/Perl
Url:            https://metacpan.org/release/lib-relative
Source: %name-%version.tar
BuildArch:      noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)

%description
This module proposes a straightforward method for adding local directory to
@INC. It takes a path relative to the current file, absolutize it, and add
it to @INC.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/* 
 
%changelog
* Mon Mar 28 2022 Alexandr Antonov <aas@altlinux.org> 1.000-alt1
- initial build for ALT
