%define _unpackaged_files_terminate_build 1
%global import_path github.com/siderolabs/talos
%global commit      5cc935f74b9183c36ffab7b7faae8e955178836b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define _libexecdir %_prefix/libexec

Name: talos
Version: 1.8.0
Release: alt1

Summary: A modern OS for Kubernetes
License: MPL-2.0
Group: System/Configuration/Boot and Init
Url: https://www.talos.dev/
Vcs: https://github.com/siderolabs/talos.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.22
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
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-w"
export TAGS="tcell_minimal,grpcnotrace"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

#export NAME=Talos
export SHA=%shortcommit
#TODO: switch to registry.altlinux.org
#export USERNAME=siderolabs
#export REGISTRY=ghcr.io
#export EXTRAS=v1.7.0-2-g7c627a8
#export PKGS=v1.7.0-21-gc58ed7f
export TAG=v%version

#echo -n ${NAME} > pkg/machinery/gendata/data/name
echo -n ${SHA} > pkg/machinery/gendata/data/sha
#echo -n ${USERNAME} > pkg/machinery/gendata/data/username
#echo -n ${REGISTRY} > pkg/machinery/gendata/data/registry
#echo -n ${EXTRAS} > pkg/machinery/gendata/data/extras
#echo -n ${PKGS} > pkg/machinery/gendata/data/pkgs
echo -n ${TAG} > pkg/machinery/gendata/data/tag
#echo -n ${ARTIFACTS} > pkg/machinery/gendata/data/artifacts

#protoc -Iapi -Iapi/vendor/ -I/usr/include \
#  --go_out=paths=source_relative:api --go-grpc_out=paths=source_relative:api \
#  --go-vtproto_out=paths=source_relative:api --go-vtproto_opt=features=marshal+unmarshal+size \
#  api/common/common.proto


%golang_prepare
%golang_build cmd/installer
%golang_build cmd/talosctl
%golang_build internal/app/init
%golang_build internal/app/machined

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
* Sun Sep 29 2024 Alexey Shabalin <shaba@altlinux.org> 1.8.0-alt1
- Initial build.

