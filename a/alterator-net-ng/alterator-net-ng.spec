%define _unpackaged_files_terminate_build 1


Name: alterator-net-ng
Version: 0.2.0
Release: alt2

Summary: Backend-agnostic alterator module for network configuration
License: GPLv3
Group: System/Configuration/Other

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-alterator

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-yaml
BuildRequires: alterator guile-devel

Requires: alterator alterator-l10n
Requires: alterator-python-functions python3-module-%name = %EVR

%description
Alterator module for network configuration (similar to net-eth), independent of used network subsystem.
It's planned to support following subsystems: Netplan, systemd-networkd, NetworkManager, ifupdown2.

%package -n python3-module-%name
Summary: Python module for %name
Group: Development/Other

BuildArch: noarch

Requires: udev
Requires: python3-module-yaml

%description -n python3-module-%name
%summary.

%prep
%setup -q

%build
%make_build
%pyproject_build

%check
%pyproject_run_pytest

%install
%makeinstall
%pyproject_install

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_backend3dir/*
%_alterator_libdir/ui/*

%files -n python3-module-%name
%python3_sitelibdir_noarch/alterator_net_ng/
%python3_sitelibdir_noarch/alterator_net_ng-*dist-info/
%doc README.md

%changelog
* Thu Apr 02 2026 Sergey Konev <darisishe@altlinux.org> 0.2.0-alt2
- Use text-wrap for Routes page notes labels (Closes: 58490)

* Fri Mar 27 2026 Sergey Konev <darisishe@altlinux.org> 0.2.0-alt1
- Networkd configs support
- Routing table support
- Clean out configs of other subsystems before apply

* Wed Feb 25 2026 Sergey Konev <darisishe@altlinux.org> 0.1.0-alt2
- Add clear error message when no network subsystem selected (Closes: 57992)

* Sun Dec 28 2025 Sergey Konev <darisishe@altlinux.org> 0.1.0-alt1
- Initial Build
