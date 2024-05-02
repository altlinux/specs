%define _unpackaged_files_terminate_build 1
%define pypi_name dunamai

%def_with check

Name: python3-module-%{pypi_name}
Version: 1.21.0
Release: alt1

Summary: Dynamic version generation
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dunamai/
Vcs: https://github.com/mtkennerly/dunamai
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: git-core
%endif

%description
Dunamai is a Python library and command line tool for producing dynamic,
standards-compliant version strings, derived from tags in your version control
system. This facilitates uniquely identifying nightly or per-commit builds in
continuous integration and releasing new versions of your software simply by
creating a tag.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
%pyproject_run_pytest -v \
--deselect=tests/integration/test_dunamai.py::test__version__from_git__shallow

%files
%doc README.*
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 02 2024 Anton Kurachenko <srebrov@altlinux.org> 1.21.0-alt1
- New version 1.21.0.

* Thu Apr 18 2024 Anton Kurachenko <srebrov@altlinux.org> 1.20.0-alt1
- New version 1.20.0.

* Sat Mar 09 2024 Anton Kurachenko <srebrov@altlinux.org> 1.19.2-alt1
- Initial build for Sisyphus.
