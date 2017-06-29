# spec file for PEAR PHP package Spreadsheet_Excel_Writer
#

%define pear_name Spreadsheet_Excel_Writer

Name: pear-%pear_name
Version: 0.9.4
Release: alt1

Summary: PHP/PEAR class for generating Excel spreadsheets

License: %lgpl21plus
Group: Development/Other
Url: http://pear.php.net/package/Spreadsheet_Excel_Writer
#Url: https://github.com/pear/Spreadsheet_Excel_Writer

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %pear_name-%version.tar
Patch0: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): pear-core rpm-build-pear rpm-build-licenses
Requires: pear-core pear-OLE

%description
Spreadsheet_Excel_Writer PEAR class allows writing of Excel spreadsheets
without the need for COM objects. It supports formulas, images (BMP) and
all kinds of formatting for text and cells. It currently supports the
BIFF5 format (Excel 5.0), so functionality appeared in the latest Excel
versions is not yet available.

%prep
%setup -n %pear_name-%version
%patch0 -p1

mkdir %pear_name-%version
mv -- Spreadsheet %pear_name-%version/

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc README.md CHANGELOG
%pear_xmldir/%pear_name.xml
%pear_dir/Spreadsheet*

%changelog
* Thu Jun 29 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.9.4-alt1
- New version

* Fri Jun 01 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3-alt1
- initial build for ALT Linux Sisyphus
