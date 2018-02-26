%define ver_major 0.28

Name: vte
Version: %ver_major.2
Release: alt2

%def_enable pty_helper
%def_disable static
%def_enable python
%define gtk_api_ver 2.0
%define vte_api_ver 0.0

Summary: Terminal emulator widget for use with GTK+
License: LGPL
Group: Terminals

Obsoletes: vte-utils

Requires: lib%name = %version-%release

Source: ftp://gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Patch: vte-0.28.2-alt-python.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=663779
# http://bugzilla-attachments.gnome.org/attachment.cgi?id=201649
Patch1: vte-virtual_modifier_mapping.patch

%define gtk_ver 2.21.6
%define gtk3_ver 2.90.0
%define glib_ver 2.22.0
%define pango_ver 1.22

BuildPreReq: rpm-build-python

BuildRequires: libSM-devel libncurses-devel libcairo-devel
BuildRequires: intltool >= 0.35.0
BuildRequires: gtk-doc >= 1.1.0
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+2-devel >= %gtk_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: python-devel >= 2.4
%{?_enable_python:BuildRequires: python-module-pygtk-devel}
BuildRequires: gobject-introspection-devel

%description
VTE is a terminal emulator widget for use with GTK+

%package -n gnome-pty-helper
Summary: Helper setuid application
Group: Graphical desktop/GNOME

%description -n gnome-pty-helper
gnome-pty-helper is a program that setuid application used to open a
pseudo-terminal, set the permissions, ownership and record user login
information. This program is called internally by VTE library.

%package -n lib%name
Summary: Terminal emulator widget library for use with GTK+
Group: System/Libraries
Requires: gnome-pty-helper

%description -n lib%name
VTE is a terminal emulator widget for use with GTK+.
This package contains the VTE shared libraries.

%package -n lib%name-devel
Summary: Development files for VTE
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
VTE is a terminal emulator widget for use with GTK+. This package
contains the files needed for building applications using VTE.

%package -n lib%name-devel-doc
Summary: Development documentation for VTE
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
API documentation for the VTE library.
VTE is a terminal emulator widget for use with GTK+.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for VTE
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
VTE is a terminal emulator widget for use with GTK+. This package
contains the libraries needed for building applications statically
linked with VTE.
%endif	# enabled static

%package -n python-module-%name
Summary: Python bindings for VTE
Group: Development/Python
Requires: lib%name = %version-%release
# not added automatically
Requires: python-module-pygtk

%description -n python-module-%name
VTE is a terminal emulator widget for use with GTK+. This package
contains bindings to VTE for the Python scripting language.

%package -n python-module-%name-devel
Summary: Development files for Python bindings for VTE
Group: Development/Python
Requires: python-module-%name = %version-%release
Requires: lib%name-devel = %version-%release

%description -n python-module-%name-devel
VTE is a terminal emulator widget for use with GTK+. This package
contains development files for bindings to VTE for the Python scripting
language.

%define helperdir %_libdir/%name
%define pkgdocdir %_docdir/%name-%version

%prep
%setup -q
%patch
%patch1 -p1

%build
%autoreconf
%{?_enable_python:export PYTHON=%__python}
%configure \
	--disable-dependency-tracking \
	--libexecdir=%helperdir \
	--without-glX \
%if_enabled pty_helper
	--enable-gnome-pty-helper \
%else
	--disable-gnome-pty-helper \
%endif
	--enable-shared \
	%{subst_enable static} \
	%{subst_enable python} \
	--with-gtk=%gtk_api_ver

%make_build

%install
%make_install DESTDIR=%buildroot install

%__install -d -m755 %buildroot%pkgdocdir
%__install -p -m644 AUTHORS ChangeLog MAINTAINERS NEWS README %buildroot%pkgdocdir/
%__bzip2 %buildroot%pkgdocdir/ChangeLog
%__ln_s %_licensedir/LGPL-2 %buildroot%pkgdocdir/COPYING

