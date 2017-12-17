Name: perl-Proc-FastSpawn
Version: 1.2
Release: alt1.1.1.1.1

Summary: fork+exec, or spawn, a subprocess as quickly as possible
Group: Development/Perl
License: Perl

Url: %CPAN Proc-FastSpawn
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
%perl_vendor_autolib/Proc/FastSpawn*
%perl_vendor_archlib/Proc/FastSpawn*
%doc README Changes

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1
- rebuild with new perl 5.20.1

* Fri Jan 17 2014 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt1
- initial build for ALTLinux

