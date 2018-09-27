%define _unpackaged_files_terminate_build 1
%define module_version 0.11
%define module_name Number-Bytes-Human
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: %module_version
Release: alt1
Summary: Perl extension for convert byte count to human readable format
Group: Development/Perl
License: perl
Url: %CPAN %module_name
BuildRequires: perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-devel
BuildArch: noarch

# git://github.com/aferreira/cpan-Number-Bytes-Human.git
Source: %name-%version.tar

%description
From summary: %summary

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Number

%changelog
* Thu Sep 27 2018 Anton Farygin <rider@altlinux.ru> 0.11-alt1
- first build for ALT

