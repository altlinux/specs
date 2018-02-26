%def_disable snapshot

%define ver_major 2.32
%define pcre_ver 8.11
%def_without sys_pcre
%def_enable selinux
%def_disable fam

%if_enabled snapshot
%def_enable gtk_doc
%else
%def_disable gtk_doc
%endif

Name: glib2
Version: %ver_major.3
Release: alt1

Summary: A library of handy utility functions
License: %lgpl2plus
Group: System/Libraries
Url: ftp://ftp.gnome.org

%if_enabled snapshot
Source: glib-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/glib/%ver_major/glib-%version.tar.xz
%endif

Source1: glib-compat.map
Source2: glib-compat.lds
Source3: gobject-compat.map
Source4: gobject-compat.lds
Source5: gio-compat.map
Source6: gio-compat.lds

Source10: glib2.sh
Source11: glib2.csh

# some tests broken
Patch: glib-2.29.16-alt-no_gapplication_tests.patch

%def_with locales
%if_with locales
Requires: %name-locales = %version
%endif

Provides: lib%name = %version
Obsoletes: lib%name < %version

Provides: %name-core = %version
Obsoletes: %name-core < %version

%if_with sys_pcre
BuildPreReq: libpcre-devel >= %pcre_ver
Requires: pcre-config(utf8) pcre-config(unicode-properties)
BuildPreReq: pcre-config(utf8) pcre-config(unicode-properties)

%endif

BuildRequires(pre): rpm-build-licenses
BuildPreReq: gtk-doc >= 1.8

BuildRequires: gtk-doc indent libdbus-devel libpcre-devel
BuildRequires: libffi-devel python-devel zlib-devel libelf-devel
%{?_enable_selinux:BuildRequires: libselinux-devel}
%{?_enable_fam:BuildRequires: libgamin-devel}

# for check
BuildRequires: /proc dbus-tools-gui desktop-file-utils
#BuildRequires: python-module-pygobject python-module-dbus

%description
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

%package locales
Summary: Glib internationalization
Group: System/Internationalization
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description locales
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

This package provides internationalization support for Glib.

%package devel
Summary: Development files and tools for GLib
Group: Development/C
Requires: %name = %version-%release
Requires: rpm-build-gir >= 0.5
Provides: lib%name-devel = %version
Obsoletes: lib%name-devel < %version

%description devel
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

This package provides header files and development tools for GLIB.

%package devel-static
Summary: Static version of GLib libraries
Group: Development/C
Requires: %name-devel = %version-%release
Provides: lib%name-devel-static = %version
Obsoletes: lib%name-devel-static < %version

%description devel-static
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

This package provides GLIB static libraries.

%package doc
Summary: Documentation for GLib
Group: Development/Documentation
Provides: %name-devel-doc = %version
Obsoletes: %name-devel-doc < %version
Conflicts: %name < %version, %name > %version
BuildArch: noarch

%description doc
GLib is the low-level core library that forms the basis for projects
such as GTK+ and GNOME. It provides data structure handling for C,
portability wrappers, and interfaces for such runtime functionality as
an event loop, threads, dynamic loading, and an object system.

This package contains documentation for GLib.

%package -n libgio
Summary: GIO input/output framework
Group: System/Libraries
Requires: %name = %version-%release
Requires: gsettings-desktop-schemas
Requires: shared-mime-info >= 0.80

%description -n libgio
GIO is a VFS API, designed to replace GnomeVFS. This GIO implementation is
a part of Glib project; it has support for local filesystems, and
a separate GVFS project contains various backend implementations (CIFS,
FTP, SFTP etc.).

%package -n libgio-devel
Summary: GIO input/output framework
Group: Development/C
Requires: libgio = %version-%release
Requires: %name-devel = %version-%release

%description -n libgio-devel
GIO is a VFS API, designed to replace GnomeVFS. This GIO implementation is
a part of Glib project; it has support for local filesystems, and
a separate GVFS project contains various backend implementations (CIFS,
FTP, SFTP etc.).

