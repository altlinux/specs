%def_disable static
%define ver_major 0.8

Name: libIDL
Version: %ver_major.14
Release: alt3

Summary: Library for parsing IDL (Interface Definition Language)
Group: System/Libraries
License: %lgpl2plus
Url: ftp://ftp.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

%define pkgconfig_ver 0.15-alt3.2
%define glib_ver 2.4.0

BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildPreReq: pkgconfig >= %pkgconfig_ver
BuildPreReq: glib2-devel >= %glib_ver

BuildRequires: gnome-common flex

%description
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

%package devel
Summary: Development libraries and header files for libIDL
Group: Development/C
Requires: %name = %version-%release

%description devel
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

This package contains the header files and libraries needed to write
or compile programs that use libIDL.

%package devel-doc
Summary: Development documentation for libIDL
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

This package contains the documentation needed to develop programs that
use libIDL.

%if_enabled static
%package devel-static
Summary: Static libraries for libIDL
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

This package contains static libraries needed to compile statically
linked programs that use %name.
%endif

%prep
%setup -q

%build
%configure \
    %{subst_enable static}

%make_build

%install
%makeinstall

mkdir %buildroot%_datadir/idl

%files
%_libdir/*.so.*
%doc AUTHORS README NEWS

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%dir %_datadir/idl
%doc BUGS HACKING MAINTAINERS

%files devel-doc
%_infodir/%{name}*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Mar 02 2011 Alexey Tourbin <at@altlinux.ru> 0.8.14-alt3
- rebuilt for debuginfo

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.14-alt2
- rebuild for soname set-versions

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.14-alt1
- new version

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 0.8.13-alt3
- removed obsolete %%{un,}install_info

* Fri Apr 17 2009 Yuri N. Sedunov <aris@altlinux.org> 0.8.13-alt2
- %%_datadir/idl owned by libIDL

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 0.8.13-alt1
- new version

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.8.12-alt1
- 0.8.12
- removed obsolete %%post{,un}_ldconfig
- move documentation to separate devel-doc subpackage

* Tue Aug 19 2008 Yuri N. Sedunov <aris@altlinux.org> 0.8.11-alt1
- new version

* Wed Mar 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.8.10-alt1
- New version (0.8.10).
- Use more RPM macros, including those from rpm-build-licenses and
  rpm-build-gnome.

* Fri Sep 21 2007 Igor Zubkov <icesik@altlinux.org> 0.8.9-alt1
- 0.8.8 -> 0.8.9

* Tue May 15 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8.8-alt1
- new version (0.8.8)
- spec cleanup

* Sun Aug 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.8.7-alt1
- new version 0.8.7 (with rpmrb script)

* Sun Aug 28 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Thu Aug 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.2-alt2
- do not package .la files.
- devel-static subpackage is optional.

* Mon May 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat May 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.8.0-alt1.1
- rebuild to move to the files

* Fri Jun 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Wed May 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt1
- Adopted for Sisyphus.
- devel-static package.

* Thu Apr 25 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- move include files to -devel
- other spec file tweaks

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 0.7.4

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- cvs snap 0.7.1.91

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- cvs snap, rebuild on new glib 1.3.11

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- glib 1.3.10

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- rebuild for new glib

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- initial build of standalone libIDL
- fix braindamage

