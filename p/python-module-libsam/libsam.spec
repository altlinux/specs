%define _unpackaged_files_terminate_build 1
%define oname libsam

%def_with python3

Name: python-module-%oname
Version: 0.1.8
Release: alt1.1
Summary: Bio-Informatics sam file libraries
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/libsam/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dlmeduLi/libsam.git
Source0: https://pypi.python.org/packages/2e/19/ac09eee4abd444761eec581941a35b93c0597ba79643dcb5079398be5ac7/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Libsam is a collection of SAM/BAM file related python library. Packaged
included in this library include:

    samparser: A robust sam file format checker and parser

%package -n python3-module-%oname
Summary: Bio-Informatics sam file libraries
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Libsam is a collection of SAM/BAM file related python library. Packaged
included in this library include:

    samparser: A robust sam file format checker and parser

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150206
- Version 0.1.4

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150204
- Initial build for Sisyphus

