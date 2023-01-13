## SPEC file for Perl module Dist::Zilla::Plugin::CheckPrereqsIndexed

%define real_name Dist-Zilla-Plugin-CheckPrereqsIndexed

Name: perl-Dist-Zilla-Plugin-CheckPrereqsIndexed
Version: 0.022
Release: alt1

Summary: prevent a release if you have prereqs not found on CPAN

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-CheckPrereqsIndexed/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Sep 20 2021
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Cpanel-JSON-XS perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Which perl-File-pushd perl-IO-Socket-IP perl-IO-String perl-IPC-Run perl-JSON-MaybeXS perl-JSON-PP perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-Perl-PrereqScanner perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-experimental perl-namespace-autoclean perl-namespace-clean perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Dist-Zilla perl-HTTP-Tiny perl-PPI-XS perl-Ref-Util perl-Ref-Util-XS perl-Test-Fatal perl-Test-RequiresInternet

%description
Perl module Dist::Zilla::Plugin::CheckPrereqsIndexed is a
Dist::Zilla plugin to prevent a release if you have prereqs
not found on CPAN.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/CheckPrereqsIndexed*

%changelog
* Fri Jan 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.022-alt1
- New version

* Mon Sep 20 2021 Vitaly Lipatov <lav@altlinux.ru> 0.021-alt2
- update BuildRequires with buildreq

* Mon Jun 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.021-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.020-alt2
- Initial build for ALT Linux Sisyphus
