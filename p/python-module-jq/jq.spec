%define oname jq

%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt1
Summary: Lightweight and flexible JSON processor
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jq/

# https://github.com/mwilliamson/jq.py.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: libjq-devel
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-Cython python-module-nose
BuildRequires: python-module-tox
BuildRequires: python-module-html5lib python-module-notebook
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-Cython python3-module-nose
BuildRequires: python3-module-tox
BuildRequires: python3-module-html5lib python3-module-notebook
%endif

%py_provides %oname

%description
jq is a lightweight and flexible JSON processor.

This project contains Python bindings for jq.

%if_with python3
%package -n python3-module-%oname
Summary: Lightweight and flexible JSON processor
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
jq is a lightweight and flexible JSON processor.

This project contains Python bindings for jq.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%build
cython jq.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 jq.pyx
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
python setup.py build_ext -i
nosetests tests -v
%if_with python3
pushd ../python3
python3 setup.py test
python3 setup.py build_ext -i
nosetests3 tests -v
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
* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1
- Updated to upstream version 0.1.6.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150118.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150118.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150118
- Initial build for Sisyphus

