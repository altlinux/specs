%define _unpackaged_files_terminate_build 1
%define pypi_name ufmt

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt2

Summary: Safe, atomic formatting with black and usort
License: MIT
Group: Development/Python3
# Source-git: https://github.com/omnilib/ufmt.git
Url: https://pypi.org/project/ufmt

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)
BuildRequires: python3(black)
BuildRequires: python3(moreorless)
BuildRequires: python3(tomlkit)
BuildRequires: python3(trailrunner)
BuildRequires: python3(usort)

%if_with check
# install_requires=
BuildRequires: python3(click)
BuildRequires: python3(typing_extensions)
# marked as install_requires but is used only in tests
BuildRequires: python3(libcst)
%endif

BuildArch: noarch

%description
%pypi_name is a safe, atomic code formatter for Python built on top of black and
usort. %pypi_name formats files in-memory, first with usort and then with black,
before writing any changes back to disk. This enables a combined, atomic step
in CI/CD workflows for checking or formatting files, without any with conflict
or intermediate changes between the import sorter and the code formatter.

%package -n %pypi_name
Summary: Executable for %pypi_name
Group: Development/Python3
Requires: %name

%description -n %pypi_name
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm -r %buildroot%python3_sitelibdir/%pypi_name/tests/

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -m %pypi_name.tests -v
EOF
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/ufmt/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %pypi_name
%_bindir/%pypi_name

%changelog
* Wed Nov 16 2022 Michael Shigorin <mike@altlinux.org> 2.0.1-alt2
- Fix BR: requisite for %%build, not just %%check.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 1.3.2 -> 2.0.1.

* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