%__install -p -m644 doc/utmpwtmp.txt doc/boxes.txt \
    %buildroot%pkgdocdir/
%__install -p -m644 src/iso2022.txt \
    %buildroot%pkgdocdir/
%__install -p -m644 doc/openi18n/*.txt \
    %buildroot%pkgdocdir/

# Remove unpackaged files
find %buildroot -type f -name '*.la' -delete

%find_lang %name-%vte_api_ver --output=%name.lang

%files
%_bindir/*

%if_enabled pty_helper
%files -n gnome-pty-helper
%dir %helperdir/*
%attr(2711,root,utmp) %helperdir/gnome-pty-helper
%endif

%files -n lib%name -f %name.lang
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/COPYING
%pkgdocdir/ChangeLog.bz2
%pkgdocdir/MAINTAINERS
%pkgdocdir/NEWS
%pkgdocdir/README
%_libdir/*.so.*
%_datadir/%name

%files -n lib%name-devel
%pkgdocdir/*.txt
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/vte.pc

%files -n lib%name-devel-doc
%doc %_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif	# enabled static

%if_enabled python
%files -n python-module-%name
%python_sitelibdir/gtk-%gtk_api_ver/*.so

%files -n python-module-%name-devel
%_datadir/pygtk/%gtk_api_ver/defs/vte.defs
%_libdir/pkgconfig/pyvte.pc
%endif

%changelog
* Wed Nov 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt2
- applied patch proposed in
  http://bugzilla-attachments.gnome.org/attachment.cgi?id=201649
  (ALT #26611)

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.28.2-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Thu Feb 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.26.2-alt2
- gnome-pty-helper moved to separate subpackage (preparation for vte3)

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 0.26.2-alt1
- 0.26.2

* Sun Oct 17 2010 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Sun Aug 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.25.91-alt1
- 2.25.91

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.24.3-alt1
- 0.24.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.24.2-alt1
- 0.24.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt1
- 0.24.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Thu Jan 14 2010 Yuri N. Sedunov <aris@altlinux.org> 0.23.5-alt1
- 0.23.5

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22.5-alt1.1
- Rebuilt with python 2.6

* Tue Nov 17 2009 Yuri N. Sedunov <aris@altlinux.org> 0.22.5-alt1
- 0.22.5

* Sun Nov 08 2009 Yuri N. Sedunov <aris@altlinux.org> 0.22.4-alt1
- 0.22.4

* Sat Oct 31 2009 Yuri N. Sedunov <aris@altlinux.org> 0.22.3-alt1
- 0.22.3

* Mon Sep 28 2009 Yuri N. Sedunov <aris@altlinux.org> 0.22.2-alt1
- 0.22.2

* Sat Sep 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.22.1-alt1
- 0.22.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Fri Sep 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.21.7-alt1
- 0.21.7

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.21.5-alt1
- 0.21.5

* Tue Jun 23 2009 Yuri N. Sedunov <aris@altlinux.org> 0.20.5-alt1
- 0.20.5

* Tue May 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- 0.20.3
- %%_libdir/vte owned by libvte package

* Tue May 05 2009 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Mon Jan 26 2009 Yuri N. Sedunov <aris@altlinux.org> 0.19.4-alt1
- 0.19.4
- new python-module-vte-devel subpackage
- updated buildreqs

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 0.17.4-alt1
- 0.17.4

* Mon Aug 11 2008 Yuri N. Sedunov <aris@altlinux.org> 0.16.14-alt2
- fix gnome bug #329108 (patch1)

* Mon Jun 30 2008 Yuri N. Sedunov <aris@altlinux.org> 0.16.14-alt1
- 0.16.14
- updated BuildRequires

* Thu Apr 24 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.13-alt2
- Fix bug #15213 (patch from Yury Aliaev <mutabor@altlinux.org>)

* Tue Mar 11 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.13-alt1
- 0.16.13

* Mon Jan 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.12-alt1
- 0.16.12

* Thu Sep 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.9-alt1
- 0.16.9

* Wed Sep 12 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.8-alt1
- 0.16.8

* Tue Jun 05 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.5-alt1
- 0.16.5

* Tue Jun 05 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.4-alt2
- Add OpenBSD patch, that fix some artefact problems

* Fri Jun 01 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.4-alt1
- Release 0.16.4

* Wed May 23 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.16.3-alt0.1
- Release 0.16.3

* Sat Oct 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.14.1-alt1
- Release 0.14.1

* Mon Sep 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.14.0-alt1
- Release 0.14.0
- Updated Patch0 & Patch1

* Sun May 28 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.12.2-alt1
- Release 0.12.2

* Fri Apr 28 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.12.1-alt1
- Release 0.12.1

* Tue Mar 14 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.12.0-alt1
- Release 0.12.0

* Sat Mar 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.21-alt1
- 0.11.21
- Patch0: detect and use libtinfo instead of ncurses
- Separated vte-utils and libvte-devel-doc packages

* Mon Feb 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.20-alt1
- 0.11.20

* Wed Feb 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.18-alt1
- 0.11.18

* Mon Jan 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.17-alt1
- 0.11.17

* Fri Jan 06 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.16-alt1
- 0.11.16
- More coherent doc installation
- Touched up sundry dependencies

* Tue Aug 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.15-alt1
- New upstream release

* Wed Aug 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.14-alt1
- New upstream release

* Sun Jun 05 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.13-alt2
- Removed libzvt-devel from build dependencies

* Wed Apr 20 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.13-alt1
- New upstream release

* Sun Mar 20 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.12-alt2
- Rebuilt with Python 2.4

* Fri Mar 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.12-alt1
- New upstream release

* Sat Nov 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.11-alt2
- Change build dependency to python-module-pygtk
- Use macros from rpm-build-python
- Added python target directory to %%_findprov_lib_path

* Tue Jul 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.11-alt1
- New upstream release
- Patch0 is obsolete
- Updated Patch1
- Renamed the python package to adhere to the New Policy

* Wed Jan 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.10-alt4
- Removed libXft-devel from BuildRequires (but see bug #2654)
- Development/Python group for the Python bindings

* Thu Dec 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.10-alt3
- Removed libtool files from the filelist

* Fri Oct 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.10-alt2
- Removed a bogus version macro

* Fri Jun 27 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.10-alt1
- New version
- Use utempter helper to update utmp/wtmp [Patch1]

* Fri Jun 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.9-alt2
- Patch0 updated

* Sun Jun 08 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.9-alt1
- New version
- Prevent configure from using glX, and let it choose over rendering
- Symlink the license from the shared licenses directory

* Tue Apr 29 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.4-alt1
- New version
- Patch0 updated

* Wed Apr 23 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.3-alt1
- New version
- Patch1 obsoleted
- --with-xft2 configure option

* Mon Mar 31 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.0-alt2
- A patch from Bugzilla against crash on tab exit [Patch1]

* Fri Mar 28 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.0-alt1
- New version

* Sat Mar 22 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.26-alt1
- 0.10.26
- Patch0: --disable-pty-helper was broken

* Wed Feb 12 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.17-alt1mhz1
- Added vte binary package with the vte binary
- Segregated the python module into the python subpackage

* Mon Feb 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.10.17-alt1
- 0.10.17

* Fri Jan 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.10.14-alt1
- 0.10.14

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.10.12-alt1
- 0.10.12

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.10.8-alt1
- 0.10.8

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.10.7-alt1
- 0.10.7

* Wed Dec 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.10.6-alt1
- 0.10.6

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.10.5-alt1
- 0.10.5

* Sun Nov 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.10.4-alt1
- 0.10.4

* Thu Nov 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt1
- First build for Sisyphus.
