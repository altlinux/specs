%define _unpackaged_files_terminate_build 1
# -*- coding: utf-8 -*-
%define version    17.5.0
%define release    alt1

%define source_version %version
%define source_name pyOpenSSL
%setup_python_module OpenSSL

%def_without doc_package
%def_with python3

Summary: Python wrapper module around the OpenSSL library
Summary(ru_RU.UTF-8): Модуль-обвязка библиотеки OpenSSL для python
Name: %packagename
Version: 17.5.0
Release: alt1
Source0: https://pypi.python.org/packages/3b/15/a5d90ab1a41075e8f0fae334f13452549528f82142b3b9d0c9d86ab7178c/pyOpenSSL-%{version}.tar.gz
License: LGPL
Group: Development/Python
Url: http://pyopenssl.sourceforge.net/
Packager: Alexey Morozov <morozov@altlinux.org>
#BuildPreReq: rpm-build-python > 0.12-alt3
BuildArch: noarch

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
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

%prep
%setup -q -n pyOpenSSL-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%if_with doc_package
pushd doc
make html
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif


%files
%doc CHANGELOG.rst CONTRIBUTING.rst INSTALL.rst README.rst
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with doc_package
%files doc
%doc examples
%doc doc/html/*
%endif

%if_with python3
%files -n python3-module-%modulename
%doc CHANGELOG.rst CONTRIBUTING.rst INSTALL.rst README.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Dec 15 2017 Vladimir Didenko <cow@altlinux.org> 17.5.0-alt1
- Version 17.5.0 (closes: #34328)

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 16.2.0-alt1
- automated PyPI update

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 16.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Mon Mar 21 2016 Vladimir Didenko <cow@altlinux.org> 16.0.0-alt1
- Version 16.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.15.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Apr 15 2015 Vladimir Didenko <cow@altlinux.org> 0.15.1-alt1
- Version 0.15.1

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt2
- Added *.egg-info

* Tue Jul 29 2014 Vladimir Didenko <cow@altlinux.org> 0.14-alt1
- Version 0.14

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1
- Version 0.13.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.13-alt1.2
- Rebuild with Python-3.3

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
