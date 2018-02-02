%define oname doctools

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20110902.2.1
Summary: Docblock manipulation utilities
License: BSD3
Group: Development/Python
Url: https://pypi.python.org/pypi/doctools/

# https://github.com/awagner83/doctools.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytest-cov
%endif

%py_provides %oname

%description
doctools - python docblock manipulation utilities.

%package -n python3-module-%oname
Summary: Docblock manipulation utilities
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
doctools - python docblock manipulation utilities.

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
./runtests.sh
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|py\.test|py.test3|' runtests.sh
./runtests.sh
popd
%endif

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.git20110902.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.2-alt1.git20110902.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20110902.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20110902
- Initial build for Sisyphus

