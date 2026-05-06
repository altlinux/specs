%define _unpackaged_files_terminate_build 1
%global import_path github.com/siderolabs/talos
%global commit      91c63991eb669602e379ff653ecc20212834390e
%global shortcommit %(c=%commit; echo ${c:0:7})
%global altkernel 6.18.26-talos
%global latest_distro_tag v11.0
%define _libexecdir %prefix/libexec
%define alt_registry registry.altlinux.org
%define alt_orchestra_registry altlinux.space/alt-orchestra
%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch sisyphus
%endif

Name: talos
Version: 1.12.7
Release: alt3

Summary: A modern OS for Kubernetes
License: MPL-2.0
Group: System/Configuration/Boot and Init
Url: https://www.talos.dev/
Vcs: https://github.com/siderolabs/talos.git

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24.0
# For define versions
BuildRequires: etcd-for-kubernetes kubernetes-common coredns-for-kubernetes containerd flannel
#BuildRequires: /usr/bin/protoc libprotobuf-devel
#BuildRequires: /usr/bin/protoc-gen-go /usr/bin/protoc-gen-go-vtproto /usr/bin/protoc-gen-go-grpc

%add_findreq_skiplist %go_path/src/%import_path/**/*
%add_findprov_skiplist %go_path/src/%import_path/**/*

%description
Talos is a container optimized Linux distro;
a reimagining of Linux for distributed systems such as Kubernetes.
Designed to be as minimal as possible while still maintaining practicality.
For these reasons, Talos has a number of features unique to it:
 * it is immutable
 * it is atomic
 * it is ephemeral
 * it is minimal
 * it is secure by default
 * it is managed via a single declarative configuration file and gRPC API

Talos can be deployed on container, cloud, virtualized, and bare metal platforms.

%package installer
Summary: Package installer provides the installer implementation
Group: System/Configuration/Boot and Init
%description installer
%summary.

%package -n talosctl
Summary: Package talosctl provides the talosctl utility implementation
Group: System/Configuration/Boot and Init
%description -n talosctl
%summary.

%package devel
Summary: Source of talos
Group: Development/Other
BuildArch: noarch
%description devel
%summary.

%prep
%setup -a1
%autopatch -p1

%define go_ver %(rpm -q --qf '%%{VERSION}' golang)
%define etcd_ver %(rpm -q --qf '%%{VERSION}' --whatprovides etcd-for-kubernetes)
%define coredns_ver %(rpm -q --qf '%%{VERSION}' --whatprovides coredns-for-kubernetes)
%define kubernetes_ver %(rpm -q --qf '%%{VERSION}' --whatprovides kubernetes-common)
%define containerd_ver %(rpm -q --qf '%%{VERSION}' containerd)
%define flannel_ver %(rpm -q --qf '%%{VERSION}' flannel)

# Set ALT rpm pckage version
sed -i \
  -e 's|GoVersion = .*|GoVersion = "go%go_ver"|' \
  -e 's|DefaultKubernetesVersion = .*|DefaultKubernetesVersion = "%kubernetes_ver"|' \
  -e 's|DefaultCoreDNSVersion = .*|DefaultCoreDNSVersion = "v%coredns_ver"|' \
  -e 's|DefaultEtcdVersion = .*|DefaultEtcdVersion = "v%etcd_ver"|' \
  -e 's|DefaultContainerdVersion = .*|DefaultContainerdVersion = "%containerd_ver"|' \
  -e 's|FlannelVersion = .*|FlannelVersion = "v%flannel_ver"|' \
  pkg/machinery/constants/constants.go

sed -i \
  -e 's|HOME_URL=.*|HOME_URL="https://altlinux.space/alt-orchestra/talos-build/wiki"|' \
  -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://altlinux.space/alt-orchestra/talos-build/issues"|' \
  -e 's|VENDOR_NAME=.*|VENDOR_NAME="ALT Linux Team"|' \
  -e 's|VENDOR_URL=.*|VENDOR_URL="https://altlinux.org"|' \
  -e 's|DefaultDiscoveryServiceEndpoint =.*|DefaultDiscoveryServiceEndpoint = "https://discovery.altlinux.space/"|' \
  pkg/machinery/constants/constants.go

sed -i \
  -e 's|discovery.talos.dev|discovery.altlinux.space|g' \
  internal/app/machined/pkg/controllers/cluster/config_test.go \
  pkg/machinery/config/configloader/internal/decoder/testdata/controlplane.yaml \
  pkg/machinery/config/configloader/internal/decoder/testdata/worker.yaml

