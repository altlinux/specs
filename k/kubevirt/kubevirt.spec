%define import_path github.com/kubevirt/kubevirt
%define _unpackaged_files_terminate_build 1
%global commit ed1e7ae8548d319fa7aacf315ad198f7241287c5

Name:          	kubevirt
Version:       	1.3.1
Release:       	alt1
Summary:       	KubeVirt is a virtual machine management add-on for Kubernetes

Group:         	Emulators
License:       	Apache-2.0
URL:           	https://github.com/kubevirt/kubevirt

Source0:       	%name-%version.tar
ExclusiveArch: 	x86_64 aarch64

BuildRequires: 	rpm-macros-golang
BuildRequires: 	rpm-build-golang
BuildRequires: 	glibc-devel-static
BuildRequires: 	golang >= 1.19
BuildRequires: 	libvirt-devel
BuildRequires: 	/proc

%description
KubeVirt extends Kubernetes by adding additional virtualization
resource types (especially the VM type) through Kubernetes's
Custom Resource Definitions API. By using this mechanism, the
Kubernetes API can be used to manage these VM resources alongside
all other resources Kubernetes provides.

%package        virtctl
Summary:        Client for managing kubevirt
Group:          Emulators

%description    virtctl
The virtctl client is a command-line utility for managing
container native virtualization resources

%package        virt-api
Summary:        Kubevirt API server
Group:          Emulators

%description    virt-api
The virt-api package provides the kubernetes API extension
for kubevirt

%package        container-disk
Summary:        Container disk for kubevirt
Group:          Emulators

%description    container-disk
The containter-disk package provides a container disk
functionality for kubevirt

%package        virt-controller
Summary:        Controller for kubevirt
Group:          Emulators

%description    virt-controller
The virt-controller package provides a controller for
Kubevirt

%package        virt-exportproxy
Summary:        Export proxy for kubevirt
Group:          Emulators

%description    virt-exportproxy
The virt-exportproxy package provides a proxy for kubevirt
to pass requests to virt-exportserver

%package        virt-exportserver
Summary:        Export server for kubevirt
Group:          Emulators

%description    virt-exportserver
The virt-exportserver package provides an http server for
kubevirt to serve the data of VirtualMachineExport resource
in different formats

%package        virt-handler
Summary:        Handler component for kubevirt
Group:          Emulators
Requires: findutils, iproute2, iptables, procps, lsscsi, nftables, tar, curl, qemu-img

%description    virt-handler
The virt-handler package provides a handler for kubevirt

%package        virt-launcher
Summary:        Launcher component for kubevirt
Group:          Emulators
Requires: libvirt-daemon-driver-qemu, libvirt-client, qemu-device-usb-redirect, qemu-kvm-core
Requires: ethtool, findutils, gawk, iptables, libcap, netcat, nftables, passt, procps, psmisc, qemu-img, socat, tar, tzdata, virtiofsd, xorriso, curl
%ifarch x86_64
Requires: qemu-system-x86
%endif
%ifarch aarch64
Requires: qemu-system-aarch64, qemu-device-display-virtio-gpu, qemu-device-display-virtio-gpu-ccw
%endif

%description    virt-launcher
The virt-launcher package provides a launcher for kubevirt

%package        virt-operator
Summary:        Operator component for kubevirt
Group:          Emulators

%description    virt-operator
The virt-opertor package provides an operator for kubevirt CRD

%package        pr-helper-conf
Summary:        Configuration files for persistent reservation helper
Group:          Emulators

%description    pr-helper-conf
The pr-helper-conf package provides configuration files
for persistent reservation helper

%package        manifests
Summary:        YAML manifests used to install kubevirt
Group:          Emulators

%description    manifests
This contains the built YAML manifests used to install kubevirt
into a kubernetes installation with kubectl apply.

%package        tests
Summary:        Kubevirt functional tests
Group:          Emulators

%description    tests
The package provides Kubevirt end-to-end tests.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export GOBIN="$BUILDDIR/bin"
reg_path="registry.altlinux.org/sisyphus"

%golang_prepare
mkdir $GOBIN
pushd $BUILDDIR/src/%import_path

env \
KUBEVIRT_GO_BASE_PKGDIR="$GOPATH/pkg" \
KUBEVIRT_VERSION=%version \
KUBEVIRT_SOURCE_DATE_EPOCH="$(date -r LICENSE +'%%s')" \
KUBEVIRT_GIT_COMMIT="%commit" \
KUBEVIRT_GIT_VERSION="v%version" \
KUBEVIRT_GIT_TREE_STATE="clean" \
build_tests="true" \
./hack/build-go.sh install \
    cmd/virt-api \
    cmd/virt-chroot \
    cmd/virt-controller \
    cmd/virt-exportproxy \
    cmd/virt-exportserver \
    cmd/virt-freezer \
    cmd/virt-handler \
    cmd/virt-launcher \
    cmd/virt-launcher-monitor \
    cmd/virt-operator \
    cmd/virt-probe \
    cmd/virt-tail \
    cmd/virtctl 

env DOCKER_PREFIX=$reg_path DOCKER_TAG=%version KUBEVIRT_NO_BAZEL=true ./hack/build-manifests.sh

popd

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
export GOFLAGS="-mod=vendor"

