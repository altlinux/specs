%global import_path     github.com/hashicorp/raft-boltdb

%global commit 6e5ba93211eaf8d9a2ad7e41ffad8c6f160f9fe3
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-hashicorp-raft-boltdb
Version: 0
Release: alt0.git%shortcommit
Summary: This repository provides the `raftboltdb` package.
License: MPL v2
Group: Development/Other
Url: https://github.com/hashicorp/raft-boltdb
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This repository provides the `raftboltdb` package. The package exports the
`BoltStore` which is an implementation of both a `LogStore` and `StableStore`.

%package devel
Summary: This repository provides the `raftboltdb` package.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detect build requirements for package only
Requires:	golang(github.com/boltdb/bolt)
Requires:	golang(github.com/hashicorp/go-msgpack/codec)
Requires:	golang(github.com/hashicorp/raft)

%description devel
This repository provides the `raftboltdb` package. The package exports the
`BoltStore` which is an implementation of both a `LogStore` and `StableStore`.

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

%files devel
%doc README.md LICENSE
%go_path/src/*

%changelog
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0-alt0.git6e5ba932
- Initial package
