%define _unpackaged_files_terminate_build 1
%define oname pytest_optional
Name: python-module-%oname
Version: 0.0.3
Release: alt1
Summary: include/exclude values of fixtures in pytest
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-optional/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/fe/7e/c967d4639cbdb581f3b625b4b41c6c9a20112284eab3c551ae42e0220bcd/pytest-optional-%{version}.tar.gz

BuildPreReq: python-module-setuptools-tests python-module-decorator
BuildArch: noarch

%py_provides %oname

%description
include/exclude values of fixtures in pytest.

%prep
%setup -q -n pytest-optional-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1
- automated PyPI update

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus

