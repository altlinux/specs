# 4.0.0.3
%define with_forky yes

Name: LibreOffice4
Version: 4.0
%define urelease 0.3
%define uversion %version.%urelease
#define sdversion 1.0.0
%define oopfx lo4
%define lodir %_libdir/%name
Release: alt1
Summary: LibreOffice Productivity Suite
License: LGPL
Group: Office
URL: http://www.libreoffice.org

%define with_lang ru de fr uk pt-BR es
#Requires: java xdg-utils hunspell-en hyphen-en mythes-en
#Requires: gst-plugins-base gst-plugins-good gst-plugins-ugly gst-plugins-bad gst-ffmpeg

Source:		libreoffice-%uversion.tar.xz
Source1:	libreoffice-dictionaries-%uversion.tar.xz
Source2:	libreoffice-help-%uversion.tar.xz
Source3:	libreoffice-translations-%uversion.tar.xz
#Source4:	sdremote-#sdversion-translations.tar.xz
#Source5:	sdremote-#sdversion.tar.xz


Source10:	libreoffice-ext_sources.%uversion.tar
Source100:	forky.c

AutoReqProv: yes, noshell, nopython

# Automatically added by buildreq on Mon Feb 11 2013
# optimized out: ant cppunit fontconfig fontconfig-devel fonts-ttf-java-1.6.0-sun glib2-devel gstreamer-devel icu-utils java java-devel jpackage-utils junit libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libXt-devel libatk-devel libcairo-devel libcom_err-devel libcurl-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-xlib libgio-devel libgmp-devel libgpg-error libgst-plugins libjpeg-devel libkrb5-devel libncurses-devel libnspr-devel libpango-devel libpng-devel libpoppler-devel libpq-devel libstdc++-devel libsystemd-daemon libtinfo-devel libwayland-client libwayland-server libwpd9-devel libxml2-devel perl-Compress-Raw-Zlib pkg-config poppler-data python-base tzdata xerces-j2 xml-common xml-commons-jaxp-1.3-apis xml-utils xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel xsltproc xz zlib-devel
BuildRequires: ant-testutil cppunit-devel flex gcc-c++ gperf gst-plugins-devel imake junit4 libGConf-devel libGLU-devel libXinerama-devel libXrandr-devel libcups-devel libdb4-devel libdbus-glib-devel libexpat-devel libgtk+2-devel libhunspell-devel libicu-devel libldap-devel liblpsolve-devel libmpfr-devel libmythes-devel libncursesw-devel libneon-devel libnss-devel liborcus-devel libpoppler-cpp-devel libreadline-devel libssl-devel libunixODBC-devel libwpg2-devel libwps-devel libxslt-devel perl-Archive-Zip postgresql-devel unzip wget xorg-cf-files zenity zip 

BuildRequires: /proc wget xdg-utils zip >= 3.0
BuildRequires: java-devel
BuildRequires: liblpsolve-devel libjpeg-devel fonts-ttf-liberation

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*

%description
LibreOffice is a productivity suite that is compatible with other major office suites

%package icons
Summary: Icon files for %name (separated for LibreOffice3 compatibility)
Group: Office
BuildArch: noarch
%description icons
Icon files for %name (separated for LibreOffice3 compatibility)

%package gnome
Summary: GNOME Extensions for %name
Group:  Office
Requires: %name = %version-%release
%description gnome
GNOME extensions for %name

%define langpack(l:n:) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %name \
Group:  Office \
Requires: %name = %version-%release \
%description %{pkgname} \
Provides additional %{langname} translations and resources for %name. \
\
%files %{pkgname} -f %{lang}.lang \
%{nil}

%prep
%ifdef with_forky
echo Using forky
%else
echo Direct build
%endif
%setup -q -n libreoffice-%uversion -a10
#-a1 -a2 -a3 -a10
#mv libreoffice-%uversion/* .
#rm -fr %name-translations-%version/git-hooks
#rm -f %name-help-%version/ChangeLog

ln -s %SOURCE0 ext_sources/
ln -s %SOURCE1 ext_sources/
ln -s %SOURCE2 ext_sources/
ln -s %SOURCE3 ext_sources/
rmdir translations dictionaries helpcontent2
ln -s src/libreoffice-%uversion/translations .
ln -s src/libreoffice-%uversion/dictionaries .
ln -s src/libreoffice-%uversion/helpcontent2 .

