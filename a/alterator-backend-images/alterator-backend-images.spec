%define _unpackaged_files_terminate_build 1
%define shortname images

Name: alterator-backend-%{shortname}
Version: 0.1.0
Release: alt1

Summary: Alterator backends for managing container images
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-backend-containers

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator rpm-build-pyproject rpm-macros-systemd
BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-hatchling
BuildRequires: gettext-tools

Requires: alterator-interface-%{shortname} = %EVR
Requires: python3-module-alterator-backend-images = %EVR
Requires: alterator-module-executor >= 0.1.29
Requires: alterator-entry >= 0.2.0
Requires: podman
Requires: shadow-submap
Requires: shadow-utils
%systemd_requires

%description
%summary.

%package -n python3-module-alterator-backend-images
Summary: Python module for alterator container images backend
Group: Development/Python3
Requires: python3-module-podman-py

%description -n python3-module-alterator-backend-images
%summary.

%package -n alterator-interface-%{shortname}
Summary: D-Bus and Polkit interface for container images backend
Group: System/Configuration/Other

%description -n alterator-interface-%{shortname}
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
%find_lang %name

install -d %buildroot%_alterator_libdir/backends
install -p -m 755 backend/images.py %buildroot%_alterator_libdir/backends/images

install -d %buildroot%_alterator_datadir/backends
install -p -m 644 backend/images.backend %buildroot%_alterator_datadir/backends/

install -d %buildroot%_datadir/dbus-1/interfaces
install -d %buildroot%_datadir/polkit-1/actions

install -p -m 644 interface/org.altlinux.alterator.*.xml \
    %buildroot%_datadir/dbus-1/interfaces/

install -p -m 644 interface/org.altlinux.alterator.*.policy \
    %buildroot%_datadir/polkit-1/actions/

install -d %buildroot%_unitdir
install -p -m 644 systemd/alterator-podman@.socket \
    %buildroot%_unitdir/
install -p -m 644 systemd/alterator-podman@.service \
    %buildroot%_unitdir/

%post
if sd_booted; then
    systemctl daemon-reload ||:
fi

%postun
if sd_booted; then
    systemctl daemon-reload ||:
fi

%files -f %name.lang
%_alterator_libdir/backends/images
%_alterator_datadir/backends/images.backend
%_unitdir/alterator-podman@.socket
%_unitdir/alterator-podman@.service

%files -n python3-module-alterator-backend-images
%python3_sitelibdir/images_backend/
%python3_sitelibdir/alterator_backend_images-*.dist-info/

%files -n alterator-interface-%{shortname}
%_datadir/dbus-1/interfaces/org.altlinux.alterator.*.xml
%_datadir/polkit-1/actions/org.altlinux.alterator.*.policy
%doc docs/*.md


%changelog
* Fri Nov 13 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.0-alt1
- Init build.

