%define mname coveralls
%define oname z4r-%mname

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.9.1
Release: alt3.1
Summary: Python interface to coveralls.io API
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/python-coveralls/

# https://github.com/z4r/python-coveralls.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-module-pytest-cov python-module-pytest-pep8 python-module-setuptools python-module-sh
BuildRequires: python-module-yaml
BuildRequires: python-module-httpretty python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-pytest-cov
BuildRequires: python3-module-setuptools python3-module-unittest2 python3-module-yaml python3-tools-pep8
BuildRequires: python3-module-httpretty python3-module-requests
%endif

%py_provides %mname z4r_%mname
Conflicts: python-module-%mname < %EVR
Conflicts: python-module-%mname > %EVR
Provides: python-module-%mname = %EVR
%py_requires yaml requests coverage six sh

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
%setup
%patch1 -p1

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.9.1-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.1-alt3
- Fixed build.
- Disabled tests.

* Tue Oct 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.1-alt2
- Fixed build with new setuptools.

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.1-alt1
- Updated to upstream release 2.9.1.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.4-alt1.git20141111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.4-alt1.git20141111.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.4-alt1.git20141111
- Initial build for Sisyphus

