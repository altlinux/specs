%global import_path     github.com/hashicorp/raft

%global commit 9c733b2b7f53115c5ef261a90ce912a1bb49e970
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-hashicorp-raft
Version: 1.0.0
Release: alt0.git%shortcommit
Summary: library for providing consensus.
License: MPL v2
Group: Development/Other
Url: https://github.com/hashicorp/raft
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
raft is a Go library that manages a replicated
log and can be used with an FSM to manage replicated state machines. It
is a library for providing consensus.

%package devel
Summary: library for providing consensus.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(github.com/armon/go-metrics)
Requires:	golang(github.com/hashicorp/go-msgpack/codec)

%description devel
raft is a Go library that manages a replicated
log and can be used with an FSM to manage replicated state machines. It
is a library for providing consensus.

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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 1.0.0-alt0.git9c733b2b
- Initial package
