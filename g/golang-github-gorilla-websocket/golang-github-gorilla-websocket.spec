%global import_path     github.com/gorilla/websocket

%global commit b824a5d8536651ad2d690c17e270d58855dbfd02
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-gorilla-websocket
Version: 0
Release: alt1.git%abbrev
Summary: The Gorilla WebSocket package provides an implementation of rfc6455 protocol.
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
The Gorilla WebSocket package provides a complete and tested implementation of
the [WebSocket](http://www.rfc-editor.org/rfc/rfc6455.txt) protocol. The
package API is stable.

%package devel
Summary: The Gorilla WebSocket package provides an implementation of rfc6455 protocol.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
The Gorilla WebSocket package provides a complete and tested implementation of
the [WebSocket](http://www.rfc-editor.org/rfc/rfc6455.txt) protocol. The
package API is stable.

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

rm -rf -- %buildroot/%go_path/src/%import_path/examples


%files devel
%doc AUTHORS README.md LICENSE
%go_path/src/*

%changelog
* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gitb824a5d8
- Initial package

