%global import_path github.com/apernet/hysteria/core/v2

%define _pseudouser_group hysteria
%define _pseudouser_user hysteria
%define _pseudouser_home /var/lib/hysteria

# TestResolver requires network
# UDPStress randomly got timeout
%define skip_tests TestResolver|TestClientServerUDPStress

Name: hysteria
Version: 2.9.2
Release: alt1

Summary: Hysteria 2 - A powerful, lightning fast network proxy
License: MIT
Group: Networking/Other
Url: https://v2.hysteria.network
Vcs: https://github.com/apernet/hysteria

Source0: %name-%version.tar
Source1: vendor.tar
Source2: hysteria-server@.service
Source3: hysteria-client@.service
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: python3 python3-module-socks python3-module-flask
BuildRequires: python3-module-requests python3-module-cryptography

ExclusiveArch: %go_arches
ExcludeArch: %ix86

%description
Hysteria is a powerful, lightning fast network proxy built on a modified
QUIC protocol. It is designed to work even under unstable or unreliable
network conditions such as high packet loss, high latency, and limited
bandwidth.

%prep
%setup -a 1
%autopatch -p1
find app/ extras/ -name '*.go' -type f -print0 | xargs -0 sed -i 's/python/python3/g'

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS="\
  -X github.com/apernet/hysteria/app/v2/cmd.appVersion=%{version} \
  -X github.com/apernet/hysteria/app/v2/cmd.appDate=$(date -u +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
  -X github.com/apernet/hysteria/app/v2/cmd.appType=release \
  -X 'github.com/apernet/hysteria/app/v2/cmd.appToolchain=$(go version | sed 's/^go version //')' \
  -X github.com/apernet/hysteria/app/v2/cmd.libVersion=$(awk '/github.com\/apernet\/quic-go/ {print $2}' core/go.mod) \
  -X github.com/apernet/hysteria/app/v2/cmd.appPlatform=linux \
  -X github.com/apernet/hysteria/app/v2/cmd.appArch=$(go env GOARCH)"

export CFLAGS="-g"

%golang_prepare
%golang_build app

%check
for dir in app core extras; do
  (pushd "$dir" && %gotest -skip '%skip_tests' ./... && popd)
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export IGNORE_SOURCES=1
%golang_install
mv %buildroot%_bindir/app %buildroot%_bindir/hysteria

mkdir -p %buildroot%_unitdir
install -m644 %SOURCE2 %buildroot%_unitdir/hysteria-server@.service
install -m644 %SOURCE3 %buildroot%_unitdir/hysteria-client@.service

mkdir -p %buildroot%_sysconfdir/%name

%pre
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'Hysteria daemon' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%files
%_bindir/hysteria
%_unitdir/hysteria-server@.service
%_unitdir/hysteria-client@.service
%dir %attr(755, root, hysteria) %_sysconfdir/%name
%doc README.md

%changelog
* Mon Jun 08 2026 Vladislav Tatjanin <l27001@altlinux.org> 2.9.2-alt1
- Initial build.
- fix(certloader): add SKI, AKI, KeyUsage extensions to test certs.

