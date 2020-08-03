%def_without check
%def_with bootstrap

# https://github.com/ajstarks/svgo
%global goipath         github.com/ajstarks/svgo
%global commit          6ce6a3bcf6cde6c5007887677ebd148ec30f42a4
%global repo svgo

Name: golang-github-ajstarks-svgo
Version: 0
Release: alt1.6ce6a3b
Summary: Go Language Library for SVG generation

License: CC-BY-3.0
Group: Development/Other
Url: https://github.com/ajstarks/svgo
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-golang
%if_without bootstrap
BuildRequires: golang(github.com/ajstarks/deck/generate)
%endif
# BuildRequires: golang(honnef.co/go/tools/structlayout)
BuildRequires: golang-honnef-tools-devel

%description
The library generates SVG as defined by the Scalable Vector Graphics 1.1
Specification (http://www.w3.org/TR/SVG11/). Output goes to the specified
io.Writer.

%package devel
Summary: Go Language Library for SVG generation
Group: Development/Other
BuildArch: noarch

%description devel
The library generates SVG as defined by the Scalable Vector Graphics 1.1
Specification (http://www.w3.org/TR/SVG11/). Output goes to the specified
io.Writer.

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
%if_with bootstrap
%gotest -d personal
%else
%gotest
%endif
%endif

%files devel
%doc README.markdown LICENSE
%go_path/src/%goipath

%changelog
* Wed Apr 22 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.6ce6a3b
- Initial build for ALT Sisyphus (thanks fedora for this spec).
