## SPEC file for Perl module  MooseX::AttributeShortcuts

Name: perl-MooseX-AttributeShortcuts
Version: 0.024
Release: alt2

Summary: Perl module to shorthand for common attribute options

License: %lgpl21only
Group: Development/Perl
URL: http://search.cpan.org/dist/MooseX-AttributeShortcuts/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name MooseX-AttributeShortcuts
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Load perl-Class-Tiny perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-PartialDump perl-Devel-StackTrace perl-Encode perl-Eval-Closure perl-JSON-PP perl-List-AllUtils perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Moose perl-Moose-Autobox perl-MooseX-Types perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Path-Class perl-Perl-OSType perl-Scope-Guard perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Uplevel perl-Syntax-Keyword-Junction perl-Try-Tiny perl-autobox perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent
BuildRequires: perl-MooseX-Role-Parameterized perl-MooseX-Types-Common perl-MooseX-Types-Path-Class perl-Test-CheckDeps perl-Test-Fatal perl-Test-Moose-More perl-Test-Warn perl-Variable-Magic perl-autobox-Core perl-autobox-Junctions

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
* Fri Sep 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.024-alt2
- Rising release to override package from Autoimports/Sisyphus repository

* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.024-alt1
- Initial build for ALT Linux Sisyphus
