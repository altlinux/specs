%define _unpackaged_files_terminate_build 1
%define module_name Hash-Merge-Extra

Name: perl-%module_name
Version: 0.06
Release: alt1

Summary: Collection of extra behaviors for Hash::Merge
License: GPL-1.0-or-later OR Artistic-1.0-clause
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/M/MI/MIXAS/%module_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-Hash-Merge

%description
This module is a collection of extra merge behaviors for Hash::Merge.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Hash/Merge/Extra.pm

%changelog
* Sat Jul 18 2026 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- initial build for ALT Sisyphus
