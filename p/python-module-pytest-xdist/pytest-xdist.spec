%define _unpackaged_files_terminate_build 1
%define oname pytest-xdist

%def_with check

Name: python-module-%oname
Version: 1.25.0
Release: alt1

Summary: pytest xdist plugin for distributed testing and loop-on-failing modes
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest-xdist.git
Url: https://pypi.python.org/pypi/pytest-xdist

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm
%if_with check
BuildRequires: /dev/pts
BuildRequires: pytest
BuildRequires: python-module-tox
BuildRequires: python-module-pycmd
BuildRequires: python-module-pytest-forked
BuildRequires: python-module-pexpect
BuildRequires: python-module-execnet
BuildRequires: pytest3
BuildRequires: python3-module-tox
BuildRequires: python3-module-pycmd
BuildRequires: python3-module-pytest-forked
BuildRequires: python3-module-pexpect
BuildRequires: python3-module-execnet
%endif

%add_python3_req_skip execnet

%define overview							 \
The pytest-xdist plugin extends py.test with some unique test execution  \
modes:                                                                   \
									 \
* test run parallelization: if you have multiple CPUs or hosts you can   \
  use those for a combined test run. This allows to speed up development \
  or to use special resources of remote machines.			 \
* --boxed: (not available on Windows) run each test in a boxed		 \
  subprocess to survive SEGFAULTS or otherwise dying processes		 \
* --looponfail: run your tests repeatedly in a subprocess. After each	 \
  run py.test waits until a file in your project changes and then	 \
  re-runs the previously failing tests. This is repeated until all tests \
  pass after which again a full run is performed.			 \
* Multi-Platform coverage: you can specify different Python interpreters \
  or different platforms and run tests in parallel on all of them.	 \
									 \
%nil

BuildArch: noarch
%py_provides %oname
%py_requires pytest-forked

%description %overview
%package -n python3-module-%oname
Summary: py.test xdist plugin for distributed testing and loop-on-failing modes
Group: Development/Python3
%py3_provides %oname
%py3_requires pytest-forked

%description -n python3-module-%oname
%overview

%prep
%setup

cp -a . ../python3

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build

pushd ../python3
%python3_build
popd

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install

pushd ../python3
%python3_install
popd

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_INDEX_URL=http://host.invalid./

# copy nessecary exec deps
tox --sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/py.cleanup .tox/py%{python_version_nodots python}/bin/
cp -f %_bindir/pytest .tox/py%{python_version_nodots python}/bin/

export PYTHONPATH=`pwd`
TOX_TESTENV_PASSENV='PYTHONPATH' tox --sitepackages -e \
py%{python_version_nodots python} -v -- -v

pushd ../python3

# copy nessecary exec deps
tox.py3 --sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/py.cleanup.py3 \
.tox/py%{python_version_nodots python3}/bin/py.cleanup
cp -f %_bindir/pytest3 .tox/py%{python_version_nodots python3}/bin/pytest

export PYTHONPATH=`pwd`
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 --sitepackages -e \
py%{python_version_nodots python3} -v -- -v
popd

%files
%doc CHANGELOG.rst LICENSE README.rst example
%python_sitelibdir/xdist/
%python_sitelibdir/pytest_xdist-*.egg-info/

%files -n python3-module-%oname
%doc CHANGELOG.rst LICENSE README.rst example
%python3_sitelibdir/xdist/
%python3_sitelibdir/pytest_xdist-*.egg-info/

%changelog
* Wed Dec 19 2018 Stanislav Levin <slev@altlinux.org> 1.25.0-alt1
- 1.23.2 -> 1.25.0.

* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 1.23.2-alt1
- 1.22.5 -> 1.23.2.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 1.22.5-alt1
- 1.22.2 -> 1.22.5.

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.22.2-alt2
- rebuild with python3.6

* Fri Apr 13 2018 Stanislav Levin <slev@altlinux.org> 1.22.2-alt1
- 1.11 -> 1.22.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt1.hg20140924.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.hg20140924
- Initial build for Sisyphus

