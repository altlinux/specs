Name:           libnanomsg
Version:        0.8
Release:        alt1.beta

Summary:        nanomsg is a socket library that provides several common communication patterns
Group:          System/Libraries
License:        MIT/X11
URL:            http://nanomsg.org/
# VCS:		https://github.com/nanomsg/nanomsg

Source0:        %name-%version.tar

Packager:	Andrey Cherepanov <cas@altlinux.org>

%description
nanomsg is a socket library that provides several common communication
patterns. It aims to make the networking layer fast, scalable, and easy
to use. Implemented in C, it works on a wide range of operating systems
with no further dependencies.

The communication patterns, also called "scalability protocols", are
basic blocks for building distributed systems. By combining them you can
create a vast array of distributed applications. The following
scalability protocols are currently available:

PAIR - simple one-to-one communication
BUS - simple many-to-many communication
REQREP - allows to build clusters of stateless services to process user
requests
PUBSUB - distributes messages to large sets of interested subscribers
PIPELINE - aggregates messages from multiple sources and load balances
them among many destinations
SURVEY - allows to query state of multiple applications in a single go

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %name = %version-%release

%description    devel
Development files for the %{name} library. nanomsg is a socket library
that provides several common communication patterns.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README COPYING
%doc doc/
%_bindir/*
%_libdir/lib*.so.*

%files devel
%dir %_includedir/nanomsg
%_includedir/nanomsg/*
%_libdir/lib*.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Dec 01 2015 Andrey Cherepanov <cas@altlinux.org> 0.8-alt1.beta
- Initial build in Sisyphus

