%def_without check

%global goipath         github.com/go-sql-driver/mysql

Name: golang-github-sql-driver-mysql
Version: 1.5.0
Release: alt1
Summary: MySQL driver for Go's database/sql package
Group: Development/Other
License: MPL-2.0
Url: https://github.com/go-sql-driver/mysql
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/mysql-%version.tar.gz
Source1: glide.yaml
Source2: glide.lock

BuildRequires(pre): rpm-build-golang

%description
A MySQL-Driver for Go's database/sql package.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
A MySQL-Driver for Go's database/sql package.

%prep
%setup -n mysql-%version
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
export GOPATH="%go_path"
%gotest
%endif

%files devel
%doc LICENSE AUTHORS CHANGELOG.md README.md
%go_path/src/%goipath

%changelog
* Fri Aug 07 2020 Leontiy Volodin <lvol@altlinux.org> 1.5.0-alt1
- New version.
- Disabled tests.

* Tue Jun 02 2020 Leontiy Volodin <lvol@altlinux.org> 1.4.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
