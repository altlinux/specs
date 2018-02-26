Name: libixp
Version: 0.5
Release: alt1

Summary: Plan9 file protocol library
License: MIT
Group: System/Libraries

Url: http://libs.suckless.org/libixp
Source: %name-%version.tar.gz
Patch: libixp-0.5-so.patch

%description
libixp is a stand-alone client/server 9P library.
libixp's server api is based heavily on that of Plan 9's lib9p.

%prep
%setup
%patch -p1

%ifarch x86_64
sed -i -r 's@/lib($|[ 	/])@/lib64\1@' config.mk
%endif


%build
%define soname libixp.so.0
%make_build LSONAME=%soname

%install
%makeinstall PREFIX=%buildroot%_prefix LSONAME=%soname
install lib/libixp.so %buildroot/%_libdir/%soname
ln -s %soname %buildroot/%_libdir/libixp.so

%files
%doc libixp/LICENSE*
%_libdir/%soname

%package devel
Summary: Plan9 file protocol library (development environment)
Group: Development/C
Requires: %name = %version-%release

%description devel
libixp is a stand-alone client/server 9P library.
libixp's server api is based heavily on that of Plan 9's lib9p.
This package contains development environment

%files devel
%doc examples
%_libdir/libixp.so
%_includedir/ixp*

%package devel-static
Summary: Plan9 file protocol library (static libraries)
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
libixp is a stand-alone client/server 9P library.
libixp's server api is based heavily on that of Plan 9's lib9p.
This package contains static libraries

%files devel-static
%_libdir/libixp*.a

%package -n ixpc
Summary: Plan9 file protocol client
Group: Networking/File transfer
Requires: %name = %version-%release

%description -n ixpc
ixpc is a client to access a 9P file server from the command line
or from shell scripts.

%files -n ixpc
%_bindir/ixpc
%_man1dir/ixpc.1*

%changelog
* Thu Apr 14 2011 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Autobuild version bump to 0.5
- Static libraries separated

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.3-alt0.3.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Mon Jun 18 2007 Alexey Tourbin <at@altlinux.ru> 0.3-alt0.3
- updated to 20070602 snapshot

* Mon Apr 02 2007 Alexey Tourbin <at@altlinux.ru> 0.3-alt0.2
- fixed rpm group

* Mon Apr 02 2007 Alexey Tourbin <at@altlinux.ru> 0.3-alt0.1
- initial revision
