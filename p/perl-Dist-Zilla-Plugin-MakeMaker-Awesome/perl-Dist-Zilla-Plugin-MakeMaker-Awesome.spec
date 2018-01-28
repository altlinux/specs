## SPEC file for Perl module Dist::Zilla::Plugin::MakeMaker::Awesome

%define real_name Dist-Zilla-Plugin-MakeMaker-Awesome

Name: perl-Dist-Zilla-Plugin-MakeMaker-Awesome
Version: 0.40
Release: alt1

Summary: a more awesome MakeMaker plugin for Dist::Zilla

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-MakeMaker-Awesome/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Dec 06 2015
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Load perl-Class-Method-Modifiers perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-JSON-MaybeXS perl-JSON-PP perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Load perl-Module-Metadata perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-Perl-OSType perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore
BuildRequires: perl-CPAN-Meta-Check perl-Class-XSAccessor perl-Dist-Zilla perl-JSON-XS perl-Module-Build-Tiny perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-StrictConstructor perl-MooseX-Types-Stringlike perl-Pod-Coverage perl-Test-Fatal perl-Test-Moose-More

%description
Perl module Dist::Zilla::Plugin::MakeMaker::Awesome is a more
awesome MakeMaker plugin for Dist::Zilla.
It is limited, if you want to stray from the marked path and do
something that would normally be done in a package MY section or
otherwise run custom code in your Makefile.PL you're out of luck.

This plugin is 100%% compatible with Dist::Zilla::Plugin::MakeMaker -
we add additional customization hooks by subclassing it.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/MakeMaker/Awesome*

%changelog
* Sun Jan 28 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.40-alt1
- New version

* Sun Nov 12 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.39-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.38-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.36-alt1
- New version

* Sun Jan 10 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.35-alt2
- Bump release to override package from the autoimports/Sisyphus repository

* Sun Dec 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.35-alt1
- Initial build for ALT Linux Sisyphus
