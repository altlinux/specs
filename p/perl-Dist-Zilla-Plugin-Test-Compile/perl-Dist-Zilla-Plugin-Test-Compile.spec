## SPEC file for Perl module Dist::Zilla::Plugin::Test::Compile

%define real_name Dist-Zilla-Plugin-Test-Compile

%define _unpackaged_files_terminate_build 1

Name: perl-Dist-Zilla-Plugin-Test-Compile
Version: 2.059
Release: alt1

Summary: common tests to check syntax of Perl modules by using only core modules

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Dist-Zilla-Plugin-Test-Compile

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Mar 10 2026
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-B-Keywords perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Find-Rule-Perl perl-File-pushd perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-CoreList perl-Module-Implementation perl-Module-Load perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-PPIx-Regexp perl-PPIx-Utils perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-Perl-MinimumVersion perl-Perl-PrereqScanner perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Safe-Isa perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Quote perl-Term-ANSIColor perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Type-Tiny perl-Variable-Magic perl-YAML-PP perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base sh5 tzdata
BuildRequires: perl-CPAN-Meta-Check perl-Class-XSAccessor perl-Dist-Zilla-Plugin-Git perl-Module-Build-Tiny perl-PPI-XS perl-Pod-Weaver perl-Ref-Util perl-Ref-Util-XS perl-Sub-Name perl-Test-MinimumVersion perl-Test-Warnings perl-YAML-LibYAML

%description
Perl module Dist::Zilla::Plugin::Test::Compile is a Dist::Zilla plugin that runs
at the gather files stage, providing a test file.
This test will find all modules and scripts in module distribution, and try to
compile them one by one. This means it's a bit slower than loading them all
at once, but it will catch more errors.

The generated test is guaranteed to only depend on modules that are available
in Perl core.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/Test/Compile*

%changelog
* Tue Mar 10 2026 Nikolay A. Fetisov <naf@altlinux.org> 2.059-alt1
- Initial build for ALT Linux Sisyphus
