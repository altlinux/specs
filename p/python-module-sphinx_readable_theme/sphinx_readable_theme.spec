%define oname sphinx_readable_theme

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.git20150327.1.1
Summary: Sphinx Readable Theme
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinx-readable-theme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ignacysokolowski/sphinx-readable-theme.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
A clean and readable Sphinx theme with focus on autodoc - documentation
from docstrings.

Inspired by flask-sphinx-themes.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx Readable Theme
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A clean and readable Sphinx theme with focus on autodoc - documentation
from docstrings.

Inspired by flask-sphinx-themes.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.rst docs/source/*.rst docs/source/example.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/source/*.rst ../python3/docs/source/example.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.git20150327.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.git20150327.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150327
- Initial build for Sisyphus

