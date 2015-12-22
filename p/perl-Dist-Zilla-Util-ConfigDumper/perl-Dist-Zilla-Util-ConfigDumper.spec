## SPEC file for Perl module Dist::Zilla::Util::ConfigDumper

%define real_name Dist-Zilla-Util-ConfigDumper

Name: perl-Dist-Zilla-Util-ConfigDumper
Version: 0.003007
Release: alt1

Summary: A Dist::Zilla plugin configuration extraction utility

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Util-ConfigDumper/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Dec 20 2015
# optimized out: perl-Algorithm-Diff perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Method-Modifiers perl-Class-XSAccessor perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-DPath perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-Zilla perl-Dist-Zilla-Role-Bootstrap perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-Iterator perl-Iterator-Util perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-List-UtilsBy perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Test-Deep perl-Test-Fatal perl-Text-Balanced perl-Text-Diff perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-recommended perl-unicore
BuildRequires: perl-Dist-Zilla-Plugin-Bootstrap-lib perl-Dist-Zilla-Util-Test-KENTNL perl-JSON-XS perl-Test-Differences

%description
Perl module Dist::Zilla::Util::ConfigDumper contains a utility
function for use within the "Dist::Zilla" plugin ecosystem, to
simplify extraction of plugin settings for plugin authors, in
order for plugins like "Dist::Zilla::Plugin::MetaConfig" to
expose those values to consumers.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Util/ConfigDumper*

%changelog
* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.003007-alt1
- Initial build for ALT Linux Sisyphus
