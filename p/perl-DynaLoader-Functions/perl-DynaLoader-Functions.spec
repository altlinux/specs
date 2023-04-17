%define _unpackaged_files_terminate_build 1
Name: perl-DynaLoader-Functions
Version: 0.004
Release: alt1

Summary: deconstructed dynamic C library loading
Group: Development/Perl
License: perl

Url: %CPAN DynaLoader-Functions
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(parent.pm) perl-devel perl(Module/Build.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/DynaLoader/Functions*
%doc Changes README

%changelog
* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 0.004-alt1
- new version

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- automated CPAN update

* Fri Dec 06 2013 Vladimir Lettiev <crux@altlinux.ru> 0.002-alt1
- initial build for ALTLinux

