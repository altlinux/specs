## SPEC file for Perl module Dist::Zilla::Plugin::Git

%define real_name Dist-Zilla-Plugin-Git

Name: perl-Dist-Zilla-Plugin-Git
Version: 2.041
Release: alt2

Summary: Dist:Zilla plugin to Update git repository after release

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Git/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jan 23 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-DateTime perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-File-Copy-Recursive perl-File-Find-Rule perl-File-HomeDir perl-File-Which perl-File-chdir perl-File-pushd perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-MooseX-Types-Stringlike perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Sort-Versions perl-String-Errf perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Test-Fatal perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Time-Piece perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: git-core gnupg perl-Archive-Tar-Wrapper perl-CPAN-Meta-Check perl-Class-XSAccessor perl-Devel-SimpleTrace perl-Dist-Zilla-Plugin-Config-Git perl-Git-Wrapper perl-IPC-System-Simple perl-JSON-XS perl-MooseX-Has-Sugar perl-MooseX-Types-Path-Tiny perl-Pod-Coverage perl-Version-Next

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
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.041-alt2
- Initial build for ALT Linux Sisyphus
