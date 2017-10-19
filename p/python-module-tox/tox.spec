%define _unpackaged_files_terminate_build 1
%define oname tox

Name: python-module-%oname
Version: 2.9.1
Release: alt1%ubt
Summary: virtualenv-based automation of test activities
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tox/

Source0: %name-%version.tar
#fix for https://github.com/tox-dev/tox/issues/655
Patch0: tox-alt-fix-test_pythonpath_usage.patch
#fix for https://github.com/tox-dev/tox/issues/654
Patch1: tox-alt-fix-test_verbosity[-vv].patch
BuildArch: noarch

%py_provides %oname

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-ubt
BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-virtualenv
BuildRequires: python-module-six
BuildRequires: python3-module-six
BuildRequires: python-module-pluggy
BuildRequires: python3-module-pluggy
BuildRequires: python-module-py
BuildRequires: python3-module-py
# requires for tests
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest
BuildRequires: python-module-pytest-cov
BuildRequires: python3-module-pytest-cov
BuildRequires: python-module-pytest-timeout
BuildRequires: python3-module-pytest-timeout
BuildRequires: python-module-pytest-xdist
BuildRequires: python3-module-pytest-xdist
BuildRequires: python-module-pytest-runner
BuildRequires: python3-module-pytest-runner
BuildRequires: python-module-pip
BuildRequires: python3-module-pip
BuildRequires: pytest
BuildRequires: pytest3


%description
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%package -n python3-module-%oname
Summary: virtualenv-based automation of test activities
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Tox as is a generic virtualenv management and test command line tool you
can use for:

* checking your package installs correctly with different Python
  versions and interpreters
* running your tests in each of the environments, configuring your test
  tool of choice
* acting as a frontend to Continuous Integration servers, greatly
  reducing boilerplate and merging CI and shell-based testing.

%prep
%setup
%patch0 -p2
%patch1 -p2
#workaround for https://github.com/tox-dev/tox/issues/651
sed -i 's/^include CHANGELOG$/include CHANGELOG.rst/g' %_builddir/%name-%version/MANIFEST.in
rm -rfv ../python3
cp -a . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
        mv $i $i.py3
done
popd

%python_install

%check
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=%buildroot%python_sitelibdir:%python_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' python setup.py pytest --addopt "--verbose --cov-config=tox.ini --cov=tox --timeout=180"
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir:%python3_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' python3 setup.py pytest --addopt "--verbose --cov-config=tox.ini --cov=tox --timeout=180"
popd

%files
%_bindir/%oname
%_bindir/%oname-quickstart
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py2.?.egg-info

%files -n python3-module-%oname
%_bindir/%oname.py3
%_bindir/%oname-quickstart.py3
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Oct 19 2017 Stanislav Levin <slev@altlinux.org> 2.9.1-alt1%ubt
- Version 2.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1
- Version 1.9.0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1
- Version 1.8.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus

