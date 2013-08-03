## SPEC file for Perl module MooX::Types::MooseLike

%define real_name MooX-Types-MooseLike

Name: perl-MooX-Types-MooseLike
Version: 0.25
Release: alt1

Summary: Perl module with some Moosish types and a type builder

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/MooX-Types-MooseLike/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
Source1: Distar.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sat Aug 03 2013
# optimized out: perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Role-Tiny perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Tie-RefHash perl-Try-Tiny perl-devel perl-strictures
BuildRequires: git-core perl-Moo perl-Test-Fatal perl-autodie

%description
Perl module MooX::Types::MooseLike provides a list of some Moosish types
and a type builder.

%prep
%setup -q -n %real_name-%version
tar xvf %SOURCE1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/MooX*

%changelog
* Sat Aug 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.25-alt1
- Initial build for ALT Linux Sisyphus
