# -*- coding: utf-8 -*-
%define version    0.13
%define release    alt1.1

%define source_version %version
%define source_name pyOpenSSL
%setup_python_module OpenSSL

%def_without doc_package
%def_with python3

Summary: Python wrapper module around the OpenSSL library
Summary(ru_RU.UTF-8): Модуль-обвязка библиотеки OpenSSL для python
Name: %packagename
Version: %version
Release: %release
Source: %source_name-%source_version.tar.bz2
License: LGPL
Group: Development/Python
Url: http://pyopenssl.sourceforge.net/
Packager: Alexey Morozov <morozov@altlinux.org>
BuildPreReq: rpm-build-python > 0.12-alt3

# Automatically added by buildreq on Mon Jan 12 2004
BuildRequires: libssl-devel python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

Provides: %__python_module_prefix-pyOpenSSL
Obsoletes: %__python_module_prefix-pyOpenSSL
%if_without doc_package
Provides: %__python_module_prefix-pyOpenSSL-doc
Obsoletes: %__python_module_prefix-pyOpenSSL-doc
%endif

%description
High-level wrapper around a subset of the OpenSSL library, includes
	* SSL.Connection objects, wrapping the methods of Python's
	  portable sockets
	* Callbacks written in Python
	* Extensive error-handling mechanism, mirroring OpenSSL's
	  error codes
	...  and much more ;)

%description -l ru_RU.UTF-8
Высокоуровневая обвязка для подмножества библиотеки OpenSSL.
Включает в себя:
	* Объекты SSL.Connection для работы с переносимыми сокетами
          python 
	* Коллбэки, написанные на python
	* Широкие возможности по обработке ошибок, отражающие коды
	  ошибок OpenSSL
	... И это еще не все ;)
	  

%if_with python3
%package -n python3-module-%modulename
Summary: Python 3 wrapper module around the OpenSSL library
Group: Development/Python3

%description -n python3-module-%modulename
High-level wrapper around a subset of the OpenSSL library, includes
	* SSL.Connection objects, wrapping the methods of Python's
	  portable sockets
	* Callbacks written in Python
	* Extensive error-handling mechanism, mirroring OpenSSL's
	  error codes
	...  and much more ;)

%package -n python3-module-%modulename-tests
Summary: %modulename tests (Python 3)
Group: Development/Python3
Requires: python3-module-%modulename = %version-%release

%description -n python3-module-%modulename-tests
%modulename is a high-level wrapper around a subset of the OpenSSL
library. This package contains tests for %modulename.
%endif

%if_with doc_package
%package doc
Summary: %modulename documentation and example programs
Summary(ru_RU.UTF-8): Документация по API и примеры программ для %modulename
Group: Development/Python
BuildArch: noarch

%description doc
%modulename is a high-level wrapper around a subset of the OpenSSL
library. Install python-pyOpenSSL-doc if you need the API
documentation and example programs for %modulename.

%description doc -l ru_RU.UTF-8
%modulename - Высокоуровневая обвязка для подмножества библиотеки
OpenSSL. Установите python-%modulename-doc, если Вам требуется
документация по API и примеры программирования с использованием
данного модуля.
%endif

%package tests
Summary: %modulename tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
%modulename is a high-level wrapper around a subset of the OpenSSL
library. This package contains tests for %modulename.

%prep
%setup -n %source_name-%source_version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build_debug
%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%if_with doc_package
pushd doc
make html
popd
%endif

%install
%python_build_install --optimize=2 \
		--record=INSTALLED_FILES
%if_with python3
pushd ../python3
%python3_build_install --optimize=2
popd
%endif


%files -f INSTALLED_FILES
%doc ChangeLog INSTALL README TODO
%exclude %python_sitelibdir/OpenSSL/test

%files tests
%python_sitelibdir/OpenSSL/test

%if_with doc_package
%files doc
%doc examples
%doc doc/html/*
%endif

%if_with python3
%files -n python3-module-%modulename
%doc ChangeLog INSTALL README TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/OpenSSL/test

%files -n python3-module-%modulename-tests
%python3_sitelibdir/OpenSSL/test
%endif

%changelog
* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.1
- Added module for Python 3

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13-alt1
- Version 0.13

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11-alt2.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2
- Rebuilt for debuginfo

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1
- Version 0.11
- Extracted tests into separate package

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2
- Rebuilt with openssl10

* Thu Jun 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt1
- 0.10

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2.1.1.1.1.1
- Rebuilt with python 2.6

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.6-alt2.1.1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.6-alt2.1.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.6-alt2.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.6-alt2.1
- Rebuilt with python-2.4.

* Wed Sep  1 2004 Alexey Morozov <morozov@altlinux.org> 0.6-alt2
- package name changed to follow real module name
- separation of doc package is optional now (and off by default)

* Thu Aug 19 2004 Alexey Morozov <morozov@altlinux.org> 0.6-alt1
- new version
- spec is changed to conform python module policy

* Sun Jan 11 2004 Alexey Morozov <morozov@altlinux.org> 0.5.1-alt1
- Initial build for ALT Linux
