# SPEC file for kepubify
#

%global import_path github.com/pgaskin/kepubify

Name:     kepubify
Version:  3.1.6
Release:  alt1

Summary:  EPUBs to KEPUBs converter

Group:    System/Servers
License:  %mit
URL:      https://pgaskin.net/kepubify/
#URL:      https://github.com/pgaskin/kepubify
Packager: Nikolay Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Source1: vendor.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-golang

%description
Kepubify converts EPUBs to KEPUBs (ePub eBook format extension
used by Kobobooks readers).

This package also includes two standalone utilities which
do not depend on kepubify (and don't conflict with Calibre):
- covergen (which pre-generates cover images), and
- seriesmeta (which updates Calibre or EPUB3 series metadata).


%prep
%setup  -n %name-%version
%patch0 -p1

tar xf %SOURCE1

%build
export GO111MODULE=auto
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/kepubify
%golang_build cmd/covergen
%golang_build cmd/seriesmeta


%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install


%files
%doc README.md LICENSE.md docs/

%_bindir/*

%changelog
* Mon Jun 28 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.1.6-alt1
- Initial build for ALT Linux Sisyphus

