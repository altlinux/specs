%def_enable cddb

Name: libcdio
Version: 2.0.0
Release: alt1.1

Summary: CD-ROM/CD-image access library
License: GPLv3+
Group: System/Libraries
Url: http://www.gnu.org/software/%name/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

#Source: ftp://ftp.gnu.org/gnu/libcdio/%name-%version.tar.gz
# git://git.sv.gnu.org/libcdio.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libncurses-devel help2man makeinfo
%{?_enable_cddb:BuildRequires: libcddb-devel}

%description
This library is to encapsulate CD-ROM reading and control. Applications
wishing to be oblivious of the OS- and device-dependant properties of a
CD-ROM can use this library.

%package -n libcdio++
Summary: C++ wrappers to the CD-ROM/CD-image access library
Group: System/Libraries
Requires: %name = %version-%release

%description -n libcdio++
These C++ libraries provide object-oriented wrappers to the libcdio APIs.

%package devel
Summary: %name development files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides %name development files.

%package -n libcdio++-devel
Summary: Development files for libcdio C++ wrappers
Group: Development/C++
Requires: libcdio++ = %version-%release
Requires: %name-devel = %version-%release

%description -n libcdio++-devel
This package provides development files for C++ wrappers to libcdio APIs.

%package utils
Summary: A simple utilities which read and displayings CD info.
Group: File tools
Requires: %name = %version-%release

%description utils
This package provides simple utilities which read and displayings CD
info.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	%{subst_enable cddb} \
	--enable-maintainer-mode \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README NEWS THANKS TODO
%_libdir/*.so.*
%_infodir/%name.info*
%exclude %_libdir/*++.so.*

%files devel
%_includedir/cdio
%_libdir/*.so
%_pkgconfigdir/*.pc
%exclude %_libdir/*++.so
%exclude %_pkgconfigdir/*++.pc

%files -n libcdio++
%_libdir/*++.so.*

%files -n libcdio++-devel
%_includedir/cdio++
%_libdir/*++.so
%_pkgconfigdir/*++.pc

%files utils
%_bindir/*
%_man1dir/*.1*

%changelog
* Mon Jan 15 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1.1
- merged lost changes

* Fri Jan 12 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Thu Mar 16 2017 Michael Shigorin <mike@altlinux.org> 0.94-alt1.1
- BOOTSTRAP: introduce cddb knob (on by default);
  breaks libcdio <-> libcddb BR loop

* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.94-alt1
- 0.94

* Mon Nov 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.93-alt1.1
- buildreqs: added makeinfo

* Mon Jul 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.93-alt1
- 0.93 (0.94_4f41eb68)

* Mon Apr 25 2011 Dmitry V. Levin <ldv@altlinux.org> 0.82-alt4
- Rebuilt for more debuginfo.

* Mon Apr 25 2011 Dmitry V. Levin <ldv@altlinux.org> 0.82-alt3
- Updated license information.
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.82-alt2
- rebuild

* Thu Nov 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.82-alt1
- 0.82

* Wed Sep 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.81-alt2
- Endless loop when no CD-rom drives (closes: #21508)

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.81-alt1
- 0.81

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.79-alt2
- Fix FTBFS with gcc 4.3.

* Tue Dec 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.79-alt1
- 0.79.

* Tue Nov 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.78.2-alt1
- 0.78.2.

* Sun Oct 29 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.78.1-alt1
- 0.78.1.
- Merge patches into source tree.

* Thu Oct 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.77-alt1
- Rebuild with newer libcddb.

* Tue May 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.77-alt0.2
- Added help2man to buildrequires.
- linux-libc-headers.

* Sun May 28 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.77-alt0.1
- Release 0.77
- Patch0: corrected interlibrary linkage issues
- Patch1 retired, not needed now
- Added packages for the C++ libraries
- Disable vcd to break a circular build dependency
- Do not test for cdparanoia during configure
- Buildreq

* Tue Mar 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.76-alt3
- Fixed build (linking with -lm).
- Building with libcddb & libvcd.

* Fri Feb 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.76-alt2
- Compressed ChangeLog (fixes #8972).

* Wed Nov 30 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.76-alt1
- 0.76 release.
- Fixed some errors in spec.

* Tue Jul 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.74-alt1
- 0.74

* Thu Jul 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.69-alt1
- 0.69

* Tue Jan 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.65-alt1
- First build for Sisyphus.
