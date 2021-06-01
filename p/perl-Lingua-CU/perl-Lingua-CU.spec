%define _unpackaged_files_terminate_build 1
%define dist Lingua-CU
Name: perl-Lingua-CU
Version: 0.04
Release: alt1

Summary: A Perl module for working with Church Slavonic text

License: BSD like
Group: Development/Perl
URL: https://github.com/typiconman/Perl-Lingua-CU

# Source-url: https://github.com/typiconman/Perl-Lingua-CU/archive/refs/heads/master.zip
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: perl-Parse-CPAN-Meta perl-Tie-IxHash perl-Unicode-Collate perl-podlators

BuildRequires: perl-devel

%description
A Perl module for working with Church Slavonic text.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/hip2unicode
%_bindir/ucs2unicode
%_man1dir/*
%dir %perl_vendor_privlib/Lingua/
%perl_vendor_privlib/Lingua/CU/
%perl_vendor_privlib/Lingua/CU.pm
%perl_vendor_privlib/Lingua/mklocale.pl

%changelog
* Tue Jun 01 2021 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- initial build for ALT Sisyphus
