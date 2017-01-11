%define _unpackaged_files_terminate_build 1
%define oname validators

%def_with python3

Name: python-module-%oname
Version: 0.11.2
Release: alt1
Summary: Python Data Validation for Humans
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/validators/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/validators.git
Source0: https://pypi.python.org/packages/fb/b7/52bd6922804ec00195ebd86656ffc2087f89626e9907f512e98e97788578/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-decorator
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-decorator
%endif

%py_provides %oname

%description
Python has all kinds of data validation tools, but every one of them
seems to require defining a schema or form. I wanted to create a simple
validation library where validating a simple value does not require
defining a form or a schema.

%package -n python3-module-%oname
Summary: Python Data Validation for Humans
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python has all kinds of data validation tools, but every one of them
seems to require defining a schema or form. I wanted to create a simple
validation library where validating a simple value does not require
defining a form or a schema.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.git20140907.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20140907
- Initial build for Sisyphus

