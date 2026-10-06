%define _unpackaged_files_terminate_build 1

Name: python3-module-yara-python

Version: 4.5.5
Release: alt1

Summary: The Python interface for YARA
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/yara-python/
Vcs: https://github.com/VirusTotal/yara-python

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libyara-devel
BuildRequires: python3-dev
%pyproject_builddeps_build

%description
With this library you can use YARA from your Python programs.
It covers all YARA's features, from compiling, saving and
loading rules to scanning files, strings and processes.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build --backend-config-settings \
	'{"--build-option": ["build", "--dynamic-linking"]}'

%install
%pyproject_install

%check
%pyproject_run_pytest tests.py

%files
%doc README.rst LICENSE
%python3_sitelibdir/yara.cpython-*.so
%python3_sitelibdir/%{pyproject_distinfo yara_python}

%changelog
* Tue Oct 06 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 4.5.5-alt1
- Initial build for Sisyphus.

