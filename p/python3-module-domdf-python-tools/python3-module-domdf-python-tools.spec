%define _unpackaged_files_terminate_build 1
%define pypi_name domdf-python-tools
%define mod_name domdf_python_tools

# some tests are broken
# see: https://github.com/domdfcoding/domdf_python_tools/issues/82
%def_without check

Name: python3-module-%pypi_name
Version: 3.7.0
Release: alt1

Summary: Helpful functions for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/domdf-python-tools/
Vcs: https://github.com/domdfcoding/domdf_python_tools

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-test
BuildRequires: python3-module-pandas
%endif

%description
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH="%buildroot%python3_sitelibdir"
%__python3 -m pytest -vra -Wignore --import-mode=append

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 3.7.0-alt1
- Updated to 3.7.0.

* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 3.6.1-alt1
- Updated to 3.6.1.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 3.4.0-alt1
- initial build for Sisyphus

