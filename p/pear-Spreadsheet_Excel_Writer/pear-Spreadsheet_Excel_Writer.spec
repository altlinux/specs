# spec file for PEAR PHP package Spreadsheet_Excel_Writer
#

%define pear_name Spreadsheet_Excel_Writer

Name: pear-%pear_name
Version: 0.9.3
Release: alt1

Summary: PHP/PEAR class for generating Excel spreadsheets

License: %lgpl21plus
Group: Development/Other
Url: http://pear.php.net/package/Spreadsheet_Excel_Writer
#Url: https://github.com/pear/Spreadsheet_Excel_Writer

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %pear_name-%version.tar

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

mkdir %pear_name-%version
mv -- Spreadsheet %pear_name-%version/

# Fix md5 sums
sed -e 's/bb1da4cd0465c92dab8c49a79b86f896/83ba5964e40266ca8563617a9428fb73/' -i package.xml

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc README CHANGELOG
%pear_xmldir/%pear_name.xml
%pear_dir/Spreadsheet*

%changelog
* Fri Jun 01 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.3-alt1
- initial build for ALT Linux Sisyphus
