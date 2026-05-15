%global import_path github.com/kafka_exporter
%define mod kafka_exporter

Name:    prometheus-kafka_exporter
Version: 1.9.0
Release: alt4

Summary: Kafka exporter for Prometheus
License: Apache-2.0
Group:   Other
Url:     https://github.com/danielqsj/kafka_exporter

Source: %mod-%version.tar
Source1: vendor.tar
Source2: %name.sysconfig
Source3: %name.service
Patch1: 0001-Updating-dependencies-to-fix-CVEs.patch
Patch2: 0002-substitute-pkg-errors-by-stdlib-errors.patch
Patch3: 0003-update-go.mod.patch
Patch4: 0004-use-q-instead-s-to-safely-quote-strings.patch
Patch5: 0005-format-code-using-gofumpt-with-no-extra-parameters-j.patch
Patch6: 0006-Update-go-and-IBM-sarama-versions-to-address-CVEs.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.25.8

Requires(pre): prometheus-common

%description
Kafka exporter for Prometheus. For other metrics from Kafka, have a look at the
JMX exporter.

%prep
%setup -n %mod-%version
%autopatch -p1
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
mkdir -p %buildroot%_sharedstatedir/prometheus/kafka-exporter

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md
%_bindir/*
%_unitdir/%name.*
%dir %attr(0775,root,prometheus) %_sharedstatedir/prometheus/kafka-exporter
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Fri May 15 2026 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt4
- Update vendoring libraries (fixes: CVE-2025-22869, CVE-2025-22870,
  CVE-2025-22872, CVE-2025-47914, CVE-2025-58181) and rebuild with new golang.

* Sun Aug 24 2025 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt3
- Removed socket file, fixed service file (ALT #54668).
- Set program version.

* Fri May 30 2025 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt2
- Added systemd units.

* Thu May 15 2025 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus.
