## SPEC file for Perl module Dist::Zilla::Plugin::Git

%define real_name Dist-Zilla-Plugin-Git

Name: perl-Dist-Zilla-Plugin-Git
Version: 2.048
Release: alt2

Summary: Dist:Zilla plugin to Update git repository after release

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Git/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Sep 20 2021
# optimized out: git-core libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-DateTime perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-REPL perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Which perl-File-chdir perl-File-pushd perl-Getopt-Long-Descriptive perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-Getopt perl-MooseX-LazyRequire perl-MooseX-Object-Pluggable perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-Sort-Versions perl-Specio perl-String-Errf perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Syntax-Keyword-Junction perl-Term-ReadLine-Gnu perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Time-Piece perl-Try-Tiny perl-Type-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: gnupg perl-Archive-Tar-Wrapper perl-CPAN-Meta-Check perl-Class-XSAccessor perl-Dist-Zilla-Plugin-Config-Git perl-Git-Wrapper perl-IPC-System-Simple perl-Moose-Autobox perl-MooseX-Aliases perl-MooseX-Has-Sugar perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-Pod-Coverage perl-Pod-Weaver perl-Ref-Util perl-Ref-Util-XS perl-Test-Fatal perl-Test-Moose-More perl-Types-Path-Tiny perl-Version-Next perl-YAML

%description
Perl module Dist::Zilla::PluginBundle::Git provides a set of
plugins for Dist::Zilla that can do interesting things for
module authors using Git (http://git-scm.com) to track their
work.

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
* Mon Sep 20 2021 Vitaly Lipatov <lav@altlinux.ru> 2.048-alt2
- update BuildRequires with buildreq

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.048-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.047-alt1
- New version

* Fri May 10 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.046-alt1
- New version

* Mon Jun 11 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.045-alt1
- New version

* Sun Jun 03 2018 Nikolay A. Fetisov <naf@altlinux.org> 2.044-alt1
- New version

* Sat Dec 23 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.043-alt1
- New version

* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.042-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.041-alt2
- Initial build for ALT Linux Sisyphus
