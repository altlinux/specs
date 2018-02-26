%define pear_name XML_NITF

Name: pear-XML_NITF
Version: 1.1.0
Release: alt4

Summary: Parse NITF documents

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_NITF

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_NITF-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-XML_Parser

%description
This package provides a NITF XML parser. The parser was designed with NITF
version 3.1, but should be forward-compatible when new versions of the NITF
DTD are produced. Various methods for accessing the major elements of the
document, such as the hedline(s), byline, and lede are provided. This class
was originally tested against the Associated Press's (AP) XML data feed.

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
%pear_dir/XML
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt4
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

