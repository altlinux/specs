%define ver_major 2.14
%def_disable static
%def_enable gtk_doc

Name: ORBit2
Version: %ver_major.19
Release: alt3

Summary: A high-performance CORBA Object Request Broker
Group: System/Libraries
License: %gpl2plus
Url: http://www.gnome.org/projects/%name

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2
Patch: %name-2.7.3-alt-test_makefile.patch
Patch1: %name-2.14.0-alt-shared_name-server.patch
Patch2: %name-2.13.3-fix-link-as-needed.patch

%define libIDL_ver 0.8.2
%define glib_ver 2.8.0
%define pkgconfig_ver 0.18

Requires: lib%name = %version-%release

BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildPreReq: pkgconfig >= %pkgconfig_ver
BuildPreReq: libIDL-devel >= %libIDL_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildRequires: indent libssl-devel 

%if_enabled gtk_doc
BuildRequires: docbook-dtds docbook-style-xsl gtk-doc xml-common xsltproc
%endif

%description
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker). It allows programs to send
requests and receive replies from other programs, regardless of the
locations of the two programs. CORBA is an architecture that enables
communication between program objects, regardless of the programming
language they're written in or the operating system they run on.

You will need to install this package and ORBit-devel if you want to
write programs that use CORBA technology.

%package -n lib%name
Summary: Shared libraries, header files and utilities for ORBit
Group: System/Libraries
License: %lgpl2plus

%description -n lib%name
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker). It allows programs to send
requests and receive replies from other programs, regardless of the
locations of the two programs. CORBA is an architecture that enables
communication between program objects, regardless of the programming
language they're written in or the operating system they run on.

This package contains the shared libraries required for ORBit
and components using it to function.

%package devel
Summary: Development libraries, header files and utilities for ORBit
Group: Development/GNOME and GTK+
License: %lgpl2plus
Requires: lib%name = %version-%release
#Requires: indent

%description devel
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker) with support for the C
language.

This package contains the header files, libraries and utilities
necessary to write programs that use CORBA technology. If you want to
write such programs, you'll also need to install the ORBit2 package.

%package devel-doc
Summary: Development documentation for ORBit
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker) with support for the C
language.

This package contains development documentation for ORBit.

%if_enabled static
%package devel-static
Summary: Static libraries for ORBit2
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker) with support for the C
language.

This package contains static versions of libraries from ORBit2 package.
%endif

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q
%patch -p1
%patch1 -p0
%patch2 -p0

%build
%autoreconf

%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

# SMP-incompatible build
%make

%check
%make check

%install
%makeinstall

# system orbitrc file
mkdir -p %buildroot%_sysconfdir
cat << EOF > %buildroot%_sysconfdir/orbitrc
## IIOP over IP server sockets disabled by default. Instead
## either UNIX domain sockets or shared memory for interprocess
## communication are used. This disables communcation over the network but
## prevents the system from Denial of Service attacks. If you want to use
## ORBit over the network you need to turn it on again (see
## http://orbit-resource.sourceforge.net/faq.html)

#ORBIIOPIPv4=1
#ORBLocalOnly=1
#ORBIIOPIPName=127.0.0.1
EOF

%files
%_bindir/typelib-dump
%_bindir/linc-cleanup-sockets
%dir %_libdir/orbit-2.0
%_libdir/orbit-2.0/*.so
%_datadir/idl/*
%config %_sysconfdir/orbitrc
%doc AUTHORS NEWS README

%files -n lib%name
%_libdir/*.so.*

%files devel
%_bindir/orbit2-config
%_bindir/orbit-idl-2
%_bindir/ior-decode-2
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*
%_datadir/aclocal/*
%doc HACKING MAINTAINERS TODO

%files devel-doc
%_gtk_docdir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%_libdir/*/*.a
%endif

