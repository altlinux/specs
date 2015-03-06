%define sover 0
Name: enet
Version: 1.3.1
Release: alt1.svn20111115
Summary: Thin, simple and robust network layer on top of UDP
License: MIT
Group: Networking/Other
Url: http://enet.bespin.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.research.cc.gatech.edu/kaos/enet/trunk/
# login: anon
# password: anon
Source: %name-%version.tar

%description
ENet is a relatively thin, simple and robust network communication
layer on top of UDP (User Datagram Protocol). The primary feature
it provides is optional reliable, in-order delivery of packets.

This version built especially for EVpath.

%package -n lib%name%sover
Summary: Thin, simple and robust network layer on top of UDP
Group: System/Libraries

%description -n lib%name%sover
ENet is a relatively thin, simple and robust network communication
layer on top of UDP (User Datagram Protocol). The primary feature
it provides is optional reliable, in-order delivery of packets.

This version built especially for EVpath.

%package -n lib%name%sover-devel
Summary: Development files of lib%name%sover
Group: Development/C
Requires: lib%name%sover = %EVR
Conflicts: libenet-devel

%description -n lib%name%sover-devel
ENet is a relatively thin, simple and robust network communication
layer on top of UDP (User Datagram Protocol). The primary feature
it provides is optional reliable, in-order delivery of packets.

This version built especially for EVpath.

This package contains development files of ENet.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure \
	--enable-static=no
%make_build

%install
%makeinstall_std

%files -n lib%name%sover
%doc README
%_libdir/*.so.*

%files -n lib%name%sover-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20111115
- Initial build for Sisyphus

