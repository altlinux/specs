%define _unpackaged_files_terminate_build 1
%define oname pytest-flake8

%def_with check

Name: python3-module-%oname
Version: 1.0.7
Release: alt2
Summary: pytest plugin for efficiently checking PEP8 compliance
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/pytest-flake8

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(flake8)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

# PyPI name(dash, underscore)
%py3_provides %oname
Provides: python3-module-pytest_flake8 = %EVR

%description
pytest plugin for efficiently checking PEP8 compliance
%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc LICENSE CHANGELOG README.rst
%python3_sitelibdir/pytest_flake8-%version-py%_python3_version.egg-info/
%python3_sitelibdir/pytest_flake8.py
%python3_sitelibdir/__pycache__/

%changelog
* Thu Jan 27 2022 Stanislav Levin <slev@altlinux.org> 1.0.7-alt2
- Fixed FTBFS (flake8 4.x).

* Tue Apr 20 2021 Stanislav Levin <slev@altlinux.org> 1.0.7-alt1
- 1.0.6 -> 1.0.7.

* Wed Aug 05 2020 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1
- 1.0.4 -> 1.0.6.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1
- 1.0.3 -> 1.0.4.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1
- 1.0.2 -> 1.0.3.

* Mon Oct 15 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 0.9.1 -> 1.0.2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.1-alt1
- Initial build for ALT.
