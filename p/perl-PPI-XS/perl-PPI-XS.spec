## SPEC file for Perl module PPI:XS
## Used in Dist::Zilla

Name: perl-PPI-XS
Version: 0.904
Release: alt1.1

Summary: Perl module with XS acceleration for PPI

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/PPI-XS/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

%define real_name PPI-XS
Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Oct 25 2015
# optimized out: perl-Clone perl-Exporter-Tiny perl-IO-String perl-List-MoreUtils perl-Params-Util
BuildRequires: perl-PPI perl-Pod-Escapes perl-devel

%description
This module  provides a (minor) XS acceleration of the core
PPI packages. It selectively replaces a (small but growing)
number of methods throughout PPI with identical but much
faster C versions.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/PPI/XS*
%perl_vendor_autolib/PPI/XS*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.904-alt1.1
- rebuild with new perl 5.26.1

* Tue Apr 25 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.904-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.902-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.902-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.902-alt1
- Initial build for ALT Linux Sisyphus
