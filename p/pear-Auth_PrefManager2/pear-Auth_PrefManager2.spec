%define pear_name Auth_PrefManager2

Name: pear-Auth_PrefManager2
Version: 2.0.0dev1
Release: alt3

Summary: Preferences management class

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Auth_PrefManager2

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Auth_PrefManager2-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Preference Manager is a class to handle user preferences in a web
application, looking them up in a table
using a combination of their userid, and the preference name to get a
value, and (optionally) returning
a default value for the preference if no value could be found for that
user.

Auth_PrefManager2 supports data containers to allow reading/writing with
different sources, currently PEAR DB and a simple array based container are
supported, although support is planned for an LDAP container as well. If
you don't need support for different sources, or setting preferences for
multiple applications you should probably use Auth_PrefManager instead.

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
%pear_dir/Auth
%pear_testdir/Auth_PrefManager2/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0dev1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0dev1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0dev1-alt1
- initial build for ALT Linux Sisyphus

