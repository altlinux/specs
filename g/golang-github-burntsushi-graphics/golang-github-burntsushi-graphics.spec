# Dead upstream
%ifnarch aarch64 ppc64le s390x
%def_without check
%endif

%global goipath         github.com/BurntSushi/graphics-go
%global commit          b43f31a4a96688fba0b612e25e22648b9267e498

Name: golang-github-burntsushi-graphics
Version: 0
Release: alt1.gitb43f31a
Summary: Graphics library for the Go programming language
Group: Graphical desktop/Other
License: BSD-3-Clause
Url: https://github.com/BurntSushi/graphics-go
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: graphics-go-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
This is a Graphics library for the Go programming language.

%package devel
Summary: Graphics library for the Go programming language
Group: Development/Other
BuildArch: noarch

%description devel
This is a Graphics library for the Go programming language.

%prep
%setup -n graphics-go-%version
find . -name "*.go" -exec sed -i "s|github.com/BurntSushi/freetype-go/freetype|github.com/golang/freetype|" "{}" +;

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
%doc LICENSE AUTHORS CONTRIBUTORS README
%go_path/src/%goipath

%changelog
* Fri May 8 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.gitb43f31a
- Initial build for ALT Sisyphus (thanks fedora for this spec).

