Name: libgrapple
Version: 0.9.8
Release: alt1.1

Summary: A network layer designed for games

License: LGPL
Group: System/Libraries
Url: http://grapple.linuxgamepublishing.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://osfiles.linuxgamepublishing.com/%name-%version.tar.bz2

# Automatically added by buildreq on Mon Sep 21 2009
BuildRequires: gcc-c++ libssl-devel

%description
Grapple is a high level network layer designed to remove the hard work from
making applications multiuser. It was designed with games in mind, but there
is no reason to stop grapple being used for any application.

Grapple supports simple development of networked applications using both
TCP/IP and UDP/IP. Grapple keeps track of connections to a server, relays
messages from client to client, all without the need to understand any
complicated network code.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc README* UPDATES
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/grapple/
#%doc examples/

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Wed Sep 09 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt1
- initial build for ALT Linux Sisyphus

