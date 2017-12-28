%define oname tinycss2

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1
Summary: Modern CSS parser for Python
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/tinycss2/

# https://github.com/Kozea/tinycss2.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-webencodings
BuildRequires: python-module-pytest-runner python-module-pytest-isort python-module-pytest-flake8 python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-webencodings
BuildRequires: python3-module-pytest-runner python3-module-pytest-isort python3-module-pytest-flake8 python3-module-pytest-cov
%endif

%py_provides %oname
%py_requires webencodings

%description
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Modern CSS parser for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires webencodings

%description -n python3-module-%oname
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
tinycss2 is a rewrite of tinycss with a simpler API, based on the more
recent CSS Syntax Level 3 specification.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES TODO LICENSE *.rst docs/*.rst docs/css_diagram_role.py
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*
%exclude %python_sitelibdir/*/css-parsing-tests

%files tests
%python_sitelibdir/*/test.*
%python_sitelibdir/*/css-parsing-tests

%if_with python3
%files -n python3-module-%oname
%doc CHANGES TODO LICENSE *.rst docs/*.rst docs/css_diagram_role.py
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/css-parsing-tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/css-parsing-tests
%endif

%changelog
* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Updated to upstream version 0.6.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20140819.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20140819.1
- NMU: Use buildreq for BR.

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140819
- Initial build for Sisyphus

