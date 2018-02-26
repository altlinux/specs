## SPEC file for Perl module MooseX-OneArgNew

Name: perl-MooseX-OneArgNew
Version: 0.002
Release: alt1

Summary: Perl module that teach ->new to accept single, non-hashref arguments

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/MooseX-OneArgNew/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name MooseX-OneArgNew
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-Variable-Magic perl-namespace-clean perl-parent
BuildRequires: perl-MooseX-Role-Parameterized perl-devel perl-namespace-autoclean

%description
Perl module MooseX::OneArgNew lets your constructor take a single
argument, which will be translated into the value for a one-entry
hashref.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX/OneArgNew*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.002-alt1
- Initial build for ALT Linux Sisyphus

