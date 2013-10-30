%global import_path     github.com/gorilla/mux
%global gopath          %_datadir/gocode

Name: golang-github-gorilla-mux
Version: 0
Release: alt2
Summary: A powerful URL router and dispatcher for golang
License: BSD
Group: Development/Other
Url: http://www.gorillatoolkit.org/pkg/mux
Source0: %name-%version.tar
BuildArch: noarch

%description
Package gorilla/mux implements a request router and dispatcher.

The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of
registered routes and calls a handler for the route that matches the URL or
other conditions.

%package devel
Summary: A powerful URL router and dispatcher for golang
Group: Development/Other
Provides: golang(%import_path) = %version-%release
Requires: golang
Requires: golang(github.com/gorilla/context)

%description devel
Package gorilla/mux implements a request router and dispatcher.

The name mux stands for "HTTP request multiplexer". Like the standard
http.ServeMux, mux.Router matches incoming requests against a list of
registered routes and calls a handler for the route that matches the URL or
other conditions.

This package contains library source intended for building other packages
which use gorilla/mux.

%prep
%setup

%build
%install
install -d %buildroot/%gopath/src/%import_path
cp -av *.go %buildroot/%gopath/src/%import_path

%files devel
%doc LICENSE README.md
%dir %attr(755,root,root) %gopath
%dir %attr(755,root,root) %gopath/src
%dir %attr(755,root,root) %gopath/src/github.com
%dir %attr(755,root,root) %gopath/src/github.com/gorilla
%dir %attr(755,root,root) %gopath/src/github.com/gorilla/mux
%gopath/src/%import_path/*.go

%changelog
* Wed Oct 30 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt2
- Update spec

* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT
