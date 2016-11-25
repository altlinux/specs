%global import_path github.com/mattn/go-sqlite3

#global commit b5c99a720374818b629fd1fbf6d2cbb4fb9a5644
#global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-mattn-go-sqlite3
Version: 1.2.0
Release: alt1
Summary: sqlite3 driver conforming to the built-in database/sql interface
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
sqlite3 driver conforming to the built-in database/sql interface

%package devel
Summary: sqlite3 driver conforming to the built-in database/sql interface
Group: Development/Other
Requires: golang
Requires: golang(golang.org/x/net/context)
Provides: golang(%import_path) = %version-%release

%description devel
sqlite3 driver conforming to the built-in database/sql interface

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

rm -rf -- %buildroot/%go_path/src/%import_path/_example
rm -rf -- %buildroot/%go_path/src/%import_path/sqlite3_test

%files devel
%doc README.md LICENSE
%go_path/src/*

%changelog
* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 1.2.0-alt1
- Update

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 0-alt3.gitb5c99a72
- Update

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.git10876d7d
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gitc5aee964
- Initial package

