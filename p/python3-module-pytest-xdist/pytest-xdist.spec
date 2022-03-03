%define _unpackaged_files_terminate_build 1
%define oname pytest-xdist

%def_with check

Name: python3-module-%oname
Version: 2.5.0
Release: alt1

Summary: pytest xdist plugin for distributed testing and loop-on-failing modes
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pytest-dev/pytest-xdist.git
Url: https://pypi.org/project/pytest-xdist/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools_scm
%if_with check
BuildRequires: /dev/pts
# install_requires=
BuildRequires: python3(execnet)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_forked)

# optional
BuildRequires: python3(psutil)
BuildRequires: python3(pexpect)

BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%py3_provides %oname
%py3_provides pytest_xdist
%py3_requires pytest-forked

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

%description
%overview

%prep
%setup
%patch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr

%files
%doc CHANGELOG.rst LICENSE README.rst example
%python3_sitelibdir/xdist/
%python3_sitelibdir/pytest_xdist-%version-py%_python3_version.egg-info/

%changelog
* Mon Feb 28 2022 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.1.0 -> 2.5.0.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 1.29.0 -> 2.1.0.
- Stopped Python2 package build(Python2 EOL).

* Wed Apr 29 2020 Stanislav Levin <slev@altlinux.org> 1.29.0-alt3
- Fixed FTBFS.

* Fri Dec 06 2019 Stanislav Levin <slev@altlinux.org> 1.29.0-alt2
- Fixed testing against Pytest 5.3+.

* Tue Aug 13 2019 Stanislav Levin <slev@altlinux.org> 1.29.0-alt1
- 1.27.0 -> 1.29.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 1.27.0-alt2
- Fixed testing against Pytest 5.

* Tue Mar 26 2019 Stanislav Levin <slev@altlinux.org> 1.27.0-alt1
- 1.26.1 -> 1.27.0.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1.26.1-alt1
- 1.26.0 -> 1.26.1.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 1.26.0-alt1
- 1.25.0 -> 1.26.0.

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

