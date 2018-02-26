%define oname rarian
%define major 0.8
# The version of Scrollkeeper that Rarian obsoletes
%define skversion 0.3.14

%def_disable static

Name: librarian
Version: %major.1
Release: alt5

Summary: A documentation meta-data library

License: %gpllgpl2plus 
Group: System/Libraries
Url: http://rarian.freedesktop.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%oname/%major/%oname-%version.tar.bz2
Source1: scrollkeeper-omf.dtd
Source2: scrollkeeper-cl.dtd
Source3: scrollkeeper.filetrigger

Provides: %oname-compat = %version-%release
Obsoletes: %oname-compat < %version-%release

Provides: scrollkeeper = %skversion.rarian.%version-%release
Provides: libscrollkeeper = %skversion.rarian.%version-%release
Obsoletes: scrollkeeper < %skversion.rarian
Obsoletes: libscrollkeeper < %skversion.rarian

PreReq: xml-common, xml-utils, docbook-dtds

BuildPreReq: rpm-build-compat rpm-build-licenses
BuildPreReq: rpm-build-gnome >= 0.8
BuildPreReq: xsltproc gcc-c++

%description
Rarian is a documentation meta-data library that allows access to
documents, man pages and info pages. It was designed as a replacement
for scrollkeeper.

%package devel
Summary: Development files for libRarian
Group: Development/C
Requires: %name = %version-%release
Obsoletes: libscrollkeeper-devel < %skversion.rarian

%description devel
This package contains files required to develop applications that use
the Rarian library ("librarian").

%if_enabled static
%package static
Summary: Static Rarian library
Group: Development/C
Requires: %name-devel = %version-%release

%description static
Static Rarian library (librarian).
%endif

%prep
%setup -q -n %oname-%version

%build
# all mainstreams sets localstatedir in var, but ALT sets it in /var/lib :(
%autoreconf
%configure \
	--enable-omf-read \
	--disable-skdb-update \
	--localstatedir=%_var

%make_build

%install
install -d %buildroot%_omfdir
install -d %buildroot%_localstatedir/%oname/

%make_install install DESTDIR=%buildroot

# dtds
install -pD -m 644 %SOURCE1 %buildroot%_datadir/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd
install -pD -m 644 %SOURCE2 %buildroot%_datadir/xml/scrollkeeper/dtds/scrollkeeper-cl.dtd

# posttrans filetrigger
install -pD -m 755 %SOURCE3 %buildroot%_rpmlibdir/scrollkeeper.filetrigger

%post
%_bindir/rarian-sk-update
%_bindir/xmlcatalog --noout --add "public" \
        "-//OMF//DTD Scrollkeeper OMF Variant V1.0//EN" \
        "%_datadir/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" %_sysconfdir/xml/catalog
%_bindir/xmlcatalog --noout --add "public" \
        "-//Scrollkeeper//DTD Contents List V1.0//EN" \
        "%_datadir/xml/scrollkeeper/dtds/scrollkeeper-cl.dtd" %_sysconfdir/xml/catalog
%_bindir/rarian-sk-rebuild -q

%preun
[ $1 = 0 ] || exit 0
%_bindir/xmlcatalog --noout --del \
	"%_datadir/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" %_sysconfdir/xml/catalog ||:
%_bindir/xmlcatalog --noout --del \
	"%_datadir/xml/scrollkeeper/dtds/scrollkeeper-cl.dtd" %_sysconfdir/xml/catalog ||:

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO MAINTAINERS
%_bindir/rarian-example
%_bindir/rarian-sk-*
%_bindir/scrollkeeper-*
%_libdir/librarian.so.*
%_datadir/librarian/
%_datadir/help/
%_datadir/xml/scrollkeeper/dtds/
%_rpmlibdir/scrollkeeper.filetrigger
%dir %_localstatedir/%oname/
%dir %_omfdir

%files devel
%_libdir/librarian.so
%_includedir/%oname/
%_pkgconfigdir/%oname.pc

%if_enabled static
%files static
%_libdir/librarian.a
%else
%exclude %_libdir/*.a
%endif

%changelog
* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt5
- used %%autoreconf to fix RPATH problem

* Sat Jan 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt4
- packaged lost .dtds

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt3
- rebuild for soname set-versions

* Mon Jun 01 2009 Alexey Rusakov <ktirf@altlinux.org> 0.8.1-alt2.1
- Removed unnecessary rpm-build-spec2macro dependency.

* Sat Nov 15 2008 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt2
- don't call ldconfig in %%post{,un}
- implemented posttrans filetrigger

* Fri Sep 05 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- New version (0.8.1).

* Tue Mar 11 2008 Alexey Rusakov <ktirf@altlinux.org> 0.8.0-alt1
- New version (0.8.0).

* Tue Feb 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.7.1-alt1
- New version (0.7.1).

* Sat Jan 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.7.0-alt6
- Pushed away definitions of RPM macros from librarian even further, to
  rpm-build-gnome package.

* Wed Dec 26 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.0-alt5
- Moved definitions of RPM macros from librarian-devel to librarian, because
  librarian (not -devel) provides scrollkeeper, and the macros are needed
  for back-compatibility with scrollkeeper.

* Sat Dec 22 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.0-alt4
- More specfile tweaks:
  + use rpm-build-licenses, rpm-build-gnome, rpm-build-spec2macro;
  + build librarian-devel-static conditionally (off by default);
  + made clauses that obsolete scrollkeeper more exactly in terms of
    versions.

* Wed Dec 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt3
- add provides/obsoletes rarian-compat

* Wed Dec 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt2
- move omf dir to librarian
- add rpm macros
- move scripts to librarian, obsolete rarian-compat
- add post/preun scripts

* Tue Dec 11 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
- scrollkeeper is replaced by rarian-compat

