## SPEC file for Perl module Dist::Zilla::Plugin::Git::Remote::Check

%define real_name Dist-Zilla-Plugin-Git-Remote-Check

%define _unpackaged_files_terminate_build 1

Name: perl-Dist-Zilla-Plugin-Git-Remote-Check
Version: 0.1.2
Release: alt4

Summary: ensure no pending commits on a remote branch before release

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Plugin-Git-Remote-Check

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Mar 09 2026
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Class-Load perl-Data-Dump perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-File-chdir perl-HTML-Parser perl-JSON-PP perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Html perl-Pod-Simple perl-Sort-Versions perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Try-Tiny perl-Variable-Magic perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators python3 python3-base sh5
BuildRequires: perl-Dist-Zilla perl-Git-Wrapper perl-Module-Build

%description
Perl module Dist::Zilla::Plugin::Git::Remote::Check provides Dist:Zilla
pluging to ensure no pending commits on a remote branch before release.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/Git/Remote*
%perl_vendor_privlib/Dist/Zilla/Role/Git*


%changelog
* Mon Mar 09 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.1.2-alt4
Bump release to override autoimports package

* Mon Mar 09 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.1.2-alt1
- Initial build for ALT Linux Sisyphus
