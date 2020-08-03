%def_without check

%global goipath         gonum.org/v1/plot
%global forgeurl        https://github.com/gonum/plot
%global commit          e2840ee46a6b612972d746f9fea9920d329a0605
%global repo plot

Name: golang-gonum-1-plot
Version: 0
Release: alt1.e2840ee
Summary: Package for plotting and visualizing data

License: BSD and OFL-1.1 and MIT and Apache-2.0
Group: Development/Other
Url: https://github.com/gonum/plot
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(github.com/ajstarks/svgo) golang(github.com/fogleman/gg) golang(github.com/golang/freetype/truetype) golang(github.com/jung-kurt/gofpdf) golang(golang.org/x/image/font) golang(golang.org/x/image/math/fixed) golang(golang.org/x/image/tiff) golang(rsc.io/pdf)
BuildRequires: golang-x-image-devel golang-rsc-pdf-devel golang-github-jung-kurt-gofpdf-devel golang-github-freetype-devel golang-github-fogleman-gg-devel golang-github-ajstarks-svgo-devel

%if_with check
# Tests
BuildRequires: golang(golang.org/x/exp/rand)
BuildRequires: golang(gonum.org/v1/gonum/floats)
BuildRequires: golang(gonum.org/v1/gonum/mat)
%endif

%description
Plot provides an API for building and drawing plots in Go.

%package devel
Summary: Package for plotting and visualizing data
Group: Development/Other
BuildArch: noarch

%description devel
Plot provides an API for building and drawing plots in Go.

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
%gotest -d palette/moreland -d plotter
%endif

%files devel
%doc README.md LICENSE AUTHORS
%go_path/src/%goipath

%changelog
* Wed Apr 22 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.e2840ee
- Initial build for ALT Sisyphus (thanks fedora for this spec).
