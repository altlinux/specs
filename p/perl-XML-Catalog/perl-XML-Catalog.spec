%define dist XML-Catalog
Name: perl-%dist
Version: 0.02
Release: alt1.1

Summary: Resolve public identifiers and remap system identifiers
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/E/EB/EBOHLMAN/XML-Catalog-0.02.tar.gz
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jan 19 2010
BuildRequires: perl-XML-Parser perl-devel

%description
This module implements draft 0.4 of John Cowan's XML Catalog (formerly
known as XCatalog) proposal
(<http://www.ccil.org/~cowan/XML/XCatalog.html>).  Catalogs may be written
in either SOCAT or XML syntax (see the proposal for syntax details);
XML::Catalog will assume SOCAT syntax if the catalog is not in well-formed
XML syntax.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/XML/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.02-alt1
- initial build for Sisyphus

