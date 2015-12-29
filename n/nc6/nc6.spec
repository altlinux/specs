Summary: Reads and writes data across network connections using TCP or UDP with IPv4 and IPv6
Name: nc6
Version: 1.0
Release: alt1
License: GPL
Group: Networking/Other
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: ftp://ftp.deepspace6.net/pub/ds6/sources/nc6/nc6-%version.tar.gz
Patch1: 01_quiet_socket_announce.diff
Patch2: 02_multicast.diff
Patch3: 03_send_crlf.diff
Patch4: 04_minus_to_hyphen.diff
Patch5: 05_source_service_and_source_address.diff
Patch6: 06_idle_timeout_parsing.diff
Patch7: 07_z_argument.diff

%description
The nc6 package contains Netcat6 (the program is actually nc6), a simple
utility for reading and writing data across network connections, using
the TCP or UDP protocols. Netcat6 is intended to be a reliable back-end
tool which can be used directly or easily driven by other programs and
scripts.  Netcat is also a feature-rich network debugging and
exploration tool, since it can create many different connections and
has many built-in capabilities.

You may want to install the netcat6 package if you are administering a
network and you'd like to use its debugging and network exploration
capabilities.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%configure
%make

%install
%make DESTDIR=%buildroot install

%files
%doc README AUTHORS NEWS
%_bindir/%name
%_man1dir/%name.1*


%changelog
* Tue Dec 29 2015 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- initial release

