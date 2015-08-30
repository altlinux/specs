## SPEC file for Perl module recommended

%define real_name recommended

Name: perl-recommended
Version: 0.003
Release: alt1

Summary: Perl module to load recommended modules on demand

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/recommended/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Aug 30 2015
# optimized out: perl-CPAN-Meta-Requirements perl-Parse-CPAN-Meta perl-parent
BuildRequires: perl-CPAN-Meta perl-Module-Runtime perl-devel

%description
Perl module recommended gathers a list of recommended modules
and versions and provides means to check if they are available.
It is a thin veneer around Module::Runtime.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/recommended*
%perl_vendor_privlib/suggested*

%changelog
* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.003-alt1
- Initial build for ALT Linux Sisyphus
