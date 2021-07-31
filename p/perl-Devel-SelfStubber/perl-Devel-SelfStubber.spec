%define modulename Devel-SelfStubber

Name:    perl-%modulename
Version: 1.05
Release: alt1

Summary: Generate stubs for a SelfLoading module
License: Perl
Group:   Development/Perl
URL:     https://metacpan.org/dist/Devel-SelfStubber

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm)

BuildArch: noarch

Source: %modulename-%version.tar.gz

%description
Devel::SelfStubber prints the stubs you need to put in the module before the
__DATA__ token (or you can get it to print the entire module with stubs
correctly placed). The stubs ensure that if a method is called, it will get
loaded. They are needed specifically for inherited autoloaded methods.

%prep
%setup -n %modulename-%version

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%makeinstall_std

%check
%make test

%files
%doc README META.yml META.json Changes
%perl_vendor_privlib/*

%changelog
* Sat Jul 31 2021 Andrey Cherepanov <cas@altlinux.org> 1.05-alt1
- Initial build for Sisyphus.
