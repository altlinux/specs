%global import_path github.com/prometheus-community/prometheus-smartctl_exporter
%define mod smartctl_exporter

Name:    prometheus-smartctl_exporter
Version: 0.14.0
Release: alt1

Summary: Export smartctl statistics to prometheus
License: Apache-2.0
Group:   Other
Url:     https://github.com/prometheus-community/smartctl_exporter

Source: %mod-%version.tar
Source1: vendor.tar
Source2: %name.sysconfig
Source3: %name.service

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: smartmontools

%description
%summary

%prep
%setup -n %mod-%version
tar xf %SOURCE1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
export LDFLAGS="-X github.com/prometheus/common/version.Version=%version \
         -X github.com/prometheus/common/version.Revision=%release \
         -X github.com/prometheus/common/version.Branch=tarball \
         -X github.com/prometheus/common/version.BuildDate=$(date -u +%%Y%%m%%d)"
cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE3 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sharedstatedir/prometheus/smartctl-exporter

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md EXAMPLE.md
%_bindir/*
%_unitdir/%name.*
%dir %attr(0775,root,prometheus) %_sharedstatedir/prometheus/smartctl-exporter
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Fri Oct 24 2025 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus (ALT #56583).
