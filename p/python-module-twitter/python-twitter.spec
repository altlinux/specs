%define modname twitter

Name: python-module-%modname
Version: 3.4.1
Release: alt1

Summary: Python Interface for Twitter API
License: Apache-2.0
Group: Development/Python

Url: https://github.com/bear/python-twitter
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
BuildArch: noarch

Source: twitter-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-devel
BuildRequires: python-module-pytest-runner
BuildRequires: python-module-objects.inv
BuildRequires: python-module-sphinx_rtd_theme

%py_requires rfc822 requests requests_oauthlib

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx 
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel
BuildPreReq: python3-module-pytest-runner


%description
This library provides a pure python interface for the Twitter API.

%package -n python3-module-%modname
Summary: Python Interface for Twitter API
Group: Development/Python3
%py3_requires rfc822py3 requests requests_oauthlib
%add_python3_req_skip rfc822
%py3_provides %modname

%description -n python3-module-%modname
This library provides a pure python interface for the Twitter API.

%prep
%setup -n twitter-%version

rm -rf ../python3
cp -fR . ../python3

%prepare_sphinx .

%build
%python_build

pushd ../python3
%python3_build
popd

export PYTHONPATH=%buildroot%python_sitelibdir
sphinx-build doc/ _build/ doc/*.rst
mkdir man
cp -fR doc/_build/html/* man/

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc AUTHORS.* CHANGES COPYING LICENSE README.*
%doc examples/ man/
%python_sitelibdir/*

%files -n python3-module-%modname
%doc AUTHORS.* CHANGES COPYING LICENSE README.*
%doc examples/ man/
%python3_sitelibdir/*


%changelog
* Fri Mar 23 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.4.1-alt1
- Version 3.4.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Added %%py3_provides for Python 3 module

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Version 2.0
- Added module for Python 3

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2
- Rebuild with Python-2.7

* Sun Mar 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Apr 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt1
- Initial
