%define _verify_elf_method 	skip
%define _strip_method 		none
%define _zfdir %php5_datadir/ZendFramework

Name: ZendFramework
Version: 1.11.7
Release: alt1

Summary: A framework for developing Web Applications and Web Services with PHP
License: BSD-style
Group: Development/Other

Url: http://framework.zend.com
Packager: Veaceslav Grecea <slavutich@altlinux.org>
BuildArch: noarch

# http://framework.zend.com/releases/ZendFramework-%version/ZendFramework-%version-minimal.tar.gz
Source0: %name-%version.tar

BuildRequires: rpm-build-php5

%description
Zend Framework is a high quality and open source framework
for developing Web Applications and Web Services with PHP.

%prep
%setup

%install
install -d %buildroot%_zfdir/library
cp -a library/* %buildroot%_zfdir/library

mkdir -p %buildroot%php5_moddir
ln -s -- $(relative %_zfdir/library/Zend %php5_moddir/Zend) %buildroot%php5_moddir/Zend

%files
%doc INSTALL.txt README.txt LICENSE.txt
%dir %_zfdir
%_zfdir/library

%php5_moddir/Zend/

%changelog
* Fri Jun 24 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.11.7-alt1
- Updated to 1.11.7 (Closes: #25808)

* Sun Jun 13 2010 Slava Semushin <php-coder@altlinux.ru> 1.10.5-alt1
- Updated to 1.10.5

* Sun Feb 28 2010 Slava Semushin <php-coder@altlinux.ru> 1.10.2-alt1
- Updated to 1.10.2

* Thu Feb 11 2010 Slava Semushin <php-coder@altlinux.ru> 1.10.1-alt1
- Updated to 1.10.1

* Fri Jan 29 2010 Slava Semushin <php-coder@altlinux.ru> 1.10.0-alt1
- Updated to 1.10.0

* Wed Jan 13 2010 Slava Semushin <php-coder@altlinux.ru> 1.9.7-alt1
- Updated to 1.9.7
- The following security vulnerabilities are resolved in this release:
  + ZF2010-06: Potential XSS or HTML Injection vector in Zend_Json
  + ZF2010-05: Potential XSS vector in Zend_Service_ReCaptcha_MailHide
  + ZF2010-04: Potential MIME-type Injection in Zend_File_Transfer
  + ZF2010-03: Potential XSS vector in Zend_Filter_StripTags when comments allowed
  + ZF2010-02: Potential XSS vector in Zend_Dojo_View_Helper_Editor
  + ZF2010-01: Potential XSS vectors due to inconsistent encodings

* Sun Jan 10 2010 Slava Semushin <php-coder@altlinux.ru> 1.9.6-alt1
- Updated to 1.9.6

* Sat Oct 31 2009 Slava Semushin <php-coder@altlinux.ru> 1.9.5-alt1
- Updated to 1.9.5

* Wed Oct 14 2009 Slava Semushin <php-coder@altlinux.ru> 1.9.4-alt1
- Updated to 1.9.4
- Changed License tag to BSD-style (Closes: #21940)
- Added symlink to made ZF available out of box (Closes: #21941)

* Wed Sep 30 2009 Slava Semushin <php-coder@altlinux.ru> 1.9.3-alt1pl1
- Updated to 1.9.3PL1

* Sun Aug 30 2009 Slava Semushin <php-coder@altlinux.ru> 1.9.2-alt1
- Updated to 1.9.2 (Closes: #19891)
- Changed Url tag

* Fri Mar 20 2009 Veaceslav Grecea <slavutich@altlinux.org> 1.7.7-alt1
- Upgrade to 1.7.7 Release

* Thu Feb 19 2009 Veaceslav Grecea <slavutich@altlinux.org> 1.7.5-alt1
- Upgrade to 1.7.5 Release

* Mon Nov 17 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.7.0-alt1
- Upgrade to 1.7.0 Release

* Tue Oct 4 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.6.2-alt1
- Upgrade to 1.6.2 Release

* Tue Sep 4 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.6.0-alt1
- 1.6.0 Release

* Tue Aug 28 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.6.0RC3-alt0.7
- 1.6.0 RC3

* Tue Aug 15 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.6.0RC2-alt0.6
- 1.6.0 RC2

* Tue Jul 22 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.6.0RC1-alt0.5
- 1.6.0 RC1

* Thu Jul 22 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus
