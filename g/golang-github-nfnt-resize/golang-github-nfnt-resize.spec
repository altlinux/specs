%def_with check

%global goipath         github.com/nfnt/resize
%global commit          83c6a9932646f83e3267f353373d47347b6036b2

Name: golang-github-nfnt-resize
Version: 0
Release: alt1.git83c6a99
Summary: Pure golang image resizing
Group: Graphical desktop/Other
License: ISC
Url: https://github.com/nfnt/resize
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: resize-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Image resizing for the Go programming language with common interpolation
methods.

%package devel
Summary: Pure golang image resizing
Group: Development/Other
BuildArch: noarch

%description devel
Image resizing for the Go programming language with common interpolation
methods.

%prep
%setup -n resize-%version

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
%gotest
%endif

%files devel
%doc LICENSE README.md
%go_path/src/%goipath

%changelog
* Tue May 12 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git83c6a99
- Initial build for ALT Sisyphus (thanks fedora for this spec).

