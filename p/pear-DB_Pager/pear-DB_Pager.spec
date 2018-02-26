%define pear_name DB_Pager

Name: pear-DB_Pager
Version: 0.7
Release: alt3

Summary: Retrieve and return information of database result sets

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/DB_Pager

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/DB_Pager-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
This class handles all the stuff needed for displaying
paginated results from a database query of Pear DB.
including fetching only the needed rows and giving extensive information
for helping build an HTML or GTK query result display.

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
%pear_dir/DB
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- initial build for ALT Linux Sisyphus

