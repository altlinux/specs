Name: libstroke
Version: 0.5.1
Release: alt11

%def_disable static
%def_disable gtk

Summary: Stroke interface library
License: GPLv2
Group: System/Libraries
Url: http://www.etla.net/libstroke

# %url/libstroke-%version.tar.gz
Source: libstroke-%version.tar
Source1: smr.m4
Source2: libstroke.m4
Source3: libgstroke.m4
Source4: gtk.m4

Patch1: libstroke-0.5.1-alt-compile.patch
Patch2: libstroke-0.5.1-alt-smr.patch
Patch3: libstroke-0.5.1-alt-makefile.patch

BuildRequires: libICE-devel libX11-devel
%if_enabled gtk
BuildRequires: gtk+-devel
%endif

%description
LibStroke is a stroke interface library.  Strokes are motions
of the mouse that can be interpreted by a program as a command.

%package devel
Summary: Development environment for libstroke
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required to build
libstroke-based software.

%package devel-static
Summary: Static libstroke library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static library required to build
statically linked libstroke-based software.

%package -n libgstroke
Summary: Stroke GTK interface library
Group: System/Libraries
Requires: %name = %version-%release

%description -n libgstroke
LibStroke is a stroke interface library.  Strokes are motions
of the mouse that can be interpreted by a program as a command.

This package contains libgstroke shared library.

%package -n libgstroke-devel
Summary: Development environment for libgstroke
Group: Development/C
Requires: libgstroke = %version-%release

%description -n libgstroke-devel
LibStroke is a stroke interface library.  Strokes are motions
of the mouse that can be interpreted by a program as a command.

This package contains development files required to build
libgstroke-based software.

%package -n libgstroke-devel-static
Summary: Static libgstroke library
Group: Development/C
Requires: libgstroke-devel = %version-%release

%description -n libgstroke-devel-static
LibStroke is a stroke interface library.  Strokes are motions
of the mouse that can be interpreted by a program as a command.

This package contains static library required to build
statically linked libgstroke-based software.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
install -p -m644 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 .
mv gtk.m4 acinclude.m4
sed -i '/^[[:space:]]*#/ d;/^EXTRA_DIST *= *$/ d' lib*/Makefile.am

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_libdir/libstroke.so.*
%doc AUTHORS ChangeLog COPYRIGHT CREDITS NEWS README* TODO doc/standard_strokes.*

%files devel
%_libdir/libstroke.so
%_includedir/stroke.h
%_datadir/aclocal/libstroke.m4
%_datadir/aclocal/smr.m4

%if_enabled static
%files devel-static
%_libdir/libstroke.a
%endif # static

%if_enabled gtk
%files -n libgstroke
%_libdir/libgstroke.so.*

%files -n libgstroke-devel
%_libdir/libgstroke.so
%_includedir/gstroke.h
%_datadir/aclocal/libgstroke.m4

%if_enabled static
%files -n libgstroke-devel-static
%_libdir/libgstroke.a
%endif # static
%endif # gtk

%changelog
* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt11
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt10
- Cleaned up License tag and descriptions.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt9
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Wed Jun 04 2008 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt8
- smr.m4: Fixed aclocal warnings (closes: #9319).
- Disabled libgstroke build and packaging by default (closes: #11403).

* Fri Mar 10 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt7
- Linked libgstroke with -lgtk.

* Thu Apr 14 2005 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt6
- Fixed build with fresh autotools.

* Sun Nov 30 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt5
- Do not package .la files.

* Fri Oct 03 2003 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt4
- Explicitly use old autotools for build.
- Do not build static library by default.

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.5.1-alt3
- rebuild

* Fri Dec 28 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.5.1-alt2
- Fixed smr_* macros duplication.

* Wed Nov 07 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.5.1-alt1
- Initial revision.
