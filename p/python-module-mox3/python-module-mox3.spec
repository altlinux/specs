%global pypi_name mox3

%def_with python3

Name:           python-module-%pypi_name
Version:        0.7.0
Release:        alt1.1
Summary:        Mock object framework for Python
License:        Apache-2.0
Group:		Development/Python
Url:            http://www.openstack.org/
Source:         %name-%version.tar
Patch: mox3-alt-requirements.patch
BuildRequires:  python-devel
BuildRequires:  python-module-pbr
BuildRequires:  python-module-setuptools-tests
BuildPreReq: python-module-fixtures python-module-testtools
BuildPreReq: python-module-mimeparse python-module-extras
BuildPreReq: python-module-testrepository python-module-subunit
BuildPreReq: python-module-discover python-module-coverage
BuildPreReq: python-module-hacking python-module-d2to1
BuildPreReq: python-module-flake8 pyflakes python-tools-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel
BuildRequires:  python3-module-pbr
BuildRequires:  python3-module-setuptools-tests
BuildPreReq: python3-module-fixtures python3-module-testtools
BuildPreReq: python3-module-mimeparse python3-module-extras
BuildPreReq: python3-module-testrepository python3-module-subunit
BuildPreReq: python3-module-discover python3-module-coverage
BuildPreReq: python3-module-hacking python3-module-d2to1
BuildPreReq: python3-module-flake8 python3-pyflakes python3-tools-pep8
%endif
Requires:       python-module-pbr >= 0.5.21

BuildArch:      noarch

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

%package -n python3-module-%pypi_name
Summary: Mock object framework for Python
Group: Development/Python3
Requires: python3-module-pbr >= 0.5.21
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
%setup
%patch -p2

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
rm -fR build
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc COPYING.txt ChangeLog AUTHORS README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%pypi_name
%doc COPYING.txt ChangeLog AUTHORS README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%pypi_name-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.1
- Added module for Python 3
- Extracted tests into separate packages
- Enabled testing

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.7.0-alt1
- First build for ALT (based on Suse 0.7.0-2.1.src)

