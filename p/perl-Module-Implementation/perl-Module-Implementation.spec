Name: perl-Module-Implementation
Version: 0.07
Release: alt1

Summary: Module::Implementation loads one of several alternate underlying implementations for a module 
Group: Development/Perl
License: Perl

Url: %CPAN Module-Implementation
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: perl-devel perl-Module-Runtime perl-Try-Tiny perl-Test-Fatal perl-Test-Requires

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Implementation*
%doc LICENSE Changes README 

%changelog
* Sun Aug 25 2013 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- 0.06 -> 0.07

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- initial build
