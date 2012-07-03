%define module Spreadsheet-WriteExcel

Name: perl-%module
Version: 2.37
Release: alt1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Perl module for generating Excel97+ compatible Spreadsheets
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMCNAMARA/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 30 2009
BuildRequires: perl-Digest-MD4 perl-Encode perl-OLE-Storage_Lite perl-Parse-RecDescent perl-devel

# About perl-Digest-MD4 run-time dependancy:
# The Spreadsheet::WriteExcel module checks in run-time for modules available
# to calculate image checksum. Excel uses MD4 but MD5 will also work.
# In the event of no checksum module being available checksum is simulated
# using the image index. perl-Digest-MD4 selected as best choice:
# real checksum, fast implementation, Excel compatibility.

Requires: perl-Digest-MD4

Obsoletes: perl-%{module}2
Provides: perl-%{module}2

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
The Spreadsheet::WriteExcel module can be used to create a cross-platform
Excel binary file. Multiple worksheets can be added to a workbook and
formatting can be applied to cells. Text, numbers, formulas, hyperlinks and
images can be written to the cells.

The Excel file produced by this module is compatible with Excel 97, 2000, 2002
and 2003. Unicode data is fully supported so generated files can be used in
OpenOffice.org Calc and Gnumeric w/o any additional converters even if
non-Latin1 strings are in use. The generated files are compatible with MS
Access as well.

%prep
%setup -n %module-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%perl_vendor_privlib/Spreadsheet
%_man1dir/*
%doc README Changes examples docs/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.37-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 2.37-alt1
- 2.37

* Mon Jan 25 2010 Victor Forsyuk <force@altlinux.org> 2.36-alt1
- 2.36

* Fri Dec 25 2009 Victor Forsyuk <force@altlinux.org> 2.31-alt1
- 2.31

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 2.30-alt1
- 2.30

* Wed Nov 18 2009 Victor Forsyuk <force@altlinux.org> 2.26-alt1
- 2.26

* Thu Sep 11 2008 Victor Forsyuk <force@altlinux.org> 2.25-alt1
- 2.25

* Wed Aug 13 2008 Victor Forsyuk <force@altlinux.org> 2.23-alt1
- 2.23

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 2.22-alt1
- 2.22

* Thu Mar 27 2008 Victor Forsyuk <force@altlinux.org> 2.21-alt1
- 2.21

* Fri Oct 26 2007 Victor Forsyuk <force@altlinux.org> 2.20-alt1
- 2.20

* Tue Jul 17 2007 Victor Forsyuk <force@altlinux.org> 2.18-alt1
- 2.18

* Thu May 19 2005 Alexey Morozov <morozov@altlinux.org> 2.14-alt1
- New version (2.14). Upstream changes:
  + This release fixes a bug that caused file corruption when using
    Unicode font names.

* Thu May 05 2005 Alexey Morozov <morozov@altlinux.org> 2.13-alt1
- New version (2.13, by the will of Andrey Orlov)

* Sun Feb 13 2005 Alexey Morozov <morozov@altlinux.org> 2.11-alt1
- New version (2.11)

* Mon Aug 30 2004 Alexey Morozov <morozov@altlinux.org> 2.04-alt2
- summary strings changed
- docs and examples added

* Thu Aug 26 2004 Alexey Morozov <morozov@altlinux.org> 2.04-alt1
- Initial build for ALT Linux
