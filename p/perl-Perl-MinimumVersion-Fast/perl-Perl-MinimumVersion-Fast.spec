## SPEC file for Perl module Perl::MinimumVersion::Fast

%define real_name Perl-MinimumVersion-Fast

Name: perl-Perl-MinimumVersion-Fast
Version: 0.20
Release: alt1

Summary: find a minimum required version of perl for Perl code

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Perl-MinimumVersion-Fast/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-JSON-PP perl-Module-Load perl-Parse-CPAN-Meta perl-Pod-Escapes perl-Pod-Simple perl-Term-ANSIColor perl-devel perl-podlators python-base python-modules python3
BuildRequires: perl-Compiler-Lexer perl-Module-Build-Tiny

%description
Perl module Perl::MinimumVersion::Fast takes Perl source code
and calculates the minimum version of perl required to be able
to run it. Because it is based on goccy's Compiler::Lexer,
it can do this without having to actually load the code.

Perl::MinimumVersion::Fast is an alternative fast & lightweight
implementation of Perl::MinimumVersion.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/Perl/MinimumVersion/Fast*

%_bindir/perlver-fast
%_man1dir/perlver-fast*

%changelog
* Tue Jul 25 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.20-alt1
- New version

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.19-alt1
- New version

* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.18-alt2
- Initial build for ALT Linux Sisyphus
