%global import_path     github.com/gorilla/context
%global gopath          %_datadir/gocode

Name: golang-github-gorilla-context
Version: 0
Release: alt1
Summary: A golang registry for global request variables
License: BSD
Group: Development/Other
Url: http://www.gorillatoolkit.org/pkg/context
Source0: %name-%version.tar
BuildArch: noarch

%description
Package gorilla/context stores values shared during a request lifetime.

For example, a router can set variables extracted from the URL and later
application handlers can access those values, or it can be used to store
sessions values to be saved at the end of a request. There are several
other common uses.

%package devel
Summary: A golang registry for global request variables
Group: Development/Other
Provides: golang("%import_path") = %version-%release
Requires: golang

%description devel
Package gorilla/context stores values shared during a request lifetime.

For example, a router can set variables extracted from the URL and later
application handlers can access those values, or it can be used to store
sessions values to be saved at the end of a request. There are several
other common uses.

This package contains library source intended for building other packages
which use gorilla/context.

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
%dir %attr(755,root,root) %gopath/src/github.com/gorilla/context
%gopath/src/%import_path/*.go

%changelog
* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT

