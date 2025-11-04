## SPEC file for Perl module Dist::Zilla::Plugin::Test::CheckBreaks

%define real_name Dist-Zilla-Plugin-Test-CheckBreaks

Name: perl-Dist-Zilla-Plugin-Test-CheckBreaks
Version: 0.020
Release: alt1

Summary: Generate a test that shows what modules you are breaking

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Test-CheckBreaks/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Nov 04 2025
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python-modules python2-base python3 python3-base sh5 tzdata
BuildRequires: perl-CPAN-Meta-Check perl-Class-XSAccessor perl-Dist-Zilla-Plugin-Git perl-Dist-Zilla-Role-ModuleMetadata perl-Module-Build-Tiny perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-Pod-Coverage perl-Pod-Weaver perl-Ref-Util perl-Ref-Util-XS perl-Sub-Name perl-Test-Moose-More perl-YAML

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
* Tue Nov 04 2025 Nikolay A. Fetisov <naf@altlinux.org> 0.020-alt1
- New version

* Wed Aug 30 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.019-alt1
- New version

* Sun Apr 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.018-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 0.017-alt2
- Initial build for ALT Linux Sisyphus
