## SPEC file for Perl module Sub::Current

%define real_name Sub-Current

Name: perl-Sub-Current
Version: 0.03
Release: alt1.1

Summary: Perl module to get the current subroutine

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Sub-Current/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-devel python-base python-modules python3
BuildRequires: perl-Test-Pod

%description
Perl module Sub::Current makes available a function ROUTINE(),
that returns a code reference pointing at the currently
executing subroutine.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Sub/Current*
%perl_vendor_autolib/Sub/Current*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- rebuild with new perl 5.26.1

* Wed Feb 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.03-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt3.1
- rebuild with new perl 5.24.1

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 0.02-alt3
- Initial build for ALT Linux Sisyphus
