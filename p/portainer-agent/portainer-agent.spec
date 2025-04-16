Name: portainer-agent
Version: 2.29.0
Release: alt1

Summary: Agent for portainer

License: Zlib
Group: System/Configuration/Other
Url: https://www.portainer.io
Vcs: https://github.com/portainer/agent.git

Source: %url/archive/%version/%name-%version.tar.gz
# go mod vendor
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): golang
BuildRequires: rpm-build-golang /proc
%description
%summary.

%prep
%setup -a1
%autopatch -p1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   --installsuffix cgo \
   --ldflags="-s" \
   -o dist/agent ./cmd/agent/

%install
install -Dm755 dist/agent %buildroot%_bindir/portainer-agent

%files
%doc LICENSE README.md
%_bindir/portainer-agent

%changelog
* Wed Apr 16 2025 Leontiy Volodin <lvol@altlinux.org> 2.29.0-alt1
- Initial build for ALT Sisyphus (for portainer).