export BUILDDIR="$PWD/.build/src/%import_path"
mkdir -p %buildroot%_bindir

install -p -m 0755 $BUILDDIR/_out/cmd/container-disk-v2alpha/container-disk %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virtctl/virtctl %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-api/virt-api %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-controller/virt-controller %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-chroot/virt-chroot %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-exportproxy/virt-exportproxy %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-exportserver/virt-exportserver %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-handler/virt-handler %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-launcher/virt-launcher %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-launcher-monitor/virt-launcher-monitor %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-freezer/virt-freezer %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-probe/virt-probe %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-tail/virt-tail %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/cmd/virt-operator/virt-operator %buildroot%_bindir/
install -p -m 0755 $BUILDDIR/_out/tests/tests.test %buildroot%_bindir/virt-tests
install -p -m 0755 $BUILDDIR/cmd/virt-launcher/node-labeller/node-labeller.sh %buildroot%_bindir/

# Install network stuff
mkdir -p %buildroot%_datadir/kube-virt/virt-handler
install -p -m 0644 $BUILDDIR/cmd/virt-handler/nsswitch.conf %buildroot%_datadir/kube-virt/virt-handler/

# virt-launcher qemu.conf
mkdir -p %buildroot%_datadir/kube-virt/virt-launcher
install -p -m 0644 $BUILDDIR/cmd/virt-launcher/virtqemud.conf %buildroot%_datadir/kube-virt/virt-launcher/
install -p -m 0644 $BUILDDIR/cmd/virt-launcher/qemu.conf %buildroot%_datadir/kube-virt/virt-launcher/

# virt-launcher SELinux policy needs to land in virt-handler container
install -p -m 0644 $BUILDDIR/cmd/virt-handler/virt_launcher.cil %buildroot%_datadir/kube-virt/virt-handler/

# Persistent reservation helper configuration files
mkdir -p %buildroot%_datadir/kube-virt/pr-helper
install -p -m 0644 $BUILDDIR/cmd/pr-helper/multipath.conf %buildroot%_datadir/kube-virt/pr-helper/

# Install release manifests
mkdir -p %buildroot%_datadir/kube-virt/manifests/release
install -m 0644 $BUILDDIR/_out/manifests/release/kubevirt-operator.yaml %buildroot%_datadir/kube-virt/manifests/release/
install -m 0644 $BUILDDIR/_out/manifests/release/kubevirt-cr.yaml %buildroot%_datadir/kube-virt/manifests/release/

# Install manifests for testing
mkdir -p %buildroot%_datadir/kube-virt/manifests/testing
install -m 0644 $BUILDDIR/_out/manifests/testing/rbac-for-testing.yaml %buildroot%_datadir/kube-virt/manifests/testing/
install -m 0644 $BUILDDIR/_out/manifests/testing/uploadproxy-nodeport.yaml %buildroot%_datadir/kube-virt/manifests/testing/
install -m 0644 $BUILDDIR/_out/manifests/testing/disks-images-provider.yaml %buildroot%_datadir/kube-virt/manifests/testing/
# The generated disks-images-provider.yaml refers to nonexistent container
# images. Overwrite it with the upstream version for testing.
install -m 0644 $BUILDDIR/tests/default-config.json %buildroot%_datadir/kube-virt/manifests/testing/

#pre virt-handler virt-launcher
#special system user and group are created directly in application container

%files virtctl
%doc README.md LICENSE
%_bindir/virtctl

%files virt-api
%doc README.md LICENSE
%_bindir/virt-api

%files container-disk
%doc README.md LICENSE
%_bindir/container-disk

%files virt-controller
%doc README.md LICENSE
%_bindir/virt-controller

%files virt-exportproxy
%doc README.md LICENSE
%_bindir/virt-exportproxy

%files virt-exportserver
%doc README.md LICENSE
%_bindir/virt-exportserver

%files virt-handler
%doc README.md LICENSE
%dir %_datadir/kube-virt
%dir %_datadir/kube-virt/virt-handler
%_bindir/virt-handler
%_bindir/virt-chroot
%_datadir/kube-virt/virt-handler/*

%files virt-launcher
%doc README.md LICENSE
%dir %_datadir/kube-virt/virt-launcher/
%_bindir/virt-launcher
%_bindir/virt-launcher-monitor
%_bindir/virt-freezer
%_bindir/virt-probe
%_bindir/virt-tail
%_bindir/node-labeller.sh
%_datadir/kube-virt/virt-launcher/*


%files virt-operator
%doc README.md LICENSE
%_bindir/virt-operator

%files pr-helper-conf
%doc README.md LICENSE
%dir %_datadir/kube-virt
%dir %_datadir/kube-virt/pr-helper/
%_datadir/kube-virt/pr-helper/*

%files manifests
%doc README.md LICENSE
%dir %_datadir/kube-virt
%dir %_datadir/kube-virt/manifests
%_datadir/kube-virt/manifests/release

%files tests
%doc README.md LICENSE
%dir %_datadir/kube-virt
%dir %_datadir/kube-virt/manifests
%_bindir/virt-tests
%_datadir/kube-virt/manifests/testing

%changelog
* Tue Oct 22 2024 Nadezhda Fedorova <fedor@altlinux.org> 1.3.1-alt1
- Initial version (thanks opensuse for the spec).
