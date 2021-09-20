## SPEC file for Perl module Dist::Zilla::Plugin::OSPrereqs

%define real_name Dist-Zilla-Plugin-OSPrereqs

Name: perl-Dist-Zilla-Plugin-OSPrereqs
Version: 0.011
Release: alt2

Summary: List prereqs conditional on operating system

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-OSPrereqs/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 21 2021
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-IO-String perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Escapes perl-Pod-Simple perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla perl-PPI-XS perl-Ref-Util perl-Ref-Util-XS perl-Test-Fatal

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
* Tue Sep 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.011-alt2
- update BuildRequires with buildreq

* Sat Jun 30 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.011-alt1
- New version

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
