%global import_path     code.google.com/p/gosqlite
%global gopath          %_datadir/gocode

Name: golang-googlecode-sqlite
Version: 0
Release: alt1
Summary: Trivial sqlite3 binding for Go
License: BSD
Group: Development/Other
Url: http://%import_path
Source0: %name-%version.tar
Source1: LICENSE-BSD3-Go
BuildArch: noarch

%description
%summary

This package has no exported API. It registers a driver for the standard Go
database/SQL package.

%package devel
Summary: Trivial sqlite3 binding for Go
Group: Development/Other
Requires: golang libsqlite-devel
Provides: golang("%import_path") = %version-%release
Provides: golang("%import_path/sqlite") = %version-%release
Provides: golang("%import_path/sqlite3") = %version-%release

%description devel
%summary

This package has no exported API. It registers a driver for the standard Go
database/SQL package.

%prep
%setup

%build
# Requested upstream to include LICENSE
# http://code.google.com/p/gosqlite/issues/detail?id=21
cp %SOURCE1 ./LICENSE

%install
install -d %buildroot/%gopath/src/%import_path
for d in sqlite sqlite3; do
   cp -av $d %buildroot/%gopath/src/%import_path/
done

%files devel
%doc LICENSE
%dir %attr(755,root,root) %gopath
%dir %attr(755,root,root) %gopath/src
%dir %attr(755,root,root) %gopath/src/code.google.com
%dir %attr(755,root,root) %gopath/src/code.google.com/p
%dir %attr(755,root,root) %gopath/src/%import_path
%dir %attr(755,root,root) %gopath/src/%import_path/sqlite
%dir %attr(755,root,root) %gopath/src/%import_path/sqlite3
%gopath/src/%import_path/sqlite/*.go
%gopath/src/%import_path/sqlite3/*.go

%changelog
* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT

