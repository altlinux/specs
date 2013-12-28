%global import_path     github.com/syndtr/gocapability
%global gopath          %_datadir/gocode

Name: golang-github-syndtr-gocapability
Version: 0
Release: alt1
Summary: POSIX capability library for the Go programming language
License: BSD
Group: Development/Other
Url: https://github.com/syndtr/gocapability
Source0: %name-%version.tar
BuildArch: noarch
BuildRequires:  golang

%description
%summary

%package devel
Summary: POSIX capability library for the Go programming language
Group: Development/Other
Provides: golang(%import_path) = %version-%release
Requires: golang
Requires: golang(%import_path/capability)
Provides: golang(%import_path/capability) = %version-%release

%description devel
%summary

%prep
%setup

%build
%install
install -d %buildroot/%gopath/src/%import_path
cp -av capability %buildroot/%gopath/src/%import_path/

%check
GOPATH=%buildroot/%gopath go test %import_path/capability

%files devel
%doc LICENSE
%dir %attr(755,root,root) %gopath/src/github.com
%dir %attr(755,root,root) %gopath/src/github.com/syndtr
%dir %attr(755,root,root) %gopath/src/%import_path
%dir %attr(755,root,root) %gopath/src/%import_path/capability
%gopath/src/%import_path/capability/*.go

%changelog
* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT
