%global import_path github.com/ncabatoff/process-exporter

Name:    process-exporter
Version: 0.8.7
Release: alt1

Summary: Prometheus exporter that mines /proc to report on selected processes
License: MIT
Group:   Monitoring
Url:     https://github.com/ncabatoff/process-exporter

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1
subst '/\/default/d' ./packaging/%name.service

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/integration-tester ./cmd/load-generator ./cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
install -D -m0644 ./packaging/%name.service %buildroot%_unitdir/%name.service
install -D -m0644 ./packaging/default/%name \
%buildroot%_sysconfdir/sysconfig/%name
install -D -m0644 ./packaging/conf/all.yaml \
%buildroot%_sysconfdir/%name/all.yaml

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%files
%doc *.md LICENSE
%_bindir/integration-tester
%_bindir/load-generator
%_bindir/process-exporter
%config(noreplace) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service

%changelog
* Mon Dec 22 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.8.7-alt1
- Initial build for Sisyphus.
