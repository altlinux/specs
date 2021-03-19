%def_without check

%define goipath github.com/Lofanmi/pinyin-golang
%define repo pinyin-golang

Name: golang-github-lofanmi-pinyin
Version: 1.0
Release: alt1
Summary: The Pinyin library of the Go language
Group: Development/Other
License: MIT
Url: https://github.com/Lofanmi/pinyin-golang
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
%summary.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%prep
%setup -n %repo-%version

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
* Fri Mar 19 2021 Leontiy Volodin <lvol@altlinux.org> 1.0-alt1
- Initial build for ALT Sisyphus (for deepin-daemon).
