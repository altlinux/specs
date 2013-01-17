%define lo_name libreoffice
%define ver_major 3.6
%define lo_ver %ver_major.5.2
%define src_url http://download.documentfoundation.org/libreoffice/src/%ver_major.5/
%define with_lang ru de fr uk pt-BR es

Name: %lo_name
Version: %lo_ver
Release: alt1
Summary: LibreOffice Productivity Suite
License: LGPL
Group: Office
URL: http://www.documentfoundation.org/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: java xdg-utils hunspell-en hyphen-en mythes-en
Requires: gst-plugins-base gst-plugins-good gst-plugins-ugly gst-plugins-bad gst-ffmpeg
Conflicts: openoffice.org < 3.3.0

Source10: libreoffice-src-3.6.3.1.tar
Source11: biblio.tar.bz2
Source12: extras-3.1.tar.bz2

Source0: %src_url/libreoffice-core-%version.tar.xz
Source1000: %src_url/libreoffice-binfilter-%version.tar.xz
Source1001: %src_url/libreoffice-dictionaries-%version.tar.xz
Source1002: %src_url/libreoffice-help-%version.tar.xz
Source1003: %src_url/libreoffice-translations-%version.tar.xz

Source1: soffice.sh
Source2: %name.config
Source3: lo-wrappers.tar
Source5: ooo-tango-icons.tar.bz2
Source6: lo-freedesktop-menu.tar
Source7: lo-res-tango.tar

Source500: extras_ru.tar.bz2
Source501: extras-templates.tar.bz2

Patch11: openoffice.org-2.4.0-alt15443-sc-crach.patch
Patch13: openoffice.org-2.3.0-alt-helpcontent2-default-css.patch
Patch14: openoffice.org-2.3.1.1-alt-helpcontent2-default-css.patch
Patch16: libreoffice-3.5.0.3-alt-sysuserconfigdir.patch
Patch17: openoffice.org-3.2.0-alt-disable-old-excel-word.patch
Patch19: libreoffice-3.5.1.2-alt-basic-cur.patch
Patch20: libreoffice-3.6.1.2-alt-xdg-config-home.patch
Patch21: libreoffice-3.5.0.3-alt-spelldict_select.patch
Patch25: libreoffice-3.5.3.1-alt-download.patch

AutoReqProv: yes, noshell, nopython

BuildRequires: /proc wget xdg-utils zip >= 3.0 gcc-c++ >= 4.6
BuildRequires: java-devel = 1.6.0 libdbus-glib-devel gst-plugins-devel postgresql-devel libncursesw-devel GConf
BuildRequires: ant ant-jakarta-regexp boost-devel flex gperf fontconfig-devel libfreetype-devel libcups-devel
BuildRequires: libGConf-devel libicu-devel libcurl-devel libexpat-devel libgtk+2-devel libjpeg-devel libneon-devel
BuildRequires: libpam0-devel libpng-devel libsane-devel libreadline-devel libwpd9-devel libxslt-devel libxml2-devel
BuildRequires: perl-Archive-Zip perl-libnet python-dev tcsh unzip libbonobo-devel zlib-devel xsltproc xulrunner-devel
BuildRequires: libldap-devel libdb4-devel libdb4_cxx-devel libssl-devel libnss-devel libnspr-devel libminizip-devel
BuildRequires: libhunspell-devel libhyphen-devel libwpg2-devel libgio-devel libunixODBC-devel gvfs-devel libGLU-devel
BuildRequires: perl-Switch junit4 boost-program_options-devel cppunit-devel libwps-devel libXaw-devel libXau-devel
BuildRequires: libXrandr-devel libXext-devel zenity libmpc-devel librsvg-devel libpq-devel libclucene-core-devel
# libpoppler-devel libpoppler-cpp-devel

%description
LibreOffice is a productivity suite that is compatible with other major office suites

%package gnome
Summary: GNOME Extensions for LibreOffice
Group: Office
Requires: %name = %version-%release

%description gnome
This package contains some GNOME extensions for LibreOffice

%package langpack-ru
Summary: Language-specific files, Russian
Group: Office
Requires: %name = %version-%release hunspell-ru hyphen-ru mythes-ru

%description langpack-ru
LibreOffice language-specific files, Russian

%package langpack-de
Summary: Language-specific files, German
Group: Office
Requires: %name = %version-%release hunspell-de hyphen-de mythes-de

