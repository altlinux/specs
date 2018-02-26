%define oname GNUnet
Name: gnunet
Version: 0.8.1
Release: alt3

Summary: Peer-to-peer framework

License: GPL
Group: Communications
Url: http://gnunet.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://gnunet.org/download/%oname-%version.tar
Patch: %name-disable-ltdl-detect.patch
Patch1: %name-fix-pointer.patch
Patch2: %{name}d-service.patch

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
%setup -n %oname-%version
%patch -p2
%patch1 -p2
%patch2 -p2

%build
%autoreconf
%configure --disable-rpath
%make_build || %make

%install
%makeinstall_std
%find_lang %oname
install -D -m0755 gnunetd.service %buildroot%_initdir/gnunetd

%files -f GNUnet.lang
%doc AUTHORS ChangeLog NEWS README
%doc %_man1dir/gnunet*.1*
%doc %_man5dir/gnunet*.5*
%_bindir/gnunet-auto-share
%_bindir/gnunet-chat
%_bindir/gnunet-directory
%_bindir/gnunet-download
%_bindir/gnunet-insert
%_bindir/gnunet-peer-info
%_bindir/gnunet-pseudonym
%_bindir/gnunet-search
%_bindir/gnunet-stats
%_bindir/gnunet-tbench
%_bindir/gnunet-tracekit
%_bindir/gnunet-transport-check
%_bindir/gnunet-unindex
%_bindir/gnunet-update
%_bindir/gnunet-vpn
%_bindir/gnunet-setup
%_bindir/gnunetd
%_datadir/GNUnet/
%_initdir/gnunetd

%files -n lib%name
%_libdir/GNUnet/
%_libdir/libgnunetcollection.so.*
%_libdir/libgnunetcore.so.*
%_libdir/libgnunetchatapi.so.*
%_libdir/libgnunetdvdhtapi.so.*
%_libdir/libgnunetecrscore.so.*
%_libdir/libgnunetmysql.so.*
%_libdir/libgnunetremoteapi.so.*
%_libdir/libgnunettracekitapi.so.*
%_libdir/libgnunetecrs.so.*
%_libdir/libgnunetfs.so.*
%_libdir/libgnunetfsui.so.*
%_libdir/libgnunetgetoptionapi.so.*
%_libdir/libgnunetidentityapi.so.*
%_libdir/libgnunetip.so.*
%_libdir/libgnunetrpcutil.so.*
%_libdir/libgnunetsetup.so.*
%_libdir/libgnunettestingapi.so.*
%_libdir/libgnunettrafficapi.so.*
%_libdir/libgnunetnamespace.so.*
%_libdir/libgnunetstatsapi.so.*
%_libdir/libgnuneturitrack.so.*
%_libdir/libgnunetutil.so.*

%files -n lib%name-devel
%_includedir/GNUnet/
%_libdir/*.so

%changelog
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
