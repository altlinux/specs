%define _unpackaged_files_terminate_build 1
%define oname requests-oauthlib

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1
Summary: OAuthlib authentication support for Requests
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/requests-oauthlib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/requests/requests-oauthlib.git
Source0: https://pypi.python.org/packages/46/9b/c28061cc63298bc29ff7d668e18c5293bb522e946aaeb98e4c552d2c0f7b/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel python-module-oauthlib
#BuildPreReq: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires oauthlib.common requests.compat

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pycrypto python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-oauthlib python-module-objects.inv python-module-requests python3-module-setuptools rpm-build-python3 time

%description
This project provides first-class OAuth library support for Requests.

%package -n python3-module-%oname
Summary: OAuthlib authentication support for Requests
Group: Development/Python3
%py3_requires oauthlib.common requests.compat

%description -n python3-module-%oname
This project provides first-class OAuth library support for Requests.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This project provides first-class OAuth library support for Requests.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This project provides first-class OAuth library support for Requests.

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst PKG-INFO docs
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO docs
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20140606.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1.git20140606.1
- NMU: Use buildreq for BR.

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140606
- Initial build for Sisyphus

