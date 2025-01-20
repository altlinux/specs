%global import_path github.com/google/go-containerregistry
%global _unpackaged_files_terminate_build 1

Name:    go-containerregistry
Version: 0.20.2
Release: alt1

Summary: This is a golang library for working with container registries
License: Apache-2.0
Group:   Development/Other
Url:     https://github.com/google/go-containerregistry

Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.23.0
BuildRequires: /proc

%description
The overarching design philosophy of this library is to define
interfaces that present an immutable view of resources (e.g. Image,
Layer, ImageIndex), which can be backed by a variety of medium
(e.g. registry, tarball, daemon, ...).

%package        crane
Summary:        Tool for interacting with remote images and registries
Group:          Other

%description    crane
Tool for interacting with remote images and registries.

%package        gcrane
Summary:        Is a GCR-specific variant of crane
Group:          Other

%description    gcrane
Gcrane is a GCR-specific variant of crane that has richer output for
the ls subcommand and some basic garbage collection support.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor -buildmode=pie -trimpath"

%golang_prepare

%golang_build ./cmd/crane
%golang_build ./cmd/gcrane

$BUILDDIR/bin/crane completion bash > crane.bash
$BUILDDIR/bin/crane completion zsh > crane.zsh
$BUILDDIR/bin/crane completion fish > crane.fish

$BUILDDIR/bin/gcrane completion bash > gcrane.bash
$BUILDDIR/bin/gcrane completion zsh > gcrane.zsh
$BUILDDIR/bin/gcrane completion fish > gcrane.fish

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dm 644 crane.bash %buildroot%_datadir/bash-completion/completions/crane
install -Dm 644 crane.zsh %buildroot%_datadir/zsh/site-functions/_crane
install -Dm 644 crane.fish %buildroot%_datadir/fish/vendor_completions.d/crane.fish

install -Dm 644 gcrane.bash %buildroot%_datadir/bash-completion/completions/gcrane
install -Dm 644 gcrane.zsh %buildroot%_datadir/zsh/site-functions/_gcrane
install -Dm 644 gcrane.fish %buildroot%_datadir/fish/vendor_completions.d/gcrane.fish

%files crane
%doc README.md SECURITY.md CONTRIBUTING.md
%_bindir/crane
%_datadir/bash-completion/completions/crane
%_datadir/zsh/site-functions/_crane
%_datadir/fish/vendor_completions.d/crane.fish

%files gcrane
%doc README.md SECURITY.md CONTRIBUTING.md
%_bindir/gcrane
%_datadir/bash-completion/completions/gcrane
%_datadir/zsh/site-functions/_gcrane
%_datadir/fish/vendor_completions.d/gcrane.fish

%changelog
* Tue Dec 17 2024 Nadezhda Fedorova <fedor@altlinux.org> 0.20.2-alt1
- Initial build for ALTLinux.
