# 4.0.0.3
%define with_forky yes

Name: LibreOffice4
Version: 4.0
%define urelease 0.3
%define uversion %version.%urelease
#define sdversion 1.0.0
%define oopfx lo4
%define lodir %_libdir/%name
Release: alt2
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

Patch1:	alt-001-MOZILLA_CERTIFICATE_FOLDER.patch

# FC patches
Patch201: 0001-Work-around-problem-with-boost-shared_array-NULL-cto.patch
Patch202: 0001-fix-compile-for-change-to-boost-1.53.0-declaring-sma.patch

AutoReqProv: yes, noshell, nopython

# Automatically added by buildreq on Mon Feb 11 2013
# optimized out: ant cppunit fontconfig fontconfig-devel fonts-ttf-java-1.6.0-sun glib2-devel gstreamer-devel icu-utils java java-devel jpackage-utils junit libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libXt-devel libatk-devel libcairo-devel libcom_err-devel libcurl-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-xlib libgio-devel libgmp-devel libgpg-error libgst-plugins libjpeg-devel libkrb5-devel libncurses-devel libnspr-devel libpango-devel libpng-devel libpoppler-devel libpq-devel libstdc++-devel libsystemd-daemon libtinfo-devel libwayland-client libwayland-server libwpd9-devel libxml2-devel perl-Compress-Raw-Zlib pkg-config poppler-data python-base tzdata xerces-j2 xml-common xml-commons-jaxp-1.3-apis xml-utils xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel xsltproc xz zlib-devel
BuildRequires: ant-testutil cppunit-devel flex gcc-c++ gperf gst-plugins-devel imake junit4 libGConf-devel libGLU-devel libXinerama-devel libXrandr-devel libcups-devel libdb4-devel libdbus-glib-devel libexpat-devel libgtk+2-devel libhunspell-devel libicu-devel libldap-devel liblpsolve-devel libmpfr-devel libmythes-devel libncursesw-devel libneon-devel libnss-devel liborcus-devel libpoppler-cpp-devel libreadline-devel libssl-devel libunixODBC-devel libwpg2-devel libwps-devel libxslt-devel perl-Archive-Zip postgresql-devel unzip wget xorg-cf-files zenity zip 

BuildRequires: /proc wget xdg-utils zip >= 3.0
BuildRequires: java-1.6.0-sun-devel
BuildRequires: liblpsolve-devel libjpeg-devel fonts-ttf-liberation
BuildRequires: kde4libs-devel

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*

%description
LibreOffice is a productivity suite that is compatible with other major
office suites

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

%package kde4
Summary: KDE4 Extensions for %name
Group:  Office
Requires: %name = %version-%release
%description kde4
KDE4 extensions for %name

# define macro for quick langpack description
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
%setup -q -n libreoffice-%uversion -a10 -b1 -b2 -b3
%patch1 -p0
%patch201 -p1
%patch202 -p1

rm -fr %name-tnslations/git-hooks

# Hack build ditrectory a little
ln -s %SOURCE0 ext_sources/
ln -s %SOURCE1 ext_sources/
ln -s %SOURCE2 ext_sources/
ln -s %SOURCE3 ext_sources/

install -D %SOURCE100 forky.c

# create shell wrappers
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
        --enable-gio \
        --with-alloc=system \
        --without-afms \
        --without-fonts \
        --without-myspell-dicts \
        --without-ppds \
        --with-system-boost \
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
        --with-system-lpsolve \
        --with-system-mozilla \
        --with-system-mythes \
        --with-system-neon \
        --with-system-nss \
        --with-system-odbc \
	--with-system-openldap \
        --with-system-openssl \
        --with-system-orcus \
        --with-system-poppler \
        --with-system-postgresql \
        --with-system-stdlibs \
        --with-system-zlib \
	\
        --with-external-dict-dir=%_datadir/myspell \
        --with-external-hyph-dir=%_datadir/hyphen \
        --with-external-thes-dir=%_datadir/mythes \
        --with-lang="en-US %with_lang" \
        --with-external-tar=`pwd`/ext_sources \
        \
        --enable-ext-report-builder \
	--with-parallelism \
	\
	--enable-kde4 \
	\
	--enable-hardlink-deliver \
	--disable-fetch-external \


# Make forky
gcc -g -DHAVE_CONFIG_H -shared -O3 -fomit-frame-pointer -fPIC forky.c -oforky.so -ldl

%make bootstrap

%ifdef with_forky
# TODO calculate forky limits
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
touch $HOME/forky.log
%make_build || { wc $HOME/forky.log; false; }
test -r $HOME/forky.log && echo "Fork() was `wc -l $HOME/forky.log` times delayed" || :
%else
%make_build
%endif

%install
%makeinstall DESTDIR=%buildroot INSTALLDIR=%lodir

# Pick up LOO-generated file lists
for l in %with_lang; do
	ll="`echo "$l" | tr '-' '_'`"
	cat %buildroot/gid_*_$ll | sort -u > $l.lang
done

# Create gnome plugin list
(
cd %buildroot
find .%lodir/program/gnome*
find .%lodir/program/gconfbe1.uno.so
find .%lodir/program/libvclplug_gtk*.so
find .%lodir/share/registry/gnome.xcd
) | sed 's/^[.]//' > files.gnome

# Create kde plugin list
(
cd %buildroot
find .%lodir/program/kde4*
find .%lodir/program/libvclplug_kde4*
) | sed 's/^[.]//' > files.kde4

# Generate base filelist by removing files from  separated packages
{ cat %buildroot/gid_* | sort -u ; cat *.lang files.gnome files.kde4; } | sort | uniq -u > files.nolang

unset RPM_PYTHON

# Install wrappers
for n in l*4*.sh; do install -m755 -D $n %buildroot%_bindir/${n%%.sh}; done

# Install renamed icons
for n in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	m=libreoffice%version-`basename "$n"`
	d=`dirname "$n"`
	install -D sysui/desktop/icons/$n %buildroot%_iconsdir/$d/$m
done
# TODO icon-themes/

# Install desktop files
mkdir -p %buildroot%_desktopdir
for n in writer impress calc base draw math qstart; do
	ln -s %lodir/share/xdg/$n.desktop %buildroot%_desktopdir/libreoffice%version-$n.desktop
done

# TODO .mime (?)

%files -f files.nolang
%exclude /gid_Module*
%_bindir/*
%_desktopdir/*
%_iconsdir/*/*/apps/*.*g

%files gnome -f files.gnome

%files kde4 -f files.kde4

%files icons
%_iconsdir/*/*/mimetypes/*

%langpack -l ru -n Russian
%langpack -l de -n German
%langpack -l fr -n French
%langpack -l uk -n Ukrainian
%langpack -l pt-BR -n Brazilian Portuguese
%langpack -l es -n Espanian

%changelog
* Tue Mar 05 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt2
- Separate KDE4 plugins
- Apply Firefox certificates import patch

* Tue Feb 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt1
Initial test build