%exclude %_libdir/*/*.la

%changelog
* Sat Feb 19 2011 Alexey Tourbin <at@altlinux.ru> 2.14.19-alt3
- rebuilt for debuginfo

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.14.19-alt2
- rebuild for soname set-versions

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.14.19-alt1
- 2.14.19

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.14.18-alt1
- new version

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.14.17-alt1
- 2.14.17
- removed obsolete %%post{,un}_ldconfig

* Thu Oct 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.16-alt2
- build devel-doc subpackage as noarch
- add system-wide orbitrc file

* Sun Sep 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.16-alt1
- new version

* Wed Sep 17 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.15-alt1
- new version

* Tue Aug 19 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.14-alt1
- new version
- don't rebuild documentation

* Mon Jun 09 2008 Yuri N. Sedunov <aris@altlinux.org> 2.14.13-alt1
- new version
- updared {Build}Requires

* Wed Mar 05 2008 Alexey Rusakov <ktirf@altlinux.org> 2.14.12-alt1
- New version (2.14.12).
- Spec cleanup (macroization and de-%%__-ization).
- Updated dependencies.

* Sat Sep 22 2007 Igor Zubkov <icesik@altlinux.org> 2.14.9-alt1
- 2.14.7 -> 2.14.9

* Sun Mar 18 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.7-alt1
- new version (2.14.7)
- fixed ALT bug 11075
- _unpackaged_files_terminate_build from now on.

* Thu Sep 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.3-alt1
- new version 2.14.3 (with rpmrb script)

* Sun Aug 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version
- spec cleanup

* Wed Mar 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)
- fixed linking with --as-needed.
- spec cleanup

* Thu Feb 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.3-alt1
- new version

* Tue Nov 08 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Sat Sep 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.4-alt1
- 2.12.4

* Tue Sep 13 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.3-alt2
- Fixed altbug #7916.

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.3-alt1
- 2.12.3

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Sat Feb 05 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.12.1-alt1
- 2.12.1
- documentation moved to devel-doc subpackage.

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.11.2-alt1
- 2.11.2

* Thu Aug 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.10.4-alt1
- 2.10.4

* Tue Jun 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.10.3-alt1
- 2.10.3

* Sat May 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.9.8-alt1
- 2.9.8

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.9.7-alt1
- 2.9.7

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.9.6-alt1
- 2.9.6

* Tue Jan 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.9.3-alt1
- 2.9.3

* Mon Dec 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.8.3-alt1
- 2.8.3

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt2
- do not package .la files.
- devel-static subpackage now is optional.

* Sun Oct 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.7.6-alt1
- 2.7.6

* Tue Jul 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.7.3-alt1
- 2.7.3

* Tue Jun 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.7.2-alt1
- 2.7.2

* Wed May 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.7.1-alt2
- make shared libname-server-2

* Sat May 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Sat Mar 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Sat Mar 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1
- move %_bindir/orbit-idl-2 to devel subpackage (close #2156)

* Tue Jan 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Dec 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sat Oct 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Sep 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.3-alt1
- 2.4.3
- Updated Buldrequires

* Wed May 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed May 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.3.110-alt1
- 2.3.110
- Adopted for Sisyphus.
- lib%name package.
- %name-2.3.109-ld.patch
- %name-am15.patch (PLD Team)

* Thu May 02 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu May  2 2002 Havoc Pennington <hp@redhat.com>
- 2.3.108

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- 2.3.107

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 2.3.105

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 2.3.103
- Rebuild for dependencies

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- build system somehow built against libglib-1.3.so.11
  even though pkg-config found 1.3.12? wtf?
  trying again

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 2.3.100.90 snap

* Mon Nov 26 2001 Havoc Pennington <hp@redhat.com>
- 2.3.99

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- new snap 2.3.97.90, rebuild for glib 1.3.11

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- new snap, glib 1.3.10 rebuild

* Tue Oct  9 2001 Havoc Pennington <hp@redhat.com>
- check rebuild against new linc with headers moved
- remove epoch, that was a screwup

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- cvs snap
- require specific glib2

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- 2.3.95 tarball
- depend on new standalone libIDL, remove all libIDL stuff from file list

* Fri Sep 21 2001 Havoc Pennington <hp@redhat.com>
- require specific linc version, unrequire specific glib version since
  we get that via linc

* Mon Sep 17 2001 Havoc Pennington <hp@redhat.com>
- newer orbit2 from CVS

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- conflict with old orbit with headers not moved

* Wed Sep 12 2001 Havoc Pennington <hp@redhat.com>
- renaming more things
- remove smp flags, doesn't work atm
- fix .pc file, trying to get bonobo-activation to build

* Tue Sep 11 2001 Havoc Pennington <hp@redhat.com>
- kill all file conflicts with ORBit1

* Mon Sep 10 2001 Havoc Pennington <hp@redhat.com>
- convert to ORBit2 spec file (from ORBit original)
