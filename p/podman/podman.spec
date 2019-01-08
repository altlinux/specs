%global import_path github.com/containers/libpod
Name:     podman
Version:  0.12.1.2
Release:  alt1

Summary:  Manage pods, containers, and container images
License:  Apache-2.0
Group:    System/Configuration/Other
# https://github.com/containers/libpod
Url:      https://podman.io/

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Patch1: makefile_remove_dev_stdin_usage.patch
Patch2: makefile_not_create_link_docs.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-md2man
BuildRequires: libseccomp-devel glib2-devel libgpgme-devel libbtrfs-devel
BuildRequires: libgio-devel libostree-devel libselinux-devel libdevmapper-devel
BuildRequires: libassuan-devel

Requires: conmon cni cni-plugins containers-common

%description
%summary.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

PODMAN_VERSION=%version make PREFIX=%buildroot%_prefix ETCDIR=%buildroot%_sysconfdir \
    install.man \
    install.cni

install -Dm 644 cni/87-podman-bridge.conflist %buildroot%_sysconfdir/cni/net.d/87-podman-bridge.conflist
install -Dm 644 completions/bash/%name %buildroot/%_sysconfdir/bash_completion.d/%name
install -Dm 644 libpod.conf %buildroot%_datadir/containers/libpod.conf

%files
%_bindir/*
%_datadir/containers/libpod.conf
%_sysconfdir/cni/net.d/87-podman-bridge.conflist
%_sysconfdir/bash_completion.d/%name
%_man1dir/*
%_man5dir/*
%doc *.md

%changelog
* Mon Jan 07 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.1.2-alt1
- Initial build for Sisyphus
