%global goipath github.com/containers/prometheus-podman-exporter
%{!?_userunitdir: %global _userunitdir /usr/lib/systemd/user}

Name: prometheus-podman-exporter
Version: 1.21.2
Release: alt1

Summary: Prometheus exporter for podman environment

License: Apache-2.0 and MPL-2.0 and BSD-3-Clause and BSD-2-Clause and MIT and CC-BY-SA-4.0 and ISC
Group: System/Configuration/Other
Url: https://github.com/containers/prometheus-podman-exporter
Vcs: https://github.com/containers/prometheus-podman-exporter

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre):  rpm-build-golang /proc
BuildRequires: git-core libdevmapper-devel glib2-devel libgpgme-devel libassuan-devel libbtrfs-devel libsystemd-devel
BuildRequires: libselinux-utils
Requires: conmon crun
%ifnarch i586 armh
Requires: netavark
%endif

%description
Prometheus exporter for podman environments exposing containers, pods, images,
volumes and networks information.

%prep
%setup
sed -i 's| selinuxenabled| %_sbindir/selinuxenabled|' \
  Makefile
sed -i 's|$(DESTDIR)/$(TARGET)|$(DESTDIR)%_bindir/$(TARGET)|' \
  Makefile

%build
%make_build

%install
%makeinstall_std
install -Dm644 contrib/systemd/system/%name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -Dm644 contrib/systemd/system/%name.service -t %buildroot%_unitdir/
install -Dm644 contrib/systemd/user/%name.service -t %buildroot%_userunitdir/

%files
%doc LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md MAINTAINERS.md README.md SECURITY.md
%_bindir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_userunitdir/%name.service

%changelog
* Mon Jun 29 2026 Leontiy Volodin <lvol@altlinux.org> 1.21.2-alt1
- New version 1.21.2 (Fixes: CVE-2026-39828, CVE-2026-39829,
  CVE-2026-39830, CVE-2026-39832, CVE-2026-39835).

* Tue Jun 23 2026 Leontiy Volodin <lvol@altlinux.org> 1.21.1-alt1
- New version 1.21.1.

* Mon Mar 16 2026 Leontiy Volodin <lvol@altlinux.org> 1.21.0-alt1
- New version 1.21.0.

* Tue Dec 23 2025 Leontiy Volodin <lvol@altlinux.org> 1.20.0-alt1
- New version 1.20.0.

* Mon Oct 06 2025 Leontiy Volodin <lvol@altlinux.org> 1.19.0-alt1
- New version 1.19.0 (Fixes: CVE-2025-47910, CVE-2025-47906).

* Mon Sep 15 2025 Leontiy Volodin <lvol@altlinux.org> 1.18.1-alt1.1
- Specified closed security vulnerabilities (Fixes: CVE-2025-58058).

* Mon Sep 15 2025 Leontiy Volodin <lvol@altlinux.org> 1.18.1-alt1
- New version 1.18.1.

* Wed Sep 10 2025 Leontiy Volodin <lvol@altlinux.org> 1.18.0-alt1
- New version 1.18.0.

* Mon Jul 14 2025 Leontiy Volodin <lvol@altlinux.org> 1.17.2-alt1
- New version 1.17.2.

* Mon Jun 09 2025 Leontiy Volodin <lvol@altlinux.org> 1.17.1-alt1
- New version 1.17.1.

* Thu May 29 2025 Leontiy Volodin <lvol@altlinux.org> 1.17.0-alt1
- New version 1.17.0.

* Fri Apr 11 2025 Leontiy Volodin <lvol@altlinux.org> 1.16.0-alt1
- New version 1.16.0.

* Mon Mar 03 2025 Leontiy Volodin <lvol@altlinux.org> 1.15.0-alt1
- New version 1.15.0.

* Tue Jan 28 2025 Leontiy Volodin <lvol@altlinux.org> 1.14.1-alt1
- New version 1.14.1.

* Fri Dec 20 2024 Leontiy Volodin <lvol@altlinux.org> 1.14.0-alt1.3
- Fixed requires.

* Fri Dec 20 2024 Leontiy Volodin <lvol@altlinux.org> 1.14.0-alt1.2
- Fixed userunitdir path.

* Thu Dec 19 2024 Leontiy Volodin <lvol@altlinux.org> 1.14.0-alt1.1
- Fixed backporting to older branches.

* Wed Dec 18 2024 Leontiy Volodin <lvol@altlinux.org> 1.14.0-alt1
- Initial build for ALT Sisyphus.
