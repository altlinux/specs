%if_enabled static
%define buildstatic 1
%else
%define buildstatic 0
%endif

Name: libmal
Version: 0.44
Release: alt3

Group: System/Libraries
Summary: MAL library for AvantGo
Url: http://jasonday.home.att.net/code/libmal/libmal.html
License: MPL

Source: libmal-%version.tar.bz2
Patch: libmal-0.20-install.patch
Patch1: libmal-0.42-lib64.patch
Patch2: libmal-0.31-64bit-fixes.patch
Patch3: libmal-0.44-alt-cflags.patch

# Automatically added by buildreq on Thu Feb 12 2004 (-bi)
BuildRequires: glibc-devel libpilot-link-devel
%if %buildstatic
BuildRequires: glibc-devel-static
%endif

%description
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions.

%package utils
Summary: Sync to Mobile Application Link servers
Group: Communications
Requires: %name = %version-%release
Provides: %name-devel = %version-%release

%description utils
This package contains malsync.
This is command line utility to enable people who have Palm OS
devices to sync to Mobile Application Link (MAL) compliant servers.
AvantGo (www.avantgo.com) and Puma Technologies (www.pumatech.com)
are the first two companies committing to producing servers which speak
this protocol. This utility will allow a user to sync with multiple servers,
simultaneously or separately. The AvantGo.com service (www.avantgo.com)
is the first such server.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release
Provides: %name-devel = %version-%release

%description devel
The %name-devel package includes the header files and static libraries
necessary for developing programs using the %name library.

If you are going to develop programs which will use the %name library
you should install %name-devel.  You'll also need to have the %name
package installed.

%prep
%setup -q
#%patch -p1
%patch1 -p1 -b .lib64
%patch2 -p1 -b .64bit-fixes
%patch3 -p1 -b .cflags

#./autogen.sh
%autoreconf

%build
export CFLAGS="%optflags" CXXFLAGS="%optflags"
%configure \
%if %buildstatic
    --enable-static \
%else
    --disable-static \
%endif
    --enable-shared \
    --with-pilot-prefix=
#    --disable-pl-test
    
%make CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
%make DESTDIR=%buildroot install


%files
%doc README ChangeLog AUTHORS
%_libdir/*.so.*

%files utils
%doc malsync/Doc/README*
%_bindir/malsync

%files devel
%dir %_includedir/libmal/
%_includedir/libmal/*.h
%_libdir/*.so

%if %buildstatic
%files devel-static
%_libdir/*.la
%_libdir/*.a
%endif

%changelog
* Tue Jan 25 2011 Sergey V Turchin <zerg@altlinux.org> 0.44-alt3
- rebuilt

* Mon Dec 21 2009 Sergey V Turchin <zerg@altlinux.org> 0.44-alt2
- remove ldconfig from %%post

* Tue Jun 10 2008 Sergey V Turchin <zerg at altlinux dot org> 0.44-alt1
- new version

* Thu Oct 12 2006 Sergey V Turchin <zerg at altlinux dot org> 0.42-alt2
- rebuilt

* Tue Oct 10 2006 Sergey V Turchin <zerg at altlinux dot org> 0.42-alt1
- new version

* Thu Jan 26 2006 Sergey V Turchin <zerg at altlinux dot org> 0.40-alt2
- fix build on x86_64

* Thu Feb 12 2004 Sergey V Turchin <zerg at altlinux dot org> 0.40-alt1
- build for ALT

* Thu Oct 23 2003 Stefan van der Eijk <stefan@eijk.nu> 0.31-6mdk
- BuildRequires

* Fri Sep  5 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.31-5mdk
- lib64 & libtool fixes

* Thu Jul 10 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-4mdk
- Rebuild

* Wed Jul 09 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-3mdk
- Fix requires

* Wed Jul 09 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-2mdk
- Rebuild

* Mon Jul 07 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-1mdk
- Update 0.31 (thanks Texstar to point me it)

* Mon Apr 28 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.20-3mdk
- Fix spec file

* Fri Dec 20 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.20-2mdk
- Fix compile

* Tue Dec 17 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.20-1mdk
- Initial package, initial spec file by ShavenYak <shavenyak@smith.dyndns.org>
