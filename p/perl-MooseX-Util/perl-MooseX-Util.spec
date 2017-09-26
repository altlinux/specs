## SPEC file for Perl module MooseX::Util

%define real_name MooseX-Util

Name: perl-MooseX-Util
Version: 0.06
Release: alt2

Summary: Perl module with Moose::Util extensions

License: %lgpl21only
Group: Development/Perl

URL: http://search.cpan.org/dist/MooseX-Util/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 26 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-JSON-PP perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Scope-Guard perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Try-Tiny perl-Variable-Magic perl-Want perl-autobox perl-autobox-Core perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3 python3-base
BuildRequires: perl-MooseX-TraitFor-Meta-Class-BetterAnonClassNames perl-Test-CheckDeps perl-Test-Moose-More perl-Test-Requires perl-aliased

%description
Perl module MooseX::Util  is a utility module that handles all of the same
functions that Moose::Util handles. Most of the functions exported by this
package are simply re-exports from Moose::Util, but some of them is
re-implemented for a variety of reasons.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX/Util*

%changelog
* Tue Sep 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.06-alt2
- Initial build for ALT Linux Sisyphus
