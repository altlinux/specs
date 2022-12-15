## SPEC file for Perl module Dist::Zilla::Plugin::PromptIfStale

%define real_name Dist-Zilla-Plugin-PromptIfStale

Name: perl-Dist-Zilla-Plugin-PromptIfStale
Version: 0.057
Release: alt1.1

Summary: Dist::Zilla module to check at build/release time

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-PromptIfStale/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu Dec 15 2022
# optimized out: libgpg-error perl perl-App-Cmd perl-CPAN-DistnameInfo perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Class-Method-Modifiers perl-Config-MVP perl-Encode perl-File-pushd perl-HTTP-Message perl-HTTP-Tiny perl-JSON-PP perl-Log-Dispatch perl-Module-CoreList perl-Module-Metadata perl-Module-Runtime perl-Moose perl-Parse-CPAN-Meta perl-Path-Tiny perl-Term-ANSIColor perl-Test-Deep perl-Test-Fatal perl-Try-Tiny perl-YAML-Tiny perl-devel perl-namespace-autoclean perl-parent sh4
BuildRequires: perl-Dist-Zilla perl-IO-Tty perl-Parse-CPAN-Packages-Fast

%description
Perl module Dist::Zilla::Plugin::PromptIfStale is a Dist::Zilla
BeforeBuild or BeforeRelease plugin that compares the
locally-installed version of a module(s) with the latest indexed
version, prompting to abort the build process if a discrepancy
is found.

# PTY is needed to run tests - disable them inside hasher
%ifdef __BTE
%def_without test
%endif

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/*

%changelog
* Thu Dec 15 2022 Ivan A. Melnikov <iv@altlinux.org> 0.057-alt1.1
- NMU: Rerun buildreq to get rid of recursive build dependencies

* Sun May 17 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.057-alt1
- New version

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.056-alt1
- New version

* Sat May 12 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.055-alt1
- New version

* Wed Aug 30 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.054-alt1
- New version

* Sun Apr 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.053-alt1
- New version

* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.052-alt1
- New version

* Mon Jan 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.051-alt1
- Initial build for ALT Linux Sisyphus