# TODO:
#KubeletSystemReservedMemoryControlPlane
#KubeletSystemReservedMemoryWorker
#KubeletSystemReservedEphemeralStorage
#DefaultNTPServer

# Define ALT kernel
sed -i 's|DefaultKernelVersion = .*|DefaultKernelVersion = "%altkernel"|' \
  pkg/machinery/constants/constants.go

# Define ALT k8s registry
sed -i \
  -e 's|KubeProxyImage = .*|KubeProxyImage = "%alt_registry/%altbranch/kube-proxy"|' \
  -e 's|KubernetesAPIServerImage = .*|KubernetesAPIServerImage = "%alt_registry/%altbranch/kube-apiserver"|' \
  -e 's|KubernetesControllerManagerImage = .*|KubernetesControllerManagerImage = "%alt_registry/%altbranch/kube-controller-manager"|' \
  -e 's|KubernetesSchedulerImage = .*|KubernetesSchedulerImage = "%alt_registry/%altbranch/kube-scheduler"|' \
  -e 's|CoreDNSImage = .*|CoreDNSImage = "%alt_registry/%altbranch/coredns"|' \
  -e 's|EtcdImage = .*|EtcdImage = "%alt_registry/%altbranch/etcd"|' \
  -e 's|KubeletImage = .*|KubeletImage = "%alt_registry/%altbranch/kubelet"|' \
  pkg/machinery/constants/constants.go

sed -i \
  -e 's|ghcr.io/siderolabs/flannel|%alt_registry/%altbranch/flannel|' \
  -e 's|DefaultSandboxImage = .*| DefaultSandboxImage = "%alt_registry/%altbranch/pause:latest"|' \
  pkg/images/list.go

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-w"
export TAGS_TALOS="tcell_minimal,grpcnotrace"
export TAGS_TALOSCTL="grpcnotrace"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

export NAME="ALT Orchestra"
export SHA=%shortcommit
export LATEST_DISTRO_TAG="%latest_distro_tag"
#TODO: switch to registry.altlinux.org
export USERNAME=alt-orchestra
export REGISTRY=altlinux.space
#export EXTRAS=v1.7.0-2-g7c627a8
#export PKGS=v1.7.0-21-gc58ed7f
export TAG=v%version

echo -n ${NAME} > pkg/machinery/gendata/data/name
echo -n ${SHA} > pkg/machinery/gendata/data/sha
echo -n ${USERNAME} > pkg/machinery/gendata/data/username
echo -n ${REGISTRY} > pkg/machinery/gendata/data/registry
#echo -n ${EXTRAS} > pkg/machinery/gendata/data/extras
#echo -n ${PKGS} > pkg/machinery/gendata/data/pkgs
echo -n ${TAG} > pkg/machinery/gendata/data/tag
#echo -n ${ARTIFACTS} > pkg/machinery/gendata/data/artifacts
echo -n ${LATEST_DISTRO_TAG} > pkg/machinery/gendata/data/latest-distro-tag

#protoc -Iapi -Iapi/vendor/ -I/usr/include \
#  --go_out=paths=source_relative:api --go-grpc_out=paths=source_relative:api \
#  --go-vtproto_out=paths=source_relative:api --go-vtproto_opt=features=marshal+unmarshal+size \
#  api/common/common.proto

%golang_prepare
TAGS=$TAGS_TALOS %golang_build cmd/installer
TAGS=$TAGS_TALOSCTL %golang_build cmd/talosctl
TAGS=$TAGS_TALOS %golang_build internal/app/init
TAGS=$TAGS_TALOS %golang_build internal/app/machined

"$BUILDDIR/bin/talosctl" completion bash > talosctl.bash
"$BUILDDIR/bin/talosctl" completion zsh > talosctl.zsh
"$BUILDDIR/bin/talosctl" completion fish > talosctl.fish

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path"
%golang_install

ln %buildroot%_bindir/installer %buildroot%_bindir/imager
mkdir -p %buildroot/usr/libexec/talos
mv %buildroot%_bindir/init %buildroot%_libexecdir/%name/init
mv %buildroot%_bindir/machined %buildroot%_libexecdir/%name/machined

