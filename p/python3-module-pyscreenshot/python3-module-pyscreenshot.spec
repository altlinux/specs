%define oname pyscreenshot
%def_without check

Name: python3-module-%oname
Version: 3.1
Release: alt1

Summary: An extension module for click to enable registering CLI commands via setuptools entry-points.
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/click-plugins
VCS: https://github.com/click-contrib/click-plugins.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif


%description
An extension module for click to enable registering CLI commands
via setuptools entry-points.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements-test.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Tue Dec 12 2023 Mikhail Chernonog <snowmix@altlinux.org> 3.1-alt1
- Initial build for Sisyphus
