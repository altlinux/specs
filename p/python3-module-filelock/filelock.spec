%define _unpackaged_files_terminate_build 1
%define pypi_name filelock

%def_with check

Name: python3-module-%pypi_name
Version: 3.9.0
Release: alt1
Summary: A platform independent file lock for Python
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/filelock/
VCS: https://github.com/tox-dev/py-filelock
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-vcs)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%prep
%setup

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

%check
%pyproject_run_pytest -vra tests

%files
%doc README.md
%python3_sitelibdir/filelock/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.8.2 -> 3.9.0.

* Tue Dec 06 2022 Stanislav Levin <slev@altlinux.org> 3.8.2-alt1
- 3.8.1 -> 3.8.2.

* Mon Dec 05 2022 Stanislav Levin <slev@altlinux.org> 3.8.1-alt1
- 3.8.0 -> 3.8.1.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 3.8.0-alt1
- 3.6.0 -> 3.8.0.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.4.2 -> 3.6.0.

* Wed Jan 12 2022 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1
- 3.3.2 -> 3.4.2.

* Tue Nov 02 2021 Stanislav Levin <slev@altlinux.org> 3.3.2-alt1
- 3.3.1 -> 3.3.2.

* Mon Oct 25 2021 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.0.10 -> 3.3.1.

* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.10-alt2
- Drop python2 support.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.0.10-alt1
- 3.0.9 -> 3.0.10.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 3.0.9-alt1
- Initial build.

