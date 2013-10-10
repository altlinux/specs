%global import_path     github.com/kr/pty
%global gopath          %_datadir/gocode

Name: golang-github-kr-pty
Version: 0
Release: alt1
Summary: PTY interface for Go
License: MIT
Group: Development/Other
Url: http://godoc.org/%import_path
Source0: %name-%version.tar
BuildArch: noarch

%description
Pty is a Go package for using UNIX pseudo-terminals.

%package devel
Summary: PTY interface for Go
Group: Development/Other
Requires: golang
Provides: golang("%import_path") = %version-%release

%description devel
Pty is a Go package for using UNIX pseudo-terminals.

This package contains library source intended for building other packages
which use kr/pty.

%prep
%setup

%build
%install
install -d %buildroot/%gopath/src/%import_path
cp -av *.go %buildroot/%gopath/src/%import_path

%files devel
%doc License README.md
%dir %attr(755,root,root) %gopath
%dir %attr(755,root,root) %gopath/src
%dir %attr(755,root,root) %gopath/src/github.com
%dir %attr(755,root,root) %gopath/src/github.com/kr
%dir %attr(755,root,root) %gopath/src/github.com/kr/pty
%gopath/src/%import_path/*.go

%changelog
* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT
