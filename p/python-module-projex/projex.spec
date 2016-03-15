%define oname projex

%def_with python3

Name: python-module-%oname
Version: 3.1.4
Release: alt1.git20150205.1
Summary: Library of useful utilities for Python used across various applications
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/projex/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ProjexSoftware/projex.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pycrypto
BuildPreReq: python-modules-logging python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pycrypto
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires logging json Crypto

%description
The projex Python package is a base set of useful methods and utilities
that are shared around the rest of our frameworks.

It has no direct dependencies, as it works on the base Python libs
providing extensions to things like text formatting, sorting,
environment management and document generation.

%package -n python3-module-%oname
Summary: Library of useful utilities for Python used across various applications
Group: Development/Python3
%py3_provides %oname
%py3_requires logging json Crypto

%description -n python3-module-%oname
The projex Python package is a base set of useful methods and utilities
that are shared around the rest of our frameworks.

It has no direct dependencies, as it works on the base Python libs
providing extensions to things like text formatting, sorting,
environment management and document generation.

%prep
%setup


mv src/* ./
sed -i 's|\r||g' projex/scripts/xbuild.py

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
	../python3/projex/scripts/xbuild.py
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
	mv $i ${i}3
done
popd
%endif

%python_install

%check
export LC_ALL=en_US.UTF-8
python setup.py test
py.test -vv $(find projex -name '*.py')
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv $(find projex -name '*.py')
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.4-alt1.git20150205.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt1.git20150205
- Version 3.1.4

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.git20141107
- Initial build for Sisyphus

