## SPEC file for Perl module Test::Deep::JSON

%define real_name Test-Deep-JSON

Name: perl-Test-Deep-JSON
Version: 0.03
Release: alt2

Summary: Perl module to compare JSON with Test::Deep

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-Deep-JSON/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Sep 17 2016
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-CBuilder perl-IPC-Cmd perl-JSON-PP perl-JSON-XS perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Types-Serialiser perl-common-sense perl-devel perl-parent perl-podlators perl-threads python-base python-modules python3
BuildRequires: perl-Exporter-Lite perl-HTML-Parser perl-JSON perl-Module-Build perl-Test-Deep

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
* Sat Sep 17 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt2
- Initial build for ALT Linux Sisyphus
