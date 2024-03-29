## SPEC file for Perl module MooseX::Types::Path::Tiny

%define real_name MooseX-Types-Path-Tiny

Name: perl-MooseX-Types-Path-Tiny
Version: 0.012
Release: alt2

Summary: Path::Tiny types and coercions for Moose

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/MooseX-Types-Path-Tiny/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri Sep 17 2021
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Tiny perl-Config-MVP perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-REPL perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-pushd perl-Getopt-Long-Descriptive perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-Getopt perl-MooseX-LazyRequire perl-MooseX-Object-Pluggable perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Term-ReadLine-Gnu perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Try-Tiny perl-Variable-Magic perl-aliased perl-autobox perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: perl-Class-XSAccessor perl-Devel-PartialDump perl-Dist-Zilla perl-Module-Build-Tiny perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-MooseX-Types-Stringlike perl-Pod-Weaver perl-Ref-Util perl-Ref-Util-XS perl-Test-Fatal perl-Test-Moose-More perl-YAML

%description
Perl module MooseX::Types::Path::Tiny provides Path::Tiny types
for Moose. It handles two important types of coercion:

- coercing objects with overloaded stringification
- coercing to absolute paths

It also can check to ensure that files or directories exist.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX/Types/Path/Tiny*

%changelog
* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.012-alt2
- update BR

* Sun Apr 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.012-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.011-alt2
- Initial build for ALT Linux Sisyphus
