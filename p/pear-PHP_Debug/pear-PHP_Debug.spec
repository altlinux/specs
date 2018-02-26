%define pear_name PHP_Debug

Name: pear-PHP_Debug
Version: 1.0.1
Release: alt1

Summary: PHP_Debug provides assistance in debugging PHP code

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/PHP_Debug

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/PHP_Debug-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The basic purpose of PHP_Debug is to provide assistance in debugging PHP
code, by "debug" i don't mean "step by step debug" but program trace,
variables display, process time, included files, queries executed, watch
variables... These informations are gathered through the script execution
and therefore are displayed at the end of the script (in a nice floating
div or a html table) so that it can be read and used at any moment.
(especially usefull during the development phase of a project or in
production with a secure key/ip)

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
%pear_dir/PHP
%pear_datadir/PHP_Debug/css
%pear_datadir/PHP_Debug/images
%pear_datadir/PHP_Debug/js
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

