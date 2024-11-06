%define import_path github.com/fluent/fluentd-forwarder

Name: fluent-forwarder
Version: 0.0.1.0.46.b7c3
Release: alt2

Summary: A lightweight Fluentd forwarder written in Go

License: Apache-2.0
Group: Monitoring
Url: https://github.com/fluent/fluentd-forwarder
Vcs: git://github.com/fluent/fluentd-forwarder.git

Source0: %name-%version.tar
Source1: vendor.tar
Patch0: fluent-forwarder-0.0.1.46.b7c3-fix-td-client-go.patch
Patch1: fluent-forwarder-0.0.1.46.b7c3-support-int64-timestamps.patch

BuildRequires(pre): rpm-build-golang

%description
%summary.

%package -n golang-github-fluent-fluentd-forwarder
Summary: Development files for %name
Group: Development/Other
BuildArch: noarch

%description -n golang-github-fluent-fluentd-forwarder
The package provides development files for %name.

%prep
%setup -a1
%patch0 -p1
%patch1 -p1
# vendor requires
rm -rf vendor/src/github.com/ugorji/go/codec/test.py
mkdir -p vendor/src/github.com/fluent/ && cd vendor/src/github.com/fluent/
ln -s ../../../.. fluentd-forwarder

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$PWD/vendor"
export GOFLAGS="-mod=vendor"
export GO111MODULE=off
%golang_prepare

pushd entrypoints/dummy_td_server
go build -ldflags '-s -w' -o $BUILDDIR/dummy_td_server main.go
popd

pushd entrypoints/fluentd_forwarder
go build -ldflags '-s -w' -o $BUILDDIR/fluentd_forwarder signal.go main.go
popd

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path"
%golang_install
install -Dm755 .build/dummy_td_server %buildroot%_bindir
install -Dm755 .build/fluentd_forwarder %buildroot%_bindir

%files
%doc LICENSE README.md
%_bindir/fluentd_forwarder
%_bindir/dummy_td_server

%files -n golang-github-fluent-fluentd-forwarder
%go_path/src/%import_path

%changelog
* Wed Nov 06 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1.0.46.b7c3-alt2
- Fixed decoding of timestamp field.

* Fri Oct 25 2024 Leontiy Volodin <lvol@altlinux.org> 0.0.1.0.46.b7c3-alt1
- Initial build for ALT Sisyphus (0.0.1-46-gb7c3958).
- Built for fluent-bit.