install -D %SOURCE100 forky.c

for n in office writer impress calc base draw math qstart; do
	oname=%{oopfx}$n
	case "$n" in 
		office) opt=""; oname=libreoffice%version;;
		qstart) opt="--quickstart --nologo --nodefault";;
		*) opt="--$n";;
	esac
	cat > $oname.sh <<@@@
#!/bin/sh
exec %lodir/program/soffice $opt "\$@"
@@@
done

%build
# XXX
#sed -i 's/MDDS_CPPFLAGS="-std=gnu++0x"/MDDS_CPPFLAGS=""/
#s/CXXFLAGS -std=gnu++0x/CXXFLAGS/
#' configure.in
# XXX
#sed -i 's/test \([$]enable_mergelibs\)/test "\1"/' configure.in

./autogen.sh \
        --with-vendor="ALT Linux Team" \
        --disable-gnome-vfs \
        --disable-odk \
        --disable-systray \
        --enable-dbus \
        --enable-evolution2 \
        --enable-ext-report-builder \
        --enable-gio \
        --with-alloc=system \
	--with-system-openldap \
        --without-afms \
        --without-fonts \
        --without-myspell-dicts \
        --without-ppds \
        --with-system-cairo \
        --with-system-cppunit \
        --with-system-curl \
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
        --with-system-poppler \
        --with-system-stdlibs \
        --with-system-zlib \
        --with-system-postgresql \
        --with-external-dict-dir=%_datadir/myspell \
        --with-external-hyph-dir=%_datadir/hyphen \
        --with-external-thes-dir=%_datadir/mythes \
        --with-lang="en-US %with_lang" \
        --with-external-tar=`pwd`/ext_sources \
        \
        --with-system-lpsolve \
        --with-system-mythes \
	--with-parallelism \
	\
	--with-system-orcus \


        #--with-system-boost \


gcc -g -O2 -DHAVE_CONFIG_H -shared -O3 -fomit-frame-pointer -fPIC forky.c -oforky.so -ldl

%make bootstrap

%ifdef with_forky
echo Using forky
export forky_max_procs=450
%ifarch x86_64
export forky_max_rss=16384000
export forky_max_vsz=81920000
%else
export forky_max_rss=8192000
export forky_max_vsz=16000000
%endif
export forky_verbose=1
export LD_PRELOAD=`pwd`/forky.so
%endif

%make_build || cat $HOME/forky.log

%install
%makeinstall DESTDIR=%buildroot INSTALLDIR=%lodir
for l in %with_lang; do
	ll="`echo "$l" | tr '-' '_'`"
	cat %buildroot/gid_*_$ll | sort -u > $l.lang
done

(
cd %buildroot
find .%lodir/program/gnome*
find .%lodir/program/gconfbe1.uno.so
find .%lodir/program/libvclplug_gtkl*.so
find .%lodir/share/registry/gnome.xcd
) | sed 's/^[.]//' > files.gnome

{ cat %buildroot/gid_* | sort -u ; cat *.lang; cat files.gnome; } | sort | uniq -u > files.nolang

unset RPM_PYTHON

for n in l*4*.sh; do install -m755 -D $n %buildroot%_bindir/${n%%.sh}; done

# TODO icon-themes/
# TODO rename icons
mkdir -p %buildroot%_iconsdir %buildroot%_desktopdir
for n in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	m=libreoffice%version-`basename "$n"`
	d=`dirname "$n"`
	install -D sysui/desktop/icons/$n %buildroot%_iconsdir/$d/$m
done

# TODO .desktop
for n in writer impress calc base draw math qstart; do
	ln -s %lodir/share/xdg/$n.desktop %buildroot%_desktopdir/libreoffice%version-$n.desktop
done

# TODO .mime (?)
# TODO package gnome

%files -f files.nolang
%exclude /gid_Module*
%_bindir/*
%_desktopdir/*
%_iconsdir/*/*/apps/*.*g

%files gnome -f files.gnome

%files icons
%_iconsdir/*/*/mimetypes/*

%langpack -l ru -n Russian
%langpack -l de -n German
%langpack -l fr -n French
%langpack -l uk -n Ukrainian
%langpack -l pt-BR -n Brazilian Portuguese
%langpack -l es -n Espanian

%changelog
* Tue Feb 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt1
Initial test build

