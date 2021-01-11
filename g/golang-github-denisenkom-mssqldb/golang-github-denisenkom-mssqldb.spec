%def_without check

%global goipath github.com/denisenkom/go-mssqldb

Name: golang-github-denisenkom-mssqldb
Version: 0.9.0
Release: alt1.pre1
Summary: Microsoft SQL server driver written in Go language
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/denisenkom/go-mssqldb
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/go-mssqldb-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(cloud.google.com/go/civil)
# BuildRequires: golang(golang.org/x/crypto/md4)
BuildRequires: golang-golang-x-crypto-devel

%description
Package Mssql implements the TDS protocol used to connect to MS SQL Server
database servers.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Package Mssql implements the TDS protocol used to connect to MS SQL Server
database servers.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name.

%prep
%setup -n go-mssqldb-%version

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
%doc LICENSE.txt doc README.md
%go_path/src/%goipath
%exclude %go_path/src/%goipath/examples

%files examples
%go_path/src/%goipath/examples

%changelog
* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.0-alt1.pre1
- New version (pre-release 0.9.0).

* Tue Jun 02 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git731ef37
- Initial build for ALT Sisyphus (thanks fedora for this spec).
