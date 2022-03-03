%define _unpackaged_files_terminate_build 1
%define oname pytest-forked

%def_with check

Name: python3-module-%oname
Version: 1.4.0
Release: alt1

Summary: pytest plugin for running tests in isolated forked subprocesses
License: MIT
Group: Development/Python3
# Source-git: https://github.com/pytest-dev/pytest-forked.git
Url: https://pypi.org/project/pytest-forked/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm

%if_with check
# install_requires=
BuildRequires: python3(py)
BuildRequires: python3(pytest)

BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%py3_provides %oname

%description
%summary.

%prep
%setup
%autopatch -p1

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
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export TOXENV=py3

tox.py3 --sitepackages --console-scripts -vvr

%files
%doc LICENSE CHANGELOG.rst README.rst
%python3_sitelibdir/pytest_forked/
%python3_sitelibdir/pytest_forked-%version-py%_python3_version.egg-info/

%changelog
* Mon Feb 28 2022 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.0 -> 1.4.0.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.1.3 -> 1.3.0.
- Stopped Python2 package build(Python2 EOL).

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
