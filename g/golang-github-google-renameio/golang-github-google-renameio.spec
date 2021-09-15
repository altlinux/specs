%def_without check

# https://github.com/google/renameio
%global goipath         github.com/google/renameio

Name: golang-github-google-renameio
Version: 1.0.1
Release: alt1.git2c2b6aa
Summary: Atomically create or replace a file or symbolic link

License: Apache-2.0
Group: Development/Other
Url: https://github.com/google/renameio
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: renameio-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Package Renameio provides a way to atomically create or replace a file or
symbolic link.

%package devel
Summary: Atomically create or replace a file or symbolic link
Group: Development/Other
BuildArch: noarch

%description devel
Package Renameio provides a way to atomically create or replace a file or
symbolic link.

%prep
%setup -n renameio-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

go mod tidy -go=1.17
%golang_prepare

cd .build/src/%goipath
%golang_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
%gotest
%endif

%files devel
%doc LICENSE CONTRIBUTING.md README.md
%go_path/src/%goipath

%changelog
* Wed Sep 15 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.1-alt1.git2c2b6aa
- New version (1.0.1).
- Built from commit 2c2b6aa5ac77d68d62173bf059243321ab26b3a8.
- Fixed build with golang 1.17.

* Tue Dec 22 2020 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- New version (1.0.0).

* Wed Apr 29 2020 Leontiy Volodin <lvol@altlinux.org> 0.1.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

