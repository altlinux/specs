%define pear_name XML_Beautifier

Name: pear-XML_Beautifier
Version: 1.2.2
Release: alt1

Summary: Class to format XML documents

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_Beautifier

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_Beautifier-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-XML_Util >= 0.5, pear-XML_Parser

%description
XML_Beautifier will add indentation and linebreaks to you XML files,
replace all entities, format your comments and makes your document easier
to read. You can influence the way your document is beautified with several
options.

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
%pear_docdir/%pear_name/
%pear_testdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt4
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus

