Name: bluehood
Version: 0.7.1
Release: alt1

Summary: Monitor your local neighbourhood's bluetooth activity
License: MIT
Group: Monitoring

Url: https://github.com/dannymcc/bluehood
Vcs: https://github.com/dannymcc/bluehood

Requires: python3-module-mac-vendor-lookup

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel jsonnet

BuildArch: noarch
ExcludeArch: %ix86
AutoProv: nopython3

Source: %name-%version.tar

%description
Bluetooth Neighborhood - Track BLE devices in your area and analyze traffic patterns.

%package -n grafana-dashboards-bluehood
Summary: The set of Grafana dashboard for monitoring purposes
Group: Monitoring
Requires: %name = %EVR
Provides: bluehood-grafana-dashboards = %EVR
%description -n grafana-dashboards-bluehood
This package provides Grafana dashboard for monitoring of BlueHood.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
install -d %buildroot%_sysconfdir/grafana/dashboards/%name-dashboard/
cp -a grafana/*.json %buildroot%_sysconfdir/grafana/dashboards/%name-dashboard/

%files
%doc LICENSE README.md
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/%{name}-*

%files -n grafana-dashboards-bluehood
%_sysconfdir/grafana/dashboards/%name-dashboard/

%changelog
* Thu Jun 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- automatic build: 0.7.0 -> 0.7.1

* Mon Apr 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- 0.6.0 -> 0.7.0

* Sat Feb 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- 0.3.5 -> 0.6.0
- added subpackage grafana-dashboards-bluehood
- excludearch: %%ix86

* Sat Feb 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.3.5-alt1
- Initial build for ALT Linux.

