Name: pkg-config
Version: 0.25
Release: alt2

Summary: Pkgconfig helps make building packages easier
License: GPLv2+
Group: Development/Other
Url: http://pkg-config.freedesktop.org/wiki/
Packager: Dmitry V. Levin <ldv@altlinux.org>

Provides: %_libdir/pkgconfig
Provides: %_datadir/pkgconfig

Provides: pkgconfig-reqprov, pkgconfig-recursion
Provides: pkgconfig-print-requires-private, pkgconfig = 1:%version-%release
Obsoletes: pkgconfig

# due to pkg.c:add_virtual_pkgconfig_package
Provides: pkgconfig(pkg-config) = %version

# http://git.altlinux.org/gears/p/pkg-config.git
Source: %name-%version-%release.tar

BuildRequires: glib2-devel libpopt-devel

%define docdir %_docdir/%name-%version

%description
The pkg-config program is used to retrieve information about installed
libraries in the system.  It is typically used to compile and link
against one or more libraries.

%prep
%setup -n %name-%version-%release
sed -i 's/^\([A-Z]*_SUBDIR *=\).*/\1/' Makefile.am

%build
%autoreconf
%configure --docdir=%docdir --with-installed-glib --with-installed-popt
%make_build

%install
%makeinstall_std
install -dm755 %buildroot{%_datadir,%_libdir}/pkgconfig
install -pm644 AUTHORS NEWS README %buildroot%docdir/

mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d
cat <<\EOF >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name
# %name buildreq filter.
^(%_libdir|%_datadir)/pkgconfig/[^/]+\.pc$
EOF

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-files.req.list
# %name dirlist for %_rpmlibdir/files.req
/usr/lib/pkgconfig	%name
/usr/lib64/pkgconfig	%name
/usr/share/pkgconfig	%name
EOF

%check
%make_build -k check

%files
%config %_sysconfdir/buildreqs/files/ignore.d/*
%config %_rpmlibdir/*
%_bindir/pkg-config
%dir %_libdir/pkgconfig
%dir %_datadir/pkgconfig
%_datadir/aclocal/*
%_man1dir/*
%docdir/

%changelog
* Mon Feb 28 2011 Alexey Tourbin <at@altlinux.ru> 0.25-alt2
- Tolerate missing Requires.private in --cflags mode.

* Mon Nov 01 2010 Dmitry V. Levin <ldv@altlinux.org> 0.25-alt1
- Updated to 0.25-6-g03bd4a5.
- Reverted all ALT-specific changes made to recursion algorithm.
  More and more freedesktop packages now use Requires.private tag
  to specify requirements for --cflags, so we have to revert to
  upstream recursion algorithm.  It will definitely bring us back
  a lot of unneeded requirements among those few really needed
  for compilation, but there seems to be no other way.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 0.23-alt4
- Moved "make check" to %%check section.

* Tue Dec 09 2008 Alexey Tourbin <at@altlinux.ru> 0.23-alt3
- added "Provides: pkgconfig(pkg-config) = %%version"

* Tue Jun 24 2008 Alexey Tourbin <at@altlinux.ru> 0.23-alt2
- added %_rpmlibdir/%name-files.req.list, to make dependencies
  on /usr/{lib,lib64,share}/pkgconfig directories

* Thu Apr 24 2008 Dmitry V. Levin <ldv@altlinux.org> 0.23-alt1
- Updated to 0.23.

* Fri Oct 05 2007 Dmitry V. Levin <ldv@altlinux.org> 0.22-alt2
- Added --enable-recursion and --disable-recursion hidden options.
- Added Provides: pkgconfig-recursion.
- Enabled recursion by default again because disabled recursion
  breaks build of many screwed packages.

* Tue Oct 02 2007 Dmitry V. Levin <ldv@altlinux.org> 0.22-alt1
- Updated to 0.22.
- Removed dead code.
- Disabled recursion while querying for libraries unless in --static mode.
  This change resurrects the behaviour which was introduced
  in 0.15.0-alt3 and lost in 0.18.

* Sun Nov 12 2006 Dmitry V. Levin <ldv@altlinux.org> 0.21-alt1
- Updated to 0.21.
- Do not package ChangeLog file, NEWS should be enough.
- Do not package COPYING symlink, License tag should be enough.

* Fri Feb 03 2006 Dmitry V. Levin <ldv@altlinux.org> 0.20-alt3.2
- Added buildreq ignore rule (#9015).

* Thu Feb 02 2006 Dmitry V. Levin <ldv@altlinux.org> 0.20-alt3.1
- Provides: pkgconfig-reqprov.

* Fri Jan 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.20-alt3
- Patch3: from Fedora CVS, add options for autoreqprov scripts

* Sun Jan 22 2006 Dmitry V. Levin <ldv@altlinux.org> 0.20-alt2.1
- Updated package provides.

* Mon Nov 21 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.20-alt2
- Patch2: always ignore Requires.private line
  unless --static option has been given

* Mon Nov 21 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.20-alt1
- 0.20
- Updated Patch0 and merged in Patch2 to it

* Sat Sep 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.19-alt1
- 0.19
- Do not remove /usr/share/pkg-config from the search path [bug #7911]
- Updated Patch1 & Patch2
- Added NEWS and COPYING do doc list

* Sun Apr 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.17.2-alt1
- 0.17.2

* Tue Apr 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.17.1-alt1
- 0.17.1
- recursion disabled in upstream.

* Mon Apr 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.16.0-alt1
- 0.16.0
- updated patches.
- use only %%_libdir/pkgconfig as a default search path for .pc files.

* Thu Jan 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.15.0-alt4
- fixed build with latest automake-1.9.4.

* Fri Mar 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.15.0-alt3.2
- fix pkg.m4 for new automake.

* Thu Feb 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.15.0-alt3.1
- provides /usr/lib/pkgconfig.

* Sat Jan 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.15.0-alt3
- disable recursion while output linker flags. New --recursive option
  restores former behavior.

* Wed Dec 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.15.0-alt2
- build with system glib and popt.

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.14.0-alt1
- 0.14.0, glib2-2.1.3 requires new version.
- removed empty NEWS from %%doc.
- small improvements in description.

* Mon Sep 23 2002 AEN <aen@altlinux.ru> 0.13.0-alt1
- new version

* Wed Mar 27 2002 AEN <aen@logic.ru> 0.12.0-alt1
- new version

* Tue Feb 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Thu Jul 26 2001 Stanislav Ievlev <inger@altlinux.ru> 0.8.0-alt1
- 0.8.0. Cleanup spec.

* Fri Jun 15 2001 AEN <aen@logic.ru> 0.7.0-alt2
- BuildReq added

* Fri Jun 15 2001 AEN <aen@logic.ru> 0.7.0-alt1
- new version

* Thu Apr 19 2001 Stanislav Ievlev <inger@altlinux.ru> 0.5.0-alt1
- Initial release for ALTLinux. Descriptions to spec from Mandrake package
