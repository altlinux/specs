%global import_path github.com/json_exporter
%define mod json_exporter

Name:    prometheus-json_exporter
Version: 0.7.0
Release: alt3

Summary: A prometheus exporter which scrapes remote JSON by JSONPath
License: Apache-2.0
Group:   Other
Url:     https://github.com/prometheus-community/json_exporter

Source: %mod-%version.tar
Source1: vendor.tar
Source2: %name.sysconfig
Source3: %name.service

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires(pre): prometheus-common

%description
A prometheus exporter which scrapes remote JSON by JSONPath.

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
mkdir -p %buildroot%_sharedstatedir/prometheus/json-exporter

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md examples
%_bindir/*
%_unitdir/%name.*
%dir %attr(0775,root,prometheus) %_sharedstatedir/prometheus/json-exporter
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Sun Aug 24 2025 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt3
- Removed socket file, fixed service file (ALT #54679).
- Set program version.

* Sun May 25 2025 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt2
- Added systemd units.
- Added examples.

* Mon May 05 2025 Anton Meleshnikov <alton@altlinux.org> 1:3.9.1-alt1

* Thu May 15 2025 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