%description langpack-de
LibreOffice language-specific files, German

%package langpack-fr
Summary: Language-specific files, French
Group: Office
Requires: %name = %version-%release hunspell-fr hyphen-fr mythes-fr

%description langpack-fr
LibreOffice language-specific files, French

%package langpack-uk
Summary: Language-specific files, Ukrainian
Group: Office
Requires: %name = %version-%release hunspell-uk hyphen-uk mythes-uk

%description langpack-uk
LibreOffice language-specific files, Ukrainian

%package langpack-pt-BR
Summary: Language-specific files, Brazil Portuguese
Group: Office
Requires: %name = %version-%release hunspell-pt hyphen-pt mythes-pt

%description langpack-pt-BR
LibreOffice language-specific files, Brazil Portuguese

%package langpack-es
Summary: Language-specific files, Spanish
Group: Office
Requires: %name = %version-%release hunspell-es hyphen-es mythes-es

%description langpack-es
LibreOffice language-specific files, Spanish

%add_findreq_skiplist %_libdir/%lo_name/share/config/webcast/*
%add_findreq_skiplist %_libdir/%lo_name/program/*open-url
%set_verify_elf_method unresolved=relaxed

%prep
%setup -q -c -a1000 -a1001 -a1002 -a1003

rm -fr %name-translations-%version/git-hooks
rm -f %name-help-%version/ChangeLog
for d in *; do
    mv -f $d/* .
    rm -fr $d
done
chmod 0777 ../%name-%version

tar -xf %SOURCE10 -C %_builddir/%name-%version/
ln -s %_builddir/../SOURCES/%name-*-%version.tar.xz ext_sources/

%patch11 -p1
%patch13 -p0
%patch14 -p0
%patch16 -p1
%patch17 -p0
%patch19 -p0
%patch20 -p1 -b .alt-xdg
%patch21 -p1
%patch25 -p1

tar -xjf %SOURCE5 -C sysui/desktop/icons/
tar -xf %SOURCE7 -C icon-themes/tango/

tar -xjf %SOURCE500
tar -xjf %SOURCE501

%build
aclocal -I m4
autoconf
%configure \
	--with-vendor="ALT Linux Team" \
	--disable-gnome-vfs \
	--disable-odk \
	--disable-systray \
	--disable-binfilter \
	--enable-dbus \
	--enable-evolution2 \
	--enable-ext-pdfimport \
	--enable-ext-report-builder \
	--enable-ext-scripting-beanshell \
	--enable-ext-scripting-javascript \
	--enable-gio \
	--with-alloc=system \
	--with-openldap \
	--without-afms \
	--without-fonts \
	--without-myspell-dicts \
	--without-ppds \
	--with-system-boost \
	--with-system-cairo \
	--with-system-cppunit \
	--with-system-curl \
	--with-system-db \
	--with-system-dicts \
	--with-system-expat \
	--with-system-hunspell \
	--with-system-icu \
	--with-system-jpeg \
	--with-system-libwpd \
	--with-system-libwpg \
	--with-system-libwps \
	--with-system-libxml \
	--with-system-mozilla \
	--with-system-nss \
	--with-system-neon \
	--with-system-odbc \
	--with-system-openssl \
	--with-system-stdlibs \
	--with-system-zlib \
	--with-system-postgresql \
	--with-system-clucene \
	--enable-librsvg=system \
	--with-external-dict-dir=%_datadir/myspell \
	--with-external-hyph-dir=%_datadir/hyphen \
	--with-external-thes-dir=%_datadir/mythes \
	--with-lang="en-US %with_lang" \
	--with-external-tar=%_builddir/%name-%version/ext_sources \
	--with-num-cpus=1
#	--with-system-poppler

ln -sf /bin/true autogen.sh
%make

subst 's|^rm|rm -f|' config_host.mk.source
source config_host.mk.source
cp $SOLARVER/$INPATH/lib/libuno_sal.so.3 $SRC_ROOT/

%install
source config_host.mk.source
#figure out the icon version
export `sed -ne "s| ||g;s|^\(PRODUCTVERSIONSHORT=.*\)|\1|p" solenv/inc/productversion.mk`
export `sed -ne "s| ||g;s|^\(PRODUCTVERSION=.*\)|\1|p" solenv/inc/productversion.mk`

export PKGFORMAT=installed
unset DEFAULT_TO_ENGLISH_FOR_PACKING
cd instsetoo_native/util
dmake openoffice_en-US

mkdir -p %buildroot%_libdir/%name
mv $SRC_ROOT/instsetoo_native/$INPATH/LibreOffice/installed/install/en-US/* %buildroot%_libdir/%name/
subst "s|^UserInstallation=.*|UserInstallation=\\\$SYSUSERCONFIG/libreoffice|" %buildroot%_libdir/%lo_name/program/bootstraprc

find %buildroot%_libdir/%name -type d | sed "s|^%buildroot|%dir |" > $SRC_ROOT/%name.files
find %buildroot%_libdir/%name -type f | grep -v "cde\|kde\|gnome\|gtk\|gconf\|eggtray\|qstart\|javafilter\|startcenter\|xsltfilter.desktop\|binfilter.desktop" | sed "s|^%buildroot||" >> $SRC_ROOT/%name.files
find %buildroot%_libdir/%name -type l | sed "s|^%buildroot||" >> $SRC_ROOT/%name.files

# fixed uk_UA files
pushd $SOLARVER/$INPATH/pck
	for z in *_ru.zip; do
		[ -f ${z/_ru.zip/_uk.zip} ] || cp $z ${z/_ru.zip/_uk.zip}
	done
popd

dmake ooolanguagepack
for p in %with_lang; do
	mkdir -p %buildroot%_libdir/%name.$p
	mv $SRC_ROOT/instsetoo_native/$INPATH/LibreOffice_languagepack/installed/install/$p/* %buildroot%_libdir/%name.$p/
	find %buildroot%_libdir/%name.$p -type d | sed "s|^%buildroot|%dir |" > $SRC_ROOT/%name.$p.files
	find %buildroot%_libdir/%name.$p -type f | sed "s|^%buildroot||" >> $SRC_ROOT/%name.$p.files
	find %buildroot%_libdir/%name.$p -type l | sed "s|^%buildroot||" >> $SRC_ROOT/%name.$p.files
	subst "s|/%name.$p|/%name|" $SRC_ROOT/%name.$p.files
	cp -a %buildroot%_libdir/%name.$p/* %buildroot%_libdir/%name/
	rm -fr %buildroot%_libdir/%name.$p
done
subst '/readmes/d' $SRC_ROOT/%name.*files

install -m755 %SOURCE1 %buildroot%_libdir/%lo_name/program/soffice
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

tar -xf %SOURCE3 -C %buildroot/
mkdir -p %buildroot%_iconsdir
tar -xf %SOURCE6 -C %buildroot%_datadir/
rm -f %buildroot%_desktopdir/qstart.desktop

tar -xjf %SOURCE5 -C %buildroot%_iconsdir/
find %buildroot%_iconsdir/hicolor/*/apps -type f | while read -r f; do
	mv $f ${f//apps\//apps\/libreoffice-}
done
find %buildroot%_iconsdir -type f -exec chmod 644 {} \;

subst "s|@LODIR@|%_libdir/%name|" \
	%buildroot%_libdir/%lo_name/program/soffice  \
	%buildroot%_bindir/lo* \
	%buildroot%_desktopdir/*.desktop
rm -f %buildroot%_libdir/%lo_name/share/xdg/*.desktop
install -m644 %buildroot%_desktopdir/*.desktop %buildroot%_libdir/%lo_name/share/xdg/

mkdir -p %buildroot%_datadir/mime-info
install -m644 $SRC_ROOT/sysui/$INPATH/misc/%name/openoffice.keys %buildroot%_datadir/mime-info/libreoffice.keys
subst 's|^\(.*icon_filename=\)libreoffice-\(.*\)|\1\2|' %buildroot%_datadir/mime-info/*.keys

# XDG open
ln -sf /usr/bin/xdg-open %buildroot%_libdir/%lo_name/program/open-url

# install don't stripped libs
install -m644 $SRC_ROOT/libuno_sal.so.3 %buildroot%_libdir/%name/ure/lib/

unset RPM_PYTHON

%files -f %name.files
%config(noreplace) %_sysconfdir/sysconfig/%name
%_libdir/%lo_name/ure/lib/libsal_textenc.so.3
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/mime-info/*.keys

%files gnome
%_libdir/%lo_name/program/gnome*
%_libdir/%lo_name/program/gconfbe1.uno.so
%_libdir/%lo_name/program/libvclplug_gtkl*.so
%_libdir/%lo_name/share/registry/gnome.xcd
#%_libdir/%lo_name/program/libqstart_gtkl*.so
#%_libdir/%lo_name/program/libeggtrayl*.so
#%_libdir/%lo_name/share/xdg/qstart.desktop

%files langpack-ru -f %name.ru.files

%files langpack-de -f %name.de.files

%files langpack-fr -f %name.fr.files

%files langpack-uk -f %name.uk.files

%files langpack-pt-BR -f %name.pt-BR.files

%files langpack-es -f %name.es.files

%changelog
* Thu Jan 17 2013 Valery Inozemtsev <shrek@altlinux.ru> 3.6.5.2-alt1
- 3.6.5 release 2

* Wed Jan 16 2013 Valery Inozemtsev <shrek@altlinux.ru> 3.6.5.1-alt1
- 3.6.5 release 1

* Thu Nov 29 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.6.4.3-alt1
- 3.6.4 release 3

* Wed Nov 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.6.4.2-alt1
- 3.6.4 RC2

* Fri Nov 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.6.4.1-alt1
- 3.6.4 RC1

* Wed Oct 24 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.6.3.2-alt1
- 3.6.3 RC2

* Thu Oct 11 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.6.3.1-alt1
- 3.6.3 RC1

* Tue Oct 09 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.7.2-alt1
- 3.5.7 RC2

* Fri Sep 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.7.1-alt1
- 3.5.7 RC1

* Wed Aug 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.6.2-alt1
- 3.5.6 RC2

* Wed Jul 04 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.5.3-alt1
- 3.5.5 RC3

* Wed Jun 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.5.2-alt1
- 3.5.5 RC2

* Wed Jun 13 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.5.1-alt1
- 3.5.5 RC1
 
* Wed May 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.4.2-alt1
- 3.5.4 RC2

* Wed May 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.4.1-alt1
- 3.5.4 RC1

* Wed Apr 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.3.2-alt1
- 3.5.3 RC2

* Sat Apr 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.3.1-alt1
- 3.5.3 RC1

* Wed Mar 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.2.2-alt1
- 3.5.2 RC2

* Mon Mar 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.1.2-alt1
- 3.5.1 RC2

* Wed Feb 15 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.5.0.3-alt1
- 3.5.0 RC3

* Tue Jan 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 3.4.5.2-alt1
- 3.4.5 RC2

* Thu Dec 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.5.1-alt1
- 3.4.5 RC1

* Tue Nov 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.4.2-alt1
- 3.4.4 RC2

* Wed Oct 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.4.1-alt1
- 3.4.4 RC1

* Wed Aug 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.3.2-alt1
- 3.4.3 RC2

* Wed Aug 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.3.1-alt1
- 3.4.3 RC1

* Tue Jul 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.2.3-alt1
- 3.4.2 RC3

* Tue Jul 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.2.2-alt1
- 3.4.2 RC2
- soffice: replaced soffice.bin to oosplash.bin (closes: #25848)

* Tue Jul 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.2.1-alt1
- 3.4.2 RC1

* Sat Jun 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.1.3-alt1
- 3.4.1 RC3

* Wed Jun 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.1.2-alt1
- 3.4.1 RC2

* Sun Jun 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.1.1-alt0.M60T.1
- build for T6 branch

* Wed Jun 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.1.1-alt1
- 3.4.1 RC1

* Tue Jun 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.4.0.2-alt1
- 3.4.0 RC2

* Wed Jun 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.3.1-alt1
- 3.3.3 RC1

* Fri May 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.2.2-alt3
- rebuild with icu-4.8

* Sat Apr 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.2.2-alt2
- updated build dependencies

* Wed Mar 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.2.2-alt1
- 3.3.2 RC2

* Tue Mar 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.2.1-alt1
- 3.3.2 RC1

* Wed Feb 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.1.2-alt1
- 3.3.1 RC2

* Wed Feb 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.1.1-alt1
- 3.3.1 RC1

* Wed Jan 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.0.4-alt1
- 3.3.0 RC4

* Tue Jan 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 3.3.0.3-alt1
- 3.3.0 RC3

* Sun Dec 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.3.0.2-alt1
- 3.3.0 RC2

* Fri Dec 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 3.3.0.1-alt1
- 3.3.0 RC1
