Name: perl-Parse-Functions
Version: 0.01
Release: alt1

Summary: list all the functions in source code
Group: Development/Perl
License: perl

Url: %CPAN Parse-Functions
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Parse/Functions*
%doc Changes

%changelog
* Sun Nov 01 2015 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt1
- initial build for ALTLinux

