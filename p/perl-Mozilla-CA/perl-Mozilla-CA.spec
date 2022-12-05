## SPEC file for Perl module Mozilla::CA
%define _unpackaged_files_terminate_build 1
%define real_name Mozilla-CA

Name: perl-Mozilla-CA
Version: 20221114
Release: alt1

Summary: Perl module provides CA cert bundle

License: %mpl
Group: Development/Perl
URL: https://metacpan.org/dist/Mozilla-CA/
#URL: https://github.com/libwww-perl/Mozilla-CA

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses
Requires: ca-certificates

# Automatically added by buildreq on Sun May 24 2020
# optimized out: perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-parent python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-devel

BuildRequires: ca-certificates

%description
Perl module Mozilla::CA provide a single function SSL_ca_file()
that returns the absolute path to the Mozilla's CA cert bundle
PEM file.

Note: this package use CA bundle from system-wide package
ca-certificates .


%prep
%setup  -n %real_name-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Mozilla/CA.pm

%exclude %perl_vendor_privlib/Mozilla/CA/*

%changelog
* Mon Dec 05 2022 Nikolay A. Fetisov <naf@altlinux.org> 20221114-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 20211001-alt1
- New version
- Update URL

* Sun May 24 2020 Nikolay A. Fetisov <naf@altlinux.org> 20200520-alt1
- New version

* Fri Mar 02 2018 Nikolay A. Fetisov <naf@altlinux.org> 20180117-alt1
- New version

* Tue Jan 05 2016 Nikolay A. Fetisov <naf@altlinux.ru> 20160104-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 20150826-alt1
- New version

* Sat Jun 13 2015 Nikolay A. Fetisov <naf@altlinux.ru> 20141217-alt1
- New version

* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 20130114-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 20120823-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 20120118-alt1
- Initial build for ALT Linux Sisyphus

