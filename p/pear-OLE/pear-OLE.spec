# spec file for PEAR PHP package OLE
#

%define pear_name OLE

Name: pear-%pear_name
Version: 1.0.0
Release: alt1

Summary: PHP/PEAR class for reading and writing OLE containers

License: PHP License 3.0.1
Group: Development/Other
Url: http://pear.php.net/package/OLE
#Url: https://github.com/pear/OLE

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %pear_name-%version.tar

BuildArch: noarch

BuildRequires(pre): pear-core rpm-build-pear
Requires: pear-core

%description
OLE PEAR class allows reading and writing of OLE (Object Linking
and Embedding) compound documents. This format is used as
container for Excel (.xls), Word (.doc) and other Microsoft file
formats.

%prep
%setup -n %pear_name-%version

mkdir %pear_name-%version
mv -- OLE OLE.php %pear_name-%version/

# Fix md5 sums:
sed -e 's/154749b82508fa8e7ce2cae12e4d6236/fd704b3fd4d112d221a67bf9c0d2639f/' -i package.xml
sed -e 's/fcf77f4d5390a523ed9a3664af1def7b/4877aa5c756e3907d003f506904c2b26/' -i package.xml
sed -e 's/8917d559c1aa3a75bd0cc6017ddd0f0f/2eaf841e28a64396fd8cc0319d726529/' -i package.xml
sed -e 's/8f6b586027b09539174828b6e9330c59/d999f73959df63a032e225bc6502ad5e/' -i package.xml
sed -e 's/b22a2aaa8186adc723e09b26e96d7dd8/2ce59e7f46eab76e1603b2a8263acbd4/' -i package.xml

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc README CHANGELOG LICENSE
%pear_xmldir/%pear_name.xml
%pear_dir/OLE*

%changelog
* Fri Jun 01 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
