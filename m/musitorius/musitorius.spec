Name: musitorius
Version: 0.4.0
Release: alt2

Packager: Michael Pozhidaev <msp@altlinux.ru>
License: %gpl3plus
URL: http://www.marigostra.ru/musitorius/

Summary: The system service to control multimedia player
Group: Sound

Source: %name-%version.tar.gz
Source1: %name.initrc

Requires: mplayer
BuildRequires: rpm-build-licenses gcc-c++

%package -n lib%name-devel
BuildArch: noarch
Summary: C/C++ development files for %name
Group: Development/C
Requires: lib%name-devel-static

%package -n lib%name-devel-static
Summary: The static library for libmusitorius
Group: Development/C

%description
Musitorius is the approach to get multimedia player as a system
service. It allows distributed control for multimedia playback tasks
with client applications. Clients can initiate new tasks, give
different commands and get various information about service
status. Musitorius uses MPlayer utility as back-end program. It can
maintain log for every user about interrupted and completed tasks so
clients can resume required file playback just from the position the
previous playback was stopped. It is very useful to maintain bookmarks
for voiced books.

%description -n lib%name-devel
This package contains files used for developing applications with C/C++ language
and necessary to make connections to %name daemon.

%description -n lib%name-devel-static
This package contains library used for static linking of libmusitorius.

%prep
%setup -q
%build
%configure default_socket=/var/run/musitorius.socket
%make_build

%install
make DESTDIR=%buildroot install 
%__install -pD -m755 %SOURCE1 %buildroot%_sysconfdir/rc.d/init.d/%name
%__install -pD -m644 ./src/libmusitorius/musitoriusclient.h %buildroot%_includedir/musitoriusclient.h
%__install -pD -m644 ./src/libmusitorius/libmusitorius.a %buildroot%_libdir/lib%name.a

%preun
%preun_service %name

%files
%_bindir/*
%doc AUTHOR COPYING README ChangeLog NEWS
#%config(noreplace) %_sysconfdir/%name.conf
%_sysconfdir/rc.d/init.d/%name

%files -n lib%name-devel
%_includedir/*

%files -n lib%name-devel-static
%_libdir/lib%name.a

%changelog
* Thu May 05 2011 Michael Pozhidaev <msp@altlinux.ru> 0.4.0-alt2
- Fixed bug with MPlayer file descriptors

* Thu May 05 2011 Michael Pozhidaev <msp@altlinux.ru> 0.4.0-alt1
- Initial package

