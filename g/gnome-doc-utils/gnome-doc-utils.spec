%define ver_major 0.20

%undefine _configure_target

Name: gnome-doc-utils
Version: %ver_major.10
Release: alt1

Summary: Documentation utilities for GNOME
Group: Development/Other
License: %gpl2plus
Url: http://www.gnome.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Source1: scrollkeeper-omf.dtd
# GNOME bug #524207
Patch1: gnome-doc-utils-0.14.0-package.patch

%define pkgdocdir %_docdir/%name-%version

%define libxml_version 2.6.12
%define libxslt_version 1.1.8

Requires: %name-xslt = %version-%release
Requires: librarian
Requires: python-modules-encodings

%add_python_compile_include %python_sitelibdir/xml2po

BuildArch: noarch

BuildPreReq: rpm-build-python rpm-build-licenses rpm-build-gnome intltool
BuildRequires: libxml2-devel >= %libxml_version
BuildRequires: libxslt-devel >= %libxslt_version
BuildRequires: python-devel python-module-libxml2 python-modules-encodings
BuildRequires: db2latex-xsl docbook-dtds librarian xsltproc

%description
gnome-doc-utils is a collection of documentation utilities for the Gnome
project. It contains the DocBook XSLT stylesheets that were once
distributed with Yelp.

%package xslt
Summary: XSLT stylesheets for %name
Group: Development/Other
License: %lgpl2plus

%description xslt
XSLT stylesheets from the gnome-doc-utils collection.

%prep
%setup
cp %SOURCE1 doc/

%if 0
%_bindir/xmlcatalog --create --noout catalog
%_bindir/xmlcatalog --noout --add "public" \
"-//OMF//DTD Scrollkeeper OMF Variant V1.0//EN" \
"doc/scrollkeeper-omf.dtd" catalog
export SGML_CATALOG_FILES=catalog
%endif

%patch1 -p1 -b .package

# Update URLs of external entities to fix build in isolated network environment.
find -type f -print0 |
	xargs -r0 grep -lZ "'http://[^']*/scrollkeeper-omf[.]dtd'" |
	xargs -r0 sed -i "s|'http://[^']*/scrollkeeper-omf[.]dtd'|'/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd'|" --

%build
export am_cv_python_pythondir=%python_sitelibdir
%configure --disable-scrollkeeper
# SMP-incompatible build
%make

%check
%make check

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang gnome-doc-make gnome-doc-xslt gnome-doc-mallard-spec gnome-doc-utils

install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS README NEWS COPYING %buildroot%pkgdocdir/
ln -s %_licensedir/GPL-2 %buildroot%pkgdocdir/COPYING.GPL
ln -s %_licensedir/LGPL-2.1 %buildroot%pkgdocdir/COPYING.LGPL

%files -f %name.lang
%_bindir/*
%_datadir/pkgconfig/*
%_datadir/aclocal/*
%_datadir/%name
%dir %_datadir/xml/mallard/1.0/
%_datadir/xml/mallard/1.0/*
%_man1dir/*
#python
%python_sitelibdir/xml2po/
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/COPYING
%pkgdocdir/COPYING.GPL
%pkgdocdir/NEWS
%pkgdocdir/README

%files xslt
%pkgdocdir/COPYING.LGPL
%_datadir/xml/gnome

%changelog
* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.20.10-alt1
- 0.20.10

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.20.6-alt2.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Dmitry V. Levin <ldv@altlinux.org> 0.20.6-alt2
- Fixed build in isolated network environment (closes: #25845).

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.20.6-alt1
- 3.0.1

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.20.5-alt1
- 0.20.5

* Tue Jan 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt1
- 0.20.4

* Fri Dec 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- 0.20.3

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.19.5-alt1
- 0.19.5

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.19.4-alt1
- 0.19.4

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 0.19.3-alt1
- 0.19.3

* Tue Jan 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt2
- %%pkgdocdir added to the file list

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 0.19.2-alt1
- 1.19.2

* Wed Jan 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt1
- 0.19.1

* Fri Nov 20 2009 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 0.17.4-alt1
- 0.17.4

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Sat Mar 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Mon Feb 02 2009 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Sat Jan 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Tue Dec 16 2008 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Fri Sep 26 2008 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- New version (0.14.0).

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt1
- New version (0.12.2).

* Wed Mar 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.12.1-alt1
- New version (0.12.1).
- Fixed Source so that rpmgs from etersoft-build-utils could use it.

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.12.0-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 30 2007 Alexey Rusakov <ktirf@altlinux.org> 0.12.0-alt1
- New version (0.12.0).
- Used license macros from rpm-build-licenses.
- added explicit Requires: python-modules-encodings, or packages that
  use xml2po would not build.

* Tue Jun 26 2007 Igor Zubkov <icesik@altlinux.org> 0.10.3-alt2
- add Url to package

* Sat Jun 16 2007 Igor Zubkov <icesik@altlinux.org> 0.10.3-alt1
- 0.6.0 -> 0.10.3
- buildreq

* Sat Apr 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.6.0-alt1
- Release 0.6.0

* Mon Feb 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.6-alt1
- Updated to 0.5.6
- Split off XSLT stylesheets due to license differencies

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.3-alt1.1
- Rebuilt for new pkg-config dependencies.

* Wed Oct 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Sat Sep 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.1-alt1
- Updated to 0.4.1
- Install the .pc file into architecture-neutral /usr/share/pkgconfig

* Tue Aug 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.3-alt1
- Updated to 0.3.3

* Thu Apr 07 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.0-alt1
- New upstream release

* Sun Mar 13 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.3-alt2
- Rebuilt with Python 2.4

* Wed Mar 09 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.3-alt1
- Updated to the latest upstream release

* Mon Jan 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.1-alt2
- Build requires rpm-build-python
- Require python 2.3 for correct generation of dependencies
- Added /usr/share/xml2po to python compile path

* Mon Jan 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.1.1-alt1
- Initial release for Sisyphus
