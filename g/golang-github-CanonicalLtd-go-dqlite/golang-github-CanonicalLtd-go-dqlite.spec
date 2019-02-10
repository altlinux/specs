%global import_path     github.com/CanonicalLtd/go-dqlite

%global commit db80752439abf27c03ad4c0cf37d11fe24f53710
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-CanonicalLtd-go-dqlite
Version: 0.2.2
Release: alt0.git%shortcommit
Summary: `dqlite` Go package
License: Apache v2
Group: Development/Other
Url: https://%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This repository provides the `dqlite` Go package, which can be used to
replicate a SQLite database across a cluster, using the Raft
algorithm.

%package devel
Summary: `dqlite` Go package
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# sqlite3 patched version is needed
Requires:	liblxd_sqlite3-devel

# Auto-detected requirements
Requires:	golang(github.com/Rican7/retry/backoff)
Requires:	golang(github.com/Rican7/retry/strategy)
Requires:	golang(github.com/hashicorp/raft)
Requires:	golang(github.com/mattn/go-sqlite3)
Requires:	golang(github.com/pkg/errors)

%description devel
This repository provides the `dqlite` Go package, which can be used to
replicate a SQLite database across a cluster, using the Raft
algorithm.

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
%doc AUTHORS README.md LICENSE
%go_path/src/*

%changelog
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0.2.2-alt0.gitdb807524
- Initial package
- Use lxd_sqlite package instead of common libsqlite