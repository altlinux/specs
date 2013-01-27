# BEGIN SourceDeps(oneline):
BuildRequires: libICE-devel libSM-devel libglpk-devel libltdl7-devel libmicrohttpd-devel libmysqlclient-devel libpq5.4-devel python-devel
# END SourceDeps(oneline)
%define oname gnunet
Name: gnunet
Version: 0.9.1
Release: alt1

Summary: Peer-to-peer framework

License: GPL
Group: Communications
Url: http://gnunet.org/

Source: http://gnunet.org/download/%name-%version.tar
# (TODO: add pseudouser)
Source1: %{name}d.init.altlinux
# LSB init example
Source2: gnunetd.init.lsb

# manually removed: libqt3-devel libqt4-devel  xorg-cf-files
# Automatically added by buildreq on Mon Feb 01 2010
BuildRequires: cvs gcc-c++ glibc-devel guile18-devel imake libMySQL-devel libcurl-devel libextractor-devel libgcrypt-devel libglade-devel libncursesw-devel libsqlite3-devel zlib-devel

%description
GNUnet is a peer-to-peer framework with focus on providing security. All
peer-to-peer messages in the network are confidential and authenticated.
The framework provides a transport abstraction layer and can currently
encapsulate the network traffic in UDP (IPv4 and IPv6), TCP (IPv4 and IPv6),
HTTP, or SMTP messages. GNUnet supports accounting to provide contributing
nodes with better service. The primary service build on top of the framework
is anonymous file sharing.

%package -n lib%name
Summary: Libraries needed for %name
Group: System/Libraries

%description -n lib%name
GNUnet is a peer-to-peer framework with focus on providing security. All
peer-to-peer messages in the network are confidential and authenticated.
The framework provides a transport abstraction layer and can currently
encapsulate the network traffic in UDP (IPv4 and IPv6), TCP (IPv4 and IPv6),
HTTP, or SMTP messages. GNUnet supports accounting to provide contributing
nodes with better service. The primary service build on top of the framework
is anonymous file sharing.

%package -n lib%name-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure --disable-rpath
%make_build || %make

%install
%makeinstall_std
%find_lang %oname
install -D -m0755 %{SOURCE1} %buildroot%_initdir/gnunetd

# unpackaged files found
rm -f %buildroot/usr/share/doc/gnunet/COPYING

%files -f %{oname}.lang
%doc AUTHORS ChangeLog NEWS README
%doc %_man1dir/gnunet*.1*
%_bindir/gnunet-arm
%_bindir/gnunet-core-list-connections
%_bindir/gnunet-daemon-exit
%_bindir/gnunet-daemon-hostlist
%_bindir/gnunet-daemon-topology
%_bindir/gnunet-daemon-vpn
%_bindir/gnunet-dht-get
%_bindir/gnunet-dht-put
%_bindir/gnunet-directory
%_bindir/gnunet-download
%_bindir/gnunet-fs
%_bindir/gnunet-helper-hijack-dns
%_bindir/gnunet-helper-nat-client
%_bindir/gnunet-helper-nat-server
%_bindir/gnunet-helper-transport-wlan
%_bindir/gnunet-helper-vpn
%_bindir/gnunet-nat-server
%_bindir/gnunet-peerinfo
%_bindir/gnunet-pseudonym
%_bindir/gnunet-publish
%_bindir/gnunet-resolver
%_bindir/gnunet-search
%_bindir/gnunet-service-arm
%_bindir/gnunet-service-ats
%_bindir/gnunet-service-core
%_bindir/gnunet-service-datastore
%_bindir/gnunet-service-dht
%_bindir/gnunet-service-dns
%_bindir/gnunet-service-fs
%_bindir/gnunet-service-mesh
%_bindir/gnunet-service-nse
%_bindir/gnunet-service-peerinfo
%_bindir/gnunet-service-resolver
%_bindir/gnunet-service-statistics
%_bindir/gnunet-service-template
%_bindir/gnunet-service-transport
%_bindir/gnunet-statistics
%_bindir/gnunet-template
%_bindir/gnunet-testing
%_bindir/gnunet-transport
%_bindir/gnunet-transport-certificate-creation
%_bindir/gnunet-unindex
%_bindir/mockup-service
%_datadir/gnunet/
%_initdir/gnunetd

%files -n lib%name
%_libdir/gnunet/
%_libdir/libgnunetarm.so.*
%_libdir/libgnunetats.so.*
%_libdir/libgnunetblock.so.*
%_libdir/libgnunetcore.so.*
%_libdir/libgnunetdatacache.so.*
%_libdir/libgnunetdatastore.so.*
%_libdir/libgnunetdht.so.*
%_libdir/libgnunetfragmentation.so.*
%_libdir/libgnunetfs.so.*
%_libdir/libgnunethello.so.*
%_libdir/libgnunetmesh.so.*
%_libdir/libgnunetnat.so.*
%_libdir/libgnunetnse.so.*
%_libdir/libgnunetpeerinfo.so.*
%_libdir/libgnunetstatistics.so.*
%_libdir/libgnunettesting.so.*
%_libdir/libgnunettransport.so.*
%_libdir/libgnunettransporttesting.so.*
%_libdir/libgnunetutil.so.*

%files -n lib%name-devel
%_includedir/gnunet/
%_libdir/*.so
%_pkgconfigdir/gnunetarm.pc
%_pkgconfigdir/gnunetblock.pc
%_pkgconfigdir/gnunetcore.pc
%_pkgconfigdir/gnunetdatacache.pc
%_pkgconfigdir/gnunetdatastore.pc
%_pkgconfigdir/gnunetdht.pc
%_pkgconfigdir/gnunetdhtlog.pc
%_pkgconfigdir/gnunetdv.pc
%_pkgconfigdir/gnunetfragmentation.pc
%_pkgconfigdir/gnunetfs.pc
%_pkgconfigdir/gnunethello.pc
%_pkgconfigdir/gnunetnat.pc
%_pkgconfigdir/gnunetnse.pc
%_pkgconfigdir/gnunetpeerinfo.pc
%_pkgconfigdir/gnunetstatistics.pc
%_pkgconfigdir/gnunettesting.pc
%_pkgconfigdir/gnunettransport.pc
%_pkgconfigdir/gnunetutil.pc

%changelog
* Sun Jan 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1
- Friendly NMU: update to 0.9.1

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt3.1
- Fixed build

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt3
- fix build

* Thu Nov 25 2010 Paul Wolneykien <manowar@altlinux.ru> 0.8.1-alt2
- Add a GNUNet daemon service (init) script.

* Sun Jan 31 2010 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version (0.8.1) import in git

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1 - 5740+/dries
- Updated to release 0.7.2.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Initial package.
