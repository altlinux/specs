%def_without check

%global goipath github.com/mattn/go-sqlite3

Name: golang-github-mattn-sqlite3
Version: 2.0.6
Release: alt1
Summary: Sqlite3 driver for go using database/sql
Group: Graphical desktop/Other
License: MIT
Url: https://github.com/mattn/go-sqlite3
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/go-sqlite3-%version.tar.gz
Source1: glide.yaml
Source2: glide.lock

BuildRequires(pre): rpm-build-golang

%description
Package Sqlite3 provides interface to SQLite3 databases.

%package devel
Summary: Sqlite3 driver for go using database/sql
Group: Development/Other
BuildArch: noarch

%description devel
Package Sqlite3 provides interface to SQLite3 databases.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name.

%prep
%setup -n go-sqlite3-%version
cp -a %SOURCE1 %SOURCE2 .

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
%gotest
%endif

%files devel
%doc LICENSE README.md
%go_path/src/%goipath
%exclude %go_path/src/%goipath/_example

%files examples
%go_path/src/%goipath/_example

%changelog
* Mon Feb 01 2021 Leontiy Volodin <lvol@altlinux.org> 2.0.6-alt1
- New version (2.0.6).

* Tue May 19 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.5-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

