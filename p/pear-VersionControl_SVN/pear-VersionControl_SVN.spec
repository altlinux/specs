# spec file for PEAR PHP package VersionControl_SVN
#

%define pear_name VersionControl_SVN

Name: pear-%pear_name
Version: 0.4.0
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
sed -e 's#301b086ce94948ee606d94988fb7ab06#55648853e4e9cc47963e1990071d433c#' -i package.xml
sed -e 's#87ce30d8ad06776ed369e73f1c5da6d1#1f2088d8f710eaa62f5c43d8748c2ba1#' -i package.xml
sed -e 's#aef69a3fdd6257817f16b4ce61aa1cca#d9667d9d5ec09c04f534cbe09382a8e5#' -i package.xml
sed -e 's#3223949fe055a120be54a7032dd29e95#3966b40803b8bd5e5d4f967ed2524b09#' -i package.xml
sed -e 's#895ddc851d7c8d3eea7d6b3751fa3307#590d1050644c336f1d154ce1fbcbe004#' -i package.xml
sed -e 's#5bef13388c02b3ae6250fe73edb6bcfa#bf78a1b691b2fd0e1486ba11744ae30c#' -i package.xml
sed -e 's#6ce16a38b5e8336d6118584f592cf398#57e0df85e7f6eb93a75f0ad425d6a7c7#' -i package.xml
sed -e 's#c9c6b2f1fcb0587694949d704753ee9d#497ce523ce745298d15d2b9c32ec7f72#' -i package.xml

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
* Thu Apr 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.0-alt1
- New version 0.4.0

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.4-alt1
- New version 0.3.4

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.3-alt1
- New version 0.3.3

* Sun Jul 20 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus
