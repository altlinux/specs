%global import_path golang.org/x/net

%global commit 4971afdc2f162e82d185353533d3cf16188a9f4e
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-golang-x-net
Version: 0
Release: alt1.git%abbrev
Summary: Go supplementary network libraries
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
Go supplementary network libraries

%package devel
Summary: golang-golang-x-net
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/bpf) = %version-%release
Provides: golang(%import_path/context) = %version-%release
Provides: golang(%import_path/dict) = %version-%release
Provides: golang(%import_path/html) = %version-%release
Provides: golang(%import_path/http2) = %version-%release
Provides: golang(%import_path/icmp) = %version-%release
Provides: golang(%import_path/idna) = %version-%release
Provides: golang(%import_path/internal) = %version-%release
Provides: golang(%import_path/ipv4) = %version-%release
Provides: golang(%import_path/ipv6) = %version-%release
Provides: golang(%import_path/lex) = %version-%release
Provides: golang(%import_path/lif) = %version-%release
Provides: golang(%import_path/netutil) = %version-%release
Provides: golang(%import_path/proxy) = %version-%release
Provides: golang(%import_path/publicsuffix) = %version-%release
Provides: golang(%import_path/route) = %version-%release
Provides: golang(%import_path/trace) = %version-%release
Provides: golang(%import_path/webdav) = %version-%release
Provides: golang(%import_path/websocket) = %version-%release
Provides: golang(%import_path/xsrftoken) = %version-%release

%description devel
Go supplementary network libraries

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
%doc AUTHORS README LICENSE PATENTS
%go_path/src/*

%changelog
* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 0-alt1.git4971afdc
- Initial package

