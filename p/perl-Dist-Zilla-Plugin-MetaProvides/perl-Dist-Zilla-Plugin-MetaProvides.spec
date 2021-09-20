## SPEC file for Perl module Dist::Zilla::Plugin::MetaProvides

%define real_name Dist-Zilla-Plugin-MetaProvides

Name: perl-Dist-Zilla-Plugin-MetaProvides
Version: 2.002004
Release: alt2

Summary: Generating and Populating 'provides' in META.yml

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-MetaProvides/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 21 2021
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Tiny perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: perl-Class-XSAccessor perl-Devel-PartialDump perl-Dist-Zilla perl-Hash-Merge-Simple perl-Ref-Util perl-Ref-Util-XS perl-Test-Fatal

%description
Perl module Dist::Zilla::Plugin::MetaProvides contains a small
bundle of plugins for various ways of populating the META.yml
that is built with your distribution.

The initial reason for this is due to stuff that uses
MooseX::Declare style class definitions not being parseable by
many tools upstream, so this is here to cover this problem by
defining it in the metadata.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/MetaProvides*
%perl_vendor_privlib/Dist/Zilla/MetaProvides*
%perl_vendor_privlib/Dist/Zilla/Role/MetaProvider*

%changelog
* Tue Sep 21 2021 Vitaly Lipatov <lav@altlinux.ru> 2.002004-alt2
- update BuildRequires with buildreq

* Sun Mar 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.002004-alt1
- New version

* Sat Jul 30 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.002003-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.001011-alt1
- New version

* Sun Jan 10 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.001002-alt2
- Bump release to override package from autoimports/Sisyphus repository

* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.001002-alt1
- Initial build for ALT Linux Sisyphus
