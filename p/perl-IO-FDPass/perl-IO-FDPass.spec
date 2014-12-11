Name: perl-IO-FDPass
Version: 1.0
Release: alt2.1

Summary: pass a file descriptor over a socket
Group: Development/Perl
License: Perl

Url: %CPAN IO-FDPass
Source: %name-%version.tar

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
%perl_vendor_autolib/IO/FDPass*
%perl_vendor_archlib/IO/FDPass*
%doc README Changes

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.1
- rebuild with new perl 5.20.1

* Fri Jan 17 2014 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt2
- fixed summary

* Thu Jan 16 2014 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- initial build for ALTLinux

