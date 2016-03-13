%define oname facebook-sdk

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.alpha.git20140828.1.1
Summary: Support the Facebook Graph API and the official Facebook JavaScript SDK
License: ASL
Group: Development/Python
Url: https://pypi.python.org/pypi/facebook-sdk
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pythonforfacebook/facebook-sdk.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: gcc-c++ python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel graphviz doxygen
#BuildPreReq: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-requests python3-module-setuptools rpm-build-python3 time

%description
This client library is designed to support the Facebook Graph API and
the official Facebook JavaScript SDK, which is the canonical way to
implement Facebook authentication.

This client library is designed to support the Facebook Graph API and
the official Facebook JavaScript SDK, which is the canonical way to
implement Facebook authentication. You can read more about the Graph API
by accessing its official documentation.

%package -n python3-module-%oname
Summary: Support the Facebook Graph API and the official Facebook JavaScript SDK
Group: Development/Python3

%description -n python3-module-%oname
This client library is designed to support the Facebook Graph API and
the official Facebook JavaScript SDK, which is the canonical way to
implement Facebook authentication.

This client library is designed to support the Facebook Graph API and
the official Facebook JavaScript SDK, which is the canonical way to
implement Facebook authentication. You can read more about the Graph API
by accessing its official documentation.

%prep
%setup

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
%make -C docs html

%files
%doc *.rst examples docs/_build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.alpha.git20140828.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.alpha.git20140828.1
- NMU: Use buildreq for BR.

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.alpha.git20140828
- Initial build for Sisyphus

