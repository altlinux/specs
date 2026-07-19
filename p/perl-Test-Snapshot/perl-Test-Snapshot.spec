%define _unpackaged_files_terminate_build 1
%define module_name Test-Snapshot

Name: perl-%module_name
Version: 0.06
Release: alt1

Summary: Test against data stored in automatically-named files
License: GPL-1.0-or-later OR Artistic-1.0-clause
Group: Development/Perl
URL: %CPAN %module_name
# Source-url: https://cpan.metacpan.org/authors/id/E/ET/ETJ/%module_name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-Text-Diff perl-Capture-Tiny

%description
Test::Snapshot provides a simple way to test code by comparing its output
against data stored in automatically-named snapshot files, updating them
when run in a special mode.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Test/Snapshot.pm

%changelog
* Sun Jul 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- initial build for ALT Sisyphus
