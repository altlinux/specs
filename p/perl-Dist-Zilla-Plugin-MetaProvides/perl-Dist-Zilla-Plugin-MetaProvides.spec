## SPEC file for Perl module Dist::Zilla::Plugin::MetaProvides

%define real_name Dist-Zilla-Plugin-MetaProvides

Name: perl-Dist-Zilla-Plugin-MetaProvides
Version: 2.001002
Release: alt1

Summary: Generating and Populating 'provides' in META.yml

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-MetaProvides/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Dec 20 2015
# optimized out: perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Method-Modifiers perl-Class-Tiny perl-Class-XSAccessor perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-DPath perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-PartialDump perl-Devel-StackTrace perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-pushd perl-Iterator perl-Iterator-Util perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Test-Deep perl-Test-Fatal perl-Text-Balanced perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-recommended perl-unicore
BuildRequires: perl-Dist-Zilla-Util-ConfigDumper perl-Dist-Zilla-Util-Test-KENTNL perl-Hash-Merge-Simple perl-JSON-XS

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
* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.001002-alt1
- Initial build for ALT Linux Sisyphus
