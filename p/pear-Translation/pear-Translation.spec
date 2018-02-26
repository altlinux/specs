%define pear_name Translation

Name: pear-Translation
Version: 1.2.6pl1
Release: alt3

Summary: Class for creating multilingual websites

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Translation

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Translation-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-DB

%description
Class allows storing and retrieving all the strings on multilingual site in
a database. The class connects to any database using PEAR::DB extension.
The object should be created for every page. While creation all the strings
connected with specific page and the strings connected with all the pages
on the site are loaded into variable, so access to them is quite fast and
does not overload database server connection.

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
%pear_dir/Translation
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.6pl1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.6pl1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.6pl1-alt1
- initial build for ALT Linux Sisyphus

