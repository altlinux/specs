%define _unpackaged_files_terminate_build 1
%define import_path github.com/enix/x509-certificate-exporter/v4

Name: x509-certificate-exporter
Version: 4.2.0
Release: alt1

Summary: Prometheus exporter for X.509 certificates
License: MIT
Group: Monitoring
URL: https://github.com/enix/x509-certificate-exporter

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %name.conf
Source3: %name.service

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.2
BuildRequires: systemd

%description
Prometheus exporter for monitoring X.509 certificates.
The exporter monitors certificates from files, directories,
Kubernetes Secrets and ConfigMaps and exposes certificate
expiration information as Prometheus metrics.

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
%golang_build ./cmd/x509-certificate-exporter

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%{_libdir}/gocode"
export IGNORE_SOURCES=1

%golang_install

install -d %buildroot%_sysconfdir/%name
install -m 0644 %SOURCE2 \
    %buildroot%_sysconfdir/%name/config.yaml

install -d %buildroot%_unitdir
install -m 0644 %SOURCE3 \
    %buildroot%_unitdir/%name.service

install -d %buildroot%_localstatedir/%name

%pre
/usr/sbin/groupadd -r -f %name 2>/dev/null || :
/usr/sbin/useradd -r -g %name \
    -d %_localstatedir/%name \
    -s /usr/sbin/nologin \
    -c "X.509 Certificate Exporter" \
    %name 2>/dev/null || :
%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE
%_bindir/x509-certificate-exporter
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.yaml
%_unitdir/%name.service
%dir %_localstatedir/%name

%changelog
* Wed Aug 26 2026 Olesya Shuster <lesyafox@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus
