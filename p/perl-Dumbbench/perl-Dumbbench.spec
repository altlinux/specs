## SPEC file for Perl module Dumbbench

%define real_name Dumbbench

Name: perl-Dumbbench
Version: 0.501
Release: alt1

Summary: Perl module for reliable benchmarking with the least amount of thinking

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dumbbench/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

Patch0: %real_name-0.111-alt-XS.patch

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri Aug 17 2018
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Params-Util perl-Parse-CPAN-Meta perl-devel perl-parent perl-prefork python-base python-modules python3 python3-base python3-dev ruby sh3
BuildRequires: perl-CPAN-Meta perl-Capture-Tiny perl-Class-XSAccessor perl-Devel-CheckOS perl-Number-WithError perl-Statistics-CaseResampling

%description
Perl module Dumbbench attempts to implement reasonably robust
benchmarking with little extra effort and expertise required
from the user.

%prep
%setup -q -n %real_name-%version
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.pod Changes
%perl_vendor_privlib/Dumbbench*
%perl_vendor_privlib/Benchmark/Dumb.pm

%_bindir/dumbbench

# We don't have (optional) SOOT module to provide graphics
%exclude %perl_vendor_privlib/Dumbbench/BoxPlot.pm

%changelog
* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.501-alt1
- New version

* Fri Aug 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.111-alt1
- Initial build for ALT Linux Sisyphus
