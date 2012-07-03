%define pear_name XML_RPC

Name: pear-XML_RPC
Version: 1.5.1
Release: alt3

Summary: PHP implementation of the XML-RPC protocol

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_RPC

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_RPC-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
A PEAR-ified version of Useful Inc's XML-RPC for PHP.

It has support for HTTP/HTTPS transport, proxies and authentication.

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
%doc LICENSE CHANGELOG
%pear_testdir/XML_RPC/tests
%pear_dir/XML
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- initial build for ALT Linux Sisyphus

