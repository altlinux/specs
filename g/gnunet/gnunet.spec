# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/git /usr/bin/svnversion glib2-devel libICE-devel libSM-devel libglpk-devel libgnutls-devel libidn-devel libltdl7-devel libmicrohttpd-devel libmysqlclient-devel libpq5.4-devel libunistring-devel pkgconfig(libgtop-2.0) python-devel
# END SourceDeps(oneline)
%define oname gnunet
Name: gnunet
Version: 0.9.5
Release: alt2

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
%doc %_man5dir/gnunet*.5*
%_bindir/gnunet-arm
%_bindir/gnunet-ats
%_bindir/gnunet-auto-share
%_bindir/gnunet-config
%_bindir/gnunet-core
%_bindir/gnunet-directory
%_bindir/gnunet-dns2gns
%_bindir/gnunet-download
%_bindir/gnunet-download-manager.scm
%_bindir/gnunet-ecc
%_bindir/gnunet-fs
%_bindir/gnunet-gns
%_bindir/gnunet-gns-import.sh
%_bindir/gnunet-gns-proxy-setup-ca
%_bindir/gnunet-mesh
%_bindir/gnunet-namestore
%_bindir/gnunet-nat-server
%_bindir/gnunet-peerinfo
%_bindir/gnunet-pseudonym
%_bindir/gnunet-publish
%_bindir/gnunet-resolver
%_bindir/gnunet-rsa
%_bindir/gnunet-search
%_bindir/gnunet-statistics
%_bindir/gnunet-template
%_bindir/gnunet-testing
%_bindir/gnunet-testing-run-service
%_bindir/gnunet-transport
%_bindir/gnunet-transport-certificate-creation
%_bindir/gnunet-unindex
%_bindir/gnunet-uri
%_bindir/gnunet-vpn
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
%_libdir/libgnunetdns.so.*
%_libdir/libgnunetdnsparser.so.*
%_libdir/libgnunetdnsstub.so.*
%_libdir/libgnunetfragmentation.so.*
%_libdir/libgnunetfs.so.*
%_libdir/libgnunetgns.so.*
%_libdir/libgnunetgns_common.so.*
%_libdir/libgnunethello.so.*
%_libdir/libgnunetlockmanager.so.*
%_libdir/libgnunetmesh.so.*
%_libdir/libgnunetmeshblock.so.*
%_libdir/libgnunetmysql.so.*
%_libdir/libgnunetnamestore.so.*
%_libdir/libgnunetnat.so.*
%_libdir/libgnunetnse.so.*
%_libdir/libgnunetpeerinfo.so.*
%_libdir/libgnunetregex.so.*
%_libdir/libgnunetstatistics.so.*
%_libdir/libgnunetstream.so.*
%_libdir/libgnunettestbed.so.*
%_libdir/libgnunettesting.so.*
%_libdir/libgnunettransport.so.*
%_libdir/libgnunettransporttesting.so.*
%_libdir/libgnunettun.so.*
%_libdir/libgnunetutil.so.*
%_libdir/libgnunetvpn.so.*

%files -n lib%name-devel
%_includedir/gnunet/
%_libdir/*.so
%_pkgconfigdir/gnunetarm.pc
%_pkgconfigdir/gnunetats.pc
%_pkgconfigdir/gnunetblock.pc
%_pkgconfigdir/gnunetcore.pc
%_pkgconfigdir/gnunetdatacache.pc
%_pkgconfigdir/gnunetdatastore.pc
%_pkgconfigdir/gnunetdht.pc
%_pkgconfigdir/gnunetdns.pc
%_pkgconfigdir/gnunetdnsparser.pc
%_pkgconfigdir/gnunetdv.pc
%_pkgconfigdir/gnunetfragmentation.pc
%_pkgconfigdir/gnunetfs.pc
%_pkgconfigdir/gnunetgns.pc
%_pkgconfigdir/gnunethello.pc
%_pkgconfigdir/gnunetlockmanager.pc
%_pkgconfigdir/gnunetmesh.pc
%_pkgconfigdir/gnunetmysql.pc
%_pkgconfigdir/gnunetnamestore.pc
%_pkgconfigdir/gnunetnat.pc
%_pkgconfigdir/gnunetnse.pc
%_pkgconfigdir/gnunetpeerinfo.pc
%_pkgconfigdir/gnunetpostgres.pc
%_pkgconfigdir/gnunetregex.pc
%_pkgconfigdir/gnunetstatistics.pc
%_pkgconfigdir/gnunetstream.pc
%_pkgconfigdir/gnunettestbed.pc
%_pkgconfigdir/gnunettesting.pc
%_pkgconfigdir/gnunettransport.pc
%_pkgconfigdir/gnunettun.pc
%_pkgconfigdir/gnunetutil.pc
%_pkgconfigdir/gnunetvpn.pc

%changelog
* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt2
- Rebuilt with glpk 4.48

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt1
- Friendly NMU: update to 0.9.5

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
