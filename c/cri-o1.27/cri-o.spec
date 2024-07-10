
%global provider github.com
%global project cri-o
%global repo cri-o

%global provider_prefix %provider/%project/%repo
%global import_path %provider_prefix

%global _unpackaged_files_terminate_build 1

%define _libexecdir /usr/libexec

%define prog_name            cri-o
%define cri_o_major          1
%define cri_o_minor          27
%define cri_o_patch          8

Name: %prog_name%cri_o_major.%cri_o_minor
Version: %cri_o_major.%cri_o_minor.%cri_o_patch
Release: alt1
Summary: Kubernetes Container Runtime Interface for OCI-based containers
Group: Development/Other
License: Apache-2.0
URL: https://cri-o.io
VCS: https://github.com/cri-o/cri-o
ExclusiveArch: %go_arches

Source: %name-%version.tar
Patch1: .gear/cri-o-vendored-cilium-ebpf-loongarch64-support.patch

Provides: %prog_name = %EVR
Conflicts: %prog_name < %EVR
Conflicts: %prog_name > %EVR

Requires: containers-common
Requires: runc
Requires: cni-plugins
Requires: conntrack-tools
Requires: iproute2
Requires: iptables
Requires: socat
Requires: conmon

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang >= 1.20
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
%patch1 -p1

sed -i 's/\/local//' contrib/systemd/crio.service
sed -i 's/\/local//' contrib/systemd/crio-wipe.service
sed -i 's/\/local//' docs/crio.8.md
sed -i 's/\/local//' docs/crio.conf.5.md

sed -i 's/install.config: crio.conf/install.config:/' Makefile
sed -i 's/install.bin: binaries/install.bin:/' Makefile
sed -i 's/\.gopathok//' Makefile
sed -i 's|$(PREFIX)/lib/systemd/system|$(DESTDIR)%_unitdir|g' Makefile

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

export COMMIT_NO=%release
export GIT_TREE_STATE=clean
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
%post_service crio

%preun
%preun_service crio

%files
%_bindir/crio
%_bindir/crio-status
%_bindir/pinns
%_man5dir/crio.conf.*
%_man8dir/crio.*
%_man8dir/crio-status.*
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
* Fri Jul 05 2024 Alexander Stepchenko <geochip@altlinux.org> 1.27.8-alt1
- 1.27.6 -> 1.27.8

* Thu Jul 04 2024 Alexander Stepchenko <geochip@altlinux.org> 1.27.6-alt2
- Use macros for systemd instead of absolute paths.

* Wed May 22 2024 Alexander Stepchenko <geochip@altlinux.org> 1.27.6-alt1
- 1.27.4 -> 1.27.6
- Fixes:
  * CVE-2023-48795: golang.org/x/crypto/ssh
  * CVE-2024-24786: google.golang.org/protobuf
  * CVE-2024-28180: gopkg.in/go-jose/go-jose.v2
  * CVE-2024-3154: CRI-O vulnerable to an arbitrary systemd property injection

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
