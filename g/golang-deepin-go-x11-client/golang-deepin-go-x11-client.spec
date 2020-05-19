# Run tests in check section
# disable for bootstrapping
%def_without check

%global goipath github.com/linuxdeepin/go-x11-client

Name: golang-deepin-go-x11-client
Version: 0.6.0
Release: alt1
Summary: A X11 client Go bindings for Deepin Desktop Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/go-x11-client
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: go-x11-client-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: golang-x-text-devel golang-gopkg-check-1-devel golang-github-stretchr-testify-devel
# BuildRequires: golang-deepin-go-lib-devel
# BuildRequires: golang(gopkg.in/check.v1) golang(golang.org/x/text/encoding/charmap) golang(github.com/stretchr/testify/assert)

%description
%summary.

%package devel
Summary: %summary
Group: Graphical desktop/Other
BuildArch: noarch

%description devel
%summary.

This package contains library source intended for
building other packages which use import path with
%goipath prefix.

%prep
%setup -n go-x11-client-%version
# remove debian files
rm -rf debian/
# undefined python scripts
sed -i -e '1 s|^|#!/usr/bin/env python3\n\n|;' tools/*.py

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in tools/*; do
%golang_build $cmd ||:
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

# %%files
# %%_bindir/*

%files devel
%doc README LICENSE
%go_path/src/%goipath

%changelog
* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.6.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

