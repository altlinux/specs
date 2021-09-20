## SPEC file for Perl module MooX::Types::MooseLike

%define real_name MooX-Types-MooseLike

Name: perl-MooX-Types-MooseLike
Version: 0.29
Release: alt3

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

# Automatically added by buildreq on Fri Sep 17 2021
# optimized out: perl perl-CPAN-Meta-Requirements perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Encode perl-Eval-Closure perl-JSON-PP perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Parse-CPAN-Meta perl-Role-Tiny perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Try-Tiny perl-devel perl-parent python3 python3-base python3-module-paste python3-module-repoze sh4 sssd-client tzdata
BuildRequires: perl-CPAN-Meta perl-Class-XSAccessor perl-Moo perl-Moose perl-Test-Fatal

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
* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.29-alt3
- update BR

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.29-alt2
- Update BuildRequires

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.29-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.27-alt1
- New version

* Sat Aug 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.25-alt1
- Initial build for ALT Linux Sisyphus
