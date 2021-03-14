## SPEC file for Perl module Dist::Zilla::Role::PluginBundle::PluginRemover

%define real_name Dist-Zilla-Role-PluginBundle-PluginRemover

%define _unpackaged_files_terminate_build 1

Name: perl-Dist-Zilla-Role-PluginBundle-PluginRemover
Version: 0.105
Release: alt2

Summary: Dist::Zilla plugin to a '-remove' functionality to a bundle

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Role-PluginBundle-PluginRemover

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Mar 14 2021
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-JSON-PP perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-MooseX-Types perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: perl-Dist-Zilla

%description
Perl module Dist::Zilla::Role::PluginBundle::PluginRemover enables
Dist::Zilla Plugin Bundle to automatically remove any plugins
specified by the -remove attribute (like @Filter does).


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Role/PluginBundle/PluginRemover*

%changelog
* Sun Mar 14 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.105-alt2
- Bump release to override autoimports package

* Sun Mar 14 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.105-alt1
- Initial build for ALT Linux Sisyphus
