## SPEC file for Perl module Dist::Zilla::Role::RegisterStash

%define real_name Dist-Zilla-Role-RegisterStash

Name: perl-Dist-Zilla-Role-RegisterStash
Version: 0.003
Release: alt2

Summary: Dist::Zilla plugin that can register stashes

License: %lgpl21only
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Role-RegisterStash/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu May 04 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-Which perl-File-pushd perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-Want perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3
BuildRequires: perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Cpanel-JSON-XS perl-Dist-Zilla perl-Ref-Util perl-Test-CheckDeps perl-autobox-Core

%description
Perl module Dist::Zilla::Role::RegisterStash provides a
_register_stash() method to Dist::Zilla plugin, allowing
to register stashes.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Role/RegisterStash*

%changelog
* Thu May 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.003-alt2
- Initial build for ALT Linux Sisyphus
