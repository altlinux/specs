## SPEC file for Perl module Dist::Zilla::Plugin::CheckPrereqsIndexed

%define real_name Dist-Zilla-Plugin-CheckPrereqsIndexed

Name: perl-Dist-Zilla-Plugin-CheckPrereqsIndexed
Version: 0.020
Release: alt2

Summary: prevent a release if you have prereqs not found on CPAN

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Plugin-CheckPrereqsIndexed/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Data-OptList perl-Data-Section perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-File-Copy-Recursive perl-File-Find-Rule perl-File-Which perl-File-pushd perl-IO-Socket-IP perl-IPC-Run perl-JSON-MaybeXS perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-Log-Log4perl perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Path-Class perl-MooseX-Types-Perl perl-Number-Compare perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Path-Class perl-Path-Tiny perl-PerlIO-utf8_strict perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Test-Deep perl-Test-Fatal perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-common-sense perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: perl-Archive-Tar-Wrapper perl-Class-XSAccessor perl-Dist-Zilla perl-HTTP-Tiny perl-JSON-XS perl-Test-RequiresInternet

%description
Perl module Dist::Zilla::Plugin::CheckPrereqsIndexed is a
Dist::Zilla plugin to prevent a release if you have prereqs
not found on CPAN.

%prep
%setup -q -n %real_name-%version

rm -f -- t/basic.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Plugin/CheckPrereqsIndexed*

%changelog
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.020-alt2
- Initial build for ALT Linux Sisyphus
