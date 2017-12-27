%define _unpackaged_files_terminate_build 1
%define oname rlr

%def_with python3

Name: python-module-%oname
Version: 2.4.3
Release: alt1
Summary: Regularized Logistic Regression
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/rlr/

# https://github.com/datamade/rlr.git
Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-Cython libnumpy-devel python-module-nose python-module-numpy-testing
BuildRequires: python-module-pylbfgs python2.7(future)
BuildRequires: python-module-html5lib python-module-notebook
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-Cython libnumpy-py3-devel python3-module-nose python3-module-numpy-testing
BuildRequires: python3-module-pylbfgs python3(future)
BuildRequires: python3-module-html5lib python3-module-notebook
%endif

%py_provides %oname
%py_requires numpy pylbfgs

%description
A Cython implementation of L2 regularized logistic regression.

%if_with python3
%package -n python3-module-%oname
Summary: Regularized Logistic Regression
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy pylbfgs

%description -n python3-module-%oname
A Cython implementation of L2 regularized logistic regression.
%endif

%prep
%setup -n %oname-%version

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

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py build_ext -i
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
nosetests3 -v
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.3-alt1
- Updated to upstream version 2.4.3.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20150507.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20150507.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5-alt1.git20150507.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20150507
- Version 1.5

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141119
- Initial build for Sisyphus

