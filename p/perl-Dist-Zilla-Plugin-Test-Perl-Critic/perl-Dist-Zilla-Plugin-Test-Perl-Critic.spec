## SPEC file for Perl module Dist::Zilla::Plugin::Test::Perl::Critic

Name: perl-Dist-Zilla-Plugin-Test-Perl-Critic
Version: 3.001
Release: alt1

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

# Automatically added by buildreq on Sun May 14 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Term-ANSIColor perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3 python3-base
BuildRequires: perl-Class-XSAccessor perl-Cpanel-JSON-XS perl-Dist-Zilla perl-Module-Build-Tiny perl-Pod-Coverage perl-Ref-Util perl-Test-Perl-Critic perl-YAML

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
* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.001-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.000-alt1
- New version

* Fri Sep 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.112410-alt4
- Rising release to override package from Autoimports/Sisyphus repository

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.112410-alt1
- Initial build for ALT Linux Sisyphus
