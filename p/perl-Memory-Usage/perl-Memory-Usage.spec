%define _unpackaged_files_terminate_build 1

Name: perl-Memory-Usage
Version: 0.201
Release: alt2

Summary: Tools to determine actual memory usage
License: %perl_license
Group: Development/Perl
URL: https://metacpan.org/pod/Memory::Usage
BuildArch: noarch

Source: https://cpan.metacpan.org/authors/id/D/DO/DONEILL/Memory-Usage-%{version}.tar.gz

BuildRequires(pre): rpm-build-licenses
BuildRequires: perl-ExtUtils-MakeMaker-CPANfile
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
This module lets you attempt to measure, from your operating system's
perspective, how much memory a process is using at any given time.

%package doc
Summary: Documentation for perl Memory::Usage module
Group: Development/Perl

%description doc
%summary.

%prep
%setup -n Memory-Usage-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/module-size
%perl_vendor_privlib/Memory*

%files doc
%_man1dir/*

%changelog
* Wed Jun 11 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.201-alt2
- Fix dubious ownership according to perl policy.

* Tue May 06 2025 Sergey Zhidkih <rx1513@altlinux.org> 0.201-alt1
- Initial build.
