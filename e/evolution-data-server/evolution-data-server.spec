%define ver_major 3.4
%define ver_base 3.4
%define ver_lib 1.2

%def_disable debug
%def_disable static
%def_with sys_db4
%def_with openldap
%def_disable static_ldap
%def_with krb5
%def_enable nntp
%def_enable goa
%def_disable gtk_doc
%def_enable introspection
%def_enable vala

Name: evolution-data-server
Version: %ver_major.3
Release: alt1

Summary: Evolution Data Server
License: %lgpl2plus
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/projects/evolution/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Patch1: %name-1.4.2.1-debug-lock.patch

# from configure.in
%define glib_ver 2.30.0
%define gtk3_ver 3.2.0
%define libsoup_ver 2.33.90
%define gnomekeyring_ver 2.32.0
%define sqlite_ver 3.5
%define gweather_ver 2.91.6
%define ical_ver 0.43
%define gdata_ver 0.9.1
%define goa_ver 3.1.1
%define vala_ver 0.13.1

BuildPreReq: rpm-build-gnome rpm-build-licenses intltool
BuildPreReq: gtk-doc >= 1.0
BuildPreReq: gnome-common
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk3_ver
BuildPreReq: libGConf-devel libdbus-glib-devel
BuildPreReq: libxml2-devel
BuildPreReq: libsoup-devel >= %libsoup_ver
BuildPreReq: libsqlite3-devel >= %sqlite_ver
BuildPreReq: libgweather-devel >= %gweather_ver
BuildPreReq: libical-devel >= %ical_ver
BuildPreReq: libgdata-devel >= %gdata_ver
BuildPreReq: libgnome-keyring-devel >= %gnomekeyring_ver
BuildRequires: gperf docbook-utils flex bison libcom_err-devel libnss-devel libnspr-devel zlib-devel
%{?_enable_goa:BuildRequires: libgnome-online-accounts-devel >= %goa_ver liboauth-devel libgdata-devel >= %gdata_ver}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel}
%{?_with_sys_db4:BuildRequires: libdb4-devel}
%{?_with_krb5:BuildRequires: libkrb5-devel}
%{?_enable_vala:BuildPreReq: vala >= %vala_ver vala-tools >= %vala_ver}

%if_with openldap
BuildRequires: libldap-devel
%if_enabled static_ldap
BuildRequires: libldap-devel-static libssl-devel libsasl2-devel
%endif
%endif

%description
Evolution Data Server provides a central location for
addressbook and calendar in the GNOME Desktop.

%package devel
Summary: Development files for Evolution Data Server
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides development files for Evolution Data Server

%package devel-doc
Summary: Development documentation for Evolution Data Server
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
Evolution Data Server provides a central location for
addressbook and calendar in the GNOME Desktop.

This package contains development documentation for Evolution Data Server.

%package gir
Summary: GObject introspection data for the EDS
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Evolution Data Server libraries

%package gir-devel
Summary: GObject introspection devel data for the EDS
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Evolution Data Server libraries

%package vala
Summary: Vala language bindings for the EDS libraries
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for the EDS libraries


%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec/%name

%add_findprov_lib_path %_libdir/%name-%ver_lib/extensions

%prep
%setup -q
%if_enabled debug
%patch1 -p1
%endif

%if_with sys_db4
rm -rf libdb
%__subst '/libdb\/Makefile/d' configure.ac
%__subst 's/^\(SUBDIRS.*\)\$(LIBDB)/\1/' Makefile.am
%endif

%build
%if_with openldap 
%if_enabled static_ldap
%define ldap_flags --with-openldap=yes --with-static-ldap 
# Set LIBS so that configure will be able to link with static LDAP libraries, 
# which depend on Cyrus SASL and OpenSSL.  XXX Is the "else" clause necessary? 
if pkg-config openssl ; then
        export LIBS="-lsasl2 `pkg-config --libs openssl`"
else
        export LIBS="-lsasl2 -lssl -lcrypto"
fi
%else
%define ldap_flags --with-openldap=yes
%endif
%else
%define ldap_flags --without-openldap
%endif

export CPPFLAGS="-I%{_includedir}/et"
export CFLAGS="$RPM_OPT_FLAGS -DLDAP_DEPRECATED -fPIC -I%{_includedir}/et"

%autoreconf
export ac_cv_path_SENDMAIL=%_sbindir/sendmail
export CAMEL_LOCK_HELPER_GROUP=mail
%configure \
%if_enabled debug
    --with-e2k-debug \
%endif
%if_with sys_db4
    --with-libdb=%_prefix \
%endif
    %{subst_enable static} \
    --enable-file-locking=fcntl \
    --enable-dot-locking=no \
    %ldap_flags \
    %{subst_enable nntp} \
    %{subst_enable goa} \
    --enable-smime \
