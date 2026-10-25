# Upstream pkg/runtimeconfig/config.go converts nanosecond constants to uint;
# these overflow on 32-bit architectures (verified with GOARCH=386).
ExcludeArch: %ix86
Name: tunnel-client
Version: 0.0.18
Release: alt1

Summary: OpenAI tunnel client for private MCP servers
License: Apache-2.0
Group: Networking/Other
URL: https://github.com/openai/tunnel-client
VCS: https://github.com/openai/tunnel-client.git

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %name@.service
Source3: %name.sysconfig
Source4: %name-user@.service

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-macros-systemd >= 6
BuildRequires: golang >= 1.27.3
Requires: ca-certificates
Requires: systemd
Requires(preun): systemd

%description
Tunnel client connects private MCP servers to OpenAI over outbound HTTPS.
The package includes the CLI, its embedded administration UI, and system
and user service templates for running multiple instances.
The optional cloudflared companion is not included.

%prep
%setup -q -a1

%build
export GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off GOWORK=off
export CGO_ENABLED=0
export GOPATH="$PWD/.gopath" GOCACHE="$PWD/.gocache"
go build -mod=vendor -trimpath -buildvcs=false -buildmode=pie \
    -ldflags "-X github.com/openai/tunnel-client/pkg/version.semanticVersion=%version" \
    -o tunnel-client ./cmd/client

%check
export GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off GOWORK=off
export CGO_ENABLED=0
export GOPATH="$PWD/.gopath" GOCACHE="$PWD/.gocache"
go test -mod=vendor -timeout=5m ./...
./tunnel-client --version
./tunnel-client run --help > /dev/null

%install
install -Dpm755 tunnel-client %buildroot%_bindir/tunnel-client
install -Dpm644 %SOURCE2 %buildroot%_unitdir/%name@.service
install -Dpm644 %SOURCE4 %buildroot%_userunitdir/%name@.service
install -Dpm644 %SOURCE3 %buildroot%_datadir/%name/config.example
install -dm750 %buildroot%_sysconfdir/%name
install -pm600 %SOURCE3 %buildroot%_sysconfdir/%name/default
# Preserve dependency license files without shipping the vendored source tree.
mkdir -p vendor-licenses
find vendor -type f \( -iname '*license*' -o -iname '*copying*' -o -iname '*notice*' \) \
    -exec cp --parents '{}' vendor-licenses/ \;

%preun
%systemd_preun %name@.service
%systemd_user_preun %name@.service

%files
%doc LICENSE NOTICE README.md vendor-licenses
%_bindir/tunnel-client
%_unitdir/%name@.service
%_userunitdir/%name@.service
%_datadir/%name
%dir %attr(0750,root,root) %_sysconfdir/%name
%config(noreplace) %attr(0600,root,root) %_sysconfdir/%name/default

%changelog
* Sat Oct 24 2026 Anton Farygin <rider@altlinux.org> 0.0.18-alt1
- initial ALT Linux package
