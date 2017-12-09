## SPEC file for Perl module Dist::Zilla::Plugin::Git::Contributors

%define real_name Dist-Zilla-Plugin-Git-Contributors

Name: perl-Dist-Zilla-Plugin-Git-Contributors
Version: 0.032
Release: alt1

Summary: Dist::Zilla plugin to add contributor names from git

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Git-Contributors/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Dec 09 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-chdir perl-File-pushd perl-Git-Wrapper perl-IO-String perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Elemental-PerlMunger perl-Pod-Eventual perl-Pod-Weaver perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Sort-Versions perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Test-Deep perl-Test-Fatal perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Unicode-Normalize perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3 python3-base
BuildRequires: git-core perl-Class-XSAccessor perl-Dist-Zilla-Plugin-Git perl-Dist-Zilla-Plugin-PodWeaver perl-List-UtilsBy perl-Module-Build-Tiny perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-PPI-XS perl-Pod-Coverage perl-Pod-Weaver-Section-Contributors perl-Ref-Util perl-Ref-Util-XS perl-Test-Moose-More perl-Test-Needs perl-Unicode-Collate perl-YAML

%description
Perl module Dist::Zilla::Plugin::Git::Contributors is a Dist::Zilla
plugin that extracts all names and email addresses from git commits
in your repository and adds them to the distribution metadata under
the x_contributors key. It takes a minimalist approach to this
-- no data is stuffed into other locations, including stashes --
if other plugins wish to work with this information, they should
extract it from the distribution metadata.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/Git/Contributors*

%changelog
* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.032-alt1
- New version

* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.030-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.029-alt2
- Initial build for ALT Linux Sisyphus
