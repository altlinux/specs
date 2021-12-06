%def_enable snapshot

%define _name gmdb
%define beta %nil

Name: %{_name}2
Version: 0.9.1
Release: alt1

Summary: M$ Access MDB File Viewer
Group: Databases
License: GPL-2.0
Url: https://github.com/mdbtools/gmdb2

%if_disabled snapshot
Source: %url/archive/v%version%beta/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

%define mdbtools_ver %version
%define gtk_ver 3.22

Obsoletes: %_name < %version
Provides: %_name = %EVR

Requires: libmdbtools >= %mdbtools_ver

BuildRequires: libmdbtools-devel >= %mdbtools_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires:  yelp-tools

%description
MDB Tools is a set of libraries and programs to help you use Microsoft
Access file in various settings.

gmdb 2 - The MDB File Viewer and debugger.

%prep
%setup -n %name-%version%beta
# GTimeVal is deprecated sinc 2.62
sed -i 's| \-Werror||' configure.ac

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pD -m644 src/%_name.desktop %buildroot/%_desktopdir/%_name.desktop
%find_lang --with-gnome --output=%_name.lang %_name %name

%files -f %_name.lang
%_bindir/%name
%_desktopdir/%_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/mdbtools.%name.gschema.xml
%_man1dir/%name.1.*
%doc AUTHORS README* TODO

%changelog
* Sat Nov 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- updated to v0.9.1-3-g60335e0 (ported to GTK 3)

* Fri Dec 18 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt0.1
- 0.9.0-beta1 (gmdb-only)

* Sat Jul 04 2020 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- updated to 0.8.2-4-ga6c3fa2 from new %%url

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt2
- updated to 0.7.1-82-gd6f5745
- enabled gmdb build
- updated buildreqs

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Jun 07 2013 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- go to new upstream: https://github.com/brianb/mdbtools
- build against libodbcinst.so.2

* Mon Apr 09 2012 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt8cvs20051217
- don't build gmdb

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt7cvs20051217
- rebuild for soname set-versions

* Mon Dec 29 2008 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt6cvs20051217
- updated buildreqs
- removed obsolete %%post{,un}_ldconfig

* Sat Apr 15 2006 Igor Zubkov <icesik@altlinux.ru> 0.6-alt5cvs20051217
- fix changelog
- buildreq

* Fri Apr 07 2006 Igor Zubkov <icesik@altlinux.ru> 0.6-alt4cvs20051217
- update from cvs
- add fix for export to sql

* Wed Apr 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt4cvs20050908
- fix build with ld --as-needed

* Mon Oct 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt3cvs20050908
- fix release (2.1cvs < 2cvs)

* Mon Sep 19 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2.1cvs20050908
- fix bug #8007 (config.h in system wide headers)
- Note: you have to define HAVE_ICONV _before_include mdbtools.h

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2cvs20050908
- come back to Sisyphus :) CVS version

* Fri Aug 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt1pre1
- 0.6pre1

* Mon Dec 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt3
- do not package .la files.
- do not build devel-static subpackage by default. 

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt2
- fixed buildreqs.

* Sun Jan 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt1
- new version.

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- First build for Sisyphus.

