%define _unpackaged_files_terminate_build 1
%define pypi_name pycodestyle

%def_with check

Name: python3-module-%pypi_name
Version: 2.12.1
Release: alt1

Summary: Python style guide checker
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pycodestyle/
Vcs: https://github.com/pycqa/pycodestyle
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

mv %buildroot%_bindir/pycodestyle{,.py3}

%check
%pyproject_run_pytest -ra tests

%files
%doc README.rst LICENSE CONTRIBUTING.rst CHANGES.txt
%_bindir/pycodestyle.py3
%python3_sitelibdir/pycodestyle.py
%python3_sitelibdir/__pycache__/pycodestyle.cpython-*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 12 2024 Stanislav Levin <slev@altlinux.org> 2.12.1-alt1
- 2.12.0 -> 2.12.1.

* Mon Jun 17 2024 Stanislav Levin <slev@altlinux.org> 2.12.0-alt1
- 2.11.1 -> 2.12.0.

* Wed Feb 07 2024 Anton Zhukharev <ancieg@altlinux.org> 2.11.1-alt1
- Updated to 2.11.1.
- Distributed under MIT license.

* Mon Aug 14 2023 Stanislav Levin <slev@altlinux.org> 2.11.0-alt1
- 2.10.0 -> 2.11.0.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.10.0-alt1
- 2.9.1 -> 2.10.0.

* Mon Oct 03 2022 Stanislav Levin <slev@altlinux.org> 2.9.1-alt2
- Modernized packaging.

* Sun Oct 02 2022 Anton Zhukharev <ancieg@altlinux.org> 2.9.1-alt1
- 2.8.0 -> 2.9.1.

* Wed Jan 26 2022 Stanislav Levin <slev@altlinux.org> 2.8.0-alt1
- 2.7.0 -> 2.8.0.

* Tue Apr 20 2021 Stanislav Levin <slev@altlinux.org> 2.7.0-alt1
- 2.6.0 -> 2.7.0.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.5.0 -> 2.6.0.

* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.5.0-alt2
- Build for python2 disabled.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Fri Oct 26 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt1
- Initial build for ALT.
