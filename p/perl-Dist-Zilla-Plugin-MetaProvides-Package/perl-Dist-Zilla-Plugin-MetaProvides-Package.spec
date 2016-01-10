## SPEC file for Perl module Dist::Zilla::Plugin::MetaProvides::Package

%define real_name Dist-Zilla-Plugin-MetaProvides-Package

Name: perl-Dist-Zilla-Plugin-MetaProvides-Package
Version: 2.003001
Release: alt2

Summary: Extract namespaces/version from traditional packages for provides

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-MetaProvides-Package/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Dec 20 2015
# optimized out: perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Method-Modifiers perl-Class-XSAccessor perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-DPath perl-Data-Dump perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-Zilla perl-Dist-Zilla-Util-ConfigDumper perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-IO-String perl-Iterator perl-Iterator-Util perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Test-Deep perl-Test-Fatal perl-Text-Balanced perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-recommended perl-unicore
BuildRequires: perl-Dist-Zilla-Plugin-MetaProvides perl-Dist-Zilla-Util-Test-KENTNL perl-JSON-XS perl-Module-Metadata perl-PPI-XS perl-Safe-Isa

%description
Perl module Dist::Zilla::Plugin::MetaProvides::Package is a
Dist::Zilla Plugin that populates the provides property of
META.json and META.yml by absorbing it from your shipped
modules, in a manner similar to how PAUSE itself does it.

This allows you to easily create an authoritative index of
what module provides what version in advance of PAUSE
indexing it, which PAUSE in turn will take verbatim.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/MetaProvides/Package*

%changelog
* Sun Jan 10 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.003001-alt2
- Bump release to override package from autoimports/Sisyphus repository

* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.003001-alt1
- Initial build for ALT Linux Sisyphus
