%ifnarch aarch64 ppc64le s390x
%def_without check
%endif

%global goipath github.com/disintegration/imaging

Name: golang-github-disintegration-imaging
Version: 1.6.2
Release: alt1
Summary: Simple image processing package for Go
Group: Development/Other
License: MIT
Url: https://github.com/disintegration/imaging
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/imaging-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(golang.org/x/image/bmp) golang(golang.org/x/image/tiff)
BuildRequires: golang-x-image-devel

%description
Package imaging provides basic image processing functions (resize, rotate, crop,
brightness/contrast adjustments, etc.).

All the image processing functions provided by the package accept any image type
that implements image.Image interface as an input, and return a new image of
*image.NRGBA type (32bit RGBA colors, non-premultiplied alpha).

%package devel
Summary: Simple image processing package for Go
Group: Development/Other
BuildArch: noarch

%description devel
Simple image processing package for Go.

%prep
%setup -n imaging-%version
%__subst 's|\r||g' README.md

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
* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 1.6.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
