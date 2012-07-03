%global __strip %_mingw32_strip
%global __objdump %_mingw32_objdump

Name: mingw32-glib2
Version: 2.33.1
Release: alt1

Summary: MinGW Windows GLib2 library

License: LGPLv2+
Group: Development/Other
Url: http://www.gtk.org

# first two digits of version
%define release_version %(echo %version | awk -F. '{print $1"."$2}')

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.gnome.org/sources/glib/%release_version/glib-%version.tar

BuildArch: noarch

%add_python_req_skip gdb

# Automatically added by buildreq on Mon Jun 25 2012
# optimized out: glib2-devel mingw32-binutils mingw32-cpp mingw32-expat mingw32-gcc mingw32-gettext mingw32-iconv mingw32-libjpeg mingw32-libpng mingw32-libtiff mingw32-pthreads mingw32-runtime mingw32-termcap mingw32-w32api mingw32-zlib pkg-config python-base python-devel python-module-distribute python-module-zope python-modules python-modules-xml xml-utils
BuildRequires: dbus gtk-doc indent libgdk-pixbuf-devel mingw32-dlfcn mingw32-gcc-c++ mingw32-gettext-static mingw32-libffi mingw32-libxml2 mingw32-wxGTK python-module-PyXML python-module-mwlib

BuildRequires: rpm-build-mingw32

BuildRequires: mingw32-filesystem >= 52
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-dlfcn
BuildRequires: mingw32-iconv
BuildRequires: mingw32-gettext
BuildRequires: mingw32-zlib

BuildRequires: pkg-config
# Native version required for msgfmt use in build
BuildRequires: gettext
# Native version required for glib-genmarshal
BuildRequires: glib2-devel

Requires: pkg-config

# As we're using libproxy-intl the libintl-8.dll dependency is a soft one
# To compile applications against glib2 we need to have gettext installed
# for it's headers
Requires: mingw32-gettext

%description
MinGW Windows Glib2 library.

%prep
%setup -n glib-%version

%build
%_mingw32_configure --disable-static
        # HACK
        cp glib/glibconfig.h ../glib
%make_build

%install
%makeinstall_std

# Manually merge the libtool files
#__subst s/"old_library=''"/"old_library='libgio-2.0.a'"/ %buildroot%_mingw32_libdir/libgio-2.0.la
#__subst s/"old_library=''"/"old_library='libglib-2.0.a'"/ %buildroot%_mingw32_libdir/libglib-2.0.la
#__subst s/"old_library=''"/"old_library='libgobject-2.0.a'"/ %buildroot%_mingw32_libdir/libgobject-2.0.la
#__subst s/"old_library=''"/"old_library='libgmodule-2.0.a'"/ %buildroot%_mingw32_libdir/libgmodule-2.0.la
#__subst s/"old_library=''"/"old_library='libgthread-2.0.a'"/ %buildroot%_mingw32_libdir/libgthread-2.0.la

rm -f %buildroot%_mingw32_libdir/charset.alias

# Drop the GDB helper files as we can't use the native Fedora GDB to debug Win32 programs
rm -rf %buildroot%_mingw32_datadir/gdb

# Remove the gtk-doc documentation and manpages which duplicate Fedora native
rm -rf %buildroot%_mingw32_mandir
rm -rf %buildroot%_mingw32_datadir/gtk-doc

# Bash-completion files aren't interesting for mingw32
rm -rf %buildroot%_mingw32_sysconfdir/bash_completion.d

