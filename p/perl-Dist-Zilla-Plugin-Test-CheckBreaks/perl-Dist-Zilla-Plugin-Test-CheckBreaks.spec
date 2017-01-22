## SPEC file for Perl module Dist::Zilla::Plugin::Test::CheckBreaks

%define real_name Dist-Zilla-Plugin-Test-CheckBreaks

Name: perl-Dist-Zilla-Plugin-Test-CheckBreaks
Version: 0.017
Release: alt2

Summary: Generate a test that shows what modules you are breaking

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Test-CheckBreaks/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: perl-CPAN-Meta-Check perl-Class-XSAccessor perl-Dist-Zilla perl-Dist-Zilla-Role-ModuleMetadata perl-JSON-XS perl-Module-Build-Tiny perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-Pod-Coverage perl-Test-Moose-More

%description
Perl module Dist::Zilla::Plugin::Test::CheckBreaks is a Dist::Zilla
plugin that runs at the gather files stage, providing a test file
that runs last in your test suite and checks for conflicting
modules, as indicated by x_breaks in your distribution metadata.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/Test/CheckBreaks*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 0.017-alt2
- Initial build for ALT Linux Sisyphus
