%global import_path github.com/nifi_exporter
Name:    prometheus-nifi_exporter
Version: 0.2.0
Release: alt1

Summary: Apache NiFi metrics exporter for Prometheus
License: Apache-2.0
Group:   Development/Other
URL:     https://github.com/msiedlarek/nifi_exporter
VCS:     https://github.com/msiedlarek/nifi_exporter

Source:  %name-%version.tar
Source1: vendor.tar
Source2: %name.sysconfig
Source3: %name.service
Source4: %name.socket
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
Requires(post): prometheus-common

%description
Exports metrics from Apache NiFi API in Prometheus-compatible format.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -Dm0644 %SOURCE4 %buildroot%_unitdir/%name.socket
mkdir -p %buildroot%_sharedstatedir/prometheus/nifi-exporter

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md
%_bindir/*
%_unitdir/%name.*
%dir %attr(0775,root,prometheus) %_sharedstatedir/prometheus/nifi-exporter
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Wed Jun 10 2026 Kirill Izmestev <felixz@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
