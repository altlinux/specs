%define _unpackaged_files_terminate_build 1
%define pypi_name logistro

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt1

Summary: Wrapper for logging
License: MIT
Group: Development/Python3
Url: https://geopozo.github.io/logistro/
Vcs: https://github.com/geopozo/logistro.git

BuildArch: noarch

Source:  %pypi_name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: logistro-%version-alt-set-starting-version.patch

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%description
Logistro is an extremely light addition to logging, providing sensible
defaults.

It also includes getPipeLogger() which can be passed to Popen() so
that its stderr is piped to the already thread-safe logging library.

%prep
%setup -q -n %pypi_name-%version
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info/
%doc README.md LICENSE

%changelog
* Tue Oct 20 2026 Mikhail Nogin <joycap@altlinux.org> 2.0.1-alt1
- Initial build for ALT Sisyphus.
