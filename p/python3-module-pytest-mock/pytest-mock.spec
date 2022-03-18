%define _unpackaged_files_terminate_build 1
%define oname pytest-mock

%def_with check

Name: python3-module-%oname
Version: 3.7.0
Release: alt2

Summary: Thin-wrapper around the mock package for easier use with py.test
License: MIT
Group: Development/Python3
# https://github.com/pytest-dev/pytest-mock.git
Url: https://pypi.org/project/pytest-mock/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires=
BuildRequires: python3(pytest)

BuildRequires: python3(pytest-asyncio)
BuildRequires: python3(tox)
%endif

%py3_provides %oname

BuildArch: noarch
%description
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

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
export PIP_NO_INDEX=YES
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc LICENSE *.rst
%python3_sitelibdir/pytest_mock/
%python3_sitelibdir/pytest_mock-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 18 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt2
- Fixed FTBFS (Pytest 7.1.1).

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.5.1 -> 3.7.0.

* Mon Apr 19 2021 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 3.3.1 -> 3.5.1.

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 1.10.4 -> 3.3.1.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.10.4-alt2
- Added missing dep on Pytest.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.10.4-alt1
- 1.10.1 -> 1.10.4.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 1.10.1-alt1
- 1.10.0 -> 1.10.1.

* Sun Oct 21 2018 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0.

* Thu Apr 12 2018 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.6.2 -> 1.9.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.2-alt1
- Updated to upstream version 1.6.2.

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux Sisyphus.
