## SPEC file for Perl module Moose::Autobox

%define real_name Moose-Autobox

Name: perl-Moose-Autobox
Version: 0.16
Release: alt2

Summary: Autoboxed wrappers for Native Perl datatypes

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Moose-Autobox/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Tue Jun 21 2016
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Carp-Clan perl-Class-Load perl-Data-OptList perl-Devel-Caller perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-CheckConflicts perl-Encode perl-Eval-Closure perl-Exporter-Tiny perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-JSON-PP perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Load perl-Module-Metadata perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-Role-Parameterized perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-PadWalker perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Role-Tiny perl-Scope-Guard perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Uplevel perl-Syntax-Keyword-Junction perl-Term-ANSIColor perl-Throwable perl-Try-Tiny perl-Variable-Magic perl-aliased perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent python-base python-modules python3
BuildRequires: perl-Class-XSAccessor perl-Config-MVP perl-Module-Build-Tiny perl-MooseX-LazyRequire perl-MooseX-Params-Validate perl-MooseX-SemiAffordanceAccessor perl-MooseX-SetOnce perl-MooseX-StrictConstructor perl-MooseX-Types perl-Pod-Coverage perl-Test-Exception perl-Test-Moose-More perl-autobox perl-List-MoreUtils

%description
Perl module Moose::Autobox provides an implementation of SCALAR,
ARRAY, HASH & CODE for use with autobox. It does this using a
hierarchy of roles in a manner similar to what Perl 6 might do.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Moose/Autobox*

%changelog
* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.16-alt2
- Fix build: BuildRequires updates

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.16-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.15-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.13-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt1
- Initial build for ALT Linux Sisyphus
