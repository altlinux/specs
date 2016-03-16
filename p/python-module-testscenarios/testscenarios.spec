%define oname testscenarios

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.1.1
Summary: Testscenarios, a pyunit extension for dependency injection
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/testscenarios/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pbr python-module-testtools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pbr python3-module-testtools
%endif

%py_provides %oname
%py_requires pbr testtools

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-extras python-module-linecache2 python-module-mimeparse python-module-pbr python-module-pyasn1 python-module-serial python-module-setuptools python-module-six python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-pytest python-module-testtools python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-pytest python3-module-unittest2 rpm-build-python3

%description
testscenarios provides clean dependency injection for python unittest
style tests. This can be used for interface testing (testing many
implementations via a single test suite) or for classic dependency
injection (provide tests with dependencies externally to the test code
itself, allowing easy testing in different situations).

%package -n python3-module-%oname
Summary: Testscenarios, a pyunit extension for dependency injection
Group: Development/Python3
%py3_provides %oname
%py3_requires pbr testtools

%description -n python3-module-%oname
testscenarios provides clean dependency injection for python unittest
style tests. This can be used for interface testing (testing many
implementations via a single test suite) or for classic dependency
injection (provide tests with dependencies externally to the test code
itself, allowing easy testing in different situations).

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
python -m testtools.run -v testscenarios.test_suite
#if_with python3
%if 0
pushd ../python3
python3 -m testtools.run -v testscenarios.test_suite
popd
%endif

%files
%doc Apache-2.0 BSD COPYING GOALS HACKING NEWS README doc
%doc AUTHORS ChangeLog
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc Apache-2.0 BSD COPYING GOALS HACKING NEWS README doc
%doc AUTHORS ChangeLog
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

