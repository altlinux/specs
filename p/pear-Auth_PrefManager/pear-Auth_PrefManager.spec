%define pear_name Auth_PrefManager

Name: pear-Auth_PrefManager
Version: 1.2.0
Release: alt3

Summary: Preferences management class

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Auth_PrefManager

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Auth_PrefManager-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-DB >= 1.7.0, pear-core >= 1.4.0

%description
Preference Manager is a class to handle user preferences in a web
application, looking them up in a table using a combination of their
userid, and the preference name to get a value, and (optionally) returning
a default value for the preference if no value could be found for that
user.

It is designed to be used alongside the PEAR Auth class, but can be used
with anything that allows you
to obtain the user's id - including your own code.

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
%pear_testdir/Auth_PrefManager/tests
%pear_dir/Auth
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

