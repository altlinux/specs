%define _unpackaged_files_terminate_build 1
%define pypi_name python-keycloak
%define mod_name keycloak

Name: python3-module-%pypi_name
Version: 4.2.0
Release: alt2

Summary: Python package providing access to the Keycloak API.
License: MIT
Group: Development/Python3
Url: https://github.com/marcospereirampj/python-keycloak.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

sed -Ei '/^version = /s|= "[0-9.]+"$|= "%version"|' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

rm %buildroot/%python3_sitelibdir/*.md
rm %buildroot/%python3_sitelibdir/LICENSE

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 24 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 4.2.0-alt2
- Fixed packaging files (closes: #50975)

* Mon Jun 24 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 4.2.0-alt1
- Initial build for ALT Linux

