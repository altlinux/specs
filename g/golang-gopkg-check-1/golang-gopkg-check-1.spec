%def_without check

# https://github.com/go-check/check
%global goipath         gopkg.in/check.v1
#global goipath         github.com/check.v1
%global forgeurl        https://github.com/go-check/check
%global commit          41f04d3bba152ddec2103e299fed053415705330

Name: golang-gopkg-check-1
Version: 1
Release: alt1.git41f04d3
Summary: Rich testing for the Go language

# Upstream license specification: BSD-2-Clause
License: BSD-2-Clause and BSD-3-Clause
Group: Development/Other
Url: https://labix.org/gocheck
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: check-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: golang-github-kr-pretty-devel

%description
Rich testing for the Go language.

%package devel
Summary: Rich testing for the Go language
Group: Development/Other
BuildArch: noarch

%description devel
Rich testing for the Go language.

%prep
%setup -n check-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path:$BUILDDIR"

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
%go_path/src/%goipath

%changelog
* Mon Mar 23 2020 Leontiy Volodin <lvol@altlinux.org> 1-alt1.git41f04d3
- Initial build for ALT Sisyphus (thanks fedora for this spec).

