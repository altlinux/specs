%global import_path     github.com/CanonicalLtd/raft-http

%global commit 4c2dd679d3b46c11b250d63ae43467d4c4ab0962
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-CanonicalLtd-raft-http
Version: 0
Release: alt0.git%shortcommit
Summary: provides the `rafthttp` package
License: Apache v2
Group: Development/Other
Url: https://github.com/CanonicalLtd/raft-http
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This repository provides the `rafthttp` package, which can be used to
establish a network connection between to raft nodes using HTTP. Once
the HTTP connection is established, the Upgrade header will be used to
switch it to raw TCP mode, and the regular TCP-based network transport
of the `raft` [package](https://github.com/hashicorp/raft) can take it
from there.

%package devel
Summary: provides the `rafthttp` package
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(github.com/CanonicalLtd/raft-membership)
Requires:	golang(github.com/hashicorp/raft)
Requires:	golang(github.com/pkg/errors)

%description devel
%summary

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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0-alt0.git4c2dd679
- Initial package
