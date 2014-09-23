## SPEC file for Perl module Test::Moose::More

%define real_name Test-Moose-More

Name: perl-Test-Moose-More
Version: 0.024
Release: alt1

Summary: more tools for testing Moose packages

License: %lgpl21only
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-Moose-More/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Check perl-CPAN-Meta-Requirements perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Encode perl-Eval-Closure perl-JSON-PP perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Scope-Guard perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Syntax-Keyword-Junction perl-Try-Tiny perl-autobox perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent
BuildRequires: perl-Moose-Autobox perl-Perl-Version perl-TAP-SimpleOutput perl-Test-CheckDeps perl-Variable-Magic perl-aliased

%description
Perl module Test::Moose::More contains a number of additional
tests that can be employed against Moose classes/roles. It is
intended to replace Test::Moose in your tests, and re-exports
any tests that it has and we do not, yet.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/Moose/More*

%changelog
* Tue Sep 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.024-alt1
- Initial build for ALT Linux Sisyphus
