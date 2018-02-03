%define _unpackaged_files_terminate_build 1
%define oname multienum

%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt1.1
Summary: Enumerator type supporting multiple equivalent names
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/multienum/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sorreltree/multienum.git
Source0: https://pypi.python.org/packages/9d/89/95b37cffa32113a49506ba38821aa6ca53829861c92e01d89d7a5c14ee53/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
An enumeration type supporting multiple equivalent names.

%package -n python3-module-%oname
Summary: Enumerator type supporting multiple equivalent names
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
An enumeration type supporting multiple equivalent names.

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
install -p -m644 %oname.py %buildroot%python_sitelibdir/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 %oname.py %buildroot%python3_sitelibdir/
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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.b.git20150202.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b.git20150202
- Initial build for Sisyphus

