%define _unpackaged_files_terminate_build 1
%define pypi_name backlash
%define module_name %pypi_name

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Backlash is a swiss army knife for web applications debugging
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/backlash/
Vcs: https://github.com/TurboGears/backlash

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Backlash is a web application debugging toolkit featuring an interactive
in-browser debugger (based on a Werkzeug fork for WebOb), crash and slow
request reporting via email and Sentry, originally developed as a WebError
replacement for TurboGears 2.3.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 27 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.4.0-alt1
- Initial build for ALT Sisyphus.
