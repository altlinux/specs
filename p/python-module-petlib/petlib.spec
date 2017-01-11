%define _unpackaged_files_terminate_build 1
%define oname petlib

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.40
Release: alt1
Summary: A library implementing a number of Privacy Enhancing Technologies (PETs)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/petlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/d5/40/166afbf4370bef77ce5f2316fda8c6976fea64231abaab74f06de1725ceb/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-setuptools-tests libssl-devel
#BuildPreReq: python-module-cffi python-module-future
#BuildPreReq: python-module-Paver python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-cffi python3-module-future
#BuildPreReq: python3-module-Paver python3-module-pytest-cov
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires cffi future pytest paver pytest_cov

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-pycparser python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-tools-2to3 python3 python3-base python3-module-pycparser
BuildRequires: libssl-devel python-module-cffi python-module-pytest-cov python3-devel python3-module-cffi python3-module-pytest-cov rpm-build-python3 time

%description
A library wrapping Open SSL low-level cryptographic libraries to build
Privacy Enhancing Technoloies (PETs).

%package -n python3-module-%oname
Summary: A library implementing a number of Privacy Enhancing Technologies (PETs)
Group: Development/Python3
%py3_provides %oname
%py3_requires cffi future pytest paver pytest_cov

%description -n python3-module-%oname
A library wrapping Open SSL low-level cryptographic libraries to build
Privacy Enhancing Technoloies (PETs).

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
py.test petlib/*.py
install -d %buildroot%python_sitelibdir/%oname/__pycache__
install -m644 %oname/__pycache__/*.so \
	%buildroot%python_sitelibdir/%oname/__pycache__/
%if_with python3
pushd ../python3
#py.test-%_python3_version petlib/*.py
python3 -c "from petlib import bindings"
install -m644 %oname/__pycache__/*.so \
	%buildroot%python3_sitelibdir/%oname/__pycache__/
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.40-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.23-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.23-alt1.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.23-alt1
- Version 0.0.23

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus

