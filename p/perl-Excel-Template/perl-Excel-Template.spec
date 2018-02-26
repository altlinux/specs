## SPEC file for Perl module Excel::Template

%define real_name Excel-Template

Name: perl-Excel-Template
Version: 0.33
Release: alt1

Summary: creating MS Excel file from HTML::Template data structure

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Excel-Template/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: perl-devel rpm-build-licenses

# Automatically added by buildreq on Tue Jun 21 2011
# optimized out: perl-Devel-Symdump perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Sub-Uplevel perl-devel
BuildRequires: perl-IO-stringy perl-Spreadsheet-WriteExcel perl-Test-Deep perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage perl-XML-Parser

%description
Perl module  Excel::Template  is a layout system to use the data
structure from HTML::Template and create a Microsoft Excel file.

CAVEAT:  All limitations stated in  Spreadsheet::WriteExcel  are
in force, as that is  the module used for rendering.  If the XLS
file is corrupted, first make sure You aren't doing anything 
that it says is bad.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%exclude /.perl.req
%perl_vendor_privlib/Excel/Template*

%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.33-alt1
- New version

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.32-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 29 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.31-alt1
- Initial build for ALT Linux Sisyphus
