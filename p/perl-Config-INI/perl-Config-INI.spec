## SPEC file for Perl module Config::INI

Name: perl-Config-INI
Version: 0.019
Release: alt1

Summary: Perl module to work with simple .ini-file format

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Config-INI/
#URL: https://github.com/rjbs/config-ini

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Config-INI
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Data-OptList perl-IO-String perl-Params-Util perl-Sub-Exporter perl-Sub-Install
BuildRequires: perl-Mixin-Linewise perl-devel

%description
Perl module Config::INI provides read and write access to the
simple .ini-file format.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Config/INI*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.019-alt1
- Initial build for ALT Linux Sisyphus

