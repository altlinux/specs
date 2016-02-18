%define oname port-for

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20140827.1
Summary: Utility that helps with local TCP ports managment
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/port-for/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kmike/port-for.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-mock
#BuildPreReq: python-tools-2to3
%endif

%py_provides port_for

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-funcsigs python-module-pbr python-module-pluggy python-module-py python-module-setuptools python-module-six python-module-unittest2 python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-setuptools python3-module-six python3-module-unittest2 xz
BuildRequires: python-module-mock python-module-pytest python3-module-html5lib python3-module-mock python3-module-pytest rpm-build-python3 time

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
%py3_provides port_for

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
py.test-%_python3_version port_for/*.py
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20140827.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20140827
- Initial build for Sisyphus

