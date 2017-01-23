## SPEC file for Perl module Dist::Zilla::Plugin::PromptIfStale

%define real_name Dist-Zilla-Plugin-PromptIfStale

Name: perl-Dist-Zilla-Plugin-PromptIfStale
Version: 0.051
Release: alt1

Summary: Dist::Zilla module to check at build/release time

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-PromptIfStale/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: perl perl-App-Cmd perl-B-Hooks-EndOfScope perl-CPAN perl-CPAN-DistnameInfo perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Capture-Tiny perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Compress-Raw-Zlib perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Which perl-File-pushd perl-Getopt-Long-Descriptive perl-HTTP-Message perl-HTTP-Tiny perl-IO-Compress perl-IO-Socket-IP perl-IO-Stty perl-IO-Tty perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-CoreList perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Term-Encoding perl-Test-Deep perl-Test-Fatal perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Dist-Zilla-Plugin-CheckExtraTests perl-JSON-XS perl-Module-Metadata perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-Parse-CPAN-Packages-Fast perl-Pod-Coverage perl-Pod-Weaver perl-Test-Moose-More

%description
Perl module Dist::Zilla::Plugin::PromptIfStale is a Dist::Zilla
BeforeBuild or BeforeRelease plugin that compares the
locally-installed version of a module(s) with the latest indexed
version, prompting to abort the build process if a discrepancy
is found.

# PTY is needed to run tests - disable them inside hasher
%ifdef __BTE
%def_without test
%endif

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/*

%changelog
* Mon Jan 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.051-alt1
- Initial build for ALT Linux Sisyphus
