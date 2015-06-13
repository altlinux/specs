## SPEC file for Perl module MooseX::Meta::TypeConstraint::Mooish

%define real_name MooseX-Meta-TypeConstraint-Mooish

Name: perl-MooseX-Meta-TypeConstraint-Mooish
Version: 0.001
Release: alt1

Summary: Perl module for translating Moo-style constraints to Moose-style

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/MooseX-Meta-TypeConstraint-Mooish/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Jun 13 2015
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-JSON-PP perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-clean perl-parent
BuildRequires: perl-Test-CheckDeps perl-Test-Fatal perl-Test-Moose-More perl-aliased perl-namespace-autoclean

%description
Perl module MooseX::Meta::TypeConstraint::Mooish translates 
Moo-style constraints to Moose-style.

Moose type constraints are expected to return true if the value
passes the constraint, and false otherwise; Moo "constraints",
on the other hand, die if validation fails.

This metaclass allows for Moo-style constraints; it will wrap 
them and translate their Moo into a dialect Moose understands.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX/Meta/TypeConstraint/Mooish*
%perl_vendor_privlib/MooseX/TraitFor/Meta/TypeConstraint/Mooish*

%changelog
* Sat Jun 13 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.001-alt1
- Initial build for ALT Linux Sisyphus
