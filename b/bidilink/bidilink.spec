Name: bidilink
Version: 0.1
Release: alt1

Summary: bidilink - Bidirectional stream linker
Group: File tools
License: GPLv2+

Url: http://0pointer.de/lennart/projects/bidilink/

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Thu Jan 17 2008
BuildRequires: lynx xmltoman

%description
bidilink is a general purpose Unix tool for linking two bidirectional
data streams together. It extends the standard Unix "filter" paradigma
to bidrectional streams.

Version 0.1 is more or less stable. Its has the following stream
drivers:
* std: - STDIN, STDOUT of the process
* exec:PROGRAM - fork() off a process and use its STDIN and STDOUT
* tty:TTYDEVICE - Open a TTY device (like a serial port) as client
* pty:[PTYNAME] - Allocate a pseudo TTY device as master
* tcp-client:HOSTNAME:PORT - Connect to another or the local host via TCP/IP
* tcp-server:[IPADDRESS:]PORT - Listen on a local port and wait for
an incoming connection
* unix-client:SOCKNAME - Connect to a local Unix domain socket
* unix-server:SOCKNAME - Listen on a local Unix domain socket
								     
%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc README
%_bindir/bidilink
%_man1dir/bidilink.*

%changelog
* Thu Jan 17 2008 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus

