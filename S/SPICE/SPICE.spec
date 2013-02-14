Name: SPICE
Version: 0.12.0
Release: alt2
Summary: Implements the SPICE protocol
Group: Graphical desktop/Other
License: LGPLv2+
Url: http://www.spice-space.org/

Source: http://www.spice-space.org/download/releases/%name-%version.tar
Source2: spice-common.tar
Source3: spice-protocol.tar
Patch1: fix-alt.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=613529
ExclusiveArch: %ix86 x86_64 armh

BuildRequires: cegui06-devel gcc-c++ 
BuildRequires: libXfixes-devel libXrandr-devel libXext-devel libX11-devel libXinerama-devel
BuildRequires: libalsa-devel libcelt051-devel libjpeg-devel libpixman-devel zlib-devel
BuildRequires: libssl-devel libsasl2-devel python-module-pyparsing
BuildRequires: libcacard-devel >= 0.1.2

%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

%package -n spice-client
Summary: Implements the client side of the SPICE protocol
Group: Graphical desktop/Other

%description -n spice-client
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the SPICE client application.

%package -n libspice-server
Summary: Implements the server side of the SPICE protocol
Group: System/Libraries

%description -n libspice-server
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the run-time libraries for any application that wishes
to be a SPICE server.

%package -n libspice-server-devel
Summary: Header files, libraries and development documentation for spice-server
Group: Development/C
Requires: libspice-server = %version-%release

%description -n libspice-server-devel
This package contains the header files, static libraries and development
documentation for spice-server. If you like to develop programs
using spice-server, you will need to install spice-server-devel.

%prep
%setup
tar -xf %SOURCE2 
tar -xf %SOURCE3 -C spice-common
%patch1 -p1

%build
rm -f GITVERSION
%autoreconf
%configure			\
	--enable-client		\
	--enable-gui		\
	--enable-smartcard	\
	--enable-static=no	\
	--with-sasl

%make_build

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_libdir/libspice-server.a
rm -f %buildroot%_libdir/libspice-server.la

%files -n spice-client
%doc COPYING README NEWS
%_bindir/spicec


%files -n libspice-server
%doc COPYING README NEWS
%_libdir/libspice-server.so.*

%files -n libspice-server-devel
%_includedir/spice-server
%_libdir/libspice-server.so
%_pkgconfigdir/spice-server.pc

%changelog
* Thu Feb 14 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.12.0-alt2
- Build for armh too

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.11.3-alt1
- 0.11.3

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.1
- Fixed build

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Thu Nov 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0
- build for 32-bit too

* Thu Sep 01 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt2
- add empty packages libspice-server and libspice-server-devel for fix autorebuild qemu on i586

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt2
- rebuild with cegui06-devel

* Fri May 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1 (thx to prividen@)

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Tue Jan 25 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Wed Jan 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt2
- don't build server for i586

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1
- enable smartcard support
- build server for i586 too

* Sat Nov 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