%if_with krb5
    --with-krb5=%_prefix \
    --with-krb5-libs=%_libdir \
    --with-krb5-includes=%_includedir/krb5 \
%endif
    %{?_enable_gtk_doc:--enable-gtk-doc} \
    --disable-schemas-compile \
    %{?_enable_vala:--enable-vala-bindings}


%make_build

%install
%make_install DESTDIR=%buildroot install

# if unstable
ln -s camel-lock-helper-1.2 %buildroot%_libexecdir/camel-lock-helper

# remove none-packaged files
rm -f %buildroot%_libdir/%name-%ver_lib/*/*.la

%find_lang --with-gnome --output=%name.lang %name-%ver_base

%files -f %name.lang
%dir %_libexecdir
%_libexecdir/*
%dir %_libdir/%name/addressbook-backends
%dir %_libdir/%name/calendar-backends
%dir %_libdir/%name/camel-providers
%_libdir/%name/*/*.so
%_libdir/%name/*/*.urls
%_libdir/*.so.*
%_datadir/%name-*/
%_datadir/dbus-1/services/*
%_datadir/pixmaps/*
%_datadir/GConf/gsettings/libedataserver.convert
%_datadir/glib-2.0/schemas/org.gnome.evolution.eds-shell.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.evolution.shell.network-config.gschema.xml
%doc AUTHORS NEWS README MAINTAINERS

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%files devel-doc
%_gtk_docdir/*

%exclude %_libdir/%name/*/*.la

%if_enabled introspection
%files gir
%_typelibdir/ECalendar-1.2.typelib
%_typelibdir/EDataServer-1.2.typelib
%_typelibdir/EBook-1.2.typelib

%files gir-devel
%_girdir/ECalendar-1.2.gir
%_girdir/EDataServer-1.2.gir
%_girdir/EBook-1.2.gir
%endif

