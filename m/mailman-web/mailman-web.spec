%define pypi_name mailman-web

Name: mailman-web
Version: 0.0.9
Release: alt1
Summary: Django project combining Postorius and HyperKitty

License: GPL-3.0-or-later
Group: Development/Python3
URL: https://gitlab.com/mailman/mailman-web
# Source-url: %__pypi_url mailman_web
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: settings.py.example
Source3: README.ALT

Patch0: mailman-web-django52.patch

BuildArch: noarch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-pdm-backend
Requires: /usr/bin/sassc

%package -n python3-module-mailman-web
Summary: Django settings and URL configuration for Mailman 3
Group: Development/Python3

%description -n python3-module-mailman-web
Default Django settings and URL configuration joining Postorius and HyperKitty.

%description
Mailman 3 Web interface combining list management and mailing list archives.

%prep
%setup
%patch0 -p1
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_sysconfdir/mailman3
touch %buildroot%_sysconfdir/mailman3/settings.py
install -m644 %SOURCE2 %SOURCE3 .

%files
%_bindir/mailman-web
%dir %_sysconfdir/mailman3
%ghost %config(noreplace) %_sysconfdir/mailman3/settings.py
%doc README.ALT settings.py.example

%files -n python3-module-mailman-web
%python3_sitelibdir/mailman_web/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Nov 01 2026 Vitaly Lipatov <lav@altlinux.ru> 0.0.9-alt1
- initial build for ALT Sisyphus

