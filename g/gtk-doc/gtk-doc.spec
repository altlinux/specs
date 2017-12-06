%def_disable snapshot
%def_with mkpdf
# our dblatex can't be --quiet
%def_disable check

Name: gtk-doc
Version: 1.27
Release: alt1

Summary: API documentation generation tool for GTK+ and GNOME
Group: Development/Other
License: %gpl2plus
Url: http://www.gtk.org/gtk-doc/

%define pkgdocdir %_docdir/%name-%version
%define python_ver 2.7

Requires: python >= %python_ver
Requires: sgml-common >= 0.6.3-alt11
Requires: docbook-dtds >= 4.3-alt1
Requires: docbook-style-xsl
Requires: libxml2 >= 2.3.6
Requires: xsltproc
%{?_with_mkpdf:Requires: highlight}
# for SGML
Requires: openjade >= 1.3.1
Requires: docbook-style-dsssl

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%version/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

Provides: python%__python_version(gtkdoc)

%add_python_lib_path %_datadir/%name/python/gtkdoc

BuildRequires: rpm-build-python python-devel >= %python_ver
BuildRequires: python-module-six
BuildRequires: docbook-dtds xml-common xml-utils
BuildRequires: common-licenses rpm-build-licenses
BuildRequires: docbook-dtds >= 1.0-alt7
BuildRequires: docbook-style-xsl bc
%{?_with_mkpdf:BuildRequires: rpm-build-gnome yelp-tools highlight}
# for SGML
BuildRequires: docbook-style-dsssl
BuildRequires: openjade >= 1.3.1
# for check
BuildRequires: glib2-devel
# since 1.25
%{?_with_mkpdf:BuildRequires: dblatex}

%description
%name is a tool for generating API reference documentation.
it is used for generating the documentation for GTK+, GLib
and GNOME.

%package mkpdf
Summary: PDF converter for %name
Group: Development/Other
Requires: %name = %version-%release

%description mkpdf
%name is a tool for generating API reference documentation.
it is used for generating the documentation for GTK+, GLib
and GNOME.

This package provides utility for saving documentation in PDF format

%package manual
Summary: Manual for gtk-doc
Group: Development/Other
License: %fdl

%description manual
Manual for gtk-doc, a tool for generating API reference documentation
used by GTK+, GLib and GNOME.

%prep
%setup
# make cmake files arch-independent
subst 's/libdir/datadir/' cmake/Makefile.am

