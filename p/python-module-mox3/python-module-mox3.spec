%global pypi_name mox3

%def_with python3

Name: python-module-%pypi_name
Version: 0.20.0
Release: alt1.1
Summary: Mock object framework for Python
License: Apache-2.0
Group: Development/Python
Url: http://docs.openstack.org/developer/%pypi_name
Source: https://tarballs.openstack.org/%pypi_name/%pypi_name-%version.tar.gz

BuildArch:      noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel
BuildRequires: python-module-pbr python-module-sphinx-devel
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-setuptools
BuildRequires: python-module-fixtures python-module-testtools
BuildRequires: python-module-mimeparse python-module-extras
BuildRequires: python-module-testrepository python-module-subunit-tests
BuildRequires: python-module-discover python-module-coverage
BuildRequires: python-module-hacking python-module-d2to1
BuildRequires: python-module-flake8 pyflakes python-tools-pep8
BuildRequires: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-pbr
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-fixtures python3-module-testtools
BuildRequires: python3-module-mimeparse python3-module-extras
BuildRequires: python3-module-testrepository python3-module-subunit-tests
BuildRequires: python3-module-discover python3-module-coverage
BuildRequires: python3-module-hacking python3-module-d2to1
BuildRequires: python3-module-flake8 python3-pyflakes python3-tools-pep8
BuildRequires: python3-module-oslosphinx python3-module-sphinx
BuildRequires: python3-module-requests
%endif

%description
Mox3 is an unofficial port of the Google mox framework
(http://code.google.com/p/pymox/) to Python 3. It was meant to be as compatible
with mox as possible, but small enhancements have been made. The library was
tested on Python version 3.2, 2.7 and 2.6.

%package tests
Summary: Tests for %pypi_name
Group: Development/Python
Requires: %name = %EVR

%description tests
Mox3 is an unofficial port of the Google mox framework
(http://code.google.com/p/pymox/) to Python 3. It was meant to be as compatible
with mox as possible, but small enhancements have been made. The library was
tested on Python version 3.2, 2.7 and 2.6.

This package contains tests for %pypi_name.

%package pickles
Summary: Pickles for %pypi_name
Group: Development/Python

%description pickles
Mox3 is an unofficial port of the Google mox framework
(http://code.google.com/p/pymox/) to Python 3. It was meant to be as compatible
with mox as possible, but small enhancements have been made. The library was
tested on Python version 3.2, 2.7 and 2.6.

This package contains pickles for %pypi_name.

%package -n python3-module-%pypi_name
Summary: Mock object framework for Python
Group: Development/Python3
%py3_provides %pypi_name

%description -n python3-module-%pypi_name
Mox3 is an unofficial port of the Google mox framework
(http://code.google.com/p/pymox/) to Python 3. It was meant to be as compatible
with mox as possible, but small enhancements have been made. The library was
tested on Python version 3.2, 2.7 and 2.6.

%package -n python3-module-%pypi_name-tests
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: python3-module-%pypi_name = %EVR

%description -n python3-module-%pypi_name-tests
Mox3 is an unofficial port of the Google mox framework
(http://code.google.com/p/pymox/) to Python 3. It was meant to be as compatible
with mox as possible, but small enhancements have been made. The library was
tested on Python version 3.2, 2.7 and 2.6.

This package contains tests for %pypi_name.

%prep
%setup -n %pypi_name-%version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc/source
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
cp -fR build/pickle %buildroot%python_sitelibdir/%pypi_name/
popd

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
rm -fR build
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test3
popd
%endif

%files
%doc COPYING.txt ChangeLog AUTHORS README.rst doc/source/build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%pypi_name
%doc COPYING.txt ChangeLog AUTHORS README.rst doc/source/build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%pypi_name-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.20.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.1
- Added module for Python 3
- Extracted tests into separate packages
- Enabled testing

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.7.0-alt1
- First build for ALT (based on Suse 0.7.0-2.1.src)

