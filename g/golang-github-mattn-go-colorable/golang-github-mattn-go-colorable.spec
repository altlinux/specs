%global import_path github.com/mattn/go-colorable

Name: golang-github-mattn-go-colorable
Version: 0.0.7
Release: alt1
Summary: Colorable writer for windows.
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
This package is possible to handle escape sequence for ansi color on windows.

%package devel
Summary: Colorable writer for windows.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
This package is possible to handle escape sequence for ansi color on windows.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot/%go_path/src/%import_path/_example

%files devel
%doc README.md LICENSE
%go_path/src/*

%changelog
* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 0.0.7-alt1
- Update

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 0.0.6-alt2.git6c903ff4
- Update

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 0.0.6-alt1
- Version update

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.git9cbef7c3
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.git9fdad7c4
- Initial package

