%define _unpackaged_files_terminate_build 1
%define oname paginate

%def_with python3

Name: python-module-%oname
Version: 0.5.6
Release: alt1
Summary: Divides large result sets into pages for easier browsing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/paginate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pylons/paginate.git
Source0: https://pypi.python.org/packages/68/58/e670a947136fdcece8ac5376b3df1369d29e4f6659b0c9b358605b115e9e/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
This module helps divide up large result sets into pages or chunks. The
user gets displayed one page at a time and can navigate to other pages.
It is especially useful when developing web interfaces and showing the
users only a selection of information at a time.

%package -n python3-module-%oname
Summary: Divides large result sets into pages for easier browsing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This module helps divide up large result sets into pages or chunks. The
user gets displayed one page at a time and can navigate to other pages.
It is especially useful when developing web interfaces and showing the
users only a selection of information at a time.

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
#export PYTHONPATH=$PWD
#py.test-%_python3_version
popd
%endif

%files
%doc README.md CHANGELOG.txt PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.md CHANGELOG.txt PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20140824.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140824
- Initial build for Sisyphus

