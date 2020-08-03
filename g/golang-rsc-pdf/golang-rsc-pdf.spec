%def_without check

%global goipath         rsc.io/pdf
%global forgeurl        https://github.com/rsc/pdf

Name: golang-rsc-pdf
Version: 0.1.1
Release: alt1
Summary: PDF reader library in Go
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/rsc/pdf
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: pdf-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
PDF reader library in Go.

%package devel
Summary: PDF reader library in Go
Group: Development/Other
BuildArch: noarch

%description devel
PDF reader library in Go.

%prep
%setup -n pdf-%version

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
* Fri May 8 2020 Leontiy Volodin <lvol@altlinux.org> 0.1.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

