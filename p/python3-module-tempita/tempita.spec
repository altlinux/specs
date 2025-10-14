%define _unpackaged_files_terminate_build 1
%define pypi_name tempita
%define module_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt1

Summary: Tempita is a small templating language for text substitution
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Tempita/
Vcs: https://github.com/TurboGears/tempita

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Tempita is a small templating language for Python, designed for situations
where string template and percent-style formatting are too limited. It
provides basic control structures like if, for, and template inheritance, while
maintaining a simple syntax. Tempita supports both text and HTML templates,
including automatic HTML escaping.

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
%__python3 tests/runtests.py

%files
%doc LICENSE README.rst
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Aug 07 2025 Maxim Tulskiy <tulskijms@altlinux.org> 0.6.0-alt1
- Initial build for ALT Sisyphus.
