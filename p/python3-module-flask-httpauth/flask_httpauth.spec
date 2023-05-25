%define _unpackaged_files_terminate_build 1
%def_with check

%define pypi_name flask-httpauth

Name: python3-module-%pypi_name
Version: 4.8.0
Release: alt1

Summary: Simple extension that provides authentication for Flask routes
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-HTTPAuth
Vcs: https://github.com/miguelgrinberg/flask-httpauth
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

# BuildRequires for check
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Simple extension that provides Basic and Digest HTTP
authentication for Flask routes

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README* CHANGES*
%python3_sitelibdir/*

%changelog
* Thu May 25 2023 Alexandr Shashkin <dutyrok@altlinux.org> 4.8.0-alt1
- 4.7.0 -> 4.8.0
- spec: reformat README and CHANGES patterns for doc macro in
  file section
- do not ship MIT license file
- reformat spec file: move some tags
- use rpm-build-pyproject

* Sun Oct 30 2022 Alexandr Shashkin <dutyrok@altlinux.org> 4.7.0-alt1
- Initial build for sisyphus

