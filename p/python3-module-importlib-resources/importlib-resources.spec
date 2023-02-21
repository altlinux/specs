%define _unpackaged_files_terminate_build 1
%define pypi_name importlib-resources

%def_with check

Name: python3-module-%pypi_name
Version: 5.12.0
Release: alt1
Summary: Read resources from Python packages
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/importlib-resources
VCS: https://github.com/python/importlib_resources.git
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

%py3_provides %pypi_name
Provides: python3-module-importlib_resources = %EVR

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools-scm)

%if_with check
BuildRequires: python3(test)
BuildRequires: python3(pytest)
%endif

%description
%pypi_name is a backport of Python standard library importlib.resources
module for older Pythons.

The key goal of this module is to replace parts of pkg_resources with a solution
in Python's stdlib that relies on well-defined APIs. This makes reading
resources included in packages easier, with more stable and consistent
semantics.

%prep
%setup
%autopatch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

# don't ship tests
rm -r %buildroot%python3_sitelibdir/importlib_resources/tests/

%check
%pyproject_run_pytest -vra

%files
%doc README.rst
%python3_sitelibdir/importlib_resources/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 21 2023 Stanislav Levin <slev@altlinux.org> 5.12.0-alt1
- 5.10.2 -> 5.12.0.

* Fri Jan 27 2023 Stanislav Levin <slev@altlinux.org> 5.10.2-alt1
- 5.10.1 -> 5.10.2.

* Wed Dec 07 2022 Stanislav Levin <slev@altlinux.org> 5.10.1-alt1
- 5.10.0 -> 5.10.1.

* Mon Oct 10 2022 Stanislav Levin <slev@altlinux.org> 5.10.0-alt1
- 5.9.0 -> 5.10.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 5.9.0-alt1
- Restored back for Sisyphus.