install -Dpm 0644 talosctl.bash %buildroot%_datadir/bash-completion/completions/talosctl
install -Dpm 0644 talosctl.zsh %buildroot%_datadir/zsh/site-functions/_talosctl
install -Dpm 0644 talosctl.fish %buildroot%_datadir/fish/vendor_completions.d/talosctl.fish

%files -n talosctl
%doc README.md LICENSE
%_bindir/talosctl
%_datadir/bash-completion/completions/talosctl
%_datadir/zsh/site-functions/_talosctl
%_datadir/fish/vendor_completions.d/talosctl.fish

%files installer
%_bindir/installer
%_bindir/imager
%_libexecdir/%name/init
%_libexecdir/%name/machined

%files devel
%go_path/src/%import_path

%changelog
* Mon May 04 2026 Alexander Stepchenko <geochip@altlinux.org> 1.12.7-alt3
- Update DefaultKernelVersion to 6.18.26.

* Thu Apr 30 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.7-alt2
- Display correct OS name in version command and dashboard
- Add LatestDistroTag and use it in gen config and talos-bundle commands
- Add DistroVersion field to profile
- Add ability to specify Version and DistroVersion from imager cli
- Use version.Name for reset option in grub
- Use DistroVersion for ISO label
- Add version.Name and DistroVersion to OutputPath

* Mon Apr 27 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.7-alt1
- New version 1.12.7.

* Wed Apr 15 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.6-alt3
- Move vendor to separate source.
- Update .gear/tags/list for correct patch generation.

* Mon Apr 13 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.6-alt2
- Remove default module.sig_enforce=1.

* Mon Mar 23 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.6-alt1
- New version 1.12.6.

* Wed Mar 18 2026 Alexander Stepchenko <geochip@altlinux.org> 1.12.5-alt2
- Update DefaultKernelVersion to 6.18.18.

* Tue Mar 10 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.5-alt1
- New version 1.12.5.

* Mon Mar 02 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.4-alt2
- Fix build with go 1.26.

* Mon Feb 16 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.4-alt1
- New version 1.12.4.

* Mon Feb 09 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.3-alt1
- New version 1.12.3.

* Mon Feb 02 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.2-alt1
- New version 1.12.2.

* Wed Dec 24 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.11.6-alt1
- New version 1.11.6.

* Fri Dec 19 2025 Alexander Stepchenko <geochip@altlinux.org> 1.10.8-alt2
- Update to kernel-image-talos-6.12.59.
- Fix detecting image-cache in OS image.
- Fix default OCI images versions.
- Package talosctl completion files.

* Fri Nov 21 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.8-alt1
- New version 1.10.8.

* Wed Sep 10 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.7-alt2
- Update DefaultKernelVersion.

* Mon Sep 08 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.7-alt1
- New version 1.10.7.

* Wed Aug 06 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.6-alt2
- Remove whitelist path validation.
- Fix build with go 1.25

* Mon Aug 04 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.6-alt1
- New version 1.10.6.
- package talos-devel

* Fri Jul 18 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.5-alt2
- Update DefaultKernelVersion.

* Mon Jul 14 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.5-alt1
- New version 1.10.5.

* Mon Jun 23 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.4-alt1
- New version 1.10.4.
- Add minimal ALT Orchestra branding

* Fri May 30 2025 Alexey Shabalin <shaba@altlinux.org> 1.10.3-alt1
- New version 1.10.3.
- Update HOME_URL and BUG_REPORT_URL.
- Set discovery.altlinux.space as Discovery Endpoint.

* Tue May 27 2025 Alexey Shabalin <shaba@altlinux.org> 1.10.2-alt1
- New version 1.10.2.

* Wed May 14 2025 Alexey Shabalin <shaba@altlinux.org> 1.10.1-alt1
- v1.10.1

* Mon Mar 31 2025 Alexey Shabalin <shaba@altlinux.org> 1.10.0-alt0.alpha.3
- v1.10.0-alpha.3
- set url for pause and flannel images to registry.a.o

* Fri Mar 07 2025 Alexey Shabalin <shaba@altlinux.org> 1.10.0-alt0.alpha.2
- v1.10.0-alpha.2

* Tue Oct 29 2024 Alexey Shabalin <shaba@altlinux.org> 1.8.2-alt1
- 1.8.2
- Define registry.altlinux.org for k8s images.

* Sun Sep 29 2024 Alexey Shabalin <shaba@altlinux.org> 1.8.0-alt1
- Initial build.

