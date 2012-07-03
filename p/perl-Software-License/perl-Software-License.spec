## SPEC file for Perl module Software::License

Name: perl-Software-License
Version: 0.103004
Release: alt1

Summary: Perl module that provide templated software licenses

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Software-License/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Software-License
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Data-OptList perl-MRO-Compat perl-Params-Util perl-Sub-Exporter perl-Sub-Install
BuildRequires: perl-Data-Section perl-Text-Template perl-devel

%description
Perl module Software::License provides templated software licenses.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Software/License*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.103004-alt1
- Initial build for ALT Linux Sisyphus

