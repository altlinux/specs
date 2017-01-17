%define _unpackaged_files_terminate_build 1
%define oname requests-cache

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.13
Release: alt1
Summary: Persistent cache for requests library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/reclosedev/requests-cache.git
Source0: https://pypi.python.org/packages/1a/cf/12349c7113b252d9a0b26d497d3349baeb6c8f293b440e55a00e7fa6e4a4/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-unittest2
#BuildPreReq: python-module-pymongo python-module-redis-py
#BuildPreReq: python-modules-sqlite3
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests python3-module-unittest2
#BuildPreReq: python3-module-pymongo python3-module-redis-py
#BuildPreReq: python3-modules-sqlite3
%endif

%py_provides requests_cache
%py_requires sqlite3

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-pytest python-module-requests python-module-unittest2 python-modules-sqlite3 python3-module-chardet python3-module-pytest python3-module-unittest2 python3-module-urllib3 rpm-build-python3 time

%description
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

%package -n python3-module-%oname
Summary: Persistent cache for requests library
Group: Development/Python3
%py3_provides requests_cache
%py3_requires sqlite3

%description -n python3-module-%oname
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst sandbox.py example.py PKG-INFO docs
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst sandbox.py example.py PKG-INFO docs
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.13-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.9-alt1.git20150117.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.9-alt1.git20150117.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20150117
- Version 0.4.9

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1.git20141219
- Initial build for Sisyphus

