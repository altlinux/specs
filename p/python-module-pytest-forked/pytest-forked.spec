%define _unpackaged_files_terminate_build 1
%define oname pytest-forked

%def_with check

Name: python-module-%oname
Version: 1.1.3
Release: alt1

Summary: pytest plugin for running tests in isolated forked subprocesses
License: MIT
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest-forked.git
Url: https://pypi.org/project/pytest-forked/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools_scm
BuildRequires: python3-module-setuptools_scm

%if_with check
BuildRequires: python-module-pycmd
BuildRequires: python-module-pytest
BuildRequires: python3-module-pycmd
BuildRequires: python3-module-tox
%endif

BuildArch: noarch
%py_provides %oname

%description
%summary.

%package -n python3-module-%oname
Summary: pytest plugin for running tests in isolated forked subprocesses
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
%summary.

%prep
%setup
%autopatch -p1

rm -rf ../python3
cp -fR . ../python3

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
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py%{python_version_nodots python}: _PYTEST_BIN=%_bindir\/py.test\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c \#!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}

tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE CHANGELOG README.rst
%python_sitelibdir/pytest_forked/
%python_sitelibdir/pytest_forked-*.egg-info/

%files -n python3-module-%oname
%doc LICENSE CHANGELOG README.rst
%python3_sitelibdir/pytest_forked/
%python3_sitelibdir/pytest_forked-*.egg-info/

%changelog
* Thu May 07 2020 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.0.2 -> 1.1.3.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2
- Fixed testing against Pytest 5.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2.

* Wed Jan 16 2019 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 0.2 -> 1.0.1.

* Fri Apr 13 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- Initial build for ALT.
