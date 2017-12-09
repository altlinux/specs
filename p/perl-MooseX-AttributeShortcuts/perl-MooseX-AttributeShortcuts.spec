## SPEC file for Perl module  MooseX::AttributeShortcuts

Name: perl-MooseX-AttributeShortcuts
Version: 0.037
Release: alt1

Summary: Perl module to shorthand for common attribute options

License: %lgpl21only
Group: Development/Perl
URL: http://search.cpan.org/dist/MooseX-AttributeShortcuts/

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

%define real_name MooseX-AttributeShortcuts
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Sep 26 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Class-Tiny perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-JSON-PP perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Moose perl-MooseX-TraitFor-Meta-Class-BetterAnonClassNames perl-MooseX-Types perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Path-Class perl-Scope-Guard perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Test-Fatal perl-Try-Tiny perl-Variable-Magic perl-Want perl-autobox perl-autobox-Core perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3 python3-base
BuildRequires: perl-Devel-PartialDump perl-MooseX-Meta-TypeConstraint-Mooish perl-MooseX-Role-Parameterized perl-MooseX-SemiAffordanceAccessor perl-MooseX-Types-Common perl-MooseX-Types-Path-Class perl-MooseX-Util perl-Test-CheckDeps perl-Test-Moose-More perl-Test-Requires perl-aliased

%description
Perl module MooseX::AttributeShortcuts causes an attribute trait
to be applied to all attributes defined to the using class.
This trait extends the attribute option processing to handle
the above variations.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX*

%changelog
* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.037-alt1
- New version

* Sun Nov 12 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.036-alt1
- New version

* Tue Sep 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.035-alt1
- New version

* Sun Jul 30 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.034-alt1
- New version

* Sun Jun 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.032-alt1
- New version

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.031-alt1
- New version

* Sun May 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.029-alt1
- New version

* Sat Jun 13 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.028-alt1
- New version

* Fri Sep 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.024-alt2
- Rising release to override package from Autoimports/Sisyphus repository

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.024-alt1
- Initial build for ALT Linux Sisyphus
