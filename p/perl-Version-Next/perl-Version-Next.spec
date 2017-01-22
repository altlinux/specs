## SPEC file for Perl module Version::Next

%define real_name Version-Next

Name: perl-Version-Next
Version: 1.000
Release: alt2

Summary: Perl module to increment module version numbers

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/Version-Next/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-CPAN-Meta-Requirements perl-Data-OptList perl-Encode perl-JSON-PP perl-Params-Util perl-Parse-CPAN-Meta perl-Sub-Install perl-Sub-Uplevel perl-devel python-base python-modules python3-base
BuildRequires: perl-CPAN-Meta perl-Sub-Exporter perl-Test-Exception

%description
Perl module Version::Next provides  a simple, correct way to
increment a Perl module version number. It does not attempt
to guess what the original version number author intended,
it simply increments in the smallest possible fashion.
Decimals are incremented like an odometer. Dotted decimals
are incremented piecewise and presented in a standardized way.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Version/Next*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.000-alt2
- Initial build for ALT Linux Sisyphus
