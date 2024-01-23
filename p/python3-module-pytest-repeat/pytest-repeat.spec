%define oname pytest-repeat
%define _unpackaged_files_terminate_build 1
%def_with check

Name: python3-module-%oname
Version: 0.9.3
Release: alt1
Summary: pytest plugin for repeating tests
License: MPL-2.0 
Group: Development/Python3
Url: https://pypi.org/project/pytest-repeat/
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description 
pytest-repeat is a plugin for py.test that makes it easy
to repeat a single test, or multiple tests, a specific number of times.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files 
%doc CHANGES.rst  LICENSE README.rst
%python3_sitelibdir/pytest_repeat.py*
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Mon Jan 22 2024 Mikhail Chernonog <snowmix@altlinux.org> 0.9.3-alt1
- 0.9.1 -> 0.9.3

* Wed Mar 31 2021 Mikhail Chernonog <snowmix@altlinux.org> 0.9.1-alt1
- 0.8.0 -> 0.9.1
- Fixed testing

* Thu Mar 07 2019 Mikhail Chernonog <snowmix@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
