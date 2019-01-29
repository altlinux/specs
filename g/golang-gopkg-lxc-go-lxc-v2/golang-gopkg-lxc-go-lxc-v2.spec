%global import_path gopkg.in/lxc/go-lxc.v2

%global commit 7c910f8a5edc8a569ffcd0c7c1f3ea56d73adab7
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-gopkg-lxc-go-lxc-v2
Version: 2.0
Release: alt10.git%abbrev
Summary: This package implements Go bindings for the LXC C API.
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This package implements Go bindings for the LXC C API.

%package devel
Summary: This package implements Go bindings for the LXC C API.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
This package implements Go bindings for the LXC C API.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

mkdir -vp -- "$BUILDDIR/src/$IMPORT_PATH"
%golang_prepare
cp -alv -- *.[ch] "$BUILDDIR/src/$IMPORT_PATH"

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot/%go_path/src/%import_path/examples

%files devel
%doc AUTHORS README.md LICENSE
%go_path/src/*

%changelog
* Fri Jan 11 2019 Denis Pynkin <dans@altlinux.org> 2.0-alt10.git7c910f8a
- Update

* Sun Jun 24 2018 Denis Pynkin <dans@altlinux.org> 2.0-alt9.git1c13b43c
- Update

* Fri Feb 02 2018 Denis Pynkin <dans@altlinux.org> 2.0-alt8.gitb964baab
- Update

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 2.0-alt7.git1a2cf29c
- Update

* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 2.0-alt6.gitde2c8bfd
- Update

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.0-alt5.git8304875c
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt4.git9b05ddae
- Update

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt3.gitc4f2de4e
- Update

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt2.gitf8a6938e
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 2.0-alt1.gitd89df0ad
- Initial package

