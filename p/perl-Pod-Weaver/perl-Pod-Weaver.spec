## SPEC file for Perl module Pod::Weaver

%define real_name Pod-Weaver

Name: perl-Pod-Weaver
Version: 4.015
Release: alt1

Summary: Perl module to weave together a Pod document from an outline

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Pod-Weaver/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-Algorithm-Diff perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Singleton perl-Clone perl-Config-INI perl-Config-MVP perl-Data-OptList perl-Data-Section perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-IO-String perl-List-MoreUtils perl-Log-Dispatch perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-Types perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-PerlIO-utf8_strict perl-Pod-Eventual perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Specio perl-String-Flogger perl-String-Formatter perl-String-RewritePrefix perl-String-Truncate perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Text-Diff perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: perl-CPAN-Meta perl-Class-XSAccessor perl-Config-MVP-Reader-INI perl-DateTime perl-Log-Dispatchouli perl-PPI-XS perl-Pod-Elemental perl-Software-License perl-Test-Differences

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
* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 4.015-alt1
- Initial build for ALT Linux Sisyphus
