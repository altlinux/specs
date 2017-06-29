# spec file for PEAR PHP package OLE
#

%define pear_name OLE

Name: pear-%pear_name
Version: 1.0.0
Release: alt2.rc3

Summary: PHP/PEAR class for reading and writing OLE containers

License: PHP License 3.0.1
Group: Development/Other
Url: http://pear.php.net/package/OLE
#Url: https://github.com/pear/OLE

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %pear_name-%version.tar
Patch0:  %name-%version-%release.patch

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
%patch0 -p1

mkdir %pear_name-%version
mv -- OLE OLE.php %pear_name-%version/

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
* Thu Jun 29 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.0.0-alt2.rc3
- New version 1.0.0RC3

* Fri Jun 01 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
