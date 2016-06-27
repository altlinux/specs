## SPEC file for Perl module Test::MinimumVersion::Fast

%define real_name Test-MinimumVersion-Fast

Name: perl-Test-MinimumVersion-Fast
Version: 0.04
Release: alt2

Summary: Perl module to check minimal Perl version

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-MinimumVersion-Fast/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Compiler-Lexer perl-Encode perl-ExtUtils-CBuilder perl-File-Find-Rule perl-IPC-Cmd perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Number-Compare perl-Params-Check perl-Params-Util perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Text-Glob perl-devel perl-parent perl-podlators perl-threads python-base python-modules python3
BuildRequires: perl-File-Find-Rule-Perl perl-HTML-Parser perl-Module-Build perl-Perl-MinimumVersion-Fast perl-YAML-Tiny

%description
Perl module Test::MinimumVersion::Fast is a faster implementation
of Test::MinimumVersion Perl::MinimumVersion::Fast.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/Test/MinimumVersion/Fast*

%changelog
* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.04-alt2
- Initial build for ALT Linux Sisyphus
