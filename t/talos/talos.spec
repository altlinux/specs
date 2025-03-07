%define _unpackaged_files_terminate_build 1
%global import_path github.com/siderolabs/talos
%global commit      d45259f89dce282eaf6bc3ed4c2106aa8a054eba
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define _libexecdir %_prefix/libexec
%define alt_registry registry.altlinux.org
%define alt_orchestra_registry altlinux.space/alt-orchestra
%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch sisyphus
%endif

Name: talos
Version: 1.10.0
Release: alt0.alpha.2

Summary: A modern OS for Kubernetes
License: MPL-2.0
Group: System/Configuration/Boot and Init
Url: https://www.talos.dev/
Vcs: https://github.com/siderolabs/talos.git

Source: %name-%version.tar
#Patch: %%name-%%version.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24.0
# For define versions
BuildRequires: etcd kubernetes-common coredns containerd flannel
#BuildRequires: /usr/bin/protoc libprotobuf-devel
#BuildRequires: /usr/bin/protoc-gen-go /usr/bin/protoc-gen-go-vtproto /usr/bin/protoc-gen-go-grpc

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

%prep
%setup
#%%autopatch -p1

%define go_ver %(rpm -q --qf '%%{VERSION}' golang)
%define etcd_ver %(rpm -q --qf '%%{VERSION}' etcd)
%define coredns_ver %(rpm -q --qf '%%{VERSION}' --whatprovides coredns)
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
  -e 's|HOME_URL=.*|HOME_URL="https://altlinux.space/alt-orchestra/talos/wiki"|' \
  -e 's|BUG_REPORT_URL=.*|BUG_REPORT_URL="https://altlinux.space/alt-orchestra/talos/issues"|' \
  -e 's|VENDOR_NAME=.*|VENDOR_NAME="ALT Linux Team"|' \
  -e 's|VENDOR_URL=.*|VENDOR_URL="https://altlinux.org"|' \
  pkg/machinery/constants/constants.go


# TODO:
#KubeletSystemReservedMemoryControlPlane
#KubeletSystemReservedMemoryWorker
#KubeletSystemReservedEphemeralStorage
#DefaultNTPServer

# Define ALT kernel
sed -i 's|DefaultKernelVersion = .*|DefaultKernelVersion = "6.12.9-talos"|' \
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

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-w"
export TAGS_TALOS="tcell_minimal,grpcnotrace"
export TAGS_TALOSCTL="grpcnotrace"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

#export NAME=Talos
export SHA=%shortcommit
#TODO: switch to registry.altlinux.org
export USERNAME=alt-orchestra
export REGISTRY=altlinux.space
#export EXTRAS=v1.7.0-2-g7c627a8
#export PKGS=v1.7.0-21-gc58ed7f
export TAG=v%version

#echo -n ${NAME} > pkg/machinery/gendata/data/name
echo -n ${SHA} > pkg/machinery/gendata/data/sha
echo -n ${USERNAME} > pkg/machinery/gendata/data/username
echo -n ${REGISTRY} > pkg/machinery/gendata/data/registry
#echo -n ${EXTRAS} > pkg/machinery/gendata/data/extras
#echo -n ${PKGS} > pkg/machinery/gendata/data/pkgs
echo -n ${TAG} > pkg/machinery/gendata/data/tag
#echo -n ${ARTIFACTS} > pkg/machinery/gendata/data/artifacts

#protoc -Iapi -Iapi/vendor/ -I/usr/include \
#  --go_out=paths=source_relative:api --go-grpc_out=paths=source_relative:api \
#  --go-vtproto_out=paths=source_relative:api --go-vtproto_opt=features=marshal+unmarshal+size \
#  api/common/common.proto


%golang_prepare
TAGS=$TAGS_TALOS %golang_build cmd/installer
TAGS=$TAGS_TALOSCTL %golang_build cmd/talosctl
TAGS=$TAGS_TALOS %golang_build internal/app/init
TAGS=$TAGS_TALOS %golang_build internal/app/machined

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
%golang_install

ln %buildroot%_bindir/installer %buildroot%_bindir/imager
mkdir -p %buildroot/usr/libexec/talos
mv %buildroot%_bindir/init %buildroot%_libexecdir/%name/init
mv %buildroot%_bindir/machined %buildroot%_libexecdir/%name/machined

%files -n talosctl
%doc README.md LICENSE
%_bindir/talosctl

%files installer
%_bindir/installer
%_bindir/imager
%_libexecdir/%name/init
%_libexecdir/%name/machined

%changelog
* Fri Mar 07 2025 Alexey Shabalin <shaba@altlinux.org> 1.10.0-alt0.alpha.2
- v1.10.0-alpha.2

* Tue Oct 29 2024 Alexey Shabalin <shaba@altlinux.org> 1.8.2-alt1
- 1.8.2
- Define registry.altlinux.org for k8s images.

* Sun Sep 29 2024 Alexey Shabalin <shaba@altlinux.org> 1.8.0-alt1
- Initial build.

