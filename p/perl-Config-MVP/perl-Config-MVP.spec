## SPEC file for Perl module Config::MVP

Name: perl-Config-MVP
Version: 2.200001
Release: alt1

Summary: Perl module to work with multivalue-property INI files

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Config-MVP/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Config-MVP
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Runtime perl-Moose perl-MooseX-Role-Parameterized perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-Variable-Magic perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent
BuildRequires: perl-Devel-StackTrace perl-Module-Pluggable perl-MooseX-OneArgNew perl-Role-HasMessage perl-Role-Identifiable perl-Test-Fatal perl-Throwable perl-Tie-IxHash

%description
Perl module Config::MVP provides read and write access to the
multivalue-property .ini-file format. MVP is a mechanism for
loading configuration (or other information) for libraries.
It doesn't read a file or a database. It's a helper for
things that do.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Config/MVP*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.200001-alt1
- Initial build for ALT Linux Sisyphus

