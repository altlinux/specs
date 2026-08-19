%global _unpackaged_files_terminate_build 1
%global __find_debuginfo_files %nil

Name: typescript-go
Version: 7.0.2
Release: alt1

Summary: Native port of the TypeScript compiler and toolset (tsgo)
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/microsoft/typescript-go
Vcs: https://github.com/microsoft/typescript-go.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Provides: tsgo = %EVR

%description
tsgo is a native port of the TypeScript compiler (tsc) and language
server to Go, developed by Microsoft as the basis of TypeScript 7.
It provides much faster type checking and editor responsiveness while
staying compatible with the JavaScript implementation of TypeScript.

The package installs the tsgo binary, a drop-in replacement for tsc
that also provides an LSP server (tsgo --lsp).

%prep
%setup -a1

%build
export GOFLAGS="-mod=vendor -trimpath"
go build -ldflags='-s -w' -o built/tsgo ./cmd/tsgo

%install
install -Dpm0755 built/tsgo %buildroot%_bindir/tsgo

%check
built/tsgo --version

%files
%doc README.md LICENSE NOTICE.txt
%_bindir/tsgo

%changelog
* Wed Aug 19 2026 Anton Farygin <rider@altlinux.org> 7.0.2-alt1
- Initial build for Sisyphus.
