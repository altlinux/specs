%global import_path     github.com/golang/protobuf

%global commit 8ee79997227bf9b34611aee7946ae64735e6fd93
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-golang-protobuf
Version: 0
Release: alt6.git%abbrev
Summary: Go support for Protocol Buffers
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

# TODO: create a binary
%description
Go support for Protocol Buffers

%package devel
Summary: Go support for Protocol Buffers
Group: Development/Other
Requires: golang

Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/ptypes) = %version-%release
Provides: golang(%import_path/ptypes/duration) = %version-%release
Provides: golang(%import_path/ptypes/struct) = %version-%release
Provides: golang(%import_path/ptypes/empty) = %version-%release
Provides: golang(%import_path/ptypes/any) = %version-%release
Provides: golang(%import_path/ptypes/timestamp) = %version-%release
Provides: golang(%import_path/ptypes/wrappers) = %version-%release
Provides: golang(%import_path/jsonpb) = %version-%release
Provides: golang(%import_path/protoc-gen-go/plugin) = %version-%release
Provides: golang(%import_path/proto) = %version-%release
Provides: golang(%import_path/proto/testdata) = %version-%release


%description devel
Go support for Protocol Buffers

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

rm -rf -- %buildroot/%go_path/src/%import_path/_conformance/_conformance
#rm -rf -- %buildroot/%go_path/src/%import_path/protoc-gen-go
#rm -rf -- %buildroot/%go_path/src/%import_path/proto/testdata
#rm -rf -- %buildroot/%go_path/src/%import_path/jsonpb/jsonpb_test_proto

%files devel
%doc AUTHORS CONTRIBUTORS README.md LICENSE
%go_path/src/*

%changelog
* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 0-alt6.git8ee79997
- Update

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 0-alt5.git98fa3571
- Update

* Mon Aug 22 2016 Denis Pynkin <dans@altlinux.org> 0-alt4.gitf592bd28
- Update

* Thu Apr 14 2016 Denis Pynkin <dans@altlinux.org> 0-alt3.gitf0a097dd
- Update

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.gitb9504f23
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.git89238a32
- Initial package for development only

