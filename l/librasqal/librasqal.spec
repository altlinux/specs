%define oname rasqal
Name: lib%oname
Version: 0.9.20
Release: alt1.1

Summary: Rasqal RDF Query Library

License: LGPL v2.1+ or GPL v2+ or Apache v2.0+
Group: System/Libraries
Url: http://librdf.org/rasqal/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.librdf.org/source/%oname-%version.tar

# Automatically added by buildreq on Mon Jan 07 2008
BuildRequires: flex gcc-c++ gtk-doc libmpfr-devel libpcre-devel libraptor-devel libxml2-devel

BuildRequires: rpm-build-intro

%description
RDF Query Language.

%package devel
Summary: Header files for the Rasqal RDF query library
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for the Rasqal RDF query library.

%package static
Summary: Static Rasqal library
Group: Development/C
Requires: %name-devel = %version-%release

%description static
Static Rasqal library.

%prep
%setup -q -n %oname-%version

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

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog LICENSE.txt NEWS README
%_bindir/roqet
%_libdir/librasqal.so.*
%_man1dir/roqet.1*

%files devel
%_bindir/rasqal-config
%_libdir/librasqal.so
#%_libdir/librasqal.la
%_includedir/rasqal/
%_pkgconfigdir/rasqal.pc
%_man1dir/rasqal-config.1*
%_man3dir/librasqal.3*
%_gtkdocdir/rasqal/

#%files static
#%_libdir/librasqal.a

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.20-alt1.1
- Removed bad RPATH

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

