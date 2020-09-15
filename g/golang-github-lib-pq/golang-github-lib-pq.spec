%def_without check

%global goipath         github.com/lib/pq

Name: golang-github-lib-pq
Version: 1.8.0
Release: alt1
Summary: Pure Go postgres driver for database/sql
Group: Development/Other
License: MIT
Url: https://github.com/lib/pq
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/pq-%version.tar.gz
Source1: glide.yaml
Source2: glide.lock
# https://github.com/lib/pq/pull/943
Patch: 0001-Skip-TestCloseBadConn-if-PGHOST-is-a-Unix-domain-soc.patch

BuildRequires(pre): rpm-build-golang
# BuildRequires:  postgresql-test-rpm-macros

%description
A pure Go postgres driver for Go's database/sql package.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
A pure Go postgres driver for Go's database/sql package.

%prep
%setup -n pq-%version
%patch -p1
cp %SOURCE1 %SOURCE2 .
mv certs/README certs-README

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
# %%postgresql_tests_run
# export PGUSER=$(id -un) PGPASSWORD=$(id -un) PGDATABASE=$(id -un)
%gotest
%endif

%files devel
%doc LICENSE.md example README.md TESTS.md
%go_path/src/%goipath

%changelog
* Tue Sep 15 2020 Leontiy Volodin <lvol@altlinux.org> 1.8.0-alt1
- New version.

* Tue Jun 02 2020 Leontiy Volodin <lvol@altlinux.org> 1.3.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
