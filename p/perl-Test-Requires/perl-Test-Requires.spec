Name: perl-Test-Requires
Version: 0.07
Release: alt1

Summary: Checks to see if the module can be loaded
Group: Development/Perl
License: perl

Url: %CPAN Test-Requires
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(CPAN/Meta.pm) perl(Module/Build.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Requires*
%doc Changes LICENSE README.md

%changelog
* Mon Sep 16 2013 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- New version 0.07

* Fri Oct 01 2010 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- New version 0.06

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build
