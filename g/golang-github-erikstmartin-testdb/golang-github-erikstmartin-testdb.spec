%def_with check

%global goipath         github.com/erikstmartin/go-testdb
%global commit          8d10e4a1bae52cd8b81ffdec3445890d6dccab3d

Name: golang-github-erikstmartin-testdb
Version: 0
Release: alt1.git8d10e4a
Summary: Framework for stubbing responses from Go's driver.Driver interface
Group: Development/Other
License: BSD-2-Clause
Url: https://github.com/erikstmartin/go-testdb
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: go-testdb-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Framework for stubbing responses from Go's driver.Driver interface.

This can be used to sit in place of your sql.Db so that you can stub responses
for sql calls, and remove database dependencies for your test suite.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Framework for stubbing responses from Go's driver.Driver interface.

This can be used to sit in place of your sql.Db so that you can stub responses
for sql calls, and remove database dependencies for your test suite.

%prep
%setup -n go-testdb-%version

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
%doc LICENSE README.md
%go_path/src/%goipath

%changelog
* Tue Jun 02 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git8d10e4a
- Initial build for ALT Sisyphus (thanks fedora for this spec).
