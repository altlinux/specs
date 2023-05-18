%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-shutil
%define mod_name pytest_shutil

%def_with check

Name: python3-module-%pypi_name
Version: 1.7.0
Release: alt5
Summary: A goodie-bag of unix shell and environment tools for py.test
License: MIT
Group: Development/Python
Url: https://pypi.org/project/pytest-shutil/
Vcs: https://github.com/man-group/pytest-plugins
BuildArch: noarch
Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: pytest-shutil-Only-require-contextlib2-on-Python-2.patch
Patch1: Replace-path.py-with-path.patch
Patch2: use-stdlib-unittest.mock-on-python-3.patch
Patch3: Fix-forcing-color-through-termcolor.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
This library is a goodie-bag of Unix shell and environment management tools for
automated tests. A summary of the available functions is below, look at the
source for the full listing.

%prep
%setup -n %pypi_name-%version
%autopatch -p2

# fix dependency
sed -i -e 's:setuptools-git:setuptools:g' \
	common_setup.py

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc CHANGES.md README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 16 2023 Stanislav Levin <slev@altlinux.org> 1.7.0-alt5
- Fixed FTBFS (termcolor 2.3.0).

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 1.7.0-alt4
- Added accidentally removed runtime requirements.

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 1.7.0-alt3
- Stopped build Python2 package.

* Mon May 04 2020 Stanislav Levin <slev@altlinux.org> 1.7.0-alt2
- Fixed FTBFS.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.0 -> 1.7.0.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt2
- Fixed minor typo in tox.ini.

* Fri Mar 22 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.2.11 -> 1.6.0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.11-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.11-alt1
- Initial build for ALT.
