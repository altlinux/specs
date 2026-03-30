%define _unpackaged_files_terminate_build 1
%define pypi_name portalocker
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.2.0
Release: alt2.1
Summary: An easy library for Python file locking
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/portalocker/
Vcs: https://github.com/wolph/portalocker.git

BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%EVR.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-portalocker
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mypy
BuildRequires: python3-module-pytest-rerunfailures
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-redis
%endif

%description
Portalocker is a library to provide an easy API to file locking.

An easy library for Python file locking. It works on Windows, Linux, BSD and
Unix systems and can even perform distributed locking. Naturally it also
supports the with statement.

An important detail to note is that on Linux and Unix systems the locks are
advisory by default. By specifying the -o mand option to the mount command it is
possible to enable mandatory file locking on Linux. This is generally not
recommended however.

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
%pyproject_run_pytest -vra -o=addopts=''

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt2.1
- Demodernized packaging.

* Tue Aug 12 2025 Stanislav Levin <slev@altlinux.org> 3.2.0-alt2
- Fixed FTBFS (setuptools-scm 9.1.1).

* Mon Jun 16 2025 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 3.1.1 -> 3.2.0.

* Tue Jan 14 2025 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1
- 2.7.0 -> 3.1.1.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 2.7.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Thu Aug 17 2023 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus.
