# TODO: x86_64
%define oname pxlib
Name: libpx
Version: 0.6.4
Release: alt1.qa1

Summary: A library to read Paradox DB files

License: GPL v2
Group: System/Libraries
Url: http://pxlib.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%oname/%oname-%version.tar.bz2
Source1: %name.watch

# Automatically added by buildreq on Sat Jul 18 2009
BuildRequires: docbook-utils intltool libgsf-devel w3c-markup-validator-libs

%description
pxlib is a simply and still small C library to read Paradox DB files.
It supports all versions starting from 3.0. It currently has a very
limited set of functions like to open a DB file, read its header and
read every single record.

%package devel
Summary: Header files for pxlib
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for pxlib.

%prep
%setup -q -n %oname-%version
%__subst "s|/usr/lib|%_libdir|g" configure.in

%build
touch config.rpath
%autoreconf
# man pages are build by docbook2man
%__subst 's#mv PXLIB.3 pxlib.3##g' doc/Makefile*
%__subst 's#docbook-to-man#docbook2man#g' configure*
%__subst 's#docbook-to-man $<.*#docbook2man $<#g' doc/Makefile*
for man in doc/*.sgml; do
	name=$(basename "$man" .sgml)
	sed -i -e "s#$name#$name#gi" $man
done

# FIXME:
CPPFLAGS="$(pkg-config glib-2.0 --cflags)"
%configure \
	--with-gsf --with-sqlite \
	--disable-static
%make_build

%install
%makeinstall_std

%find_lang %oname

%files -f %oname.lang
%doc AUTHORS ChangeLog doc/*.txt
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/*.h
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat Jul 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- new version 0.6.4 (with rpmrb script)
- fix build on x86_64

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt2
- add autoreconf, update buildreqs
- drop post/postun spections

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)
- cleanup spec, enable SMP-build, fix packager

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.1
- new version 0.6.1 (with rpmrb script)

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

