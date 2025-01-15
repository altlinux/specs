%define _unpackaged_files_terminate_build 1
%define pypi_name portalocker
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.1
Release: alt1
Summary: An easy library for Python file locking
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/portalocker/
Vcs: https://github.com/wolph/portalocker.git

BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%EVR.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
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
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

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
* Tue Jan 14 2025 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1
- 2.7.0 -> 3.1.1.

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 2.7.0-alt1.1
- NMU: added missing build dependency on setuptools.

* Thu Aug 17 2023 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus.
