## SPEC file for Perl module Dist::Zilla::Plugin::Config::Git

%define real_name Dist-Zilla-Plugin-Config-Git

Name: perl-Dist-Zilla-Plugin-Config-Git
Version: 0.92
Release: alt2

Summary: Dist::Zilla plugin configuration for a Git repo

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Config-Git/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-JSON-PP perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Moose perl-MooseX-Types perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-String-Errf perl-String-Formatter perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Time-Piece perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3-base
BuildRequires: perl-Dist-Zilla perl-Test-CheckDeps

%description
Perl module Dist::Zilla::Plugin::Config::Git is a Dist:Zilla
configuration plugin for Git repo/branch information.
A configuration plugin is sort of like a Stash, but is better
suited for intra-plugin data sharing, using distro (not user)
data.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_privlib/Dist/Zilla/*

%changelog
* Mon Jan 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.92-alt2
- Initial build for ALT Linux Sisyphus
