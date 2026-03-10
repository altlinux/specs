## SPEC file for Perl module Dist::Zilla::Config::Slicer

%define real_name Dist-Zilla-Config-Slicer

%define _unpackaged_files_terminate_build 1

Name: perl-Dist-Zilla-Config-Slicer
Version: 0.202
Release: alt2

Summary: Config::MVP::Slicer customized for Dist::Zilla

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Config-Slicer

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Mar 10 2026
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-JSON-PP perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-MooseX-Types perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Install perl-Try-Tiny perl-Variable-Magic perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base sh5
BuildRequires: perl-Config-MVP-Slicer perl-Dist-Zilla

%description
Perl module Dist::Zilla::Config::Slicer is a subclass of Config::MVP::Slicer
that overrides the default match_package to expand packages according
to Dist::Zilla's rules.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Config/Slicer*
%perl_vendor_privlib/Dist/Zilla/PluginBundle/*
%perl_vendor_privlib/Dist/Zilla/Role/PluginBundle/Config/Slicer*


%changelog
* Tue Mar 10 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.202-alt2
Bump release to override autoimports package

* Tue Mar 10 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.202-alt1
- Initial build for ALT Linux Sisyphus
