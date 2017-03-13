%global import_path     github.com/gorilla/websocket

Name: golang-github-gorilla-websocket
Version: 1.1.0
Release: alt1
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
* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 1.1.0-alt1
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 1.0.0-alt3.gite8f0f8aa
- Update

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 1.0.0-alt2.git0b847f2f
- Update

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 1.0.0-alt1.gita69d25be
- Update

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 0-alt2.gita622679e
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gitb824a5d8
- Initial package

