## SPEC file for Perl module Role-Identifiable

Name: perl-Role-Identifiable
Version: 0.009
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

# Automatically added by buildreq on Sun Oct 06 2013
# optimized out: perl-B-Hooks-EndOfScope perl-Class-Load perl-Data-OptList perl-Devel-GlobalDestruction perl-Eval-Closure perl-List-MoreUtils perl-MRO-Compat perl-Module-Implementation perl-Module-Runtime perl-Moose perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Pod-Escapes perl-Pod-Simple perl-Sub-Exporter perl-Sub-Exporter-Progressive perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-devel perl-namespace-clean
BuildRequires: perl-Capture-Tiny perl-Devel-PartialDump perl-Test-Pod perl-Variable-Magic perl-Moose

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
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.009-alt1
- New version

* Mon Dec 05 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.008-alt1
- New version

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.007-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.006-alt1
- New version (ATTENTION: not quite backward compatible)

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.005-alt1
- Initial build for ALT Linux Sisyphus

