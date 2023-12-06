%define _unpackaged_files_terminate_build 1
%define pypi_name Flake8-pyproject
%define mod_name flake8p

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.3
Release: alt1

Summary: Flake8 plug-in loading the configuration from pyproject.toml
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flake8-pyproject/
Vcs: https://github.com/john-hen/Flake8-pyproject

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
Provides: python3-module-%{pep503_name %pypi_name}
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check
%endif

%description
%summary.

Flake8 cannot be configured via pyproject.toml, even though virtually
all other Python dev tools have adopted it as the central location for
project configuration. The discussion of the original proposal was
closed as "too heated", subsequent feature and pull requests were
marked as "spam".

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc ReadMe.md license.txt
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Dec 06 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.3-alt1
- Built for ALT Sisyphus.

