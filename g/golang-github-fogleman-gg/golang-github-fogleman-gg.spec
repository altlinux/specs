# https://github.com/fogleman/gg/issues/79
%ifnarch aarch64 ppc64le s390x
%def_without check
%endif

%global goipath         github.com/fogleman/gg

Name: golang-github-fogleman-gg
Version: 1.3.0
Release: alt1
Summary: 2D rendering in Go with a simple API
Group: Development/Other
License: MIT
Url: https://github.com/fogleman/gg
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: gg-%version.tar.gz
# https://github.com/fogleman/gg/issues/93
Patch: 0001-fix-test-for-1.13.patch

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(github.com/golang/freetype/raster) golang(github.com/golang/freetype/truetype) golang(golang.org/x/image/draw) golang(golang.org/x/image/font) golang(golang.org/x/image/font/basicfont) golang(golang.org/x/image/font/gofont/goregular) golang(golang.org/x/image/math/f64) golang(golang.org/x/image/math/fixed)
BuildRequires: golang-x-image-devel golang-github-freetype-devel

%description
Gg is a library for rendering 2D graphics in pure Go.

%package devel
Summary: 2D rendering in Go with a simple API
Group: Development/Other
BuildArch: noarch

%description devel
Gg is a library for rendering 2D graphics in pure Go.

%prep
%setup -n gg-%version
%patch -p1

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
%doc LICENSE.md examples README.md
%go_path/src/%goipath

%changelog
* Fri May 8 2020 Leontiy Volodin <lvol@altlinux.org> 1.3.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

