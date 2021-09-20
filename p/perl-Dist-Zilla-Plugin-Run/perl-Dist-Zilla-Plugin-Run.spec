## SPEC file for Perl module Dist::Zilla::Plugin::Run

%define real_name Dist-Zilla-Plugin-Run

Name: perl-Dist-Zilla-Plugin-Run
Version: 0.048
Release: alt3

Summary: Perl module to run commands at specific phases of Dist::Zilla

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Plugin-Run

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 21 2021
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Inspector perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-REPL perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-ShareDir perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-Getopt perl-MooseX-LazyRequire perl-MooseX-Object-Pluggable perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Specio perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Term-ReadLine-Gnu perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Dist-Zilla-Plugin-Git perl-Module-Build-Tiny perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-Pod-Weaver perl-Ref-Util perl-Ref-Util-XS perl-Test-Fatal perl-Test-File-ShareDir perl-Test-Moose-More perl-YAML

%description
Perl module Dist::Zilla::Plugin::Run allows to run external
commands and code at specific phases of Dist::Zilla.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/Run*

%changelog
* Tue Sep 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.048-alt3
- update BuildRequires with buildreq

* Mon May 18 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.048-alt2
Bump release to override autoimports package

* Mon May 18 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.048-alt1
- Initial build for ALT Linux Sisyphus
