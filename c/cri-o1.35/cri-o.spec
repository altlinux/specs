
%global provider github.com
%global project cri-o
%global repo cri-o

%global provider_prefix %provider/%project/%repo
%global import_path %provider_prefix

%global _unpackaged_files_terminate_build 1

%define _libexecdir /usr/libexec

# git rev-parse v1.35.3^{commit}
%define git_commit 5a749bae37de8a35e8ebb7c56920dae0dd8fa0d7

%define prog_name            cri-o
%define cri_o_major          1
%define cri_o_minor          35
%define cri_o_patch          3

Name: %prog_name%cri_o_major.%cri_o_minor
Version: %cri_o_major.%cri_o_minor.%cri_o_patch
Release: alt1
Summary: Kubernetes Container Runtime Interface for OCI-based containers
Group: Development/Other
License: Apache-2.0
Url: https://cri-o.io
VCS: https://github.com/cri-o/cri-o
ExclusiveArch: %go_arches

Source: %name-%version.tar

Provides: %prog_name = %EVR
Conflicts: %prog_name < %EVR
Conflicts: %prog_name > %EVR

# Versions info from ./scripts/versions or ./dependencies.yaml
Requires: containers-common
Requires: crun
Requires: cni-plugins >= 1.8.0
Requires: conntrack-tools
Requires: iproute2
Requires: iptables
Requires: socat
Requires: conmon >= 2.1.13

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25
BuildRequires: glib2-devel
BuildRequires: glibc-devel-static
BuildRequires: libbtrfs-devel
BuildRequires: libdevmapper-devel
BuildRequires: libgpgme-devel libassuan-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: libsystemd-devel
BuildRequires: go-md2man
BuildRequires: /proc
Provides: oci-runtime = 2
Provides: cri-runtime

%description
%summary

%prep
%setup

sed -i 's/\/local//' contrib/systemd/crio.service
sed -i 's/\/local//' contrib/systemd/crio-wipe.service
sed -i 's/\/local//' docs/crio.8.md
sed -i 's/\/local//' docs/crio.conf.5.md

sed -i 's/install.config: crio.conf/install.config:/' Makefile
sed -i 's/install.bin: binaries/install.bin:/' Makefile
sed -i 's/\.gopathok//' Makefile
sed -i 's|$(PREFIX)/lib/systemd/system|$(DESTDIR)%_unitdir|g' Makefile

# Build with debuginfo.
sed -i 's/SHRINKFLAGS = -s -w/SHRINKFLAGS = /' Makefile
sed -i 's/TRIMPATH ?= -trimpath/TRIMPATH ?= /' Makefile
sed -Ei 's/(\s+\$\(STRIP\) -s \$@)/#\1/' pinns/Makefile

sed -Ei 's/(\s+)gitCommit := unknown/\1gitCommit := "%git_commit"/' internal/version/version.go

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

export BRANCH=altlinux
export GOFLAGS="-mod=vendor"

cd .build/src/%import_path
%make

%install
cd .build/src/%import_path
./bin/crio \
      --cgroup-manager "systemd" \
      --storage-driver "overlay" \
      --root "/var/lib/containers/storage" \
      --runroot "/var/run/containers/storage" \
      --listen "/var/run/crio/crio.sock" \
      --conmon "%_bindir/conmon" \
      --cni-plugin-dir "%_libexecdir/cni,/opt/cni/bin" \
      --storage-opt "overlay.override_kernel_check=1" \
      config > ./crio.conf

# install conf files
install -dp %buildroot%_sysconfdir/cni/net.d
install -p -m 644 contrib/cni/10-crio-bridge.conflist %buildroot%_sysconfdir/cni/net.d/100-crio-bridge.conflist.sample
install -p -m 644 contrib/cni/99-loopback.conflist %buildroot%_sysconfdir/cni/net.d/200-loopback.conflist.sample

