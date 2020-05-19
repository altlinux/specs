%def_without check

%global goipath         gopkg.in/errgo.v2
%global forgeurl        https://github.com/go-errgo/errgo

Name: golang-gopkg-errgo-2
Version: 2.1.0
Release: alt1
Summary: Dependable Go errors with tracebacks
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/go-errgo/errgo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: errgo-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
The Errgo package provides a way to create and diagnose errors. It is compatible
with the usual Go error idioms but adds a way to wrap errors so that they record
source location information while retaining a consistent way for code to inspect
errors to find out particular problems.

%package devel
Summary: Dependable Go errors with tracebacks
Group: Development/Other
BuildArch: noarch

%description devel
The Errgo package provides a way to create and diagnose errors. It is compatible
with the usual Go error idioms but adds a way to wrap errors so that they record
source location information while retaining a consistent way for code to inspect
errors to find out particular problems.

%prep
%setup -n errgo-%version

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

%check
%if_with check
export GOPATH="%go_path"
%gotest
%endif

%files devel
%doc README.md LICENSE
%go_path/src/%goipath

%changelog
* Thu Apr 30 2020 Leontiy Volodin <lvol@altlinux.org> 2.1.0-alt1
- Initial build for ALT SIsyphus (thanks fedora for this spec).