This package contains files necessary for development with GIO.

%package -n libgio-doc
Summary: GIO documentation
Group: Development/Documentation
# due to HTML links
Requires: %name-doc = %version
BuildArch: noarch

%description -n libgio-doc
GIO is a VFS API, designed to replace GnomeVFS. This GIO implementation is
a part of Glib project; it has support for local filesystems, and
a separate GVFS project contains various backend implementations (CIFS,
FTP, SFTP etc.).

This package contains documentation for GIO.

%if 0
%package gdb
%description gdb
%endif

%prep
%setup -q -n glib-%version

%if_with sys_pcre
rm glib/pcre/*.[ch]
%endif

install -p -m644 %_sourcedir/glib-compat.map glib/compat.map
install -p -m644 %_sourcedir/glib-compat.lds glib/compat.lds
install -p -m644 %_sourcedir/gobject-compat.map gobject/compat.map
install -p -m644 %_sourcedir/gobject-compat.lds gobject/compat.lds
install -p -m644 %_sourcedir/gio-compat.map gio/compat.map
install -p -m644 %_sourcedir/gio-compat.lds gio/compat.lds

# gapplication tests require x11
#%patch -b .tests

# abicheck always ok
for d in glib gio gobject; do
echo : >> $d/abicheck.sh
done

%build
%if_enabled snapshot
NOCONFIGURE=1 ./autogen.sh
%else
%autoreconf
%endif

%configure \
    --enable-static \
    %{subst_enable selinux} \
    --enable-fam \
    --enable-xattr \
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    --enable-included-printf=no \
    %{?_with_sys_pcre:--with-pcre=system} \
    %{subst_enable fam}

%make_build LIBTOOL_EXPORT_OPTIONS='-Wl,--version-script=compat.map -Wl,compat.lds'

%install
%make_install install DESTDIR=%buildroot

# Relocate libgilb-2.0.so.0 to /%_lib.
mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/libglib-2.0.so.0* %buildroot/%_lib
rm %buildroot%_libdir/libglib-2.0.so
ln -s ../../%_lib/libglib-2.0.so.0 %buildroot%_libdir/libglib-2.0.so

install -pD -m755 %_sourcedir/glib2.sh %buildroot%_sysconfdir/profile.d/glib2.sh
install -pD -m755 %_sourcedir/glib2.csh %buildroot%_sysconfdir/profile.d/glib2.csh

chmod +x %buildroot%_bindir/gtester-report

# GIO modules cache
touch %buildroot%_libdir/gio/modules/giomodule.cache
# filetrigger that updates GIO modules cache
cat <<EOF > filetrigger
#!/bin/sh -e

dir=%_libdir/gio/modules/
grep -qs '^'\$dir'' && /usr/bin/gio-querymodules \$dir ||:
EOF

install -pD -m 755 filetrigger %buildroot%_rpmlibdir/gio.filetrigger

# filetrigger that compiles all the GSettings XML schema files under %_datadir/glib-2.0/schemas
cat <<EOF > filetrigger
#!/bin/sh -e

dir=%_datadir/glib-2.0/schemas
grep -qs '^'\$dir'' && /usr/bin/glib-compile-schemas --allow-any-name \$dir ||:
EOF

install -pD -m 755 filetrigger %buildroot%_rpmlibdir/gsettings.filetrigger


%find_lang glib20
%set_verify_elf_method strict

%check
# g_mapped_file_new fails on /dev/null in hasher
#%%make check

%files
/%_lib/libglib-2.0.so.0*
%_libdir/libgobject-2.0.so.0*
%_libdir/libgmodule-2.0.so.0*
%_libdir/libgthread-2.0.so.0*
%config(noreplace) %_sysconfdir/profile.d/*
%doc AUTHORS NEWS README

%files locales -f glib20.lang

%files devel
%_bindir/glib-genmarshal
%_bindir/glib-gettextize
%_bindir/glib-mkenums
%_bindir/gobject*
%_bindir/gtester*
%dir %_includedir/glib-2.0
%_includedir/glib-2.0/glib*
%_includedir/glib-2.0/gobject*
%_includedir/glib-2.0/gmodule*
%dir %_libdir/glib-2.0
%dir %_libdir/glib-2.0/include
%_libdir/glib-2.0/include/*.h
%_libdir/libglib-2.0.so
%_libdir/libgmodule-2.0.so
%_libdir/libgobject-2.0.so
%_libdir/libgthread-2.0.so
%_pkgconfigdir/glib-2.0.pc
%_pkgconfigdir/gmodule*-2.0.pc
%_pkgconfigdir/gobject-2.0.pc
%_pkgconfigdir/gthread-2.0.pc
%_datadir/aclocal/glib*.m4
%_datadir/aclocal/gsettings.m4
%dir %_datadir/glib-2.0
%_datadir/glib-2.0/gettext/
%_man1dir/glib-genmarshal.*
%_man1dir/glib-gettextize.*
%_man1dir/glib-mkenums.*
%_man1dir/gobject*
%_man1dir/gtester*

%files devel-static
%_libdir/libglib-2.0.a
%_libdir/libgobject-2.0.a
%_libdir/libgthread-2.0.a
# gmodule and gio use dynamic loading
%exclude %_libdir/libgmodule-2.0.a
%exclude %_libdir/libgio-2.0.a
%if_enabled fam
%exclude %_libdir/gio/modules/libgiofam.a
%exclude %_libdir/gio/modules/libgiofam.la
%endif

%files doc
%doc %_datadir/gtk-doc/html/glib
%doc %_datadir/gtk-doc/html/gobject

%files -n libgio
%_bindir/gio-querymodules
%_bindir/gsettings
%_bindir/glib-compile-schemas
%_bindir/gresource
%_bindir/glib-compile-resources
%_bindir/gdbus
%_libdir/libgio-2.0.so.*
%dir %_libdir/gio
%dir %_libdir/gio/modules
%{?_enable_fam:%_libdir/gio/modules/libgiofam.so}
%_libdir/gio/modules/giomodule.cache
%_rpmlibdir/gio.filetrigger
%_rpmlibdir/gsettings.filetrigger
%_datadir/glib-2.0/schemas/
%_man1dir/gsettings.*
%_man1dir/glib-compile-schemas.*
%_man1dir/gresource.*
%_man1dir/glib-compile-resources.1*
%_man1dir/gdbus.*
%_man1dir/gio-querymodules.*
%_sysconfdir/bash_completion.d/gresource-bash-completion.sh

%files -n libgio-devel
%_bindir/gdbus-codegen
%_libdir/gdbus-2.0/codegen/
%dir %_includedir/glib-2.0
%dir %_includedir/glib-2.0/gio
%_includedir/glib-2.0/gio/*.h
%dir %_includedir/gio-unix-2.0
%dir %_includedir/gio-unix-2.0/gio
%_includedir/gio-unix-2.0/gio/*.h
%_libdir/libgio-2.0.so
%_pkgconfigdir/gio-2.0.pc
%_pkgconfigdir/gio-unix-2.0.pc
%_man1dir/gdbus-codegen.*

%files -n libgio-doc
%doc %_datadir/gtk-doc/html/gio

%exclude %_sysconfdir/bash_completion.d/gdbus-bash-completion.sh
%exclude %_sysconfdir/bash_completion.d/gsettings-bash-completion.sh
%exclude %_datadir/gdb/auto-load/%_libdir/libglib-2.0.so.0.*-gdb.py
%exclude %_datadir/gdb/auto-load/%_libdir/libgobject-2.0.so.0.*-gdb.py
%exclude %_datadir/glib-2.0/gdb/


%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3
- built with intenrnal PCRE as recommended
- disabled optional fam monitor support

* Mon May 07 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Sat Mar 24 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.31.22-alt1
- 2.31.22
- removed g_unix_resolver_get_type from gio-compat.lds

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Sat Nov 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.30.1-alt2.1
- Rebuild with Python-2.7
- bootstrap without python-module-pygobject python-module-dbus

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt2
- fixed https://bugzilla.gnome.org/show_bug.cgi?id=661896

* Sat Oct 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Jun 06 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.8-alt1
- 2.28.8

* Sat May 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.7-alt1
- 2.28.7

* Thu Apr 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt1
- 2.28.6

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.5-alt2
- glib2-devel requires rpm-build-gir >= 0.5

* Fri Apr 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.5-alt1
- 2.28.5
- %%check section

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Mon Mar 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Fri Feb 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Feb 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 2.26.2-alt3
- added ld scripts to mitigate symbol versioning issues

* Mon Feb 07 2011 Alexey Tourbin <at@altlinux.ru> 2.26.2-alt2
- rebuilt for debuginfo
- disabled symbol versioning

* Mon Dec 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2 current snapshot

* Sun Nov 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Sat Oct 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt3
- %%_datadir/glib-2.0/schemas/ moved to the libgio subpackage
- gsettings-desktop-schemas rqs moved to libgio

* Thu Oct 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- %%_datadir/glib-2.0/schemas/ moved to the main glib2 subpackage
- gsettings-desktop-schemas added to rqs

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sun Sep 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.25.17-alt1
- 2.25.17

* Sun Aug 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Sat Jul 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.25.12-alt1
- 2.25.12

* Thu Jun 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.25.10-alt1
- 2.25.10
- updated version scripts for GLIB_2.25.10 and GIO_2.25.10

* Mon May 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Mar 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Mar 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.6-alt1
- 2.23.6
- updated version scripts for GLIB_2.23.6

* Tue Mar 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.5-alt1
- 2.22.5

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.5-alt1
- 2.23.5
- updated version scripts for GLIB_2.23.5

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.4-alt1
- 2.23.4
- updated version scripts for GLIB_2.23.4 and GIO_2.23.4

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.3-alt1
- 2.23.3

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.2-alt1
- 2.23.2

* Thu Dec 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt1
- 2.23.1

* Tue Dec 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.22.3-alt1
- 2.22.3

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.22.2-alt1
- 2.22.2

* Wed Sep 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.22.1-alt1
- 2.22.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.21.6-alt1
- 2.21.6

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.21.5-alt1
- 2.21.5 
- updated version scripts for GIO_2.21.5

* Mon Aug 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt1
- 2.21.4
- updated version scripts for GLIB_2.21.4 and GIO_2.21.4

* Sat Jun 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.4-alt1
- 2.20.4

* Sat May 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.3-alt1
- 2.20.3

* Sun May 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.2-alt1
- 2.20.2

* Fri Apr 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.1-alt1
- 2.20.1

* Fri Mar 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Mon Mar 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.10-alt1
- 2.19.10

* Wed Feb 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.8-alt1
- 2.19.8

* Tue Feb 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.6-alt1
- 2.19.6
- updated version script for GIO_2.19.6

* Tue Jan 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.5-alt1
- 2.19.5
- drop upstreamed patches
- updated version scripts for GLIB_2.19.5, GIO_2.19.5

* Sat Jan 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.18.4-alt1
- 2.18.4

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.18.3-alt1
- 2.18.3
- drop upstreamed patches
- remove obsolete ldconfig from %%post{,un}

* Sun Nov 09 2008 Yuri N. Sedunov <aris@altlinux.org> 2.18.2-alt2
- fix gnome bugs ##528670, 528320

* Fri Oct 17 2008 Yuri N. Sedunov <aris@altlinux.org> 2.18.2-alt1
- 2.18.2

* Thu Sep 18 2008 Alexey Tourbin <at@altlinux.ru> 2.18.1-alt1
- 2.16.6 -> 2.18.1
- updated version scripts for shared libraries (GLIB_2.18, GIO_2.18)
- only libglib-2.0.so.0 must be relocated from /usr/lib to /lib
- renamed /etc/profile.d/libglib2.sh back to glib2.sh (in setup-2.2.8-alt1,
  lang.sh was renamed to 0lang.sh, so now it goes before glib2.sh)
- glib2: split glib2-locales subpackage (noarch)
- glib2-devel-doc: renamed to glib2-doc, split libgio-doc (noarch)
- glib2-devel-static: packaged only libglib-2.0.a, libgobject-2.0.a,
  and libgthread-2.0.a (libgmodule-2.0 and libgio-2.0 use dynamic loading,
  and should not be used for static linking)

* Sat Sep 13 2008 Yuri N. Sedunov <aris@altlinux.org> 2.16.6-alt1
- new bugfix release
- build with system pcre, always enable regex (at@)

* Sun Jul 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.16.5-alt1
- new version
- temporarily disabled gtk-doc due to gnome bug #543855

* Wed Jul 02 2008 Yuri N. Sedunov <aris@altlinux.org> 2.16.4-alt1
- new version
- libgio reqiures %%name = %%version-%%release
- small fix in gtester-report

* Wed Apr 09 2008 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version (2.16.3)

* Tue Mar 11 2008 Alexey Rusakov <ktirf@altlinux.org> 2.16.1-alt1
- New version (2.16.1).

* Sat Mar 01 2008 Alexey Rusakov <ktirf@altlinux.org> 2.15.6-alt1
- New version (2.15.6).
- Updated dependencies and version scripts.
- New subpackages, libgio and libgio-devel.
- %%__autoreconf -> %%autoreconf.

* Thu Jan 10 2008 Alexey Rusakov <ktirf@altlinux.org> 2.14.5-alt1
- New version (2.14.5).

* Sat Dec 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.4-alt1
- new version (2.14.4)

* Thu Nov 08 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.3-alt1
- New version (2.14.3).
- Added --enable-regex switch.
- Enforce usage of the system supplied printf (just to make sure).

* Tue Oct 02 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.1-alt4
- fixed files in -devel moved accidentally to /lib, too.

* Mon Oct 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.1-alt3
- made the splitting optional, disabled by default (since it brings some
  troubles if glib2 is being installed as a dependency).

* Sat Sep 29 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.1-alt2
- split out glib2-core from glib2 and moved its contents to /lib, since
  system programs depend on glib2 (ALT Bug #12936).

* Mon Sep 17 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.1-alt1
- new version (2.14.1)

* Mon Aug 27 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.0-alt1
- new version
- updated symver scripts
- removed %%__ macros
- use macros from rpm-build-gnome and rpm-build-licenses

* Fri Jul 27 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.13-alt1
- new version 2.12.13 (with rpmrb script)

* Sun May 20 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.12-alt1
- new version (2.12.12)

* Sun Jan 21 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.9-alt1
- new version 2.12.9 (with rpmrb script)

* Fri Jan 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.12.7-alt1
- new version 2.12.7 (with rpmrb script)

* Tue Oct 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.4-alt2
- enabled building static libraries.
- fixed typos in comments.

* Tue Oct 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.4-alt1
- new version 2.12.4 (with rpmrb script)

* Thu Aug 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.2-alt1
- new version 2.12.2 (with rpmrb script)

* Tue Jul 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version 2.12.1 (with rpmrb script)

* Mon Jul 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- new version (2.12.0)

* Sun May 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.3-alt1
- new version 2.10.3 (with rpmrb script)

* Sat Apr 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.2-alt1
- new version (2.10.2)

* Thu Mar 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10.1-alt1
- new version (2.10.1)

* Sun Feb 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.9.6-alt1
- new version
- fixed bug #9005

* Sun Jan 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.9.5-alt1
- new version

* Thu Jan 26 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.9.4-alt1
- new version

* Sat Jan 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.6-alt1
- new version

* Sat Jan 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.5-alt2
- replaced pkgconfig with pkg-config.

* Wed Jan 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8.5-alt1
- new version

* Wed Nov 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.4-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.3-alt1
- new version

* Tue Sep 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 2.8.1-alt2
- NMU: introduced GLIB_2.8 ABI interface for new functions in
  libglib-2.0.so.0 and libgobject-2.0.so.0

* Sun Aug 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.1-alt1
- 2.8.1
- Renamed scripts for profile.d so that they go after lang.* scripts
  (thanks to Vitaly Lipatov).

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Wed Apr 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3
- set G_FILENAME_ENCODING using natspec.

* Fri Feb 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sat Jan 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Thu Dec 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Fri Dec 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.7-alt1
- 2.5.7
- documentation moved to devel-doc subpackage.

* Tue Nov 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt2
- fix #5567 (thanks lav@).

* Sat Nov 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Thu Nov 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Mon Sep 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Mon Aug 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.6-alt1
- 2.4.6

* Sat Jul 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.5-alt1
- 2.4.5
- #4873 fixed in upstream.

* Mon Jul 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4-alt1.1
- fix g_unescape_uri_string. Thanks lav@ (close #4873).

* Sun Jul 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Fri Apr 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Mar 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Fri Jan 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed Dec 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt2
- do not package .la files.
- devel-static subpackage is optional now.

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Mon Jun 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Sat Dec 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Wed Nov 27 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt2
- remove deps on csh by fixing headers of /etc/profile.d files

* Tue Nov 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Sun Sep 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt2
- glib2.{sh,csh) added (RH).

* Sat Sep 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt1
- 2.0.6
- fixed-ltmain.sh removed, not needed more.
- post/postun scripts improved.
- gcc-3.2 used.

* Fri Jun 14 2002 Igor Androsov <blake@altlinux.ru> 2.0.4-alt1
- New release

* Wed May 29 2002 Igor Androsov <blake@altlinux.ru> 2.0.3-alt2
- Return removed in 2.0.1-alt2 fixed-ltmain.sh - fixed not installing
  gobject, module, gthread if host where building not have installed
  glib2-devel

* Tue May 28 2002 Igor Androsov <blake@altlinux.ru> 2.0.3-alt1
- New release

* Thu May 23 2002 Igor Androsov <blake@altlinux.ru> 2.0.1-alt2
- clean spec
- added /usr/share/glib-2.0/*

* Sun Mar 31 2002 AEN <aen@logic.ru> 2.0.1-alt1
- new verson

* Wed Mar 27 2002 AEN <aen@logic.ru> 2.0.0-alt1
- release

* Tue Feb 05 2002 AEN <aen@logic.ru> 1.3.12.90-alt2
- .so links moved to devel

* Wed Jan 09 2002 AEN <aen@logic.ru> 1.3.12.90 -alt1
- sources from Rawide

* Wed Oct 17 2001 AEN <aen@logic.ru> 1.3.9-alt1
- new version

* Tue Sep 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3.7-alt1
- Renamed to glib2.

* Fri Sep 21 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.7-alt1
- 1.3.7

* Fri Jun 15 2001 AEN <aen@logic.ru> 1.3.6-alt1
- new version
- BuildReq added
- Make patch
* Thu May 31 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Fri Apr 20 2001 Stanislav Ievlev <inger@altlinux.ru> 1.3.4-alt1
- Up to 1.3.4. Cleanup spec, librification, statification

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation

* Mon Nov 20 2000 DindinX <odin@mandrakesoft.com> 1.3.2-3mdk
- redo my patch to best fit glib-1.3.2
- move %%doc to -devel

* Mon Nov 20 2000 Daouda Lo <daouda@mandrakesoft.com> 1.3.2-2mdk
- regenerate Dindinx's patch.

* Sat Nov 18 2000 Daouda Lo <daouda@mandrakesoft.com> 1.3.2-1mdk
- release

* Wed Nov 15 2000 DindinX <odin@mandrakesoft.com> 1.3.1-1mdk
- version 1.3.1 (first pre2)

