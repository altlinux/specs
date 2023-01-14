## SPEC file for Perl module Pod::Weaver

%define real_name Pod-Weaver

Name: perl-Pod-Weaver
Version: 4.019
Release: alt1

Summary: Perl module to weave together a Pod document from an outline

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Pod-Weaver/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat May 15 2021
# optimized out: perl perl-Algorithm-Diff perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Inspector perl-Class-Load perl-Class-Singleton perl-Clone perl-Config-INI perl-Config-MVP perl-Data-OptList perl-Data-Section perl-DateTime perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-ShareDir perl-IO-String perl-JSON-PP perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatch perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-Types perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-PerlIO-utf8_strict perl-Pod-Elemental perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Specio perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Text-Diff perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Class-XSAccessor perl-Config-MVP-Reader-INI perl-PPI-XS perl-Ref-Util perl-Ref-Util-XS perl-Software-License perl-Test-Differences perl-experimental

BuildRequires: perl-List-MoreUtils perl-List-MoreUtils-XS perl-Log-Dispatchouli perl-Pod-Elemental perl-DateTime perl-String-Flogger perl-String-RewritePrefix

%description
Perl module Pod::Weaver is a system for building Pod documents
from templates. It doesn't perform simple text substitution,
but instead builds a Pod::Elemental::Document. Its plugins
sketch out a series of sections that will be produced based
on an existing Pod document or other provided information.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Pod/Weaver*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 4.019-alt1
- New version

* Mon Jun 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.018-alt1
- New version

* Sat May 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.017-alt1
- New version

* Thu May 09 2019 Nikolay A. Fetisov <naf@altlinux.org> 4.015-alt2
- Fix BuildRequires

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 4.015-alt1
- Initial build for ALT Linux Sisyphus
