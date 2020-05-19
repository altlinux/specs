%def_without check

%global goipath github.com/sqs/goreturns
%global commit  538ac601451833c7c4449f8431d65d53c1c60e41

Name: golang-github-sqs-goreturns
Version: 0
Release: alt1.git538ac60
Summary: A gofmt/goimports-like tool for Go programmers that fills in Go return statements with zero values to match the func return types
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/sqs/goreturns.git
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: goreturns-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: golang(golang.org/x/tools/imports)

%description
%summary.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%package samples
Summary: Samples for %name
Group: Development/Other
BuildArch: noarch

%description samples
This package provides samples for %name.

%prep
%setup -n goreturns-%version

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
%exclude %go_path/src/%goipath/_samples

%files samples
%go_path/src/%goipath/_samples

%changelog
* Fri Jun 05 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git538ac60
- Initial build for ALT Sisyphus.

