%def_without check

%global goipath         github.com/pmezard/go-difflib

Name: golang-github-pmezard-difflib
Version: 1.0.0
Release: alt1
Summary: Partial port of python difflib package to Go
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/pmezard/go-difflib
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/go-difflib-%version.tar.gz
Source1: glide.yaml
Source2: glide.lock

BuildRequires(pre): rpm-build-golang

%description
Go-difflib is a partial port of python 3 difflib package. Its main goal is to
make unified and context diff available in pure Go, mostly for testing
purposes.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%prep
%setup -n go-difflib-%version
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
%doc README.md LICENSE
%go_path/src/%goipath

%changelog
* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

