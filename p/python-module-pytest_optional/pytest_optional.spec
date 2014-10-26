%define oname pytest_optional
Name: python-module-%oname
Version: 0.0.2
Release: alt1
Summary: include/exclude values of fixtures in pytest
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-optional/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-decorator
BuildArch: noarch

%py_provides %oname

%description
include/exclude values of fixtures in pytest.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
rm -fR build
py.test

%files
%python_sitelibdir/*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus

