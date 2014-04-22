%define import_path     github.com/godbus/dbus
%define gopath          %_datadir/gocode
%define commit          %nil
%define shortcommit     %(c=%commit; echo ${c:0:7})

Name: golang-github-godbus-dbus
Version: 1
Release: alt1
Summary: Go client bindings for D-Bus
License: BSD
Group: Development/Other
Url: https://%import_path

BuildArch: noarch

# git clone https://github.com/godbus/dbus.git
Source0: %name-%version.tar

BuildRequires: golang

%description
Simple library that implements native Go client bindings for the
D-Bus message bus system.

Features include:
Complete native implementation of the D-Bus message protocol
Go-like API (channels for signals / asynchronous method calls, Goroutine-safe
connections)
Subpackages that help with the introspection / property interfaces.

%package devel
Requires: golang
Summary: Go client bindings for D-Bus
Group: Development/Other
Provides: golang(%import_path) = %version-%release
Provides: golang(%import_path/_examples) = %version-%release
Provides: golang(%import_path/introspect) = %version-%release
Provides: golang(%import_path/prop) = %version-%release

%description devel
%summary

This package contains library source intended for building other packages
which use %import_path.

%prep
%setup

%build
%install
for d in . _examples introspect prop; do
    install -d -p %buildroot/%gopath/src/%import_path/$d
    cp -av $d/*.go %buildroot/%gopath/src/%import_path/$d
done

%check

%files devel
%doc LICENSE README.markdown
%dir %attr(755,root,root) %gopath
%dir %attr(755,root,root) %gopath/src
%dir %attr(755,root,root) %gopath/src/github.com
%dir %attr(755,root,root) %gopath/src/github.com/godbus
%dir %attr(755,root,root) %gopath/src/%import_path
%dir %attr(755,root,root) %gopath/src/%import_path/_examples
%dir %attr(755,root,root) %gopath/src/%import_path/introspect
%dir %attr(755,root,root) %gopath/src/%import_path/prop
%gopath/src/%import_path/*.go
%gopath/src/%import_path/_examples/*.go
%gopath/src/%import_path/introspect/*.go
%gopath/src/%import_path/prop/*.go

%changelog
* Tue Apr 22 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1-alt1
- Initial build.

* Mon Mar 31 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Initial fedora package
