## SPEC file for Perl module Dist::Zilla::Plugin::Test::Perl::Critic

Name: perl-Dist-Zilla-Plugin-Test-Perl-Critic
Version: 2.112410
Release: alt4

Summary: Dist::Zilla tests to check code against best practices

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-Test-Perl-Critic/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Dist-Zilla-Plugin-Test-Perl-Critic
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Encode perl-Eval-Closure perl-File-Copy-Recursive perl-File-Find-Rule perl-File-HomeDir perl-File-Which perl-File-pushd perl-HTML-Parser perl-Hash-Merge-Simple perl-IPC-Run3 perl-Import-Into perl-JSON perl-JSON-PP perl-JSON-XS perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-Moose-Autobox perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Perl-OSType perl-PerlIO-utf8_strict perl-Pod-Escapes perl-Pod-Simple perl-Probe-Perl perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Scope-Guard perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-YAML-Tiny perl-aliased perl-autobox perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-podlators perl-strictures perl-unicore
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-Module-Build perl-Test-Script perl-Variable-Magic

%description
Perl module Dist::Zilla::Plugin::Test::Perl::Critic provides
Dist::Zilla tests to check code against best practices.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin*

%changelog
* Fri Sep 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.112410-alt4
- Rising release to override package from Autoimports/Sisyphus repository

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.112410-alt1
- Initial build for ALT Linux Sisyphus