# The .def files are also of no use to other binaries
rm -f %buildroot%_mingw32_libdir/*.def

# The gdbus-codegen pieces are already in the native glib2 package
rm -f %buildroot%_mingw32_bindir/gdbus-codegen
rm -rf %buildroot%_mingw32_libdir/gdbus-2.0

%find_lang glib20

%files -f glib20.lang
%_mingw32_bindir/gdbus.exe
%_mingw32_bindir/glib-compile-schemas.exe
%_mingw32_bindir/glib-compile-resources.exe
%_mingw32_bindir/glib-genmarshal.exe
%_mingw32_bindir/glib-gettextize
%_mingw32_bindir/glib-mkenums
%_mingw32_bindir/gobject-query.exe
%_mingw32_bindir/gio-querymodules.exe
%_mingw32_bindir/gsettings.exe
%_mingw32_bindir/gresource.exe
%_mingw32_bindir/gspawn-win32-helper-console.exe
%_mingw32_bindir/gspawn-win32-helper.exe
%_mingw32_bindir/libgio-2.0-0.dll
%_mingw32_bindir/libglib-2.0-0.dll
%_mingw32_bindir/libgmodule-2.0-0.dll
%_mingw32_bindir/libgobject-2.0-0.dll
%_mingw32_bindir/libgthread-2.0-0.dll
%_mingw32_includedir/glib-2.0/
%_mingw32_includedir/gio-win32-2.0/
%_mingw32_libdir/glib-2.0/
%dir %_mingw32_libdir/gio/
%dir %_mingw32_libdir/gio/modules/
%_mingw32_libdir/libgio-2.0.dll.a
%_mingw32_libdir/libgio-2.0.la
%_mingw32_libdir/libglib-2.0.dll.a
%_mingw32_libdir/libglib-2.0.la
%_mingw32_libdir/libgmodule-2.0.dll.a
%_mingw32_libdir/libgmodule-2.0.la
%_mingw32_libdir/libgobject-2.0.dll.a
%_mingw32_libdir/libgobject-2.0.la
%_mingw32_libdir/libgthread-2.0.dll.a
%_mingw32_libdir/libgthread-2.0.la
%_mingw32_libdir/pkgconfig/gio-2.0.pc
%_mingw32_libdir/pkgconfig/gio-windows-2.0.pc
%_mingw32_libdir/pkgconfig/glib-2.0.pc
%_mingw32_libdir/pkgconfig/gmodule-2.0.pc
%_mingw32_libdir/pkgconfig/gmodule-export-2.0.pc
%_mingw32_libdir/pkgconfig/gmodule-no-export-2.0.pc
%_mingw32_libdir/pkgconfig/gobject-2.0.pc
%_mingw32_libdir/pkgconfig/gthread-2.0.pc
%_mingw32_datadir/aclocal/glib-2.0.m4
%_mingw32_datadir/aclocal/glib-gettext.m4
%_mingw32_datadir/aclocal/gsettings.m4
%_mingw32_datadir/glib-2.0/

%if 0
%files static
%_mingw32_libdir/libgio-2.0.a
%_mingw32_libdir/libglib-2.0.a
%_mingw32_libdir/libgmodule-2.0.a
%_mingw32_libdir/libgobject-2.0.a
%_mingw32_libdir/libgthread-2.0.a
%endif

%changelog
* Mon Jun 25 2012 Vitaly Lipatov <lav@altlinux.ru> 2.33.1-alt1
- new version 2.33.1 (with rpmrb script)

* Fri Jun 17 2011 Vitaly Lipatov <lav@altlinux.ru> 2.28.6-alt1
- initial build for ALT Linux Sisyphus

* Thu Apr 28 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.6-3
- Own the folders %%{_mingw32_libdir}/gio and %%{_mingw32_libdir}/gio/modules
- Dropped the .def files as they aren't useful for other binaries

* Wed Apr 27 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.6-2
- Dropped the proxy-libintl pieces

* Sat Apr 23 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.28.6-1
- Update to 2.28.6
- Dropped the ugly build hack as it isn't needed anymore (the
  broken mingw32-runtime has been fixed by now)
- Made the pkgconfig LDFLAGS libtool friendly (fixes compilation for
  non-libtool based projects such as midori)

* Sun Feb 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.28.0-1
- update to 2.28.0

* Sun Feb 13 2011 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.27.93-1
- update to 2.27.93

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.27.4-1
- update to 2.27.4

* Sun Nov  7 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.0-4
- Fix a build failure in mingw32-libsoup and mingw32-webkitgtk

* Sun Oct 17 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.0-3
- Let binaries depending on GLib link against the libintl wrapper library
  in a way that libtool doesn't refuse

* Sat Oct 16 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.0-2
- Rebuild in order to make libintl-8.dll a soft dependency

* Mon Oct 11 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.26.0-1
- Update to 2.26.0

* Thu Sep 23 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.25.17-1
- Update to 2.25.17

* Sun Sep 12 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.25.15-1
- Update to 2.25.15

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.25.12-2
- recompiling .py files against Python 2.7 (rhbz#623338)

* Thu Aug  5 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.25.12-1
- update to 2.25.12

* Fri Jun 11 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.24.1-1
- Update to 2.24.1

* Wed Feb 24 2010 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.4-1
- Update to 2.23.4

* Sun Jan 31 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.23.2-1
- Update to 2.23.2

* Wed Dec  2 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.23.0-1
- Update to 2.23.0
- Added BR: mingw32-zlib

* Fri Oct  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.2-1
- Update to 2.22.2

* Wed Sep 23 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.22.0-1
- Update to 2.22.0

* Fri Sep 18 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.6-2
- Rebuild because of broken mingw32-gcc/mingw32-binutils

* Sat Sep  5 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.6-1
- Update to 2.21.6

* Mon Aug 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.5-1
- Update to 2.21.5

* Thu Aug 13 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.4-1
- Update to 2.21.4

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul  6 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.3-1
- Update to 2.21.3
- Drop upstreamed patch

* Mon Jun 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.2-2
- The wrong RPM variable was overriden for -debuginfo support. Should be okay now

* Mon Jun 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.2-1
- Update to 2.21.2
- Split out debug symbols to a -debuginfo subpackage

* Wed Jun 10 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.21.1-1
- Update to 2.21.1
- Use %%global instead of %%define
- Dropped the glib-i386-atomic.patch as it doesn't have any effect (the mingw32
  toolchain is called i686-pc-mingw32, not i386-pc-mingw32)

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 2.20.1-1
- Update to 2.20.1

* Thu Mar 5 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.19.10-1
- Update to 2.19.10
- Dropped the gtk-doc documentation as it's identical to the base glib2 package

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Erik van Pienbroek <info@nntpgrab.nl> - 2.19.5-4
- Added -static subpackage
- Developers using the static build of GLib need to add
  -DGLIB_STATIC_COMPILATION and -DGOBJECT_STATIC_COMPILATION to
  their CFLAGS to avoid compile failures
- Fixed the %%defattr line
- Rebuild for mingw32-gcc 4.4 (RWMJ)

* Fri Jan 30 2009 Richard W.M. Jones <rjones@redhat.com> - 2.19.5-3
- Requires pkg-config.

* Fri Jan 23 2009 Richard W.M. Jones <rjones@redhat.com> - 2.19.5-2
- Rebase to native Fedora version 2.19.5.
- Use _smp_mflags.
- Use find_lang.
- Don't build static libraries.
- +BR dlfcn.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.1-2
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.18.1-1
- Update to 2.18.1 release

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.18.0-3
- Remove manpages which duplicate Fedora native.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 2.18.0-2
- Add BR on pkgconfig, gettext and glib2 (native)

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 2.18.0-1
- Initial RPM release
