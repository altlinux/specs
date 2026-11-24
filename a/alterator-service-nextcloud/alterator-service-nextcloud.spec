%define alterator_service_libexecdir %_prefix/libexec
%define module_name alterator_service_nextcloud
%define _unpackaged_files_terminate_build 1

Name: alterator-service-nextcloud
Version: 0.2
Release: alt1

Summary: Alterator service backend for rootless Nextcloud containers
License: GPLv3
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-service-nextcloud

BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-tomlkit
%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

Requires: python3-module-alterator-service-nextcloud
Requires: alterator-manager
Requires: alterator-module-executor
Requires: alterator-interface-service >= 0.3
Requires: alterator-backend-images
Requires: alterator-service-nextcloud-quadlet
Requires: python3-base
Requires: podman >= 5
Requires: systemd
Requires: systemd-analyze
Requires: control
Requires: util-linux

%description
Alterator service lifecycle backend for a rootless Nextcloud pod with
PostgreSQL and Redis.

%package -n python3-module-alterator-service-nextcloud
Summary: Python module for the Alterator Nextcloud service
Group: Development/Python3

%description -n python3-module-alterator-service-nextcloud
%summary.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install
install -p -m 0750 -D alterator-service-nextcloud \
    %buildroot%alterator_service_libexecdir/alterator-service-nextcloud
install -p -m 0644 -D alterator/service-nextcloud.service \
    %buildroot%_datadir/alterator/services/service-nextcloud.service
install -p -m 0644 -D alterator/service-nextcloud.backend \
    %buildroot%_datadir/alterator/backends/service-nextcloud.backend

%files
%alterator_service_libexecdir/alterator-service-nextcloud
%_datadir/alterator/services/service-nextcloud.service
%_datadir/alterator/backends/service-nextcloud.backend

%files -n python3-module-alterator-service-nextcloud
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %module_name}

%changelog
* Tue Aug 18 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.2-alt1
- Validate cron units only in the standard systemd user unit directory.
- Require image backend provisioning of rootless mapping helpers.

* Mon Aug 17 2026 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial package.
