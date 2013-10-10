%global import_path     code.google.com/p/go.net
%global gopath          %_datadir/gocode

Name: golang-googlecode-net
Version: 0
Release: alt1
Summary: Supplementary Go networking libraries
License: BSD
Group: Development/Other
Url: http://%import_path
Source0: %name-%version.tar
BuildArch: noarch

%description
%summary

%package devel
Summary: Supplementary Go networking libraries
Group: Development/Other
Requires: golang
Provides: golang("%import_path") = %version-%release
Provides: golang("%import_path/dict") = %version-%release
Provides: golang("%import_path/html") = %version-%release
Provides: golang("%import_path/html/atom") = %version-%release
Provides: golang("%import_path/idna") = %version-%release
Provides: golang("%import_path/ipv4") = %version-%release
Provides: golang("%import_path/ipv6") = %version-%release
Provides: golang("%import_path/proxy") = %version-%release
Provides: golang("%import_path/publicsuffix") = %version-%release
Provides: golang("%import_path/spdy") = %version-%release
Provides: golang("%import_path/websocket") = %version-%release

%description devel
%summary

This package contains library source intended for building other packages
which use the supplementary Go networking libraries.

%prep
%setup
cp html/testdata/webkit/README README-webkit

%build
%install
install -d %buildroot/%gopath/src/%import_path
for d in dict html idna ipv4 ipv6 proxy publicsuffix spdy websocket; do
   cp -av $d %buildroot/%gopath/src/%import_path/
done

%files devel
%doc AUTHORS CONTRIBUTORS LICENSE PATENTS README
%doc README-webkit
%dir %attr(755,root,root) %gopath
%dir %attr(755,root,root) %gopath/src
%dir %attr(755,root,root) %gopath/src/code.google.com
%dir %attr(755,root,root) %gopath/src/code.google.com/p
%dir %attr(755,root,root) %gopath/src/%import_path
%dir %attr(755,root,root) %gopath/src/%import_path/dict
%dir %attr(755,root,root) %gopath/src/%import_path/html
%dir %attr(755,root,root) %gopath/src/%import_path/html/atom
%dir %attr(755,root,root) %gopath/src/%import_path/html/testdata
%dir %attr(755,root,root) %gopath/src/%import_path/html/testdata/webkit
%dir %attr(755,root,root) %gopath/src/%import_path/html/testdata/webkit/scripted
%dir %attr(755,root,root) %gopath/src/%import_path/idna
%dir %attr(755,root,root) %gopath/src/%import_path/ipv4
%dir %attr(755,root,root) %gopath/src/%import_path/ipv6
%dir %attr(755,root,root) %gopath/src/%import_path/proxy
%dir %attr(755,root,root) %gopath/src/%import_path/publicsuffix
%dir %attr(755,root,root) %gopath/src/%import_path/spdy
%dir %attr(755,root,root) %gopath/src/%import_path/websocket
%gopath/src/%import_path/dict/*.go
%gopath/src/%import_path/html/*.go
%gopath/src/%import_path/html/atom/*.go
%gopath/src/%import_path/html/testdata/*.html
%gopath/src/%import_path/html/testdata/webkit/*.dat
%gopath/src/%import_path/html/testdata/webkit/README
%gopath/src/%import_path/html/testdata/webkit/scripted/*.dat
%gopath/src/%import_path/idna/*.go
%gopath/src/%import_path/ipv4/*.go
%gopath/src/%import_path/ipv6/*.go
%gopath/src/%import_path/proxy/*.go
%gopath/src/%import_path/publicsuffix/*.go
%gopath/src/%import_path/spdy/*.go
%gopath/src/%import_path/websocket/*.go

%changelog
* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0-alt1
- Build for ALT

