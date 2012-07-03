%define pear_name Text_TeXHyphen

Name: pear-Text_TeXHyphen
Version: 0.1.0
Release: alt1

Summary: Implements the TeX hyphenation algotithm

License: PHP
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
This package hyphenates words by applying the TeX algorithm for automated
hyphenation.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Text/TeXHyphen.php
%pear_dir/Text/TeXHyphen/
%pear_testdir/Text_TeXHyphen/
%pear_datadir/Text_TeXHyphen/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

