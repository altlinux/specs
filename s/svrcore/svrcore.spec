Summary:	Secure PIN handling using NSS crypto
Name:		svrcore
Version:	4.0.4
Release:	alt4
License:	MPL/GPL/LGPL
URL:		http://www.mozilla.org/projects/security/pki/
Group:		System/Libraries
Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/directory/svrcore/releases/4.0.4/%name-%version.tar.bz2

# Automatically added by buildreq on Tue Mar 10 2009
BuildRequires: gcc-c++ glibc-devel-static
BuildRequires: libnss-devel >= 3.12.9.0-alt2

%description
svrcore provides applications with several ways to handle secure PIN storage
e.g. in an application that must be restarted, but needs the PIN to unlock
the private key and other crypto material, without user intervention.  svrcore
uses the facilities provided by NSS.

%package -n lib%name
Summary:	Secure PIN handling using NSS crypto
Group:		System/Libraries
Provides:	%name = %version

%description -n lib%name
svrcore provides applications with several ways to handle secure PIN storage
e.g. in an application that must be restarted, but needs the PIN to unlock
the private key and other crypto material, without user intervention.  svrcore
uses the facilities provided by NSS.

%package -n lib%name-devel
Summary:	Development files for secure PIN handling using NSS crypto
Group:		Development/Other
Requires:	lib%name = %version-%release

%description -n lib%name-devel
svrcore provides applications with several ways to handle secure PIN storage
e.g. in an application that must be restarted, but needs the PIN to unlock
the private key and other crypto material, without user intervention.  svrcore
uses the facilities provided by NSS.

This package contains header files and symlinks to develop programs which will
use the libsvrcore library.  You should install this package if you need to
develop programs which will use the svrcore library.

%prep
%setup -q

%build
%configure
%make

%install
%make_install install DESTDIR=%buildroot
rm -f %buildroot/%_libdir/libsvrcore.a
rm -f %buildroot/%_libdir/libsvrcore.la

%files -n lib%name
%doc LICENSE README NEWS
%_libdir/libsvrcore.so.*

%files  -n lib%name-devel
%_libdir/pkgconfig/%name.pc
%_libdir/libsvrcore.so
%_includedir/svrcore.h

%changelog
* Thu Mar 10 2011 Alexey Gladkov <legion@altlinux.ru> 4.0.4-alt4
- Rebuilt to enable proper debuginfo.

* Fri Dec 17 2010 Alexey Gladkov <legion@altlinux.ru> 4.0.4-alt3
- Rebuilt for new depends.

* Tue Mar 10 2009 Alexey Gladkov <legion@altlinux.ru> 4.0.4-alt2
- Remove obsolete macros.
- Update buildrequires.

* Fri Jul 04 2008 Alexey Gladkov <legion@altlinux.ru> 4.0.4-alt1
- New version (4.0.4).

* Fri Feb 23 2007 Alexey Gladkov <legion@altlinux.ru> 4.0.3.01-alt1
- Build for ALT Linux.

* Wed Dec 13 2006 Rich Megginson <richm@stanfordalumni.org> - 4.0.3.01-0
- Fixed support for windows build by moving old makefile to src/Makefile.win
- and updating instructions - I could not get configure/libtool to work
- with cygwin and the msvc compiler
- Added support for --with-nspr and --with-nss and finding nspr/nss
- "in-tree" when building with other mozilla components
- Use PK11_TokenKeyGenWithFlags instead of PK11_KeyGen

* Fri Dec 08 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 4.0.2.02-0
- Test build based on an second experimental autotools version of svrcore.

* Thu Dec 07 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 4.0.2.01-0
- Test build based on an experimental autotools version of svrcore.

* Thu Jul 13 2006 Rich Megginson <rmeggins@redhat.com> - 4.0.2-3
- Bump spec rev to 3
- Remove unneeded buildrequires perl, gawk, sed
- Remove leading / from path macros
- Remove provides for package name - done automatically
- Move pkgconfig file stuff under install
- Added LICENSE and README under docs

* Mon Jun 26 2006 Rich Megginson <rmeggins@redhat.com> - 4.0.2-2
- Bump spec rev to 2 due to change of spec file name from svrcore
- to svrcore-devel to comply with fedora packaging guidelines

* Thu Jun 22 2006 Rich Megginson <rmeggins@redhat.com> - 4.0.2-1
- Bump rev to 4.0.2; now using HEAD of mozilla/security/coreconf
- which includes the coreconf-location.patch, so got rid of patch

* Tue Apr 18 2006 Rich Megginson <rmeggins@redhat.com> - 4.0.1-3
- Use pkg-config --variable=includedir to get include dirs

* Wed Feb  1 2006 Rich <rmeggins@redhat.com> - 4.0.1-2
- Requires nss version was wrong

* Wed Jan 11 2006 Rich Megginson <rmeggins@redhat.com> - 4.01-1
- Removed svrcore-config - use pkg-config instead

* Mon Dec 19 2005 Rich Megginson <rmeggins@redhat.com> - 4.01-1
- Initial revision
