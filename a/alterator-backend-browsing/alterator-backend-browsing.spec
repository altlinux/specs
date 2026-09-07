%define _unpackaged_files_terminate_build 1
%define shortname browsing

Name: alterator-backend-%{shortname}
Version: 0.1.0
Release: alt1

Summary: Alterator backend for browsing components and applications
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-backend-browsing

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator rpm-build-pyproject
BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-hatchling

Requires: alterator-interface-%{shortname} = %EVR
Requires: python3-module-alterator-backend-browsing = %EVR
Requires: alterator-module-executor >= 0.1.29
Requires: alt-components-base >= 0.10.9

%description
%summary.

%package -n python3-module-alterator-backend-browsing
Summary: Python module for alterator browsing backend
Group: Development/Python3
Requires: python3-module-dbus

%description -n python3-module-alterator-backend-browsing
%summary.

%package -n alterator-interface-%{shortname}
Summary: D-Bus and Polkit interface for alterator browsing backend
Group: System/Configuration/Other

%description -n alterator-interface-%{shortname}
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

install -d %buildroot%_alterator_libdir/backends
install -p -m 755 backend/browsing.py %buildroot%_alterator_libdir/backends/browsing

install -d %buildroot%_alterator_datadir/backends
install -p -m 644 backend/browsing.backend %buildroot%_alterator_datadir/backends/

install -d %buildroot%_datadir/dbus-1/interfaces
install -d %buildroot%_datadir/polkit-1/actions

install -p -m 644 interface/org.altlinux.alterator.*.xml \
    %buildroot%_datadir/dbus-1/interfaces/

install -p -m 644 interface/org.altlinux.alterator.*.policy \
    %buildroot%_datadir/polkit-1/actions/

%files
%_alterator_libdir/backends/browsing
%_alterator_datadir/backends/browsing.backend

%files -n python3-module-alterator-backend-browsing
%python3_sitelibdir/browsing_backend/
%python3_sitelibdir/alterator_backend_browsing-*.dist-info/

%files -n alterator-interface-%{shortname}
%_datadir/dbus-1/interfaces/org.altlinux.alterator.*.xml
%_datadir/polkit-1/actions/org.altlinux.alterator.*.policy
%doc docs/*.md


%changelog
* Mon Aug 24 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.0-alt1
- First build.
