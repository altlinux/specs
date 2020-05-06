## SPEC file for Perl module Dist::Zilla::Plugin::ContributorsFile

%define real_name Dist-Zilla-Plugin-ContributorsFile

Name: perl-Dist-Zilla-Plugin-ContributorsFile
Version: 0.3.0
Release: alt2

Summary: Perl module to add a file listing all contributors

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Plugin-ContributorsFile

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Wed May 06 2020
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-HTML-Parser perl-JSON-PP perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Moose perl-MooseX-SetOnce perl-MooseX-Types perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Path-Tiny perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Text-Template perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators python-modules python2-base python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: perl-Dist-Zilla perl-Module-Build

%description
Perl module  Dist::Zilla::Plugin::ContributorsFile populates
a CONTRIBUTORS file with all the contributors of the project
as found under the x_contributors key in the META files.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/ContributorsFile*

%changelog
* Wed May 06 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.3.0-alt2
- Bump release to override autoimport package

* Wed May 06 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.3.0-alt1
- Initial build for ALT Linux Sisyphus
