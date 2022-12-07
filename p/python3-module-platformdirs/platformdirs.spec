%define _unpackaged_files_terminate_build 1
%define pypi_name platformdirs

%def_with check

Name: python3-module-%pypi_name
Version: 2.6.0
Release: alt1

Summary: Determining appropriate platform-specific dirs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/platformdirs
VCS: https://github.com/platformdirs/platformdirs.git

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-vcs)

%if_with check
BuildRequires: python3(appdirs)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
%endif

BuildArch: noarch

%description
A small Python module for determining appropriate platform-specific dirs, e.g.
a "user data dir". When writing desktop application, finding the right location
to store user data and configuration varies per platform. Even for
single-platform apps, there may by plenty of nuances in figuring out the right
location.

%prep
%setup
%autopatch -p1

# hatch-vcs can use setuptools_scm which implements a file_finders entry point
# which returns all files tracked by SCM. Though that is version detection usage
# only (at least for now), it's safer to provide a real git tree.
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

%check
%tox_check_pyproject -- -vra tests

%files
%doc README.rst
%python3_sitelibdir/platformdirs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Dec 07 2022 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1
- 2.5.4 -> 2.6.0.

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 2.5.4-alt1
- 2.5.2 -> 2.5.4.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 2.5.2-alt1
- 2.5.1 -> 2.5.2.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 2.5.1-alt1
- 2.5.0 -> 2.5.1.

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1
- 2.4.1 -> 2.5.0.

* Thu Jan 13 2022 Stanislav Levin <slev@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0.

* Tue Sep 07 2021 Stanislav Levin <slev@altlinux.org> 2.3.0-alt1
- 2.1.0 -> 2.3.0.

* Mon Jul 26 2021 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus.
