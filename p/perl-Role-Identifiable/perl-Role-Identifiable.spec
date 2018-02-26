## SPEC file for Perl module Role-Identifiable

Name: perl-Role-Identifiable
Version: 0.005
Release: alt1

Summary: Perl module to provide a thing with an ident attribute

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Role-Identifiable/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Role-Identifiable
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-parent
BuildRequires: perl-Moose perl-devel

%description
Perl module Role-Identifiable provides a thing with an ident
attribute. This is an incredibly simple role. It adds a required
ident attribute that stores a simple string, meant to identify
exceptions.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Role/Identifiable*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.005-alt1
- Initial build for ALT Linux Sisyphus

