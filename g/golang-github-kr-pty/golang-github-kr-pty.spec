%def_without check

%global goipath github.com/kr/pty

Name: golang-github-kr-pty
Version: 1.1.8
Release: alt1
Summary: Go package for using unix pseudo-terminals

License: MIT
Group: Development/Other
Url: https://github.com/kr/pty
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: pty-%version.tar.gz
Source1: glide.yaml
Source2: glide.lock

BuildRequires: rpm-build-golang

%description
Go package for using unix pseudo-terminals.

%package devel
Summary: Go package for using unix pseudo-terminals
Group: Development/Other
BuildArch: noarch

%description devel
Go package for using unix pseudo-terminals.

%prep
%setup -n pty-%version
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
%doc LICENSE README.md
%go_path/src/%goipath

%changelog
* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 1.1.8-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

