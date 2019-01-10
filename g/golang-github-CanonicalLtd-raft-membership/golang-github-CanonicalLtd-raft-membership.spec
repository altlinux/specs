%global import_path     github.com/CanonicalLtd/raft-membership

%global commit 3846634b0164affd0b3dfba1fdd7f9da6387e501
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-CanonicalLtd-raft-membership
Version: 0
Release: alt0.git%shortcommit
Summary: `raftmembership` package
License: Apache v2
Group: Development/Other
Url: https://github.com/CanonicalLtd/raft-membership
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This repository provides the `raftmembership` package, which contains
an extensions of the `raft` Go package from Hashicorp to easily make 
a node join or leave a cluster.

%package devel
Summary: `raftmembership` package
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(github.com/hashicorp/raft)

%description devel
This repository provides the `raftmembership` package, which contains
an extensions of the `raft` Go package from Hashicorp to easily make 
a node join or leave a cluster.

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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0-alt0.git3846634b
- Initial package
