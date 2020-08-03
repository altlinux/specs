%def_without check

%global goipath github.com/davecgh/go-spew

Name: golang-github-davecgh-spew
Version: 1.1.1
Release: alt1
Summary: Implements a deep pretty printer for go data structures to aid in debugging
Group: Development/Other
License: ISC
Url: https://github.com/davecgh/go-spew
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/go-spew-%version.tar.gz
Source1: glide.lock
Source2: glide.yaml

BuildRequires(pre): rpm-build-golang

%description
Go-spew implements a deep pretty printer for Go data structures to aid in
debugging. A comprehensive suite of tests with 100 percent test coverage is
provided to ensure proper functionality.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%prep
%setup -n go-spew-%version
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
%doc LICENSE README.md test_coverage.txt
%go_path/src/%goipath

%changelog
* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 1.1.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

