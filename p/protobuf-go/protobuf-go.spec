%global import_path google.golang.org/protobuf

Name: protobuf-go
Version: 1.34.2
Release: alt1

Summary: Go support for Google's protocol buffers
License: BSD-3-Clause
Group: Development/Other
Url: https://protobuf.dev/
Vcs: https://github.com/protocolbuffers/protobuf-go.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.20
Provides: protoc-gen-go = %EVR

%description
This project hosts the Go implementation for protocol buffers,
which is a language-neutral, platform-neutral, extensible mechanism
for serializing structured data. The protocol buffer language is a language
for specifying the schema for structured data. This schema is compiled
into language specific bindings. This project provides both a tool
to generate Go code for the protocol buffer language, and also the runtime
implementation to handle serialization of messages in Go.

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
%golang_build cmd/protoc-gen-go

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md LICENSE
%_bindir/*

%changelog
* Mon Aug 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.34.2-alt1
- Initial build.

