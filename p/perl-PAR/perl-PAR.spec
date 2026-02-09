## SPEC file for Perl module PAR

%define real_name PAR

Name: perl-PAR
Version: 1.021
Release: alt1

Summary: Perl Archive Toolkit

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/PAR/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Feb 09 2026
# optimized out: libgpg-error perl perl-CPAN-Meta-Requirements perl-Compress-Raw-Zlib perl-Digest-SHA perl-Encode perl-IO-Compress perl-JSON-PP perl-Parse-CPAN-Meta perl-devel perl-parent python-modules python2-base python3 python3-base sh5
BuildRequires: perl-Archive-Zip perl-CPAN-Meta perl-PAR-Dist perl-prefork

%description
Perl module PAR is a toolkit to create and use perl scripts
and modules stored inside compressed .par files.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/PAR*

%changelog
* Mon Feb 09 2026 Nikolay A. Fetisov <naf@altlinux.org> 1.021-alt1
- New version

* Thu Mar 28 2024 Nikolay A. Fetisov <naf@altlinux.org> 1.020-alt1
- New version

* Tue Nov 07 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.019-alt1
- New version

* Mon Dec 05 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.018-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.017-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.016-alt1
- New version

* Fri Mar 09 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.015-alt2
- Initial build for ALT Linux Sisyphus
