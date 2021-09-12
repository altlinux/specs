%define pear_name Mail_Mime

Name: pear-Mail_Mime
Version: 1.10.11
Release: alt1

Summary: Mail_Mime provides classes to create mime messages

License: BSD Style
Group: Development/Other
Url: http://pear.php.net/package/Mail_Mime

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://download.pear.php.net/package/Mail_Mime-%version.tgz
Source: %name-%version.tar

BuildArchitectures: noarch

BuildRequires(pre): rpm-build-pear
BuildRequires: pear-core
Requires: pear-core

%description
Mail_Mime provides classes to deal with the creation and manipulation of
mime messages.
It allows people to create Email messages consisting of:
* Text Parts
* HTML Parts
* Inline HTML Images
* Attachments
* Attached messages

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
%pear_testdir/Mail_Mime/
%pear_dir/Mail/
#pear_datadir/Mail_Mime/
#pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.11-alt1
- new version 1.10.11 (with rpmrb script)

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.10-alt1
- new version 1.10.10 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.10.2-alt1
- new version 1.10.2 (with rpmrb script)

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Fri Feb 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Mon Oct 04 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version (1.8.0) import in git (ALT bug #24046)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- initial build for ALT Linux Sisyphus

