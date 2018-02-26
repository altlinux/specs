%define pear_name XML_fo2pdf

Name: pear-XML_fo2pdf
Version: 0.98
Release: alt3

Summary: Converts a xsl-fo file to pdf/ps/pcl/text/etc with the help of apache-fop

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_fo2pdf

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_fo2pdf-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Converts a xsl-fo file to pdf/ps/pcl/text/etc with the help of apache-fop

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
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.98-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.98-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.98-alt1
- initial build for ALT Linux Sisyphus

