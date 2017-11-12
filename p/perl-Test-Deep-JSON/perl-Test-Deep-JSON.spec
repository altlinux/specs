## SPEC file for Perl module Test::Deep::JSON

%define real_name Test-Deep-JSON

Name: perl-Test-Deep-JSON
Version: 0.04
Release: alt1

Summary: Perl module to compare JSON with Test::Deep

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-Deep-JSON/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Nov 12 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-JSON-PP perl-JSON-XS perl-Parse-CPAN-Meta perl-Term-ANSIColor perl-Types-Serialiser perl-common-sense perl-devel perl-threads python-base python-modules python3 python3-base
BuildRequires: perl-Exporter-Lite perl-JSON perl-Module-Build-Tiny perl-Test-Deep

%description
Perl module Test::Deep::JSON provides provides json($expected)
function to expect that target can be parsed as a JSON string
and matches (by cmp_deeply) with $expected.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/Test/Deep/JSON*

%changelog
* Sun Nov 12 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.04-alt1
- New version

* Sat Sep 17 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt2
- Initial build for ALT Linux Sisyphus
