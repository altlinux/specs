%def_without check

%global goipath         github.com/golang/freetype
%global commit          e2365dfdc4a05e4b8299a783240d4a7d5a65d4e4

%global goaltipaths     github.com/BurntSushi/freetype-go

Name: golang-github-freetype
Version: 0
Release: alt1.gite2365df
Summary: Freetype font rasterizer in the Go programming language
Group: Development/Other
License: GPL-2.0+ or FTL
Url: https://github.com/golang/freetype
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: freetype-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(golang.org/x/image/font) golang(golang.org/x/image/math/fixed)
BuildRequires: golang-x-image-devel

%description
The Freetype font rasterizer in the Go programming language.

%package devel
Summary: Freetype font rasterizer in the Go programming language
Group: Development/Other
BuildArch: noarch

%description devel
The Freetype font rasterizer in the Go programming language.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name package.

%prep
%setup -n freetype-%version

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
%doc LICENSE licenses/gpl.txt licenses/ftl.txt example AUTHORS CONTRIBUTORS README
%go_path/src/%goipath
%exclude %go_path/src/%goipath/example

%files examples
%go_path/src/%goipath/example

%changelog
* Fri May 8 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.gite2365df
- Initial build for ALT Sisyphus (thanks fedora for this spec).

