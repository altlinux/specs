Name: db2latex-xsl
Version: 0.8
Release: alt0.pre1.2
Group: Publishing

Summary: XSLT stylesheets which generate high level LaTeX2e from DocBook document

License: Distributable
Url: http://db2latex.sourceforge.net

PreReq: xml-common xml-utils

Source0: %name-%{version}pre1.tar.bz2
Source1: catalog.xml.bz2
Patch: %name-%{version}pre1-template.patch

BuildArch: noarch

%define xmlconfdir %_sysconfdir/xml
%define db2latexdir %_datadir/xml/%name-%{version}pre1
%define catalog %xmlconfdir/catalog

%description
DB2LaTeX are a set of XSLT stylesheets which generate high level
LaTeX2e from your docbook document. They do not perform any FO
transformation, the only thing they do is to map DocBook tags into
more or less standard LaTeX.

%description -l ru_RU.CP1251
DB2LaTeX - это набор стилей для преобразования документов из формата
DocBook в формат LaTeX2e. Эти стили не выполняют никаких FO обработок,
они только делают из тегов DocBook более или менее стандартные теги LaTeX.

%prep

%setup -q -n %name-%{version}pre1
%patch0 -p1

find ./doc -perm 755 -regex ".*[^h]" -type f -exec chmod a-x {} \;

%build

%install

%__mkdir_p $RPM_BUILD_ROOT%db2latexdir
%__cp -a VERSION contrib xsl $RPM_BUILD_ROOT%db2latexdir
bzcat %SOURCE1 > $RPM_BUILD_ROOT%db2latexdir/catalog.xml
%__ln_s -f %name-%{version}pre1 $RPM_BUILD_ROOT%_datadir/xml/%name

%files
%db2latexdir
%_datadir/xml/%name
%doc AUTHOR CHANGES COPYING COPYRIGHT DOCBOOK.RFE README THANKS TODO doc

%post
if [ $1 = 1 ] ; then
/usr/bin/xmlcatalog --noout --add "nextCatalog" \
        "file://%_datadir/xml/%name/catalog.xml" \
        "" \
        %catalog ||:
fi

%postun
if [ $1 = 0 ] ; then
/usr/bin/xmlcatalog --noout --del \
        "file://%_datadir/xml/%name/catalog.xml" \
        %catalog ||:
fi

%changelog
* Wed Oct 27 2004 Vladimir Lettiev <crux@altlinux.ru> 0.8-alt0.pre1.2
- added patch (removed duplicate template 'question.answer.label')

* Sun Oct 03 2004 Vladimir Lettiev <crux@altlinux.ru> 0.8-alt0.pre1.1
- 0.8pre1

* Tue Jul  1 2003 Vyt <vyt@altlinux.ru> 0.7-alt2.cvs20030622
- Fixed release in spec

* Tue Jul  1 2003 Vyt <vyt@altlinux.ru> 0.7-alt1.cvs20030622
- First build for Sisyphus
