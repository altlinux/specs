%ifndef _gtkdocdir
%define _gtkdocdir %_datadir/gtk-doc/html
%endif

%define sover 3
Name: rasqal
Version: 0.9.32
Release: alt2

Group: System/Libraries
Summary: Rasqal RDF Query Library
License: LGPL v2.1+ or GPL v2+ or Apache v2.0+
Url: http://librdf.org/rasqal/

Source: http://download.librdf.org/source/%name-%version.tar
Patch1: rasqal-0.9.29-alt-automake.patch

# Automatically added by buildreq on Thu Sep 01 2011 (-bi)
# optimized out: elfutils libgmp-devel libxml2-devel pkg-config
#BuildRequires: flex glibc-devel-static gtk-doc libmpfr-devel libpcre-devel raptor2-devel
BuildRequires: flex glibc-devel gtk-doc libmpfr-devel libpcre-devel raptor2-devel
BuildRequires: libuuid-devel

%description
RDF Query Language.

%package -n lib%name%sover
Summary: %name core library
Group: System/Libraries
Provides: librasqal = %EVR
Obsoletes: librasqal < %EVR
%description -n lib%name%sover
%name core library.

%package -n lib%name-devel
Summary: Header files for the Rasqal RDF query library
Group: Development/C
Provides: rasqal-devel = %EVR
Obsoletes: rasqal-devel < %EVR
%description  -n lib%name-devel
Header files for the Rasqal RDF query library.

%package  -n lib%name-devel-static
Summary: Static Rasqal library
Group: Development/C
Requires: lib%name-devel = %version-%release
%description  -n lib%name-devel-static
Static Rasqal library.

%prep
%setup -q
%patch1 -p1
%autoreconf

%build
cp -f %_datadir/automake/config.* .
%configure \
	--disable-static \
	--enable-datatypes \
	--enable-release \
	--with-html-dir=%_gtkdocdir \
	--with-raptor=system \
	--with-triples-source=raptor
# don't use redland as triples-source, as it would cause linking loop

%make_build

%install
%makeinstall_std

%files
%_bindir/roqet
%_man1dir/roqet.1*

%files -n lib%name%sover
%doc AUTHORS ChangeLog LICENSE.txt NEWS README
%_libdir/librasqal.so.%sover
%_libdir/librasqal.so.%sover.*

%files -n lib%name-devel
%_bindir/rasqal-config
%_libdir/librasqal.so
#%_libdir/librasqal.la
%_includedir/rasqal/
%_pkgconfigdir/rasqal.pc
%_man1dir/rasqal-config.1*
%_man3dir/librasqal.3*
%_gtkdocdir/rasqal/

#%files devel-static
#%_libdir/librasqal.a

%changelog
* Thu Mar 27 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.32-alt2
- clean build requires

* Wed Mar 26 2014 Sergey V Turchin <zerg@altlinux.org> 0.9.32-alt1
- new version

* Tue Apr 02 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.30-alt1
- new version

* Tue Mar 05 2013 Sergey V Turchin <zerg@altlinux.org> 0.9.29-alt2
- obsolete librasqal package

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.29-alt1.1
- Rebuilt with mpfr 3.1.1

* Fri May 25 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.29-alt0.M60P.1
- build for M60P

* Thu May 24 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.29-alt1
- new version

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.28-alt0.M60P.1
- built for M60P

* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.28-alt1
- new version

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.27-alt0.M60P.1
- built for M60P

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.27-alt1
- new version

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.20-alt1
- new version 0.9.20 (with rpmrb script)

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.16-alt1
- new version 0.9.16 (with rpmrb script)
- cleanup spec

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.15-alt1
- new version 0.9.15
- update buildreq (add mpfr buildreq)
- disable static build

* Sun Oct 21 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.14-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

