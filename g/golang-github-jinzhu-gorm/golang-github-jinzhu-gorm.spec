%def_without check

%global goipath github.com/jinzhu/gorm

Name: golang-github-jinzhu-gorm
Version: 1.9.15
Release: alt1
Summary: The fantastic ORM library for Golang, aims to be developer friendly
Group: Development/Other
License: MIT
Url: https://github.com/jinzhu/gorm
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/gorm-%version.tar.gz
Source1: glide.yaml
Source2: glide.lock

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(github.com/denisenkom/go-mssqldb) golang(github.com/erikstmartin/go-testdb) golang(github.com/go-sql-driver/mysql) golang(github.com/jinzhu/inflection) golang(github.com/jinzhu/now) golang(github.com/lib/pq) golang(github.com/lib/pq/hstore) golang(github.com/mattn/go-sqlite3)
BuildRequires: golang-github-sql-driver-mysql-devel golang-github-mattn-sqlite3-devel golang-github-lib-pq-devel golang-github-jinzhu-now-devel golang-github-jinzhu-inflection-devel golang-github-erikstmartin-testdb-devel golang-github-denisenkom-mssqldb-devel

%description
The fantastic ORM library for Golang, aims to be developer friendly.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
The fantastic ORM library for Golang, aims to be developer friendly.

%prep
%setup -n gorm-%version
cp %SOURCE1 %SOURCE2 .

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
%doc License README.md
%go_path/src/%goipath

%changelog
* Fri Aug 07 2020 Leontiy Volodin <lvol@altlinux.org> 1.9.15-alt1
- New version.

* Tue Jun 02 2020 Leontiy Volodin <lvol@altlinux.org> 1.9.8-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
