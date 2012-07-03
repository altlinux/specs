## SPEC file for Perl module MooseX-SetOnce

Name: perl-MooseX-SetOnce
Version: 0.200001
Release: alt1

Summary: Perl module to write-once, read-many attributes for Moose

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/MooseX-SetOnce/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name MooseX-SetOnce
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Classify perl-Params-Util perl-Sub-Exporter perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-devel perl-parent
BuildRequires: perl-Moose perl-Test-Fatal

%description
Perl module MooseX::SetOnce provides lets a class to  have attributes
that are not lazy and not set, but that cannot be altered once set.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MooseX/SetOnce*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.200001-alt1
- Initial build for ALT Linux Sisyphus

