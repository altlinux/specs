%define _unpackaged_files_terminate_build 1

%define oname setuptools_scm
%def_with check

Name: python3-module-%oname
Version: 6.4.2
Release: alt1
Summary: The blessed package to manage your versions by scm tags
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/setuptools-scm/

# https://github.com/pypa/setuptools_scm.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires
BuildRequires: python3(packaging)
BuildRequires: python3(setuptools)
BuildRequires: python3(tomli)

BuildRequires: git-core
BuildRequires: mercurial
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%py3_provides setuptools-scm
Requires: git-core mercurial
%py3_requires packaging
%py3_requires setuptools
%py3_requires tomli

%description
setuptools_scm is a simple utility for the setup_requires feature of
setuptools for use in Mercurial and Git based projects.

It uses metadata from the SCM to generate the version of a project and
is able to list the files belonging to that project (which makes the
MANIFEST.in file unnecessary in many cases).

It falls back to PKG-INFO/.hg_archival.txt when necessary.

%prep
%setup
%patch1 -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_build_debug

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export TESTS_NO_NETWORK=1
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='TESTS_NO_NETWORK'
export TOXENV=py%{python_version_nodots python3}-test
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc *.rst
%python3_sitelibdir/setuptools_scm/
%python3_sitelibdir/setuptools_scm-%version-py%_python3_version.egg-info/

%changelog
* Fri Jan 21 2022 Stanislav Levin <slev@altlinux.org> 6.4.2-alt1
- 6.3.2 -> 6.4.2.

* Mon Oct 25 2021 Stanislav Levin <slev@altlinux.org> 6.3.2-alt2
- Fixed FTBFS (setuptools 58.3.0).

* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 6.3.2-alt1
- 6.0.1 -> 6.3.2.

* Sun Apr 18 2021 Stanislav Levin <slev@altlinux.org> 6.0.1-alt1
- 4.1.2 -> 6.0.1.

* Mon Oct 05 2020 Stanislav Levin <slev@altlinux.org> 4.1.2-alt1
- 3.5.0 -> 4.1.2.

* Wed Feb 19 2020 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 3.3.3 -> 3.5.0.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 3.3.3-alt2
- Fixed testing against Pytest 5.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 3.3.3-alt1
- 2.1.0 -> 3.3.3.

* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Updated to upstream version 2.1.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.15.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 01 2017 Michael Shigorin <mike@altlinux.org> 1.15.0-alt1.1
- R: git-core instead of full-blown git metapackage
- fix build --with python3 (actually the test)

* Mon Jan 02 2017 Anton Midyukov <antohami@altlinux.org> 1.15.0-alt1
- Version 1.15.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.0-alt1.git20150812.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.0-alt1.git20150812.1
- NMU: Use buildreq for BR.

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1.git20150812
- Version 1.7.0

* Sun Jul 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20150723
- Version 1.6.0

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus

