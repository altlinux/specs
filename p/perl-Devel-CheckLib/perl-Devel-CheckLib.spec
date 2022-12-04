## SPEC file for Perl module Devel::CheckLib

%define real_name Devel-CheckLib

Name: perl-Devel-CheckLib
Version: 1.16
Release: alt1

Summary: check that a library is available

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Devel-CheckLib/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue May 05 2020
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-Pod-Escapes perl-Pod-Simple perl-parent perl-podlators python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Capture-Tiny perl-devel perl-podlators

%description
Perl module Devel::CheckLib provides a way of checking whether
a particular library and its headers are available, by
attempting to compile a simple program and link against it.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%exclude /.perl.req
%_bindir/use-devel-checklib
%_man1dir/use-devel-checklib*
%perl_vendor_privlib/Devel/CheckLib*

%changelog
* Sun Dec 04 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.16-alt1
- New version

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.14-alt1
- New version

* Mon Jun 11 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.13-alt1
- New version

* Sun Jun 03 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.12-alt1
- New version

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.11-alt1
- New version

* Sun Apr 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.10-alt1
- New version

* Sat Mar 25 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.09-alt1
- New version

* Sat May 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.07-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.06-alt1
- New version

* Mon Sep 28 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.05-alt1
- New version

* Sat Jan 10 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.03-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.01-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.99-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.98-alt1
- New version

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.91-alt1
- Initial build for ALT Linux Sisyphus