%make PREFIX=%buildroot%prefix DESTDIR=%buildroot \
            install.bin \
            install.completions \
            install.config \
            install.man \
            install.systemd

%post
%post_systemd crio.service

%preun
%preun_systemd crio.service

%files
%_bindir/crio
%_bindir/pinns
%_man5dir/crio.conf.*
%_man8dir/crio.*
%dir %_sysconfdir/crio
%config(noreplace) %_sysconfdir/crio/crio.conf
%_sysconfdir/cni/net.d/100-crio-bridge.conflist.sample
%_sysconfdir/cni/net.d/200-loopback.conflist.sample
%config(noreplace) %_sysconfdir/crictl.yaml
%_unitdir/*.service
%_datadir/oci-umount
%_datadir/bash-completion/completions/*
%_datadir/fish/completions/*
%_datadir/zsh/site-functions/*

%changelog
* Fri May 22 2026 Alexander Stepchenko <geochip@altlinux.org> 1.35.3-alt1
- 1.35.2 -> 1.35.3.
- Fixes:
  + CVE-2026-35469: SpdyStream: DOS on CRI

* Mon Apr 06 2026 Alexander Stepchenko <geochip@altlinux.org> 1.35.2-alt1
- 1.35.1 -> 1.35.2.

* Mon Mar 30 2026 Alexander Stepchenko <geochip@altlinux.org> 1.35.1-alt1
- 1.35.0 -> 1.35.1.
- Fixes:
  + CVE-2025-31133: runc container escape via "masked path" abuse due to mount race conditions
  + CVE-2025-52565: container escape due to /dev/console mount and related races
  + CVE-2025-52881: runc: LSM labels can be bypassed with malicious config using dummy procfs files

* Tue Dec 23 2025 Alexander Stepchenko <geochip@altlinux.org> 1.35.0-alt1
- 1.34.3 -> 1.35.0.

* Mon Dec 15 2025 Alexander Stepchenko <geochip@altlinux.org> 1.34.3-alt1
- 1.33.7 -> 1.34.3.

* Thu Dec 11 2025 Alexander Stepchenko <geochip@altlinux.org> 1.33.7-alt1
- 1.33.6 -> 1.33.7.

* Thu Nov 13 2025 Alexander Stepchenko <geochip@altlinux.org> 1.33.6-alt1
- 1.33.4 -> 1.33.6.

* Tue Sep 02 2025 Alexander Stepchenko <geochip@altlinux.org> 1.33.4-alt1
- Update to 1.33.4.

* Sat Aug 30 2025 Alexander Stepchenko <geochip@altlinux.org> 1.33.3-alt1
- Update to 1.33.3.

* Thu Jul 24 2025 Alexander Stepchenko <geochip@altlinux.org> 1.33.2-alt1
- Update to 1.33.2

* Mon Jun 09 2025 Alexander Stepchenko <geochip@altlinux.org> 1.33.1-alt1
- 1.33.0 -> 1.33.1

* Tue May 20 2025 Alexander Stepchenko <geochip@altlinux.org> 1.33.0-alt1
- 1.32.3 -> 1.33.0

* Thu May 08 2025 Alexander Stepchenko <geochip@altlinux.org> 1.32.3-alt2
- Fix systemd service disabling before package deletion (Closes: #49768)

* Thu Apr 17 2025 Alexander Stepchenko <geochip@altlinux.org> 1.32.3-alt1
- 1.32.1 -> 1.32.3

* Thu Feb 20 2025 Alexander Stepchenko <geochip@altlinux.org> 1.32.1-alt1
- 1.31.5 -> 1.32.1

* Thu Feb 20 2025 Alexander Stepchenko <geochip@altlinux.org> 1.31.5-alt1
- 1.31.4 -> 1.31.5

* Sun Jan 26 2025 Alexander Stepchenko <geochip@altlinux.org> 1.31.4-alt1
- 1.31.1 -> 1.31.4

* Wed Oct 30 2024 Alexander Stepchenko <geochip@altlinux.org> 1.31.1-alt1
- 1.31.0 -> 1.31.1

* Wed Sep 11 2024 Alexander Stepchenko <geochip@altlinux.org> 1.31.0-alt1
- 1.30.5 -> 1.31.0

* Wed Sep 11 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.5-alt1
- 1.30.4 -> 1.30.5

* Tue Aug 06 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.4-alt1
- 1.30.3 -> 1.30.4

* Wed Jul 10 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.3-alt1
- 1.30.1 -> 1.30.3

* Fri Jul 05 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.1-alt2
- Use macros for systemd instead of absolute paths.

* Thu May 23 2024 Alexander Stepchenko <geochip@altlinux.org> 1.30.1-alt1
- 1.29.4 -> 1.30.1 (Fixes: CVE-2024-5154)

* Wed May 22 2024 Alexander Stepchenko <geochip@altlinux.org> 1.29.4-alt1
- 1.28.6 -> 1.29.4

* Wed May 22 2024 Alexander Stepchenko <geochip@altlinux.org> 1.28.6-alt1
- 1.28.4 -> 1.28.6
- Fixes:
  * CVE-2023-48795: golang.org/x/crypto/ssh
  * CVE-2024-24786: google.golang.org/protobuf
  * CVE-2024-28180: gopkg.in/go-jose/go-jose.v2
  * CVE-2024-3154: CRI-O vulnerable to an arbitrary systemd property injection

* Tue Mar 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.28.4-alt1
- 1.28.4.

* Tue Mar 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.27.4-alt1
- 1.27.4.

* Tue Mar 05 2024 Ivan A. Melnikov <iv@altlinux.org> 1.27.1-alt1.1
- NMU: loongarch64 support

* Tue Oct 31 2023 Alexey Shabalin <shaba@altlinux.org> 1.27.1-alt1
- 1.27.1.

* Tue Oct 31 2023 Alexey Shabalin <shaba@altlinux.org> 1.26.4-alt3
- Rename the package to include major and minor versions.
- Update BR golang >= 1.19.

* Mon Oct 16 2023 Alexander Stepchenko <geochip@altlinux.org> 1.26.4-alt2
- Add BuildRequires: /proc

* Sat Oct 07 2023 Alexander Stepchenko <geochip@altlinux.org> 1.26.4-alt1
- 1.26.2 -> 1.26.4

* Mon Mar 27 2023 Alexander Stepchenko <geochip@altlinux.org> 1.26.2-alt1
- 1.26.2
- Fixes: CVE-2022-2995, CVE-2022-27652, CVE-2022-4318

* Thu Nov 24 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.24.3-alt1
- 1.24.3
- Fixes: CVE-2022-1708

* Mon Mar 21 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.3-alt2
- Add cve fix to changelog
- Fixes: CVE-2022-0811

* Wed Mar 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.3-alt1
- 1.22.3

* Tue Mar 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.2-alt1
- 1.22.2

* Wed Jan 12 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.1-alt2
- Rename default network configs to samples
- Add /opt/cni/bin (it is default place for some k8s networks) to plugins dir

* Thu Dec 02 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.1-alt1
- 1.22.1

* Wed Jun 30 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.21.1-alt1
- new version 1.21.1

* Thu Jan 21 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.20.0-alt1
- new version 1.20.0

* Tue Nov 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.18.4-alt1
- new version 1.18.4

* Thu Sep 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.18.3-alt1
- new version 1.18.3

* Sat Jul 04 2020 Alexey Shabalin <shaba@altlinux.org> 1.18.2-alt1
- new version 1.18.2

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.18.1-alt1
- new version 1.18.1

* Wed May 06 2020 Alexey Shabalin <shaba@altlinux.org> 1.18.0-alt1
- 1.18.0

* Tue Apr 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.17.4-alt1
- 1.17.4

* Thu Sep 19 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.2-alt1
- initial build
