%define oname pyOpenSSL

%def_without doc_package

Name: python3-module-openssl
Version: 22.1.0
Release: alt1

Summary: Python wrapper module around the OpenSSL library
Summary(ru_RU.UTF-8): Модуль-обвязка библиотеки OpenSSL для python

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/pyca/pyopenssl

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

Provides: python3-module-OpenSSL = %EVR
Obsoletes: python3-module-OpenSSL

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

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


%if_with doc_package
%package doc
Summary: %oname documentation and example programs
Summary(ru_RU.UTF-8): Документация по API и примеры программ для %oname
Group: Development/Python
BuildArch: noarch

%description doc
%modulename is a high-level wrapper around a subset of the OpenSSL
library. Install python-pyOpenSSL-doc if you need the API
documentation and example programs for %oname.

%description doc -l ru_RU.UTF-8
%oname - Высокоуровневая обвязка для подмножества библиотеки
OpenSSL. Установите python-%oname-doc, если Вам требуется
документация по API и примеры программирования с использованием
данного модуля.
%endif

%prep
%setup

%build
%python3_build

%if_with doc_package
pushd doc
make html
popd
%endif

%install
%python3_install
%python3_prune

%files
%doc CHANGELOG.rst CONTRIBUTING.rst INSTALL.rst README.rst
%python3_sitelibdir/OpenSSL/
%python3_sitelibdir/%oname-*.egg-info

%if_with doc_package
%files doc
%doc examples
%doc doc/html/*
%endif

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 22.1.0-alt1
- new version 22.1.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 22.0.0-alt1
- new version 22.0.0 (with rpmrb script)

* Wed Mar 10 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 20.0.1-alt1
- 20.0.1
- spec: fix license field

* Fri Nov 06 2020 Vitaly Lipatov <lav@altlinux.ru> 19.1.0-alt1
- new version 19.1.0 (with rpmrb script)

* Fri Nov 06 2020 Vitaly Lipatov <lav@altlinux.ru> 19.0.0-alt2
- build python3 module separately, cleanup spec

* Sun Oct 06 2019 Anton Farygin <rider@altlinux.ru> 19.0.0-alt1
- 19.0.0

* Mon Jul 30 2018 Vladimir Didenko <cow@altlinux.org> 18.0.0-alt1
- Version 18.0.0 (closes: #35155)

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
