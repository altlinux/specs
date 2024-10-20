## SPEC file for Perl module Dist::Zilla::Plugin::Git::Contributors

%define real_name Dist-Zilla-Plugin-Git-Contributors

Name: perl-Dist-Zilla-Plugin-Git-Contributors
Version: 0.037
Release: alt1

Summary: Dist::Zilla plugin to add contributor names from git

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Plugin-Git-Contributors/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 21 2021
# optimized out: git-core libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-REPL perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-chdir perl-File-pushd perl-Getopt-Long-Descriptive perl-Git-Wrapper perl-IO-String perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-Getopt perl-MooseX-LazyRequire perl-MooseX-Object-Pluggable perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Elemental-PerlMunger perl-Pod-Eventual perl-Pod-Weaver perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Sort-Versions perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Term-ReadLine-Gnu perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Unicode-Normalize perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla-Plugin-Git perl-Dist-Zilla-Plugin-PodWeaver perl-List-UtilsBy perl-Module-Build-Tiny perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-PPI-XS perl-Pod-Coverage perl-Pod-Weaver-Section-Contributors perl-Ref-Util perl-Ref-Util-XS perl-Test-Fatal perl-Test-Moose-More perl-Test-Needs perl-Unicode-Collate perl-YAML

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
* Thu Mar 28 2024 Nikolay A. Fetisov <naf@altlinux.org> 0.037-alt1
- New version

* Tue Sep 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.036-alt2
- update BuildRequires with buildreq

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.036-alt1
- New version

* Sun Sep 16 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.035-alt1
- New version

* Thu May 03 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.034-alt1
- New version

* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.032-alt1
- New version

* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.030-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.029-alt2
- Initial build for ALT Linux Sisyphus
