## SPEC file for Perl module CPAN-Uploader

Name: perl-CPAN-Uploader
Version: 0.103000
Release: alt1

Summary: Perl module to upload things to the CPAN

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/CPAN-Uploader/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name CPAN-Uploader
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-HTTP-Date perl-HTTP-Message perl-URI
BuildRequires: perl-Getopt-Long-Descriptive perl-Term-ReadKey perl-devel perl-libwww

%description
Perl module CPAN::Uploader upload things to the CPAN.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/CPAN/Uploader*

%_bindir/cpan-upload

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.103000-alt1
- Initial build for ALT Linux Sisyphus

