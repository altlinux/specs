%define pypi_name hyperkitty

Name: python3-module-hyperkitty
Version: 1.3.12
Release: alt1
Summary: Django web interface for mailing list archives

License: GPL-3.0-or-later
Group: Development/Python3
URL: https://gitlab.com/mailman/hyperkitty
# Source-url: %__pypi_url hyperkitty
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch0: hyperkitty-django52.patch

BuildArch: noarch
# ALT names these flufl.lock and dateutil; their imports generate requirements.
%add_pyproject_deps_runtime_filter 'flufl-lock$' 'python-dateutil$'
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-pdm-backend

%description
A web interface to access GNU Mailman v3 archives.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/hyperkitty/tests

%files
%python3_sitelibdir/hyperkitty/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1.3.12-alt1
- initial build for ALT Sisyphus

