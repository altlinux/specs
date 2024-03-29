%define _libexecdir %_prefix/libexec

%define oldname libgtop2
%define ver_major 2.41
%define api_ver 2.0

%def_disable static
%def_with examples
%def_enable introspection
%def_enable check

Name: libgtop
Version: %ver_major.3
Release: alt1

Summary: LibGTop library
License: GPLv2+
Group: System/Libraries
Url: ftp://ftp.gnome.org

Obsoletes: %oldname < 2.14.2
Provides: %oldname = %EVR

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Patch2: %name-2.0.0-texinfo.patch
Patch4: %name-2.9.90-alt-examples_makefile.patch

# from configure.ac
%define glib_ver 2.26.0

BuildPreReq: rpm-build-gnome
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: gtk-doc >= 1.4
BuildRequires: makeinfo
BuildRequires: libICE-devel libX11-devel perl-XML-Parser
%{?_enable_static:BuildPreReq: glibc-devel-static}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.6.7}

%description
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

On Linux systems, this information is taken directly from the /proc
filesystem while on other systems a server is used to read that
information from other /dev/kmem, among others.

%package examples
Group: Development/GNOME and GTK+
Summary: The LibGTop samples
Obsoletes: %oldname-examples < 2.14.2
Provides: %oldname-examples = %EVR
Requires: %name = %EVR

%description examples
This package contains some example of using %name library

%package devel
Summary: Development files for %name
Group: Development/GNOME and GTK+
Obsoletes: %oldname-devel < 2.14.2
Provides: %oldname-devel = %EVR
Requires: %name = %EVR

%description devel
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

Install this package if you wish to develop applications that access
information on system statistics such as CPU and memory usage.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name-devel < %version-%release
BuildArch: noarch

%description devel-doc
LibGTop is a library that fetches information about the running
system such as CPU and memory useage, active processes and more.

This package contains development documentation for the library.

%package devel-static
Summary: Static libraries for %name
Group: Development/GNOME and GTK+
Obsoletes: %oldname-devel-static < 2.14.2
Provides: %oldname-devel-static = %EVR
Requires: %name-devel = %EVR

%description devel-static
This package contains static libraries for development with %name.

%package gir
Summary: GObject introspection data for the LibGTop library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the LibGTop library

%package gir-devel
Summary: GObject introspection devel data for the LibGTop library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the LibGTop library


%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup
%patch2 -p1
%patch4 -p1

rm -rf doc/*.info

%build
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-gtk-doc \
	%{subst_with examples}
%make_build

%install
%makeinstall_std
%find_lang %name

%check
%make -k check VERBOSE=1

%files -f %name.lang
%_libexecdir/%{name}_daemon2
%attr(4711,root,root) %_libexecdir/%{name}_server2
%_libdir/*.so.*
%doc AUTHORS NEWS README

%if_with examples
%files examples
%dir %_libdir/%name
%_libdir/%name/*
%endif

%files devel
%_includedir/%name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/*
%_infodir/*.info*

%files devel-doc
%_gtk_docdir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%if_enabled introspection
%files gir
%_typelibdir/GTop-%api_ver.typelib

%files gir-devel
%_girdir/GTop-%api_ver.gir
%endif

%changelog
* Fri Feb 16 2024 Yuri N. Sedunov <aris@altlinux.org> 2.41.3-alt1
- 2.41.3

* Sun Oct 15 2023 Yuri N. Sedunov <aris@altlinux.org> 2.41.2-alt1
- 2.41.2

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 2.34.2-alt1
- 2.34.2

* Sat Aug 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.34.1-alt1
- 2.34.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1.1
- 2.34.0

* Mon Nov 30 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1.1
- buildreqs: added makeinfo

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Apr 29 2014 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 2.28.5-alt1
- 2.28.5

* Tue Aug 30 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Sat Mar 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3
- introspection support
- updated buildreqs

* Mon Mar 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt2
- rebuild for debuginfo

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Dec 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- fixed build with new gtk-doc

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.3-alt1
- 2.27.3

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3
- removed obsolete *ldconfig from post{,un}

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)
- build devel-doc as noarch

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- rebuild for Gnome-2.22

* Tue Mar 11 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)
- update BuildRequires (remove popt and gdbm)

* Thu Nov 22 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- new version (2.20.0)
- add Packager
- drop package utils

* Sat Jul 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.9-alt1
- new version (2.14.9)
- spec cleanup

* Wed Jan 17 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14.6-alt1
- new version (2.14.6)
- includes the fix for GNOME Bug 396477 (privilege escalation, Secunia advisory SA23736)
- updated dependencies, introduced a new devel-doc subpackage with gtk-doc book.

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.4-alt1
- new version (2.14.4)
- patch for --as-needed went upstream.
- removed no more necessary subst in examples' sources.

* Thu Aug 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- removed '2' from the package name

* Wed Mar 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)
- fixed linking with --as-needed.

* Sat Feb 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.3-alt1
- new version
- spec cleanup, buildreqs updated

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Tue Aug 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Removed excess buildreqs.

* Wed Jun 15 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Mon Feb 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92.

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90.

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1
- isdn patch removed (fixed in upstream).

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sat Jan 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt2
- do not package .la files.
- do not build devel-static subpackage by default.
- make buildable with recent autoconf (2.59).

* Mon Oct 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Mon Aug 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Sat May 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Jan 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- new version.

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.0-alt3
- rebuild to fix broken .la file.

* Fri Sep 27 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.0-alt2
- build without internal gnomesupport (this was a hack). Use our libpopt instead.
- additional package splitting (added utils(for daemon) and examples(optional))
- added source url

* Sat Jun 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
- First build for Sisyphus
- Applied patches from libgtop package
- daemon_build.patch
