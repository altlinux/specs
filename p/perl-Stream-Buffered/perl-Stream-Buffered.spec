Name: perl-Stream-Buffered
Version: 0.03
Release: alt1.1

Summary: temporary buffer to save bytes
Group: Development/Perl
License: perl

Url: %CPAN Stream-Buffered
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
%perl_vendor_privlib/Stream/Buffered*
%doc Changes README.md

%changelog
* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- dropped deprecated BR: perl-Module-Install

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Fri Dec 14 2012 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build for ALTLinux

