%global import_path google.golang.org/protobuf
%define _unpackaged_files_terminate_build 1

Name:    protobuf-go
Version: 1.36.12
Release: alt1

Summary: Go support for Google's protocol buffers
License: BSD-3-Clause
Group:   Development/Other
Url:     https://protobuf.dev/
Vcs:     https://go.googlesource.com/protobuf

Source: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.23

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
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-trimpath"
export LDFLAGS="-buildid="
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build cmd/protoc-gen-go

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
%golang_install

%check
%gotest ./...

%files
%doc README.md LICENSE
%_bindir/protoc-gen-go

%changelog
* Wed Aug 12 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.36.12-alt1
- New version 1.36.12.

* Wed Aug 05 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.36.11-alt1
- New version 1.36.11.
- Enable tests.

* Mon Aug 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.34.2-alt1
- Initial build.

