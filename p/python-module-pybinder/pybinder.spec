%define oname pybinder

%def_with python3

Name: python-module-%oname
Version: 1.5.1
Release: alt1.git20141209.1.1
Summary: Dependency injection and management tool for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyBinder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rmk135/pybinder.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six python-module-coverage
#BuildPreReq: python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six python3-module-coverage
#BuildPreReq: python3-module-unittest2
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-linecache2 python-module-pytest python-module-setuptools python-module-six python-module-traceback2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-coverage python-module-setuptools-tests python-module-unittest2 python3-module-coverage python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3 time

%description
Dependency injection and management tool for Python.

%package -n python3-module-%oname
Summary: Dependency injection and management tool for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Dependency injection and management tool for Python.

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
./test.sh
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|unit2|unit2.py3|' test.sh
sed -i 's|^coverage|coverage3|' test.sh
./test.sh
popd
%endif

%files
%doc *.md examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.1-alt1.git20141209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.1-alt1.git20141209.1
- NMU: Use buildreq for BR.

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20141209
- Version 1.5.1

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20141130
- Version 1.3.0

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.git20141119
- Version 1.2.4

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.git20141118
- Version 1.2.3

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20141118
- Version 1.2.2

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141116
- Version 1.1.0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20141112
- Initial build for Sisyphus

