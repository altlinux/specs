%global import_path github.com/prometheus/graphite_exporter
%define oname graphite_exporter

Name:           graphite_exporter
Version:        0.16.0
Release:        alt1.1
Summary:        Server that accepts metrics via the Graphite protocol and exports them as Prometheus metrics

License:        Apache-2.0
Group:          Monitoring
URL:            https://github.com/prometheus/graphite_exporter

Source0:        %name-%version.tar
Source1:        vendor.tar
Source2:        graphite_exporter.service
Source3:        graphite_exporter.sysconfig
Source4:        graphite_exporter.conf

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libselinux-utils
BuildRequires: libpcre2-devel
BuildRequires: glibc-devel-static
BuildRequires: systemd
Requires(pre): systemd

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

%install
export BUILDDIR="$PWD/.build"
%golang_install

install -D -m0644 %SOURCE2 %buildroot%_unitdir/%oname.service
install -D -m0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%oname
install -d %buildroot/var/lib/%oname

%pre
if [ $1 -eq 1 ]; then
    %sysusers_create_package %name %SOURCE4
    echo "User and group 'graphite_exporter' created via sysusers.d"
    echo "Home directory: /var/lib/graphite_exporter"
fi

%post
%systemd_post %oname.service

%preun
%systemd_preun %oname.service

%postun
%systemd_postun_with_restart %oname.service

%files
%doc README.md LICENSE
%_bindir/%name
%_bindir/%oname
%_unitdir/%oname.service
%config(noreplace) %_sysconfdir/sysconfig/%oname
%dir %attr(0755,graphite_exporter,graphite_exporter) /var/lib/%oname

%changelog
* Wed Aug 13 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.16.0-alt1.1
- Added graphite_exporter user creation (closes: #55351).
- Added sysconfig configuration (closes: #55353).

* Mon Jul 21 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus (thx lesyafox@).
