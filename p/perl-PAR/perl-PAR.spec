## SPEC file for Perl module PAR

%define real_name PAR

Name: perl-PAR
Version: 1.018
Release: alt1

Summary: Perl Archive Toolkit

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/PAR/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri Mar 09 2018
# optimized out: perl perl-CPAN-Meta-Requirements perl-Compress-Raw-Zlib perl-Encode perl-IO-Compress perl-JSON-PP perl-Parse-CPAN-Meta perl-devel perl-parent python-base python-modules python3 python3-base python3-module-mpl_toolkits python3-module-zope ruby ruby-stdlibs
BuildRequires: perl-Archive-Zip perl-CPAN-Meta perl-Digest-SHA

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
* Mon Dec 05 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.018-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.017-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.016-alt1
- New version

* Fri Mar 09 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.015-alt2
- Initial build for ALT Linux Sisyphus
