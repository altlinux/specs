%define module PDF-ReportWriter

Name: perl-PDF-ReportWriter
Version: 1.5
Release: alt2

Summary: quality business reports, for archiving or printing

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %module-%version.tar.gz

BuildRequires: perl-Image-Size perl-PDF-API2 perl-XML-Simple perl-devel perl-DBI
BuildRequires: perl-Compress-Raw-Zlib perl-Compress-Zlib perl-Encode perl-IO-Compress-Base
BuildRequires: perl-IO-Compress-Zlib perl-Storable perl-XML-LibXML perl-XML-LibXML-Common
BuildRequires: perl-XML-SAX perl-unicore

%description
PDF::ReportWriter is designed to create high-quality business reports, for archiving or printing.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/PDF/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt2
- drop %%perl_vendor_man3dir

* Fri Dec 12 2008 Alexey Shabalin <shaba@altlinux.ru> 1.5-alt1
- initial build for ALT Linux Sisyphus

