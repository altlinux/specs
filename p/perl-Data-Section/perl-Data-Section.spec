## SPEC file for Perl module Data::Section

Name: perl-Data-Section
Version: 0.200008
Release: alt1

Summary: Perl module to read multiple hunks of data out of DATA section

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Data-Section/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Data-Section
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Mar 01 2014
# optimized out: perl-Data-OptList perl-Params-Util perl-Sub-Install perl-devel
BuildRequires: perl-Encode perl-MRO-Compat perl-Sub-Exporter perl-Test-FailWarnings

%description
Perl module Data::Section provides an easy way to access multiple
named chunks of line-oriented data in your module's DATA section.
It was written to allow modules to store their own templates, but
probably has other uses.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Data/Section*

%changelog
* Fri Jan 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.200008-alt1
- New version

* Sat Jul 15 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.200007-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.200006-alt1
- New version

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.101622-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.101621-alt1
- Initial build for ALT Linux Sisyphus

