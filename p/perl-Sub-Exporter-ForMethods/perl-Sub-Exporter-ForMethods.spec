## SPEC file for Perl module Sub-Exporter-ForMethods

Name: perl-Sub-Exporter-ForMethods
Version: 0.100055
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


# Automatically added by buildreq on Sun Aug 31 2014
# optimized out: perl-B-Hooks-EndOfScope perl-Data-OptList perl-Module-Implementation perl-Module-Runtime perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Try-Tiny perl-namespace-clean
BuildRequires: perl-Sub-Exporter perl-Sub-Name perl-Variable-Magic perl-devel perl-namespace-autoclean

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
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.100055-alt1
- New version

* Sat May 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.100054-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.100052-alt1
- New version

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.100051-alt2
- Updating BuildRequires

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.100051-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.100050-alt1
- Initial build for ALT Linux Sisyphus

