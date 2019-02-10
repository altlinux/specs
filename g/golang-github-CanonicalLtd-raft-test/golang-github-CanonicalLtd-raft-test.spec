%global import_path     github.com/CanonicalLtd/raft-test

%global commit c3345b5e43c2b542007a11093afbbfecedd41648
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-CanonicalLtd-raft-test
Version: 0
Release: alt0.git%shortcommit
Summary: `rafttest` package
License: Apache v2
Group: Development/Other
Url: https://github.com/CanonicalLtd/raft-test
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This repository provides the `rafttest` package, which contains
helpers to test code based on the `raft` Go package from Hashicorp.

%package devel
Summary: `rafttest` package
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(github.com/hashicorp/raft)
Requires:	golang(github.com/hashicorp/logutils)

%description devel
This repository provides the `rafttest` package, which contains
helpers to test code based on the `raft` Go package from Hashicorp.

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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0-alt0.gitc3345b5e
- Initial package
