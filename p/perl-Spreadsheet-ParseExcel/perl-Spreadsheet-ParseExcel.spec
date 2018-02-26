Name: perl-Spreadsheet-ParseExcel
Version: 0.59
Release: alt1
Epoch: 1

Summary: Extract information from Excel file
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/Spreadsheet-ParseExcel/
Source: Spreadsheet-ParseExcel-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Crypt-RC4 perl-Digest-Perl-MD5 perl-Encode-JP perl-Spreadsheet-WriteExcel perl-Unicode-Map perl-devel

%description
The Spreadsheet::ParseExcel module can be used to read information from Excel
95-2003 binary files.  The module cannot read files in the Excel 2007 Open XML
XLSX format.  See the Spreadsheet::XLSX module instead.

%prep
%setup -q -n Spreadsheet-ParseExcel-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# requires Jcode
%add_findreq_skiplist */Spreadsheet/ParseExcel/FmtJapan*
# requires Spreadsheet::WriteExcel, optional
%add_findreq_skiplist */Spreadsheet/ParseExcel/SaveParser.pm

%files
%doc Changes README* examples sample
%perl_vendor_privlib/Spreadsheet

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 1:0.59-alt1
- 0.2603 -> 0.59

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.2603-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2603-alt1
- fix directory ownership violation

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2603-alt0.1
- new version (0.2603)
- fix Url, Source, update buildreq
- change packager

* Thu Feb 26 2004 Alexey Morozov <morozov@altlinux.org> 0.2602-alt1
- Initial real ALTLinux build
- freshen the spec
- exclude Spreadsheet::ParseExcel::FmtJapan* to avoid Jcode dependancy

* Fri Oct 5 2001 Alexey Morozov <morozov@novosoft.ru> 0.2403-local2
- Re-built with perl-5.6.1

* Thu Aug  16 2001 Alexey Morozov <morozov@novosoft.ru> 0.2403-local1
- Initial build. Spec is based on modern ALTLinux perl modules specs
  and almost compatible w/ their new police. Some backward compability
  things (particularly w/ Mandrake8 RPM) remains in place however
