Name: libschroedinger
Version: 1.0.10
Release: alt2

Summary: Library for decoding and encoding video in the Dirac format
Group: System/Libraries
License: LGPL/MIT/MPL
URL: http://www.diracvideo.org/

Source0: http://www.diracvideo.org/download/schroedinger/schroedinger-%version.tar.gz

#Patch0: ldadd.patch

Packager: Paul Wolneykien <manowar@altlinux.ru>

# Automatically added by buildreq on Thu Sep 23 2010
BuildRequires: gcc-c++ gtk-doc liborc-test-devel orc

BuildRequires: glib2-devel >= 2.10.0

%description
Library for decoding and encoding video in the Dirac format. It is implemented
in ANSI C and optimized through the us of liboil. libschro is written as a
collaboration between the BBC Research and Development, David Schleef and
Fluendo.

%package devel
Summary: Development files and static libraries for libschroedinger
Group: Development/C
Requires: %name = %version-%release

%description devel
libschroedinger-devel contains the files needed to build packages that depend
on libschroedinger.

%package devel-doc
Summary: Development documantation for libschroedinger
Group: Development/C
BuildArch: noarch

%description devel-doc
Development documantation for libschroedinger.

%prep
%setup -q -n schroedinger-%version
#%patch0 -p1

%build

%define _optlevel 3

%autoreconf
%configure \
	--disable-static \
	--enable-gtk-doc
%make_build

%install
%make_install DESTDIR=%buildroot install

%check
%make check

%files
%doc AUTHORS COPYING* NEWS TODO
%_libdir/libschroedinger-1.0.so.*

%files devel
%_pkgconfigdir/schroedinger-1.0.pc
%_libdir/libschroedinger-1.0.so
%_includedir/schroedinger-1.0

%files devel-doc
%_datadir/gtk-doc/html/schroedinger

%changelog
* Wed Oct 26 2011 Paul Wolneykien <manowar@altlinux.ru> 1.0.10-alt2
- Add glib-2.0 to the set of build requisites.

* Tue Sep 13 2011 Paul Wolneykien <manowar@altlinux.ru> 1.0.10-alt1
- Package new version 1.0.10.

* Sun Sep 26 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.9-alt2
- Mark devel-doc as noarch.

* Thu Sep 23 2010 Paul Wolneykien <manowar@altlinux.ru> 1.0.9-alt1
- Use GIT upstream: git://diracvideo.org/git/schroedinger.git.
- Upgrade to v1.0.9.

* Wed Mar 03 2010 Konstantin Pavlov <thresh@altlinux.org> 1.0.8-alt1
- 1.0.8 release.

* Fri Jul 31 2009 Konstantin Pavlov <thresh@altlinux.org> 1.0.7-alt2
- Fix installation of headers.

* Fri Apr 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.7-alt1
- 1.0.7 release.
- bump required liboil buildrequire.

* Tue Apr 21 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.0.6-alt1
- 1.0.6 release.
- Remove unneeded post/postun ldconfig calls.

* Thu Aug 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5-alt2
- Introduce gst-libschro subpackage (fixes #16920).
- Build with -O3 (fixes #16332).
- Fixed files section.

* Sat Jul 05 2008 Igor Zubkov <icesik@altlinux.org> 1.0.5-alt1
- 1.0.4 -> 1.0.5

* Sat Jul 05 2008 Igor Zubkov <icesik@altlinux.org> 1.0.4-alt1
- 1.0.3 -> 1.0.4

* Fri May 16 2008 Igor Zubkov <icesik@altlinux.org> 1.0.3-alt2
- rebuild

* Wed Apr 23 2008 Igor Zubkov <icesik@altlinux.org> 1.0.3-alt1
- 1.0.1 -> 1.0.3

* Fri Apr 04 2008 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt1
- 1.0.0 -> 1.0.1

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 1.0.0-alt1
- 0.9.0 -> 1.0.0

* Tue Nov 13 2007 Igor Zubkov <icesik@altlinux.org> 0.9.0-alt1
- 0.6.1 -> 0.9.0
- update patch0
- enable build gtk-doc documentation
- buildreq

* Fri Jun 08 2007 Igor Zubkov <icesik@altlinux.org> 0.6.1-alt1
- build for Sisyphus

* Thu Apr 05 2007 Thomas Vander Stichele <thomas at apestaart dot org>
- Further updates.

* Thu Apr 27 2006 Christian F.K. Schaller <christian@fluendo.com>
- Updates for carid -> schroedinger change
