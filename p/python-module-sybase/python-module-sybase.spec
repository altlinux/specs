# -*- coding: utf-8 -*-
Name: python-module-sybase
Version: 0.40
Release: alt0.2.1
Epoch: 1
License: BSD
Packager: Alexey Morsov <swi@altlinux.ru>
Group: Databases
Summary: Python interface for Sybase DB
Summary(ru_RU.UTF-8): Интерфейс к БД Sybase для Python

Url: http://python-sybase.sourceforge.net/

Source: %name-%version.tar

Requires: python >= 2.4
Requires: libfreetds >= 0.64
Requires: python-module-egenix-mx-base

BuildPreReq: python-module-setuptools
# Automatically added by buildreq on Wed Dec 13 2006
BuildRequires: libfreetds-devel >= 0.64 python-devel python-modules-encodings
# for build pdf from tex docs
BuildRequires: python-doc-tools


%description
Sybase module developed by Dave Cole, provides a Python interface to
the Sybase relational database system. The Sybase package supports all
of the Python Database API, version 2.0 with extensions.

This build use freetds instead Sybase libs

%description -l ru_RU.UTF-8
Модуль Sybase разработаный Dave Cole предоставляет интерфейс доступа к
базам данных Sybase для языка Python. Этот пакет поддерживает весь
Python Database API версии 2.0 со всеми расширениями.

Этот пакет использует библиотеку freetds вместо Sybase


%prep
%setup

%build
export SYBASE=/usr
%python_build_debug build_ext -D WANT_THREADS -D HAVE_FREETDS \
	-U WANT_BULKCOPY -lct
cd doc
%make MKHOWTO=/usr/share/python-doc-tools/tools/mkhowto

%install
export SYBASE=/usr
%python_install --optimize=2

%files
%doc doc/*.pdf examples/ ChangeLog LICENCE TODO
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:0.40-alt0.2.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.40-alt0.2
- Rebuilt for debuginfo

* Sat Dec 18 2010 Alexey Morsov <swi@altlinux.ru> 1:0.40-alt0.1
- new version
- clean spec
- change url (fork)

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.39-alt2
- Rebuilt with python 2.6

* Tue Apr 15 2008 Alexey Morsov <swi@altlinux.ru> 1:0.39-alt1
- 0.39 release

* Wed Feb 13 2008 Alexey Morsov <swi@altlinux.ru> 1:0.39-alt0.2.pre1
- Added type mapping
- Handle engineer notation of numbers in numeric
- Added support for CS_DATE_TYPE
- Added support for python Decimal objects in databuf
- Added a prepare method to Cursor
- Additional 'locale' argument to connect and Connection to set 
  the locale of the connection
- Added conversion from string to int when assigning to a 
  CS_INT_TYPE DataBuf

* Mon Jan 28 2008 Alexey Morsov <swi@altlinux.ru> 1:0.38-alt1.1
- rebuild with freetds-0.64

* Fri May 04 2007 Alexey Morsov <swi@altlinux.ru> 1:0.38-alt1
- 0.38 release
- add requires for mxDateTime module (internal python-module-sybase datetime
will be deprecated in 0.39)

* Wed Dec 13 2006 Alexey Morsov <swi@altlinux.ru> 0.38pre1-alt1
- Initial build for Sisyphus

