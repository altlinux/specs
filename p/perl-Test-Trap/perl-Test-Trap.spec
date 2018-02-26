Name: perl-Test-Trap
Version: 0.2.1
Release: alt1

Summary: Test::Trap perl module
Group: Development/Perl
License: Perl

Url: %CPAN Test-Trap
Source: %name-%version.tar

BuildRequires: perl-devel perl-base perl-Module-Build perl-Test-Tester perl-Data-Dump

BuildArch: noarch
%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Trap*
%doc Changes README

%changelog
* Mon Oct 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.1-alt1
- initial build
