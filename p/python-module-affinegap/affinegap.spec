%define oname affinegap

%def_with python3

Name: python-module-%oname
Version: 1.10
Release: alt2.1
Summary: A Cython implementation of the affine gap string distance
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/affinegap/

# https://github.com/datamade/affinegap.git
Source0: https://pypi.python.org/packages/d7/f6/3e188daf864cffb526a786f81112bdb42dab94cd19513d8196389bf484f3/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Cython libnumpy-devel python-module-nose
BuildRequires: python-module-html5lib python-module-notebook python-module-numpy-testing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Cython libnumpy-py3-devel python3-module-nose
BuildRequires: python3-module-html5lib python3-module-notebook python3-module-numpy-testing
%endif

%py_provides %oname
%py_requires numpy


%description
A Cython implementation of the affine gap penalty string distance also
known as the Smith-Waterman algorithm.

%package -n python3-module-%oname
Summary: A Cython implementation of the affine gap string distance
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy

%description -n python3-module-%oname
A Cython implementation of the affine gap penalty string distance also
known as the Smith-Waterman algorithm.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
#cython affinegap/affinegap.pyx
%python_build_debug

%if_with python3
pushd ../python3
#cython3 affinegap/affinegap.pyx
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
python setup.py test build_ext -i
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test build_ext -i
nosetests3 -v
popd
%endif

%files
#doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
#doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10-alt2
- Updated build dependencies

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150304.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt1.git20150304.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150304
- Version 1.1

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141119
- Initial build for Sisyphus

