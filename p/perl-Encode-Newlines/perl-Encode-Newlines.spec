%define _unpackaged_files_terminate_build 1
%define sname Encode-Newlines

Name:  perl-Encode-Newlines
Version: 0.05
Release: alt1
Summary: Normalize line ending sequences
License: GPL-1.0+ or Artistic-1.0-Perl
Group: Development/Perl
Url: https://metacpan.org/release/Encode-Newlines
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Encode/Encoding.pm)

%description
This module provides the CR, LF, CRLF and Native encodings, to aid in
normalizing line endings.

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendorlib/*

%changelog
* Mon May 16 2022 Alexandr Antonov <aas@altlinux.org> 0.05-alt1
- initial build for ALT

