%define pear_name Mail_Queue

Name: pear-Mail_Queue
Version: 1.2.2
Release: alt2

Summary: Class for put mails in queue and send them later in background

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/Mail_Queue

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Mail_Queue-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Mail, pear-Mail_Mime, pear-core >= 1.4.0b1

%description
Class to handle mail queue managment.
Wrapper for PEAR::Mail and PEAR::DB (or PEAR::MDB/MDB2).
It can load, save and send saved mails in background and also backup some
mails.

The Mail_Queue class puts mails in a temporary container, waiting to be
fed to
the MTA (Mail Transport Agent), and sends them later (e.g. a certain
amount of
mails every few minutes) by crontab or in other way.

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
%pear_dir/Mail
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt2
- autorebuild for correct requires(pre) (see bug #16086)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus

