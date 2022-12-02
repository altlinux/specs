%define _unpackaged_files_terminate_build 1
%define pypi_name trove-classifiers

%def_with check

Name: python3-module-%pypi_name
Version: 2022.12.1
Release: alt1

Summary: Canonical source for classifiers on PyPI
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/trove-classifiers
VCS: https://github.com/pypa/trove-classifiers.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

# PEP503 name
%py3_provides %pypi_name

%description
Canonical source for classifiers on PyPI:
https://pypi.org/classifiers/

Classifiers categorize projects per PEP 301. Use this package to validate
classifiers in packages for PyPI upload or download.

%prep
%setup
%autopatch -p1

# calver doesn't provide means for reproducible builds from source tree
echo '%version' > ./calver_version

%build
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    # keep a synced steps to Makefile:test
    pytest
    python -m tests.lib
EOF
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/trove_classifiers/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 02 2022 Stanislav Levin <slev@altlinux.org> 2022.12.1-alt1
- 2022.10.19 -> 2022.12.1.

* Wed Oct 19 2022 Stanislav Levin <slev@altlinux.org> 2022.10.19-alt1
- 2022.9.26 -> 2022.10.19.

* Tue Sep 27 2022 Stanislav Levin <slev@altlinux.org> 2022.9.26-alt1
- 2022.8.31 -> 2022.9.26.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 2022.8.31-alt1
- 2022.8.7 -> 2022.8.31.

* Thu Aug 11 2022 Stanislav Levin <slev@altlinux.org> 2022.8.7-alt1
- 2022.3.30 -> 2022.8.7.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 2022.3.30-alt1
- Initial build for Sisyphus.
