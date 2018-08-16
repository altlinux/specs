## SPEC file for Perl module Number::WithError

%define real_name Number-WithError

Name: perl-Number-WithError
Version: 1.01
Release: alt2

Summary: real numbers with error propagation and scientific rounding

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Number-WithError

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu Aug 16 2018
# optimized out: perl perl-CPAN-Meta-Requirements perl-Devel-Symdump perl-Encode perl-Filter perl-JSON-PP perl-Math-BigInt perl-Parse-CPAN-Meta perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-parent python-base python-modules python3 python3-base python3-dev ruby sh3
BuildRequires: perl-CPAN-Meta perl-Params-Util perl-Test-LectroTest perl-Test-Pod perl-Test-Pod-Coverage perl-prefork

%description
Perl module Number::WithError is a container class for numbers
with a number of associated symmetric and asymmetric errors.
It overloads practically all common arithmetic operations and
trigonometric functions to propagate the errors. It can do
proper scientific rounding. 

You can use Math::BigFloat objects as the internal representation
of numbers in order to support arbitrary precision calculations.

Errors are propagated using Gaussian error propagation.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Number/WithError*

%changelog
* Thu Aug 16 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.01-alt2
- Initial build for ALT Linux Sisyphus
