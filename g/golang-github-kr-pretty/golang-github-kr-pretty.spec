%def_without check

# https://github.com/kr/pretty
%global goipath github.com/kr/pretty

Name: golang-github-kr-pretty
Version: 0.2.0
Release: alt1
Summary: Pretty printing for go values

License: MIT
Group: Development/Other
Url: https://github.com/kr/pretty
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: pretty-%version.tar.gz
Source1: glide.yaml
Source2: glide.lock

BuildRequires: rpm-build-golang
# BuildRequires: golang(github.com/kr/text) fsextender-devel
BuildRequires: fsextender-devel golang-github-kr-text-devel

%description
Package pretty provides pretty-printing for go values. This is useful during
debugging, to avoid wrapping long output lines in the terminal.

%package devel
Summary: Pretty printing for go values
Group: Development/Other
BuildArch: noarch

%description devel
Package pretty provides pretty-printing for go values. This is useful during
debugging, to avoid wrapping long output lines in the terminal.

%prep
%setup -n pretty-%version
cp %SOURCE1 %SOURCE2 .

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path:$BUILDDIR"

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
%go_path/src/%goipath

%changelog
* Mon Mar 23 2020 Leontiy Volodin <lvol@altlinux.org> 0.2.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

