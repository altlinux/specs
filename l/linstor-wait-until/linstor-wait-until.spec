%global import_path github.com/LINBIT/linstor-wait-until
%define _unpackaged_files_terminate_build 1

Name:    linstor-wait-until
Version: 0.3.3
Release: alt1

Summary: Waits until a specific component of LINSTOR is online and usable
License: Apache-2.0
Group:   Other
Url:     https://github.com/LINBIT/linstor-wait-until

Source: %name-%version.tar
Patch:   %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: golang rpm-build-golang

%description
Waits until a specific component of LINSTOR is online and usable.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.Version=%version"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Thu Mar 19 2026 Nadezhda Fedorova <fedor@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus.
