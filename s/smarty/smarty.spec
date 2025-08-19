%define _smartydir %php_datadir/Smarty
%define php_extension Smarty

Name: smarty
Version: 5.5.1
Release: alt1

Summary: Template engine for PHP

License: LGPL-3.0-or-later
Group: Development/Other
Url: https://www.smarty.net
VCS: https://github.com/smarty-php/smarty

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: rpm-build-php-version

%description
Smarty is a template engine for PHP. Smarty provides your basic
variable substitution and dynamic block functionality, and also takes
a step further to be a "smart" template engine, adding features such
as configuration files, template functions, variable modifiers, and
making all of this functionality as easy as possible to use for both
programmers and template designers.

%package -n php%_php_suffix-%php_extension
Summary: Template engine for PHP
Group: Development/Other
BuildArch: noarch

%description -n php%_php_suffix-%php_extension
Smarty is a template engine for PHP. Smarty provides your basic
variable substitution and dynamic block functionality, and also takes
a step further to be a "smart" template engine, adding features such
as configuration files, template functions, variable modifiers, and
making all of this functionality as easy as possible to use for both
programmers and template designers.

%prep
%setup
%patch0 -p1

%install
install -d %buildroot%_smartydir
install libs/Smarty.class.php %buildroot%_smartydir

%files -n php%_php_suffix-%php_extension
%doc LICENSE CHANGELOG.md README.md CONTRIBUTING.md TODO.txt
%dir %_smartydir
%_smartydir/*.class.php

%changelog
* Tue Aug 19 2025 Leontiy Volodin <lvol@altlinux.org> 5.5.1-alt1
- New version 5.5.1.
- Returned to Sisyphus (for self-service-password).

* Tue Jan 27 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.6.22-alt1
- Updated to 2.6.22. Security fixes:
  + CVE-2008-4810
  + CVE-2008-4811

* Wed Mar 12 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 2.6.19-alt1
- 2.6.19. Security fixes:
  + CVE-2008-1066 (Smarty "regex_replace" Modifier Template Security Bypass)

* Thu May 24 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.6.18-alt1
- Initial build for Sisyphus
