%define oname wheel

%def_with python3

Name: python-module-%oname
Version: 0.29.0
Release: alt1.1
Summary: A built-package format for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/wheel/
Packager: Python Development Team <python@packages.altlinux.org>

# Source-url: https://bitbucket.org/pypa/wheel/get/%version.tar.gz
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-module-jsonschema python-module-keyring python-module-pytest-cov python-module-pyxdg python-module-setuptools
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-keyring python-module-pyxdg
#BuildPreReq: python-module-jsonschema
#python-module-ed25519ll
#BuildPreReq: python-module-pytest python-module-coverage
#BuildPreReq: python-module-pytest-cov python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jsonschema python3-module-keyring python3-module-pytest-cov python3-module-pyxdg python3-module-setuptools
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-keyring python3-module-pyxdg
#BuildPreReq: python3-module-ed25519ll python3-module-jsonschema
#BuildPreReq: python3-module-jsonschema
#BuildPreReq: python3-module-pytest python3-module-coverage
#BuildPreReq: python3-module-pytest-cov python3-module-py
%endif

%py_provides %oname

%description
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A built-package format for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A wheel is a ZIP-format archive with a specially formatted filename and
the .whl extension. It is designed to contain all the files for a PEP
376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked
archive preserves enough information to "Spread" (copy data and scripts
to their final locations) at any later time.

This package contains tests for %oname.

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
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.29.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 0.29.0-alt1
- New version 0.29.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.24.0-alt2
- cleanup buildreq

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.0-alt1
- Initial build for Sisyphus
