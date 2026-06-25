Name: portainer-agent
Version: 2.39.4
Release: alt1

Summary: Agent for portainer

License: Zlib
Group: System/Configuration/Other
Url: https://www.portainer.io
Vcs: https://github.com/portainer/agent

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
# go mod vendor -o ../vendor
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
go build -x \
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
* Thu Jun 25 2026 Leontiy Volodin <lvol@altlinux.org> 2.39.4-alt1
- New LTS version 2.39.4.

* Thu Jun 04 2026 Leontiy Volodin <lvol@altlinux.org> 2.39.3-alt1
- New LTS version 2.39.3 (Fixes: CVE-2026-3416, CVE-2026-33762,
  GHSA-3xc5-wrhm-f963, GHSA-pmwq-pjrm-6p5r, CVE-2026-27141,
  CVE-2026-33814, CVE-2026-39830, CVE-2026-39831, CVE-2026-39832,
  CVE-2026-39833, CVE-2026-39834, CVE-2026-42508, CVE-2026-46595).

* Thu May 07 2026 Leontiy Volodin <lvol@altlinux.org> 2.39.2-alt1
- New LTS version 2.39.2.

* Mon Mar 23 2026 Leontiy Volodin <lvol@altlinux.org> 2.39.1-alt1
- New LTS version 2.39.1 (Fixes: CVE-2026-33186, GO-2026-4394,
  GO-2026-4473, GO-2026-4550).

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 2.39.0-alt1
- New LTS version 2.39.0.

* Thu Feb 12 2026 Leontiy Volodin <lvol@altlinux.org> 2.33.7-alt1
- New LTS version 2.33.7 (Fixes: CVE-2025-47914, CVE-2025-58181,
  CVE-2025-61726, CVE-2025-68121).

* Tue Dec 16 2025 Leontiy Volodin <lvol@altlinux.org> 2.33.6-alt1
- New LTS version 2.33.6 (Fixes: CVE-2025-62725, CVE-2025-47906,
  CVE-2025-47910, CVE-2025-47913, CVE-2024-25621).

* Tue Sep 30 2025 Leontiy Volodin <lvol@altlinux.org> 2.33.2-alt1
- New LTS version 2.33.2.

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


