%def_without check

%global goipath         github.com/fsnotify/fsnotify
%global goaltipaths     gopkg.in/fsnotify/fsnotify.v1 gopkg.in/fsnotify/v1/fsnotify

Name: golang-github-fsnotify
Version: 1.5.1
Release: alt1
Summary: Cross-platform file system notifications for Go
Group: Development/Other
License: BSD-3-Clause
Url: https://fsnotify.org/
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: https://github.com/fsnotify/fsnotify/archive/%version/fsnotify-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: golang-golang-x-sys-devel

%description
Cross-platform file system notifications for Go.

%package devel
Summary: Cross-platform file system notifications for Go
Group: Development/Other
BuildArch: noarch

%description devel
Cross-platform file system notifications for Go.

This package provides development files for %name.

%prep
%setup -n fsnotify-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
%golang_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

%files devel
%doc LICENSE AUTHORS CHANGELOG.md CONTRIBUTING.md README.md
%go_path/src/%goipath

%changelog
* Mon Sep 06 2021 Leontiy Volodin <lvol@altlinux.org> 1.5.1-alt1
- New version (1.5.1).

* Wed Sep 09 2020 Leontiy Volodin <lvol@altlinux.org> 1.4.9-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
