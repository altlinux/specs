%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.vcs
%define pypi_nname jaraco-vcs
%define ns_name jaraco
%define mod_name vcs

%def_with check

Name: python3-module-%pypi_nname
Version: 2.4.1
Release: alt1.2
Summary: Facilities for working with VCS repositories
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco-vcs
Vcs: https://github.com/jaraco/jaraco.vcs
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-jaraco-classes
BuildRequires: python3-module-jaraco-path
BuildRequires: python3-module-jaraco-versioning
BuildRequires: python3-module-more-itertools
BuildRequires: python3-module-packaging
BuildRequires: python3-module-pygments
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-home
BuildRequires: python3-module-python-dateutil
BuildRequires: python3-module-tempora
%endif

# python3.req.py doesn't support namespaces,
# e.g. 'from jaraco import text' gives 'python3(jaraco)'
%add_python3_req_skip jaraco

%description
%summary.

%prep
%setup
%autopatch -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.4.1-alt1.2
- Demodernized packaging.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Wed Mar 05 2025 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1.

* Thu Sep 19 2024 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.1 -> 2.4.0.

* Fri Aug 02 2024 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1
- 2.3.0 -> 2.3.1.

* Mon Jul 29 2024 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.2.0 -> 2.3.0.

* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 2.2.0-alt1
- 2.1.0 -> 2.2.0.

* Tue Apr 23 2024 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.0 -> 2.1.0.

* Thu Mar 14 2024 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.1.0 -> 2.0.0.

* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
