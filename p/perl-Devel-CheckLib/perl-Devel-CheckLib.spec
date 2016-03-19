## SPEC file for Perl module Devel::CheckLib

%define real_name Devel-CheckLib

Name: perl-Devel-CheckLib
Version: 1.06
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

# Automatically added by buildreq on Mon Sep 28 2015
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-parent
BuildRequires: perl-IO-CaptureOutput perl-devel perl-podlators

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
