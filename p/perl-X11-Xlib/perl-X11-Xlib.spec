Name: perl-X11-Xlib
Version: 0.14
Release: alt1.1

Summary: Low-level access to the X11 library
Group: Development/Perl
License: Perl

Url: %CPAN X11-Xlib
Source: %name-%version.tar

BuildRequires: perl-devel perl-Devel-CheckLib libX11-devel libXtst-devel xvfb-run perl(ExtUtils/Depends.pm) perl(Try/Tiny.pm)

%description
%summary

%prep
%setup -q

%build
%def_without test
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%perl_vendor_autolib/X11/Xlib*
%perl_vendor_archlib/X11/Xlib*
%doc Changes README

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- rebuild with new perl 5.26.1

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build for ALTLinux

