%define dist XML-Catalog
Name: perl-%dist
Version: 1.03
Release: alt1.1

Summary: Resolve public identifiers and remap system identifiers
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: https://metacpan.org/release/XML-Catalog
# http://search.cpan.org/CPAN/authors/id/E/EB/EBOHLMAN/XML-Catalog-0.02.tar.gz
Source: %dist-%version.tar
# Fedora: CPAN RT#176391, fix with XML-Parser >= 2.48
Patch: XML-Catalog-1.03-Adapt-to-changes-in-XML-Parser-2.48.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jan 19 2010
BuildRequires: perl-XML-Parser perl-devel perl(Module/Build.pm)

%description
This module implements draft 0.4 of John Cowan's XML Catalog (formerly
known as XCatalog) proposal
(<http://www.ccil.org/~cowan/XML/XCatalog.html>).  Catalogs may be written
in either SOCAT or XML syntax (see the proposal for syntax details);
XML::Catalog will assume SOCAT syntax if the catalog is not in well-formed
XML syntax.

%prep
%setup -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/XML/

%changelog
* Sun Oct 18 2026 Vitaly Lipatov <lav@altlinux.ru> 1.03-alt1.1
- NMU: fix build with XML-Parser >= 2.48 (patch from Fedora, CPAN RT#176391)
- update URL

* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update (closes: #31781)

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.02-alt1
- initial build for Sisyphus

