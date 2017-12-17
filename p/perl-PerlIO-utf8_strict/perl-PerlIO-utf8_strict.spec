## SPEC file for Perl module PerlIO::utf8_strict

Name: perl-PerlIO-utf8_strict
Version: 0.007
Release: alt1.1

Summary: fast and correct UTF-8 IO module

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/PerlIO-utf8_strict/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

%define real_name PerlIO-utf8_strict
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Sat Jun 13 2015
# optimized out: perl-Sub-Uplevel perl-devel
BuildRequires: perl-Test-Exception

%description
Perl module PerlIO::utf8_strict provides a fast and correct UTF-8
PerlIO layer. Unlike perl's default :utf8 layer it checks the
input for correctness.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PerlIO*
%perl_vendor_autolib/PerlIO*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1.1
- rebuild with new perl 5.26.1

* Sun Apr 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.007-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1.1
- rebuild with new perl 5.22.0

* Sat Jun 13 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.006-alt1
- New version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1.1
- rebuild with new perl 5.20.1

* Sun Nov 16 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.005-alt1
- New version

* Wed Sep 17 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.004-alt3
- Rising release to override package from Autoimports/Sisyphus repository

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.004-alt1
- Initial build for ALT Linux Sisyphus