# Move this doc file to avoid name collisions
mv doc/README doc/README.docs
rm -f examples/*~

%build
%autoreconf
%undefine _configure_target
export ac_cv_path_JADE=%_bindir/openjade
export ac_cv_path_XSLTPROC=%_bindir/xsltproc
%{?_with_mkpdf:export ac_cv_path_DBLATEX=%_bindir/dblatex}
%configure \
    --with-xml-catalog=%_sysconfdir/xml/catalog \
    --docdir=%pkgdocdir \
    %{?_with_mkpdf:--with-highlight=highlight}
%make_build

%install
%make_install DESTDIR=%buildroot pkgconfigdir=%_datadir/pkgconfig install
install -d -m755 %buildroot%_datadir/gtk-doc/html
mkdir -p %buildroot%_sysconfdir/buildreqs/files/ignore.d/
cat <<EOF >%buildroot%_sysconfdir/buildreqs/files/ignore.d/%name
^%_datadir/(gtk-doc|gnome|bonobo)/html/.
EOF

%find_lang --with-gnome gtk-doc-manual

install -d -m755 %buildroot%pkgdocdir
install -p -m644 AUTHORS ChangeLog MAINTAINERS NEWS README TODO doc/* \
    %buildroot%pkgdocdir/
bzip2 -9 %buildroot%pkgdocdir/ChangeLog
ln -s %_licensedir/GPL-2 %buildroot%pkgdocdir/COPYING
ln -s %_licensedir/FDL-1.1 %buildroot%pkgdocdir/COPYING-DOCS
cp -a examples %buildroot%pkgdocdir/

%check
%make check

%files
%_bindir/*
%{?_with_mkpdf:%exclude %_bindir/gtkdoc-mkpdf}
%_datadir/%name/
%_datadir/pkgconfig/%name.pc
%_datadir/aclocal/%name.m4
%dir %_datadir/cmake/GtkDoc
%_datadir/cmake/GtkDoc/*.cmake
%_sysconfdir/buildreqs/files/ignore.d/*
%dir %pkgdocdir
%pkgdocdir/AUTHORS
%pkgdocdir/COPYING
%pkgdocdir/ChangeLog.bz2
%pkgdocdir/MAINTAINERS
%pkgdocdir/NEWS
%pkgdocdir/README*
%pkgdocdir/TODO
%pkgdocdir/*.txt
%pkgdocdir/examples
#%pkgdocdir/gtkdoc.dot

%if_with mkpdf
%files mkpdf
%_bindir/gtkdoc-mkpdf
%endif

%files manual -f gtk-doc-manual.lang
%dir %pkgdocdir
%pkgdocdir/COPYING-DOCS

%changelog
* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.27-alt1
- 1.27

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 1.26.1-alt0.2
- updated to GTK_DOC_1_26-23-g8ad03e1 (fixed BGO ##787862, 787768)

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1.26.1-alt0.1
- updated to GTK_DOC_1_26-14-g95a9312

* Tue Aug 15 2017 Yuri N. Sedunov <aris@altlinux.org> 1.26-alt1
- 1.26

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.25-alt1
- 1.25

* Sat May 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.24-alt1
- 1.24

* Sun May 17 2015 Yuri N. Sedunov <aris@altlinux.org> 1.23-alt1
- 1.23

* Thu May 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22-alt1
- 1.22

* Fri Jul 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.21-alt1
- 1.21

* Sun Feb 16 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20-alt1
- 1.20

* Wed Jun 05 2013 Yuri N. Sedunov <aris@altlinux.org> 1.19-alt1
- 1.19

* Sat Mar 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt0.1
- 1.18.1 snapshot (8972559)

* Thu Dec 08 2011 Yuri N. Sedunov <aris@altlinux.org> 1.18-alt2
- fixed gtk-doc.m4 for glib independent packages

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.18-alt1.1
- Rebuild with Python-2.7

* Wed Sep 14 2011 Yuri N. Sedunov <aris@altlinux.org> 1.18-alt1
- 1.18

* Sat Feb 26 2011 Yuri N. Sedunov <aris@altlinux.org> 1.17-alt1
- 1.17

* Sat Jan 15 2011 Yuri N. Sedunov <aris@altlinux.org> 1.16-alt1
- 0.16

* Sat May 22 2010 Yuri N. Sedunov <aris@altlinux.org> 1.15-alt1
- 0.15

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 1.14-alt1
- 0.14
- removed upstreamed patches
- %%check section

* Wed Jan 20 2010 Yuri N. Sedunov <aris@altlinux.org> 1.13-alt2
- fixed GNOME bug #605211 (closes #22794)

* Sat Dec 19 2009 Yuri N. Sedunov <aris@altlinux.org> 1.13-alt1
- 1.13
- new -pdf subpackage

* Fri Dec 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.12-alt1
- 1.12

* Mon Nov 17 2008 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt1
- 1.11
- fixed %%url, packager tag
- don't run {update,clean}_scrollkeeper in %%post{,un} scripts
- updated buildreqs

* Sun Jul 20 2008 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- new version

* Tue Jan 22 2008 Alexey Rusakov <ktirf@altlinux.org> 1.9-alt2
- Fixed installation dependency on scrollkeeper (gtk-doc does not need SK
  at all).
- Use rpm-build-licenses and rpm-build-gnome.

* Thu Jan 03 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.9-alt1
- Release 1.9

* Mon Apr 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 1.8-alt1
- Release 1.8
- Update url

* Sun Nov 12 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.7-alt1
- Release 1.7

* Sun Apr 09 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.6-alt1
- Release 1.6
- Dropped dependencies on openjade and DSSSL

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.5-alt1
- Release 1.5
- Introduced gtk-doc-manual package for the new manual
- Buildreq
- Added xsltproc to dependencies

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.4-alt2.1
- Rebuilt for new pkg-config dependencies.

* Sat Sep 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4-alt2
- Put the .pc file into architecture-independent /usr/share/pkgconfig

* Thu Jul 21 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4-alt1
- New upstream release
- Hack against broken perl autoreq

* Mon Jan 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3-alt1
- New upstream release
- Create the ignore file in place

* Sun Mar 28 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2-alt1
- New upstream release
- Specify the local XML catalog for configure
- Add SGML catalog to the filelist

* Sat Oct 04 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1-alt2
- Added docbook-style-xsl to BuildRequires
- Added versioned perl dependency

* Wed Apr 30 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1-alt1
- New version
- Requires docbook-dtds >= 1.0-alt7 which fixed a stupid catalog bug

* Sun Apr 06 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt1
- New version

* Sat Nov 30 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.10-alt1
- 0.10

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.9-alt5
- rebuild

* Wed May 15 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.9-alt4
- Added /usr/share/bonobo/html/ to buildreq ignores as well

* Tue May 14 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.9-alt3
- Added /usr/share/gnome/html/ to buildreq ignores, as half of uses
  specify this directory for destination/search

* Wed May 08 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.9-alt2
- Added buildreqs ignore stuff
- Added /usr/share/gtk-doc/html/ to the file list
- Require docbook-dtds

* Fri Mar 15 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.9-alt1
- 0.9
- License is GPL
- Removed buildrequires, dependencies on docbook-utils

* Thu May 31 2001 AEN <aen@logic.ru> 0.5.9-alt1
- build for Sisyphus

* Fri Mar 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.4b1-1mdk
- added by eric.m.c.declerck@free.fr

* Wed Feb 28 2001 eric.m.c.declerck@free.fr
- compiled for Mandrake

* Tue Jan 16 2001 Tim Waugh <twaugh@redhat.com>
- Replace docbook, sgml-common, and stylesheets requirements with
  docbook-utils requirement.
- Use public identifier in custom stylesheets.

* Thu Dec 14 2000 Bill Nottingham <notting@redhat.com>
- rebuild because of broken fileutils

* Mon Nov 13 2000 Owen Taylor <otaylor@redhat.com>
- Version 0.4b1 (CVS snapshot)

* Fri Apr 23 1999 Owen Taylor <otaylor@redhat.com>
- added Requires

* Fri Apr 23 1999 Owen Taylor <otaylor@redhat.com>
- Initial RPM, version 0.2