%if_enabled vala
%files vala
%_datadir/vala/vapi/*.deps
%_datadir/vala/vapi/*.vapi
%endif


%changelog
* Mon Jun 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt1
- 3.4.3

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Jan 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sun Sep 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92

* Sun Sep 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90
- new vala subpackage

* Wed Aug 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2.1-alt1
- 3.0.2.1

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.3-alt1
- 2.32.3

* Sat Mar 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt2
- updated buildreqs
- fixed build with newer GTK

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Thu Aug 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2.1-alt1
- 2.30.2.1

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Sat Mar 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0
- removed upstreamed patches
- removed upstreamed patch and other hacks for build with --as-needed

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92
- updated as_needed patch
- updated buildreqs

* Tue Mar 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3.1-alt1
- 2.28.3.1

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- updated patches

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3
- fixed krb5 detection

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri May 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1.1-alt2
- fixed build with new libtool_2.2

* Wed Apr 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1.1-alt1
- 2.26.1.1

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- drop upstreamed patches

* Wed Mar 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Mon Jan 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3
- fixed build from SVN (thanks shaba@)

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete *ldconfig from %%post{,un}

* Fri Nov 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1.1-alt1
- 2.24.1.1
- don't rebuild documentation

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Fri May 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.1-alt1
- 2.22.1.1

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1
- changed libexec dir to %_prefix/libexec/%name

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 1.12.3-alt1
- 1.12.3
- Removed patch for GNOME bug #363695 (causes issues)
- Add patch for RH bug #215702 / GNOME bug #487988 (fix ldap query)
- Run gtkdocize to avoid requiring gtk-doc 1.9

* Thu Nov 29 2007 Alexey Shabalin <shaba@altlinux.ru> 1.12.2-alt1
- 1.12.2

* Wed Nov 21 2007 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt2
- fix link with libedataserverui (evolution-data-server-1.11.3-as-needed.patch)
- remove set_verify_elf_method unresolved=relaxed

* Thu Oct 25 2007 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt1
- 1.12.1
- Disable patch for GNOME bug #376991 for now.  It may be contributing
  to password prompting problems as described in RH bug #296671.
- Remove patch for GNOME bug #420167 (fixed upstream)

* Fri Oct 12 2007 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt1
- 1.12.0
- Add support build with static ldap (default disable-> %%def_disable ldap_static)
- Add Requires: glib2 >= 2.14.0, since it's in the buildroot now, and
  forcibly introduces deps on symbols that don't exist in 2.13.  If
  only we had working symbol versioning.
- Add Requires: libbonobo >= 2.20.0, libgnome >= 2.20.0
- Add patch for GNOME bug #420167 (fix e-d-s leaks)
- Revise patches:
  + mandriva patch for fix empty error dialog in non utf8 locale
  + GNOME bug #417999 to fix GNOME bug #447591 
    (Automatic Contacts combo boxes don't work).
  + evolution-data-server-1.8.0-no-gnome-common.patch 
    so that we no longer have to run autoconf before building.
  + GNOME bug #363695 evolution-data-server-1.9.1-kill-ememory.patch
    (deprecate EMemPool, EStrv, EPoolv).
  + GNOME bug #376991.
- Remove patches:
  + RH bug #203058 (fixed upstream)
  + RH bug #210142 (fixed upstream)
  + GNOME bug #360240 (fixed upstream)
  + GNOME bug #360619 (fixed upstream)
  + GNOME bug #373117 (fixed upstream)
  + GNOME bug #415891 (fixed upstream)
  + GNOME bug #415922 (fixed upstream)
  + RH bug #215634 (fixed upstream)
  + GNOME bug #466987 (fixed upstream)

* Fri Aug 17 2007 Alexey Shabalin <shaba@altlinux.ru> 1.10.3.1-alt1
- Updated to 1.10.3.1
- change packager
- add/remove patches from fc7

* Sun Mar 25 2007 Ilya Mashkin <oddity@altlinux.ru> 1.8.3-alt2
- add some patches
- add URL

* Sat Feb 24 2007 Ilya Mashkin <oddity@altlinux.ru> 1.8.3-alt1
- Updated to 1.8.3

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 1.8.2-alt1
- New release 1.8.2

* Mon Oct 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.8.1-alt1
- Release 1.8.1

* Tue Sep 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.8.0-alt1
- Release 1.8.0
- Patch0 has gone upstream
- Enabled gnome-keyring
- Buildreq

* Fri Sep 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.3-alt1
- Release 1.6.3

* Thu Jun 01 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.2-alt1
- Release 1.6.2

* Sat Apr 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.1-alt1
- Release 1.6.1

* Wed Mar 15 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6.0-alt1
- Release 1.6.0

* Thu Mar 09 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.92-alt2
- Patch0: Adopted the dynamic libdb patch from Ross Burton (GNOME bug 319393)
- Enabled sys_db4 by default after a discussion on evolution-hackers
- Patch2: proper use of variables affecting the krb5 library test
- Relaxed the unresolved symbol check (proper fix blocked by GNOME bug 334169)

* Sun Mar 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.92-alt1
- 1.5.92

* Thu Feb 16 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5.91-alt1
- Updated to 1.5.91

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.2.1-alt2.1
- Rebuilt for new pkg-config dependencies.

* Sat Jan 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2.1-alt2
- Explicit dependency on libnss and libnspr

* Wed Dec 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2.1-alt1
- 1.4.2.1

* Wed Nov 30 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt2
- Disable system libdb patch by default in hope to stop
  index corruption
- Compile with separately installed libnspr and libnss

* Tue Nov 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.2-alt1
- 1.4.2
- Run intltoolize

* Sat Nov 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1.1-alt2.1
- Spec cosmetics
- Drop explicit nspr/nss configure flags, relying on mozilla .pc files instead

* Sat Oct 22 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1.1-alt2
- Version required for libsoup bumped to 2.2.6

* Wed Oct 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1.1-alt1
- 1.4.1.1

* Tue Oct 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.1-alt1
- 1.4.1
- Patch1 is obsolete
- Specify mozilla library directories

* Tue Sep 06 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0-alt1
- 1.4.0
- Updated Patch1

* Sun Sep 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.8-alt2
- --with-e2k-debug for the debug build
- --enable-nntp
- Correct name for lock helper (GNOME bug #305633) [Patch1]

* Fri Aug 26 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.8-alt1
- 1.3.8
- Updated Patch0

* Mon Aug 08 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.7-alt0.1
- 1.3.7

* Thu Aug 04 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.6.1-alt0.1
- 1.3.6.1

* Fri Jul 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.6-alt0.1
- 1.3.6

* Fri Jul 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.5-alt0.1
- 1.3.5
- Updated Patch0

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Tue Apr 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu Mar 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Fri Feb 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Sat Dec 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3
- development documentation moved to devel-doc subpackage.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Sep 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sun Sep 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.99-alt1
- 0.0.99

* Wed Aug 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.97-alt1
- 0.0.97

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.96-alt1
- 0.0.96

* Tue Jul 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.95-alt1
- 0.0.95

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.94.1-alt1
- 0.0.94.1

* Sat Jun 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.94-alt1
- 0.0.94

* Fri May 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.93-alt1
- 0.0.93

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.92-alt1
- 0.0.92

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.91-alt2
- rebuild against new gnutls (1.0.10)

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.91-alt1
- 0.0.91

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.90-alt1
- 0.0.90

* Thu Feb 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.7-alt2
- rebuild against libdb4.2

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.7-alt1
- 0.0.7

* Tue Jan 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.6-alt1
- First build for Sisyphus.
