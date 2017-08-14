%define oname port-for

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1
Summary: Utility that helps with local TCP ports managment
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/port-for/

# https://github.com/kmike/port-for.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch
BuildArch: noarch

BuildRequires: python-module-mock python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-mock python3-module-pytest
%endif

%description
port-for is a command-line utility and a python library that helps with
local TCP ports management.

It can find an unused TCP localhost port and remember the association.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
port-for is a command-line utility and a python library that helps with
local TCP ports management.

It can find an unused TCP localhost port and remember the association.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Utility that helps with local TCP ports managment
Group: Development/Python3

%description -n python3-module-%oname
port-for is a command-line utility and a python library that helps with
local TCP ports management.

It can find an unused TCP localhost port and remember the association.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
port-for is a command-line utility and a python library that helps with
local TCP ports management.

It can find an unused TCP localhost port and remember the association.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1

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
	2to3 -w -n $i
	mv $i $i.py3
done
popd
%endif

%python_install

%check
py.test port_for/*.py
%if_with python3
pushd ../python3
py.test3 port_for/*.py
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
* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4-alt1
- Updated to upstream version 0.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20140827.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20140827.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20140827
- Initial build for Sisyphus

