%global import_path github.com/prometheus/graphite_exporter

Name:           graphite_exporter
Version:        0.16.0
Release:        alt1
Summary:        Server that accepts metrics via the Graphite protocol and exports them as Prometheus metrics

License:        Apache-2.0
Group:          Monitoring
URL:            https://github.com/prometheus/graphite_exporter

Source0:        %name-%version.tar
Source1:        vendor.tar
Source2:        graphite_exporter.service

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libselinux-utils
BuildRequires: libpcre2-devel
BuildRequires: glibc-devel-static

%description
%summary

This exporter accepts metrics in Graphite format over TCP or UDP
and exports them as Prometheus metrics.

%prep
%setup -q -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build cmd/getool cmd/graphite_exporter

#export GO111MODULE=on
#cd cmd/graphite_exporter
#go build -ldflags="-s -w" -o graphite_exporter

%install
export BUILDDIR="$PWD/.build"
%golang_install
install -D -m0644 %SOURCE2 %buildroot%_unitdir/graphite_exporter.service

%post
%systemd_post graphite_exporter.service

%preun
%systemd_preun graphite_exporter.service

%postun
%systemd_postun_with_restart graphite_exporter.service

%files
%doc *.md LICENSE
%_bindir/%name
%_bindir/graphite_exporter
%_unitdir/graphite_exporter.service

%changelog
* Mon Jul 21 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus (thx lesyafox@).
