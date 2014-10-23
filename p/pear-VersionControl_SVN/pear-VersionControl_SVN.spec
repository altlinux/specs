# spec file for PEAR PHP package VersionControl_SVN
#

%define pear_name VersionControl_SVN

Name: pear-%pear_name
Version: 0.5.2
Release: alt1

Summary: PHP/PEAR simple OO interface for the Subversion

License: %bsdstyle
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar

BuildArch: noarch

BuildRequires(pre): pear-core rpm-build-pear rpm-build-licenses
Requires: pear-core subversion pear-XML_Parser

%description
VersionControl_SVN PEAR class is a simple OO-style interface for
Subversion, the free/open-source version control system.

VersionControl_SVN can be used to manage trees of source code,
text files, image files -- just about any collection of files.


%prep
%setup -n %pear_name-%version

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
%pear_dir/VersionControl
%exclude %pear_dir/docs
%pear_xmldir/%pear_name.xml

%changelog
* Thu Oct 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.2-alt1
- New version 0.5.2

* Tue Jun 11 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.1-alt1
- New version 0.5.1

* Thu Apr 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.0-alt1
- New version 0.4.0

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.4-alt1
- New version 0.3.4

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.3-alt1
- New version 0.3.3

* Sun Jul 20 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus
