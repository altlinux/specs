%global import_path google.golang.org/grpc

Name: grpc-go
Version: 1.5.1
Release: alt1

Summary: The Go implementation of gRPC
License: Apache-2.0
Group: Development/Other
Url: https://grpc.io
Vcs: https://github.com/grpc/grpc-go.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.21

%description
The Go implementation of gRPC: A high performance, open source, general
RPC framework that puts mobile and HTTP/2 first.

%package -n protoc-gen-go-grpc
Summary: gRPC bindings generator for Go language
Group: Development/Other

%description -n protoc-gen-go-grpc
This tool generates Go language bindings of service in protobuf definition
files for gRPC.

%prep
%setup
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-w"
export TAGS="protolegacy"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build cmd/protoc-gen-go-grpc

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
%golang_install

%files -n protoc-gen-go-grpc
%doc README.md LICENSE
%_bindir/*

%changelog
* Mon Aug 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.5.1-alt1
- Initial build.

