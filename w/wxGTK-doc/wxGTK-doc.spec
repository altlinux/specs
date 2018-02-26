Name: wxGTK-doc
Version: 2.8.0
Release: alt0.1

Summary: Documentation for the wxWidgets in HTML
Summary(ru_RU.KOI8-R): дПЛХНЕОФБГЙС ДМС wxWidgets Ч HTML

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: LGPL
Group: Development/C++
Url: http://www.wxwidgets.org/docs.htm

BuildArch: noarch
AutoReqProv: no

Provides: wxGTK2-doc
Obsoletes: wxGTK2-doc

Source: http://dl.sf.net/wxwindows/wxWidgets-%version-HTML.tar.bz2
#Source1: wx-docs-extra-html.tar.bz2

%description
Documentation for the Python programming language, interpreter,
and bundled module library in the HTML format.

%description -l ru_RU.CP1251
Документация по языку программирования Python, его интерпретатору
и распространяемой с ним библиотеке модулей, в формате HTML.

%prep
%setup -q -n html
#%setup -q -n wxWidgets-%version

%files
%doc *

%changelog
* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt0.1
- new version
- rename package to wxGTK-doc

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.6.3-alt0.1
- new version 2.6.3 (with rpmrb script)
- contribs is left

* Tue Nov 01 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.2-alt1
- new version (docs-extra is missed)

* Sun Apr 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.5-alt1
- first release for ALT Linux Sisyphus
