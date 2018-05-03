## SPEC file for Perl module Dist::Zilla::Plugin::OSPrereqs

%define real_name Dist-Zilla-Plugin-OSPrereqs

Name: perl-Dist-Zilla-Plugin-OSPrereqs
Version: 0.010
Release: alt1

Summary: List prereqs conditional on operating system

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-OSPrereqs/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu May 03 2018
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Lite perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-IO-String perl-JSON perl-JSON-MaybeXS perl-JSON-PP perl-JSON-XS perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Test-Fatal perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3 python3-base python3-module-mpl_toolkits python3-module-zope ruby
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-PPI-XS perl-Ref-Util perl-Ref-Util-XS perl-Test-Deep-JSON

%description
Perl module Dist::Zilla::Plugin::OSPrereqs provides a Dist::Zilla
plugin that allows you to specify OS-specific prerequisites.
You must give the plugin a name corresponding to an operating
system that would appear in $^O. Any prerequisites listed will
be conditionally added to "PREREQ_PM" in the Makefile.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/OSPrereqs*

%changelog
* Thu May 03 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.010-alt1
- New version

* Sat Sep 17 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.008-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.007-alt1
- New version

* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.006-alt1
- New version

* Sun Jan 10 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.005-alt3
- Bump release to override package from autoimports/Sisyphus repository

* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.005-alt1
- Initial build for ALT Linux Sisyphus
