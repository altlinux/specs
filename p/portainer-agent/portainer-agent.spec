Name: portainer-agent
Version: 2.31.3
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
* Mon Jul 14 2025 Leontiy Volodin <lvol@altlinux.org> 2.31.3-alt1
- New version 2.31.3.

* Fri Jun 27 2025 Leontiy Volodin <lvol@altlinux.org> 2.31.2-alt1
- New version 2.31.2.

* Thu Jun 19 2025 Leontiy Volodin <lvol@altlinux.org> 2.31.1-alt1
- New version 2.31.1.

* Wed Jun 18 2025 Leontiy Volodin <lvol@altlinux.org> 2.31.0-alt1
- New version 2.31.0.
- Fixes:
  + CVE-2025-22871.

* Wed Apr 16 2025 Leontiy Volodin <lvol@altlinux.org> 2.29.0-alt1
- Initial build for ALT Sisyphus (for portainer).


