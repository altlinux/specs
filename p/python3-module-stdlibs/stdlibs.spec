%define _unpackaged_files_terminate_build 1
%define pypi_name stdlibs

%def_with check

Name: python3-module-%pypi_name
Version: 2023.11.2
Release: alt1

Summary: List of packages in the stdlib
License: MIT
Group: Development/Python3
# Source-git: https://github.com/jreese/stdlibs.git
Url: https://pypi.org/project/stdlibs

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

BuildArch: noarch

%description
Simple list of top-level packages in Python's stdlib.

Note: If you only need the live module names on 3.10+, just use
sys.stdlib_module_names. This is not exactly a backport, but a static list of
those for most useful Python versions.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# don't package tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -m stdlibs.tests -v
EOF
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/stdlibs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 09 2023 Stanislav Levin <slev@altlinux.org> 2023.11.2-alt1
- 2022.10.9 -> 2023.11.2.

* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 2022.10.9-alt1
- 2022.6.8 -> 2022.10.9.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 2022.6.8-alt1
- 2022.3.16 -> 2022.6.8.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 2022.3.16-alt1
- 2022.2.2 -> 2022.3.16.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 2022.2.2-alt1
- Initial build for Sisyphus.
