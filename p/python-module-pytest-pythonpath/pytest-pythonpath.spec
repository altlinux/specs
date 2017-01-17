%define _unpackaged_files_terminate_build 1
%define oname pytest-pythonpath

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1
Summary: pytest plugin for adding to the PYTHONPATH from command line or configs
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-pythonpath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bigsassy/pytest-pythonpath.git
Source0: https://pypi.python.org/packages/ad/28/c0068d0bbdec562bacbe1de866138ae10241cc0b7eba7c4b8a2ac8d4474d/%{oname}-%{version}.tar.gz
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
%setup -q -n %{oname}-%{version}

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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20140208.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20140208
- Initial build for Sisyphus

