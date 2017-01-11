%define _unpackaged_files_terminate_build 1
%define mname coveralls
%define oname z4r-%mname

%def_with python3

Name: python-module-%oname
Version: 2.9.0
Release: alt1
Summary: Python interface to coveralls.io API
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/python-coveralls/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/z4r/python-coveralls.git
Source0: https://pypi.python.org/packages/a7/75/c07d88092ad2eeab254abd86c526c5577365be22f8927e9215970973ed6e/python-coveralls-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-yaml python-module-requests
#BuildPreReq: python-module-coverage python-module-six
#BuildPreReq: python-module-sh python-module-pytest-pep8
#BuildPreReq: python-module-pytest-cov python-module-httpretty
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-yaml python3-module-requests
#BuildPreReq: python3-module-coverage python3-module-six
#BuildPreReq: python3-module-sh python3-module-pytest-pep8
#BuildPreReq: python3-module-pytest-cov python3-module-httpretty
%endif

%py_provides %mname z4r_%mname
Conflicts: python-module-%mname < %EVR
Conflicts: python-module-%mname > %EVR
Provides: python-module-%mname = %EVR
%py_requires yaml requests coverage six sh

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-pytest-cache python-module-requests python-module-rlcompleter2 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-tools-pep8 python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ndg-httpsclient python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-pytest-cache python3-module-pytest-pep8 python3-module-requests python3-module-setuptools python3-module-sh python3-module-urllib3
BuildRequires: python-module-pytest-cov python-module-pytest-pep8 python-module-setuptools-tests python-module-sh python-module-yaml python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-pytest-cov python3-module-setuptools-tests python3-module-unittest2 python3-module-yaml python3-tools-pep8 rpm-build-python3

%description
This package provides a module to interface with the https://coveralls.io
API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pytest_pep8 pytest_cov httpretty

%description tests
This package provides a module to interface with the https://coveralls.io
API.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python interface to coveralls.io API
Group: Development/Python3
%py3_provides %mname z4r_%mname
Conflicts: python3-module-%mname < %EVR
Conflicts: python3-module-%mname > %EVR
Provides: python3-module-%mname = %EVR
%py3_requires yaml requests coverage six sh

%description -n python3-module-%oname
This package provides a module to interface with the https://coveralls.io
API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pytest_pep8 pytest_cov httpretty

%description -n python3-module-%oname-tests
This package provides a module to interface with the https://coveralls.io
API.

This package contains tests for %oname.

%prep
%setup -q -n python-coveralls-%{version}

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.4-alt1.git20141111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.4-alt1.git20141111.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt1.git20141111
- Initial build for Sisyphus

