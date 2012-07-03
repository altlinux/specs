%define pear_name DbUnit

Name: pear-DbUnit
Version: 1.0.0
Release: alt1

Summary: DbUnit port for PHP/PHPUnit

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.phpunit.de/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
DbUnit port for PHP/PHPUnit

%prep
%setup -c -n %pear_name-%version
# Hack against Unknown channel "pear.phpunit.de"
%__subst "s|pear.phpunit.de|pear.php.net|g" package.xml

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
%_bindir/dbunit
%pear_dir/PHPUnit/
#%pear_testdir/MDB2/
#%pear_datadir/MDB2/LICENSE
#%pear_dir/MDB2.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Mon Dec 20 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
