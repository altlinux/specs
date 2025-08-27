Name: portainer-agent
Version: 2.33.1
Release: alt1

Summary: Agent for portainer

License: Zlib
Group: System/Configuration/Other
Url: https://www.portainer.io
Vcs: https://github.com/portainer/agent

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
%patch -p1

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
* Wed Aug 27 2025 Leontiy Volodin <lvol@altlinux.org> 2.33.1-alt1
- New LTS version 2.33.1 (Fixes: GHSA-2464-8j7c-4cjm).

* Wed Aug 20 2025 Leontiy Volodin <lvol@altlinux.org> 2.33.0-alt1
- New LTS version 2.33.0 (Fixes: CVE-2025-54388, CVE-2025-8556,
  GHSA-fv92-fjc5-jj9h).

* Thu Jul 24 2025 Leontiy Volodin <lvol@altlinux.org> 2.32.0-alt1
- New version 2.32.0 (Fixes: CVE-2025-53547, CVE-2025-22874,
  CVE-2025-22781).

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


