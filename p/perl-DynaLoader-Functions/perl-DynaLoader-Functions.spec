Name: perl-DynaLoader-Functions
Version: 0.002
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
* Fri Dec 06 2013 Vladimir Lettiev <crux@altlinux.ru> 0.002-alt1
- initial build for ALTLinux

