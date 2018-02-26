%define php_lang ru

Name: php-manual-%php_lang
Version: 20110218
Release: alt1
Serial: 1

Group: Development/Other
License: PHP
Summary: On-line manual for PHP (Russian)
Summary(ru_RU.UTF-8): Электронная документация PHP на русском языке
Url: http://www.php.net/download-docs.php

Source: php_manual_%php_lang.tar

BuildArch: noarch

%description
The php-manual package provides comprehensive documentation
for the PHP HTML-embedded scripting language, in HTML format.

%prep
%setup -q -c

%install
install -dm 755 %buildroot/%_defaultdocdir/php-manual/%php_lang
find . -mindepth 1 -maxdepth 1 | xargs -r mv -ft %buildroot/%_defaultdocdir/php-manual/%php_lang

%files
%_defaultdocdir/php-manual/

%changelog
* Mon Aug 15 2011 Sergey Kurakin <kurakin@altlinux.org> 1:20110218-alt1
- new version

* Wed Jul 22 2009 Sergey Kurakin <kurakin@altlinux.org> 1:20090619-alt1
- new version
- spare level removed from the directory tree (fix #12161)
- fixed directory ownership
- minor spec changes

* Sun May 13 2007 L.A. Kostis <lakostis@altlinux.ru> 1:20070126-alt1
- new version.

* Fri Nov 25 2005 Alexey Gladkov <legion@altlinux.ru> 1:20051125-alt1
- new version.

* Thu Feb 10 2005 Alexey Gladkov <legion@altlinux.ru> 1:20050209-alt1
- new version buileded;
- spec cleanup;
- symlink from %%apache_htdocsdir/addon-modules was removed.

* Thu May 06 2004 Alexander Bokovoy <ab@altlinux.ru> 1:4.3.0-alt2
- Updated build dependencies.

* Mon Feb 03 2003 Alexey Gladkov <legion@altlinux.ru> 1:4.3.0-alt1
- 4.3.0
- package splited into separate localized packages

* Fri Mar 01 2002 Alexander Bokovoy <ab@altlinux.ru> 1:4.1.2-alt1
- Initial build
- 4.1.2
