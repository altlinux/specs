%global _unpackaged_files_terminate_build 1
%global import_path kubevirt.io/containerized-data-importer

# git rev-parse v1.64.0^{commit}
%global rev_commit 58b908c6731c55da28e02ee5034d7d3fbb9be2e3

Name:    kubevirt-cdi
Version: 1.64.0
Release: alt1

Summary: Data Import Service for kubernetes, designed with kubevirt in mind
License: Apache-2.0
Group:   System/Configuration/Other
URL:     https://github.com/kubevirt/containerized-data-importer
Vcs:     https://github.com/kubevirt/containerized-data-importer

ExcludeArch: %ix86

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.23
BuildRequires: gcc
BuildRequires: /proc
BuildRequires: pkgconfig(libnbd)

%description
Containerized-Data-Importer (CDI) is a persistent storage management add-on
for Kubernetes. It's primary goal is to provide a declarative way to build
Virtual Machine Disks on PVCs for Kubevirt VMs.

CDI works with standard core Kubernetes resources and is storage device
agnostic, while its primary focus is to build disk images for Kubevirt,
it's also useful outside of a Kubevirt context to use for initializing
your Kubernetes Volumes with data.

%package -n cdi-apiserver
Summary: CDI API server for validation and upload token handling
Group:   System/Configuration/Other
%description -n cdi-apiserver
The CDI API server is a core component of the Containerized Data
Importer (CDI) for KubeVirt. It exposes an aggregated Kubernetes API
used for admission validation of CDI custom resources and for issuing
short-lived upload tokens that authorize clients to upload disk images
into PersistentVolumeClaims through the upload proxy.

%package -n cdi-cloner
Summary: CDI cloner that copies data between PersistentVolumeClaims
Group:   System/Configuration/Other
%description -n cdi-cloner
The CDI cloner is a worker component of the Containerized Data Importer
(CDI) used to clone the contents of an existing PersistentVolumeClaim
into a new one. It supports both host-assisted (smart) cloning via
CSI snapshot/clone capabilities and fallback pod-based cloning through
a network data transfer when the storage backend does not support
smart cloning.

%package -n cdi-controller
Summary: CDI controller managing DataVolume and PVC population lifecycle
Group:   System/Configuration/Other
%description -n cdi-controller
The CDI controller is the main reconciliation loop of the Containerized
Data Importer (CDI). It watches DataVolume, PersistentVolumeClaim, and
related custom resources, and orchestrates the pods and jobs needed to
populate PersistentVolumeClaims with data from HTTP/S3 sources,
container registries, cloned volumes, or client uploads.

%package -n cdi-importer
Summary: CDI importer that populates a PVC with data from an external source
Group:   System/Configuration/Other
%description -n cdi-importer
The CDI importer is a short-lived worker component of the Containerized
Data Importer (CDI). It runs inside a pod attached to a target
PersistentVolumeClaim and streams data into it from the configured
source - an HTTP/S3 URL, a container registry disk image, an uploaded
stream, or an external virtualization platform via a volume populator -
converting and resizing the disk image as required.

%package -n cdi-operator
Summary: CDI operator managing installation and lifecycle of CDI
Group:   System/Configuration/Other
%description -n cdi-operator
The CDI operator installs, upgrades, and manages the lifecycle of the
Containerized Data Importer (CDI) components on a Kubernetes cluster.
It reconciles the CDI custom resource, deploying and configuring the
controller, API server, upload proxy, and supporting infrastructure
required to populate PersistentVolumeClaims with virtual machine disk
images and other data.

%package -n cdi-uploadproxy
Summary: CDI upload proxy for client-initiated disk image uploads
Group:   System/Configuration/Other
%description -n cdi-uploadproxy
The CDI upload proxy is a front-facing component of the Containerized
Data Importer (CDI). It authenticates upload requests using tokens
issued by the CDI API server and forwards the incoming disk image
stream to the appropriate cdi-uploadserver pod bound to the target
PersistentVolumeClaim.

%package -n cdi-uploadserver
Summary: CDI upload server that writes an uploaded disk image into a PVC
Group:   System/Configuration/Other
%description -n cdi-uploadserver
The CDI upload server is a worker component of the Containerized Data
Importer (CDI). It runs alongside a target PersistentVolumeClaim,
accepts an authenticated disk image stream forwarded by the upload
proxy, and writes the converted image data directly into the volume.

%package -n openstack-populator
Summary: Volume populator that imports a disk image from OpenStack
Group:   System/Configuration/Other
%description -n openstack-populator
The OpenStack volume populator is a CDI/Forklift component that
populates a PersistentVolumeClaim with a virtual machine disk image
retrieved from an OpenStack environment (Cinder volumes or Glance
images). It is driven by an OpenstackVolumePopulator custom resource
and is used during migration of virtual machines from OpenStack into
KubeVirt.

%package -n ovirt-populator
Summary: Volume populator that imports a disk image from oVirt/RHV
Group:   System/Configuration/Other
%description -n ovirt-populator
The oVirt volume populator is a CDI/Forklift component that populates
a PersistentVolumeClaim with a virtual machine disk image retrieved
from an oVirt or Red Hat Virtualization (RHV) environment. It is driven
by an OvirtVolumePopulator custom resource and is used during migration
of virtual machines from oVirt/RHV into KubeVirt.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath"
export CGO_CFLAGS="-std=gnu17"

# 1788792900: git show -s --format=format:%ct HEAD (see hack/build/version.sh)
BUILD_DATE="$(date --date=@1788792900 -u +'%Y-%m-%dT%H:%M:%SZ')"
export LDFLAGS="-X %import_path/pkg/version.gitVersion=v%version \
                -X %import_path/pkg/version.gitCommit=%rev_commit \
                -X %import_path/pkg/version.gitTreeState=clean \
                -X %import_path/pkg/version.buildDate=$BUILD_DATE \
                -buildid="

%golang_prepare
%golang_build ./cmd/*

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
export CGO_CFLAGS="-std=gnu17"
%gotest -v $(go list ./... | grep -Ev '^%import_path/(pkg/(uploadserver|system|importer)|tests)$')

%files
%doc LICENSE README.md

%files -n cdi-apiserver
%_bindir/cdi-apiserver

%files -n cdi-cloner
%_bindir/cdi-cloner

%files -n cdi-controller
%_bindir/cdi-controller

%files -n cdi-importer
%_bindir/cdi-importer

%files -n cdi-operator
%_bindir/cdi-operator

%files -n cdi-uploadproxy
%_bindir/cdi-uploadproxy

%files -n cdi-uploadserver
%_bindir/cdi-uploadserver

%files -n openstack-populator
%_bindir/openstack-populator

%files -n ovirt-populator
%_bindir/ovirt-populator

%changelog
* Fri Sep 04 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.64.0-alt1
- Initial build for ALT.
