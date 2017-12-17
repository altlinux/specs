Name: perl-IO-FDPass
Version: 1.2
Release: alt1.1.1

Summary: pass a file descriptor over a socket
Group: Development/Perl
License: Perl

Url: %CPAN IO-FDPass
Source: %name-%version.tar

BuildRequires: perl-devel perl(Canary/Stability.pm)

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1
- rebuild with new perl 5.24.1

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.1
- rebuild with new perl 5.20.1

* Fri Jan 17 2014 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt2
- fixed summary

* Thu Jan 16 2014 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- initial build for ALTLinux

