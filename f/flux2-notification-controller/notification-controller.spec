%define prog_name notification-controller
%global import_path github.com/fluxcd/%prog_name

Name:       flux2-%prog_name
Version:    1.8.0
Release:    alt1
Summary:    Flux event forwarder and notification dispatcher
Group:      System/Configuration/Other
License:    Apache-2.0
Url:        https://github.com/fluxcd/notification-controller

Source0:    %name-%version.tar
Source1:    vendor.tar

Patch0: fix-receiver-handler-test-32bit.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang >= 1.26
BuildRequires: /proc

%description
Event forwarder and notification dispatcher for
the GitOps Toolkit controllers.
The notification-controller is an implementation of the
notification.toolkit.fluxcd.io API based on the specifications
described in the RFC.

%prep
%setup -a 1
%patch0 -p1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
export TAGS="netgo,osusergo"
LDFLAGS="-w" %golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
export CGO_ENABLED=0
# Skip internal/controller: it needs envtest (kube-apiserver and etcd binaries)
# The GCR receiver test validates its token against oauth2.googleapis.com
%gotest -tags "netgo,osusergo" \
    -skip "^Test_handlePayload$/^CEL_filtering_a_GCR_receiver$" \
    $(go list -tags "netgo,osusergo" ./... | grep -vE '/internal/controller$')

%files
%_bindir/%prog_name
%doc README.md CHANGELOG.md LICENSE
%doc docs/spec/v1

%changelog
* Wed Oct 14 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.8.0-alt1
- New version 1.8.0.
- Set CGO_ENABLED=0.
- Enable tests.
- Fix import_path.

* Wed Feb 18 2026 Aleksandr Gamzin <gamzin@altlinux.org> 1.7.5-alt1
- 1.7.5.

* Sat Nov 02 2024 Alexey Kostarev <kaf@altlinux.org> 1.3.0-alt1
- Initial build.
