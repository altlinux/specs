# stalled mainstream, revised at 19.06.08
Name: python-module-PyXML
Version: 0.8.4
Release: alt5.1.1

Summary: XML libraries for python

Group: Development/Python
License: Various
Url: http://pyxml.sourceforge.net/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/pyxml/PyXML-%version.tar.bz2
Patch0: %name-0.8.4-gentoo-python2.6.patch

%setup_python_module PyXML

# hack for unknown deps
%add_python_req_skip XMLFactory XMLinter xml_dc XMLClient

Provides: PyXML
Obsoletes: PyXML

BuildPreReq: libexpat-devel python-devel

%description
An XML package for Python.  The distribution contains a
validating XML parser, an implementation of the SAX and DOM
programming interfaces and an interface to the Expat parser.

%prep
%setup -n PyXML-%version
%patch0 -p1
rm -rf extensions/expat/lib/

%build
%python_build_debug --with-libexpat=%_prefix

%install
%python_install

%files
%doc LICENCE ANNOUNCE CREDITS README* TODO doc/*
%_bindir/xmlproc_parse
%_bindir/xmlproc_val
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt5.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt5.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt5
- Rebuilt for debuginfo

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt4.1
- Rebuilt with python 2.6

* Sat Jul 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.8.4-alt4
- fix incompatibility with python2.6 (Gentoo)
- spec cleanup

* Sat Jun 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt3
- fix unmets, update buildreqs

* Thu Jun 19 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt2
- fix dir packing

* Tue Mar 22 2005 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- NMU: new version
- rename package to python-module-PyXML
- rebuild with python 2.4

* Tue Feb 24 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.3-alt1
- New upstream release
- Built against python 2.3
- Cleaned up install

* Tue Mar 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.2-alt1
- 0.8.2
- Use system libexpat
- Changed License field to Various, to reflect on the multitude of licenses

* Wed Oct 23 2002 Stanislav Ievlev <inger@altlinux.ru> 0.8.1-alt1
- 0.8.1
- build with gcc3

* Fri Aug 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.8-alt1
- 0.8.0

* Mon Jan 28 2002 Stanislav Ievlev <inger@altlinux.ru> 0.7.0-alt1
- 0.7.0
- rebuild with new python

* Wed Jun 27 2001 AEN <aen@logic.ru> 0.6.5-alt1
- first build for Sisyphus

* Thu Jun  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Don't obsolete itself

* Mon May  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Initial build, it's no longer part of 4Suite
