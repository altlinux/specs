Name: libixp0
Version: 0.3
Release: alt1

Summary: Plan9 file protocol library
License: MIT
Group: System/Libraries
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

URL: http://www.suckless.org/wiki/libs/libixp
Source: %name-%version-%release.tar
Conflicts: libixp

%description
libixp is a stand-alone client/server 9P library.
libixp's server api is based heavily on that of Plan 9's lib9p.

%prep
%setup -n %name-%version-%release

%build
%define soname libixp.so.0
cp -p libixp/fcall.h include/ixp_fcall.h
gcc -shared %optflags %optflags_shared -Iinclude libixp/*.c -o %soname -Wl,-soname=%soname,-z,defs
gcc -DVERSION=\"%version-%release\" %optflags -Iinclude cmd/ixpc.c -o ixpc ./%soname

%install
install -pD -m644 include/ixp.h %buildroot%_includedir/ixp.h
install -pD -m644 include/ixp_fcall.h %buildroot%_includedir/ixp_fcall.h
install -pD -m755 %soname %buildroot%_libdir/%soname
ln -s %soname %buildroot%_libdir/libixp.so
install -pD -m755 ixpc %buildroot%_bindir/ixpc
install -pD -m644 man/ixpc.1 %buildroot%_man1dir/ixpc.1

%files
%doc libixp/LICENSE*
%_libdir/%soname

%package devel
Summary: Plan9 file protocol library
Group: Development/C
Requires: %name = %version-%release
Conflicts: libixp-devel

%description devel
libixp is a stand-alone client/server 9P library.
libixp's server api is based heavily on that of Plan 9's lib9p.

%files devel
%_libdir/libixp.so
%_includedir/ixp.h
%_includedir/ixp_fcall.h

%package -n ixpc0
Summary: Plan9 file protocol client
Group: Networking/File transfer
Requires: %name = %version-%release
Conflicts: ixpc

%description -n ixpc0
ixpc is a client to access a 9P file server from the command line
or from shell scripts.

%files -n ixpc0
%_bindir/ixpc
%_man1dir/ixpc.1*

%changelog
* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Rebuilt compat version as %name

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.3-alt0.3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Jun 18 2007 Alexey Tourbin <at@altlinux.ru> 0.3-alt0.3
- updated to 20070602 snapshot

* Mon Apr 02 2007 Alexey Tourbin <at@altlinux.ru> 0.3-alt0.2
- fixed rpm group

* Mon Apr 02 2007 Alexey Tourbin <at@altlinux.ru> 0.3-alt0.1
- initial revision
