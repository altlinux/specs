Name: alt-docs-xsl
Version: 0.4
Release: alt2
Group: Publishing

Summary: All XSL stylesheets from ALT Linux Documentation Project

License: Distributable
Url: http://docs.altlinux.ru

Source0: http://docs.altlinux.ru/%name-%version.tar.bz2

BuildArch: noarch

Requires: alt-docs-xsl-common = %version-%release
Requires: alt-docs-xsl-print = %version-%release
Requires: alt-docs-xsl-html = %version-%release
Requires: alt-docs-xsl-xhtml = %version-%release

%define xmlconfdir	%_sysconfdir/xml
%define xsldir          %_datadir/xml/alt-docs-xsl
%define catalog         %xmlconfdir/catalog

%description
Virtual package with all of XSL stylesheets from ALT Linux
Documentation Project.

%description -l ru_RU.CP1251
Виртуальный пакет для установки всех XSL стилей из проекта
документации ALT Linux.


%package common
Summary: Common stylesheets from ALT Linux Documentation Project
Group: Publishing
PreReq: xml-common xml-utils
Conflicts: alt-docs-xsl < 0.3-alt1

%description common
Common stylesheets used for all output formats.

%description common -l ru_RU.CP1251
Общие стили, используемые для всех выходных форматов.


%package print
Summary: Printable (XSL/FO) stylesheets from ALT Linux Documentation Project
Group: Publishing
Requires: alt-docs-xsl-common >= %version-%release
Requires: docbook-style-xsl

%description print
Stylesheets from ALT Linux Documentation Project for XSL/FO
output. This styles modified original DocBook styles
http://www.docbook.org

%description print -l ru_RU.CP1251
Стили для получения документов в формате XSL/FO, который может быть
преобразован в печатные форматы (PDF, PS). Эти стили изменяют
оригинальные стили DocBook
http://www.docbook.org

%package html
Summary: HTML XSL stylesheets from ALT Linux Documentation Project
Group: Publishing
Requires: alt-docs-xsl-common >= %version-%release
Requires: docbook-style-xsl

%description html
XSL sylesheets from ALT Linux Documentation Project for HTML
output. This styles modified original DocBook styles
http://www.docbook.org

%description html -l ru_RU.CP1251
XSL стили для получения формата HTML из исходных документов DocBook
XML. Эти стили изменяют оригинальные стили DocBook
http://www.docbook.org


%package xhtml
Summary: HTML XSL stylesheets from ALT Linux Documentation Project
Group: Publishing
Requires: alt-docs-xsl-common >= %version-%release
Requires: docbook-style-xsl

%description xhtml
XSL sylesheets from ALT Linux Documentation Project for XHTML
output. This styles modified original DocBook styles
http://www.docbook.org

%description xhtml -l ru_RU.CP1251
XSL стили для получения формата XHTML из исходных документов DocBook
XML. Эти стили изменяют оригинальные стили DocBook
http://www.docbook.org

%prep
%setup

%build

%install

%__mkdir -p $RPM_BUILD_ROOT%xsldir
%__cp -a common html xhtml print website catalog.xml $RPM_BUILD_ROOT%xsldir
%__mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
%__cp -a alt-docs-xsl.ignore.buildreq %buildroot%_sysconfdir/buildreqs/files/ignore.d/alt-docs-xsl-common


# FIXME: add ChangeLog (building from cvs)
%files

%files common
%dir %xsldir
%xsldir/catalog.xml
%xsldir/common
%doc README
%_sysconfdir/buildreqs/files/ignore.d/alt-docs-xsl-common

%files print
%xsldir/print

%files html
%xsldir/html

%files xhtml
%xsldir/xhtml

%post common
if [ $1 = 1 ] ; then
/usr/bin/xmlcatalog --noout --add "nextCatalog" \
        "file://%xsldir/catalog.xml" \
        "" \
        %catalog ||:
fi

%postun common
if [ $1 = "0" ] ; then
/usr/bin/xmlcatalog --noout --del \
	"file://%xsldir/catalog.xml" \
        %catalog ||:
fi

%changelog
* Mon Oct 20 2008 Vitaly A. Ostanin <vyt@altlinux.ru> 0.4-alt2
- Drop website subpackage (unsupported)

* Thu Dec 14 2006 Vitaly A. Ostanin <vyt@altlinux.ru> 0.4-alt1
- 0.4 (Fixed invalid QName in 'common' subpackage)
- Relaxing requires in subpackages

* Mon Oct  6 2003 Vyt <vyt@altlinux.ru> 0.3-alt2
- added missing catalog.xml to alt-docs-xsl-common
- changed buildreq ignored name to alt-docs-xsl-common

* Mon Oct  6 2003 Vyt <vyt@altlinux.ru> 0.3-alt1
- 0.3 (added xhtml output)
- splitted to subpackages (-common, -print, -website, -html, -xhtml). Thanks for hints to Sir Raorn.

* Fri Sep 19 2003 Vyt <vyt@altlinux.ru> 0.2-alt1
- 0.2 (added website customization stylesheets)
- Added catalog.xml to buildreq ignores

* Tue Aug 26 2003 Vyt <vyt@altlinux.ru> 0.1-alt1
- 0.1
- First build for Sisyphus
