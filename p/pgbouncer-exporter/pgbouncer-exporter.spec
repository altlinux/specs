%define _unpackaged_files_terminate_build 1
%define import_path github.com/prometheus-community/pgbouncer_exporter

Name: pgbouncer-exporter
Version: 0.12.1
Release: alt1

Summary: Prometheus exporter for PgBouncer
License: Apache-2.0
Group: Monitoring
URL: https://github.com/prometheus-community/pgbouncer_exporter

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %name.conf
Source3: %name.service

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.2
BuildRequires: systemd

%description
Prometheus exporter for PgBouncer.

The exporter connects to PgBouncer and exposes PgBouncer
statistics as Prometheus metrics.

%prep
%setup -q -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%{_libdir}/gocode"
export GOFLAGS="-mod=vendor"
export CGO_ENABLED=0

%golang_prepare

cd "$BUILDDIR/src/%import_path"
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%{_libdir}/gocode"
export IGNORE_SOURCES=1

%golang_install

install -d %buildroot%_sysconfdir/%name
install -m 0600 %SOURCE2 \
    %buildroot%_sysconfdir/%name/config

install -d %buildroot%_unitdir
install -m 0644 %SOURCE3 \
    %buildroot%_unitdir/%name.service

install -d %buildroot%_localstatedir/%name

%pre
/usr/sbin/groupadd -r -f %name 2>/dev/null || :
/usr/sbin/useradd -r -g %name \
    -d %_localstatedir/%name \
    -s /usr/sbin/nologin \
    -c "Prometheus PgBouncer Exporter" \
    %name 2>/dev/null || :

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE
%_bindir/pgbouncer_exporter
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config
%_unitdir/%name.service
%dir %_localstatedir/%name

%changelog
* Fri Aug 28 2026 Olesya Shuster <lesyafox@altlinux.org> 0.12.1-alt1
- Initial build for Sisyphus
