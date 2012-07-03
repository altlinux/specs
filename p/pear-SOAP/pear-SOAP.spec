%define pear_name SOAP
%add_findreq_skiplist %pear_docdir/%pear_name/example/*

Name: pear-SOAP
Version: 0.11.0
Release: alt1

Summary: SOAP Client/Server for PHP

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/SOAP/

Packager: Maxim Ivanov <redbaron at altlinux.ru>

Source: http://pear.php.net/get/SOAP-%version.tgz

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-HTTP_Request 
#Recommends: pear-Mail pear-Mail_Mime pear-Net_DIME

%description
Implementation of SOAP protocol and services

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%pear_dir/%pear_name
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sun Jun 08 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.11.0-alt1
- Initial build for Sisyphus
