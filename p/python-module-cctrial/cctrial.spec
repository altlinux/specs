%define oname cctrial

%def_with python3

Name: python-module-%oname
Version: 1.2.0
Release: alt1.git20150814.1.1
Summary: Continous trial runner
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cctrial
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tardyp/cctrial.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-twisted-core-test python-module-argh
#BuildPreReq: python-module-watchdog
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-twisted-core-test python3-module-argh
#BuildPreReq: python3-module-watchdog
%endif

%py_provides %oname
Requires: python-module-twisted-core-test
%py_requires argh watchdog

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-OpenSSL python-module-argh python-module-cffi python-module-cryptography python-module-enum34 python-module-pathtools python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-serial python-module-setuptools python-module-six python-module-twisted-core python-module-yaml python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-enum34 python3-module-pathtools python3-module-pycparser python3-module-setuptools python3-module-yaml python3-module-zope.interface
BuildRequires: python-module-setuptools-tests python-module-twisted-core-test python-module-twisted-logger python-module-watchdog python3-module-cryptography python3-module-pygobject3 python3-module-pytest python3-module-serial python3-module-watchdog python3-module-zope rpm-build-python3 time

%description
cctrial is a tool for using twisted trial in a continuous manner.

cctrial will re-run failed tests until all succeed.

cctrial is designed for a specific workflow, which helps doing big
refactors that break lots of tests.

cctrial smart mode can run only the tests that import the modified file.

cctrial is not designed to replace trial, for all other usecases.

%if_with python3
%package -n python3-module-%oname
Summary: Continous trial runner
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-twisted-core-test
%py3_requires argh watchdog

%description -n python3-module-%oname
cctrial is a tool for using twisted trial in a continuous manner.

cctrial will re-run failed tests until all succeed.

cctrial is designed for a specific workflow, which helps doing big
refactors that break lots of tests.

cctrial smart mode can run only the tests that import the modified file.

cctrial is not designed to replace trial, for all other usecases.
%endif

%prep
%setup

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test -v
py.test -vv %oname/*.py
#if_with python3
%if 0
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv %oname/*.py
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.git20150814.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.git20150814.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20150814
- Initial build for Sisyphus

