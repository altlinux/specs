%global import_path github.com/VictoriaMetrics/operator
%global _unpackaged_files_terminate_build 1

Name:    victoriametrics-operator
Version: 0.68.4
Release: alt1
Summary: Kubernetes operator for Victoria Metrics
License: Apache-2.0
Group:   Other
Url:     https://github.com/VictoriaMetrics/operator

Source:   %name-%version.tar
Source1:  vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-build-golang

BuildRequires: golang >= 1.25.5

%description
Operator serves to make running VictoriaMetrics applications
on top of Kubernetes as easy as possible while preserving
Kubernetes-native configuration options.

%package -n victoriametrics-config-reloader
Summary:  Config reloader for Victoria Metrics
License:  Apache-2.0
Group:    Other

ExcludeArch: %ix86

%description -n victoriametrics-config-reloader
It's alternative version of "prometheus-config-reloader".
The main difference is ability to read secret directly from 
kubernetes and write it to local file system.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

VERSION_STR="operator-%version"

# ldflags existence check
grep -rq "var Version string"; [ $? -ne 0 ] && echo "Version is missing (tune ldflags)" && exit 1

export LDFLAGS="-X github.com/VictoriaMetrics/VictoriaMetrics/lib/buildinfo.Version=${VERSION_STR}"

%golang_prepare
%golang_build ./cmd ./cmd/config-reloader

_BBDIR="$BUILDDIR"/bin
mv "$_BBDIR"/cmd                "$_BBDIR"/vmoperator
mv "$_BBDIR"/config-reloader    "$_BBDIR"/victoria-config-reloader

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md
%_bindir/vmoperator

%files -n victoriametrics-config-reloader
%_bindir/victoria-config-reloader

%changelog
* Thu Oct 29 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.68.4-alt1
- New version 0.68.4.
- New subpackage config-reloader.

* Wed Mar 25 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.68.3-alt1
- Initial build for Sisyphus
