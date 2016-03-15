%define oname pytest-pythonpath

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20140208.1
Summary: pytest plugin for adding to the PYTHONPATH from command line or configs
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-pythonpath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bigsassy/pytest-pythonpath.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides pytest_pythonpath

%description
This is a py.test plugin for adding to the PYTHONPATH from the
pytests.ini file before tests run.

%package -n python3-module-%oname
Summary: pytest plugin for adding to the PYTHONPATH from command line or configs
Group: Development/Python3
%py3_provides pytest_pythonpath

%description -n python3-module-%oname
This is a py.test plugin for adding to the PYTHONPATH from the
pytests.ini file before tests run.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20140208.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20140208
- Initial build for Sisyphus

