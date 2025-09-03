%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-flake8
%define mod_name pytest_flake8

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Pytest plugin to run flake8

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-flake8/
Vcs: https://github.com/coherent-oss/pytest-flake8

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools_scm
%if_with check
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%python3_sitelibdir_noarch/%mod_name.py
%python3_sitelibdir_noarch/__pycache__/%mod_name.*
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}/

%changelog
* Tue Aug 26 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.3.0-alt1
- Built for sisyphus again (New version 1.3.0).

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1
- 1.0.7 -> 1.1.1.

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
