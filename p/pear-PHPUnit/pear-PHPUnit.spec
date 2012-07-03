%define pear_name PHPUnit

Name: pear-PHPUnit
Version: 3.5.6
Release: alt2

Summary: Regression testing framework for unit tests

License: BSD License
Group: Development/Other
Url: http://pear.phpunit.de/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.phpunit.de/get/%pear_name-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: php5-dom, pear-Benchmark, pear-Console_Getopt

Requires: pear-DbUnit >= 1.0.0
Requires: pear-File_Iterator >= 1.2.3
Requires: pear-Text_Template >= 1.1.0
Requires: pear-PHP_CodeCoverage >= 1.0.2
Requires: pear-PHP_Timer >= 1.0.0
Requires: pear-PHPUnit_MockObject >= 1.0.3
Requires: pear-PHPUnit_Selenium >= 1.0.1
Requires: pear-YAML >= 1.0.4

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP.

%prep
%setup -n %pear_name-%version
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
%_bindir/phpunit
%pear_dir/%pear_name/
#%pear_testdir/%pear_name/
#%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Tue Dec 21 2010 Vitaly Lipatov <lav@altlinux.ru> 3.5.6-alt2
- pack bindir/phpunit
- add requires to needed packages

* Mon Dec 20 2010 Vitaly Lipatov <lav@altlinux.ru> 3.5.6-alt1
- new version 3.5.6 (with rpmrb script)

* Thu Oct 07 2010 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt1
- new version (3.5.0) import in git (ALT bug #23243)

* Thu Jun 10 2010 Vitaly Lipatov <lav@altlinux.ru> 3.4.13-alt1
- new version (3.4.13) import in git
- rename package to pear-PHPUnit

* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt4
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.6-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.6-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.6-alt1
- initial build for ALT Linux Sisyphus

