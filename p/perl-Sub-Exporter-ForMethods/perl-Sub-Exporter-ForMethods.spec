## SPEC file for Perl module Sub-Exporter-ForMethods

Name: perl-Sub-Exporter-ForMethods
Version: 0.100050
Release: alt1

Summary: Perl module with helper routines for using Sub::Exporter

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Sub-Exporter-ForMethods/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Sub-Exporter-ForMethods
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-Variable-Magic perl-namespace-clean perl-parent
BuildRequires: perl-devel perl-namespace-autoclean

%description
Perl module Sub::Exporter::ForMethods provides a helper routines
for using Sub::Exporter to build methods.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Sub/Exporter/ForMethods*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.100050-alt1
- Initial build for ALT Linux Sisyphus

