%define oname entrypoint2
%def_with check
%define _unpackaged_files_terminate_build 1

Name: python3-module-%oname
Version: 1.1
Release: alt1

Summary: easy to use command-line interface for Python modules
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/entrypoint2
VCS: https://github.com/click-contrib/click-plugins
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
entrypoint2 is an easy to use argparse based command-line interface for python
modules. It translates function signature and documentation to argparse
configuration.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements-test.txt

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/entrypoint2/examples 

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Tue Dec 12 2023 Mikhail Chernonog <snowmix@altlinux.org> 1.1-alt1
- Initial build for Sisyphus
