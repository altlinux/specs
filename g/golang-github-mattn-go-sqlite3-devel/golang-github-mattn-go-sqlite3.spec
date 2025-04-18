%global import_path github.com/mattn/go-sqlite3

Name: golang-github-mattn-go-sqlite3-devel
Version: 1.14.6
Release: alt1

Summary: sqlite3 driver conforming to the built-in database/sql interface
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Vcs: https://%import_path

Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
sqlite3 driver conforming to the built-in database/sql interface

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export IMPORT_PATH="%import_path"
mkdir -vp -- "$BUILDDIR/src/$IMPORT_PATH"
%golang_prepare

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install
rm -rf -- %buildroot/%go_path/src/%import_path/_example
rm -rf -- %buildroot/%go_path/src/%import_path/sqlite3_test

%files
%doc README.md LICENSE
%go_path/src/*

%changelog
* Fri Apr 18 2025 Ulysses Apokin <ulysses@altlinux.org> 1.14.6-alt1
- New version.

* Fri Jan 11 2019 Denis Pynkin <dans@altlinux.org> 1.9.0-alt1.git25ecb14a
- Update version

* Fri Feb 02 2018 Denis Pynkin <dans@altlinux.org> 1.6.0-alt1.git75de30ee
- Update

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 1.2.0-alt3.git47fc4e5e
- Update

* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 1.2.0-alt2.gitafe454f6
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 1.2.0-alt1
- Update

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 0-alt3.gitb5c99a72
- Update

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.git10876d7d
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gitc5aee964
- Initial package

