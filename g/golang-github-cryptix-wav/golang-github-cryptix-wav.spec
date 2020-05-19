%def_without check

# https://github.com/cryptix/wav
%global goipath         github.com/cryptix/wav
%global commit          8bdace674401f0bd3b63c65479b6a6ff1f9d5e44
%global repo wav

Name: golang-github-cryptix-wav
Version: 0
Release: alt1.8bdace6
Summary: Golang .wav reader and writer

License: GPL-2.0
Group: Development/Other
Url: https://github.com/cryptix/wav
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(gonum.org/v1/plot) golang(gonum.org/v1/plot/plotter) golang(gonum.org/v1/plot/plotutil) golang(gonum.org/v1/plot/vg)
BuildRequires: golang-gonum-1-plot-devel

%if_with check
# Tests
BuildRequires: golang(github.com/cheekybits/is)
%endif

%description
Golang .wav reader and writer.

%package devel
Summary: Golang .wav reader and writer
Group: Development/Other
BuildArch: noarch

%description devel
Golang .wav reader and writer.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name package.

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

%check
%if_with check
export GOPATH="%go_path"
%gotest
%endif

%files devel
%doc README.md LICENSE
%go_path/src/%goipath
%exclude %go_path/src/%goipath/examples

%files examples
%go_path/src/%goipath/examples

%changelog
* Wed Apr 22 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.8bdace6
- Initial build for ALT Sisyphus (thanks fedora for this spec).
