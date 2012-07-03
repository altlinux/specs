%define module PDF-Reuse-Barcode

Name: perl-%module
Version: 0.06
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Create barcodes for PDF documents with PDF::Reuse
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/L/LA/LARSLUND/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Jan 15 2010
BuildRequires: perl-Barcode-Code128 perl-GD-Barcode perl-PDF-Reuse perl-devel

%description
This is a sub-module to PDF::Reuse. It creates barcode "images" to be used in
PDF documents. It uses GD::Barcode and its sub-modules: GD::Barcode::Code39,
COOP2of5, EAN13 and so on, to calculate the barcode pattern. For Code128 it uses
Barcode::Code128.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/PDF/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 15 2010 Victor Forsyuk <force@altlinux.org> 0.06-alt1
- 0.06

* Sun Oct 26 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.05-alt2.1
- rebuild

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.05-alt2
- fixed build

* Fri Jul 04 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus

