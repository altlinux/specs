%define _unpackaged_files_terminate_build 1
%define pypi_name usort
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.3
Release: alt1.1
Summary: A small, safe import sorter
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/usort
Vcs: https://github.com/facebook/usort
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-attrs
BuildRequires: python3-module-click
BuildRequires: python3-module-libcst
BuildRequires: python3-module-moreorless
BuildRequires: python3-module-stdlibs
BuildRequires: python3-module-trailrunner
%endif

%description
usort is a safe, minimal import sorter. Its primary goal is to make no
"dangerous" changes to code. This is achieved by detecting distinct "blocks" of
imports that are the most likely to be safely interchangeable, and only
reordering imports within these blocks without altering formatting. Code style
is left as an exercise for linters and formatters.

%package -n %pypi_name
Summary: Executable for %pypi_name
Group: Development/Python3
Requires: %name

%description -n %pypi_name
%summary

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
%pyproject_run -- python3 -m %mod_name.tests -v

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests/

%files -n %pypi_name
%_bindir/%pypi_name

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt1.1
- Demodernized packaging.

* Tue Feb 10 2026 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.1.0 -> 1.1.3.

* Thu Dec 11 2025 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 1.0.8.post1 -> 1.1.0.

* Wed Feb 19 2025 Stanislav Levin <slev@altlinux.org> 1.0.8.post1-alt1
- 1.0.7 -> 1.0.8.post1.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 1.0.7-alt1
- 1.0.6 -> 1.0.7.

* Wed May 10 2023 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1
- 1.0.5 -> 1.0.6.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1
- 1.0.2 -> 1.0.5.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2.

* Thu Feb 10 2022 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
