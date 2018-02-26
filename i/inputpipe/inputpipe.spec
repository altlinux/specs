%define svn_revision 11919

Name: inputpipe
Version: 0.0.0
Release: alt1.svn%svn_revision

Summary: Client/server application for making any input device network-transparent

License: GPL
Group: Networking/Remote access
Url: http://freshmeat.net/projects/inputpipe

Source: %name-%version.tar
Packager: Denis Klimov <zver@altlinux.org>


%description
Inputpipe is a client/server application for making any Linux input 
device network-transparent. An inputpipe client runs on a computer 
with some arbitrary input devices, forwarding information and status 
from those devices to an inputpipe server. The server creates local 
input devices that are identical copies of the devices being 
forwarded for all practical purposes.

%package server
Summary: Server part of inputpipe
Group: Networking/Remote access
%description server
Server part of inputpipe.


%package client
Summary: Client part of inputpipe
Group: Networking/Remote access
%description client
Client part of inputpipe

%prep
%setup

%build
%make_build 

%install
mkdir -p %buildroot%_bindir
%make_install INSTDIR=%buildroot%_bindir install

%files server
%_bindir/inputpipe-server

%files client
%_bindir/inputpipe-client

%changelog
* Sat Dec 20 2008 Denis Klimov <zver@altlinux.org> 0.0.0-alt1.svn11919
- Initial build for ALT Linux


