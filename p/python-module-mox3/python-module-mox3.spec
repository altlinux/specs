%global pypi_name mox3

%def_with python3

Name:           python-module-%pypi_name
Version:        0.8.0
Release:        alt1.1
Summary:        Mock object framework for Python
License:        Apache-2.0
Group:		Development/Python
Url:            http://www.openstack.org/
Source:         %name-%version.tar
Patch: mox3-alt-requirements.patch
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-extras python-module-fixtures python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-linecache2 python-module-markupsafe python-module-mccabe python-module-mimeparse python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-pytest python-module-pytz python-module-requests python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-subunit python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-discover python3-module-docutils python3-module-enum34 python3-module-extras python3-module-fixtures python3-module-flake8 python3-module-genshi python3-module-hacking python3-module-jinja2 python3-module-linecache2 python3-module-markupsafe python3-module-mccabe python3-module-mimeparse python3-module-ndg-httpsclient python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-pytz python3-module-requests python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx_rtd_theme python3-module-subunit python3-module-testtools python3-module-traceback2 python3-module-unittest2 python3-module-urllib3 python3-module-yieldfrom.http.client python3-pyflakes python3-tools-pep8 xz
BuildRequires: git-core python-module-alabaster python-module-coverage python-module-d2to1 python-module-discover python-module-docutils python-module-html5lib python-module-objects.inv python-module-oslosphinx python-module-setuptools-tests python-module-testrepository python3-module-coverage python3-module-d2to1 python3-module-html5lib python3-module-jinja2-tests python3-module-oslosphinx python3-module-setuptools-tests python3-module-sphinx python3-module-testrepository python3-module-yieldfrom.urllib3 rpm-build-python3 time

#BuildRequires:  python-devel git
#BuildRequires:  python-module-pbr python-module-sphinx-devel
#BuildRequires:  python-module-oslosphinx
#BuildRequires:  python-module-setuptools-tests
#BuildPreReq: python-module-fixtures python-module-testtools
#BuildPreReq: python-module-mimeparse python-module-extras
#BuildPreReq: python-module-testrepository python-module-subunit
#BuildPreReq: python-module-discover python-module-coverage
#BuildPreReq: python-module-hacking python-module-d2to1
#BuildPreReq: python-module-flake8 pyflakes python-tools-pep8
#BuildPreReq: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:  python3-devel
#BuildRequires:  python3-module-pbr
#BuildRequires:  python3-module-setuptools-tests
#BuildPreReq: python3-module-fixtures python3-module-testtools
#BuildPreReq: python3-module-mimeparse python3-module-extras
#BuildPreReq: python3-module-testrepository python3-module-subunit
#BuildPreReq: python3-module-discover python3-module-coverage
#BuildPreReq: python3-module-hacking python3-module-d2to1
#BuildPreReq: python3-module-flake8 python3-pyflakes python3-tools-pep8
#BuildPreReq: python3-module-oslosphinx python3-module-sphinx
#BuildPreReq: python3-module-requests
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

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

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
py.test-%_python3_version
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

