%def_without check

%global goipath github.com/BurntSushi/toml

Name: golang-github-burntsushi-toml
Version: 0.4.1
Release: alt1
Summary: Toml parser with reflection for Golang

License: MIT and BSD
Group: Development/Other
Url: https://github.com/BurntSushi/toml
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: toml-%version.tar.gz

BuildRequires(pre): rpm-build-golang rpm-build-python3

%description
TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library json and xml packages.
This package also supports the encoding.TextUnmarshaler and
encoding.TextMarshaler interfaces so that you can define custom data
representations.

%package devel
Summary: Toml parser with reflection for Golang
Group: Development/Other
BuildArch: noarch

%description devel
TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library json and xml packages.
This package also supports the encoding.TextUnmarshaler and
encoding.TextMarshaler interfaces so that you can define custom data
representations.

%prep
%setup -n toml-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in cmd/* ; do
%golang_build $cmd ||:
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

%files
%_bindir/*

%files devel
%doc COPYING _examples README.md COMPATIBLE
%go_path/src/%goipath

%changelog
* Tue Sep 21 2021 Leontiy Volodin <lvol@altlinux.org> 0.4.1-alt1
- New version (0.4.1).
- Fixed build with golang 1.17.

* Sat Feb 20 2021 Leontiy Volodin <lvol@altlinux.org> 0.3.1-alt2
- Fixed build.

* Tue Apr 28 2020 Leontiy Volodin <lvol@altlinux.org> 0.3.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
