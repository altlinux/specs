Name: simpleproxy
Version: 3.4
Release: alt1

Summary: Simple TCP/IP proxy
License: GPL
URL: http://sourceforge.net/projects/simpleproxy/
Group: Networking/Other
Source0: http://dl.sf.net/simpleproxy/%name-%version.tar.gz

%description
Simpleproxy program acts as simple TCP proxy. It listens on a local
socket, and any connection to this port will be forwarded to another
socket at the remote host. It can also use an HTTPS proxy server to
forward connections, and can be configured via command line as well as a
config file.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files
%doc ChangeLog pop3users.txt README sample.cfg TODO
%_bindir/*
%_man1dir/*

%changelog
* Fri Aug 26 2005 Victor Forsyuk <force@altlinux.ru> 3.4-alt1
- 3.4

* Thu Jul 21 2005 Victor Forsyuk <force@altlinux.ru> 3.2-alt1
- 3.2

* Thu Dec 12 2002 Oleg Prokopyev <riiki@altlinux.ru> 3.1-alt1
- Build for Sisyphus.
