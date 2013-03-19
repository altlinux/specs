# 4.0.2.1
%define with_forky yes

Name: LibreOffice4
Version: 4.0
%define urelease 2.1
%define uversion %version.%urelease
%define oopfx lo4
%define lodir %_libdir/%name
%define uname libreoffice4
%define conffile %_sysconfdir/sysconfig/%uname
Release: alt4
Summary: LibreOffice Productivity Suite
License: LGPL
Group: Office
URL: http://www.libreoffice.org

# Change this to -integrated to make LO4 default
Requires: %name-standalone = %version-%release
Requires: %name-common = %version-%release

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

# Automatically added by buildreq on Wed Mar 06 2013
# optimized out: ant boost-devel boost-devel-headers boost-interprocess-devel boost-intrusive-devel bzlib-devel cppunit fontconfig fontconfig-devel fonts-ttf-java-1.6.0-sun glib2-devel gstreamer-devel icu-utils java java-devel jpackage-utils junit kde4libs libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXt-devel libatk-devel libcairo-devel libcom_err-devel libcurl-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-xlib libgio-devel libgmp-devel libgpg-error libgst-plugins libkrb5-devel libncurses-devel libnspr-devel libpango-devel libpcre-devel libpng-devel libpoppler-devel libpq-devel libqt4-core libqt4-devel libqt4-gui libssl-devel libstdc++-devel libsystemd-daemon libtinfo-devel libunixODBC-devel libwayland-client libwayland-server libwpd9-devel libxml2-devel perl-Compress-Raw-Zlib pkg-config poppler-data python-base tzdata tzdata-java xerces-j2 xml-common xml-commons-jaxp-1.3-apis xml-utils xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel xsltproc xz zlib-devel
BuildRequires: ant-testutil cppunit-devel flex fonts-ttf-liberation gcc-c++ gperf gst-plugins-devel imake junit4 kde4libs-devel libGConf-devel libcups-devel libdb4-devel libdbus-glib-devel libexpat-devel libgtk+2-devel libhunspell-devel libicu-devel libjpeg-devel libldap-devel liblpsolve-devel libmpfr-devel libmysqlclient-devel libmythes-devel libncursesw-devel libneon-devel libnss-devel liborcus-devel libpoppler-cpp-devel libreadline-devel libvigra-devel libwpg2-devel libwps-devel libxslt-devel perl-Archive-Zip postgresql-devel unzip xorg-cf-files zenity zip

BuildRequires: libbluez-devel libhyphen-devel libclucene-core-devel

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*

%description
LibreOffice is a productivity suite that is compatible with other major
office suites

%package common
Summary: Basic installation of %name
Group: Office
AutoReqProv: yes, noshell, nopython
%description common
Common part of %name that does not interfere with other packages

%package full
Summary: LibreOffice Productivity Suite
Group: Office
Requires: %name-integrated = %version-%release
Requires: %name-common = %version-%release
Requires: %name-mimetypes = %version-%release
%description full
Full installation of %name, except of language packs
and GNOME/KDE bindings.

%package standalone
Summary: Renamed binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %version-%release
Conflicts: %name-integrated
%description standalone
Wrapper scripts, icons and desktop files for running %name as lo4*

%package integrated
Summary: Binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %version-%release
Conflicts: %name-standalone
%description integrated
Wrapper scripts, icons and desktop files for running %name

%package gnome
Summary: GNOME Extensions for %name
Group:  Office
Requires: %uname = %version-%release
%description gnome
GNOME extensions for %name

%package kde4
Summary: KDE4 Extensions for %name
Group:  Office
Requires: %uname = %version-%release
%description kde4
KDE4 extensions for %name

%package extensions
Summary: Additional extensions for %name
Group:  Office
Requires: %uname = %version-%release
AutoReqProv: yes, noshell, nopython
%description extensions
Additional extensions for %name.
One can choose either to install this package at once,
or to download and install (possibly newer) extensions manually.

%package mimetypes
Summary: Mimetype keys support for %name
Group: Office
BuildArch: noarch
%description mimetypes
%name is distributed along with some mimetype settings and files.
This package installs them.

# define macro for quick langpack description
%define langpack(l:n:) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %name \
Group:  Office \
Requires: %uname = %version-%release \
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
##ln -s %SOURCE0 ext_sources/
##ln -s %SOURCE1 ext_sources/
##ln -s %SOURCE2 ext_sources/
##ln -s %SOURCE3 ext_sources/

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

# Now create a config file
grep -r getenv * | sed -n 's/.*getenv *( *"\([^"]*\).*/\1/p' | sort -u | egrep 'STAR_|SAL_|OOO_' > %name.config.ENV

sed -n '/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/p' < desktop/scripts/soffice.sh > libreoffice.config
test -n "libreoffice.config"
sed -i '/# STAR_PROFILE_LOCKING_DISABLED/i\
test -r %conffile && . %conffile ||:
/# STAR_PROFILE_LOCKING_DISABLED/,/#.*JITC_PROCESSOR_TYPE_EXPORT/d' desktop/scripts/soffice.sh

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
	--with-system-altlinuxhyph \
        --with-system-boost \
        --with-system-cairo \
	--with-system-clucene \
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
	--with-system-vigra \
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
  	\
  --enable-ext-diagram \
  --enable-ext-google-docs \
  --enable-ext-nlpsolver \
  --enable-ext-numbertext \
  --enable-ext-typo \
  --enable-ext-validator \
  --enable-ext-watch-window \
  --enable-ext-wiki-publisher \
  --enable-ext-ct2n \
  --enable-ext-barcode \
  --with-system-bluez \
  \
  --with-system-mysql \
  --enable-ext-mysql-connector \
  \
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
{ cat %buildroot/gid_* | sort -u ; cat *.lang files.gnome files.kde4; } | sort | uniq -u | grep -v '~$' | grep -v '/share/extensions/.' > files.nolang

unset RPM_PYTHON

# Install renamed wrappers
for n in l*4*.sh; do install -m755 -D $n %buildroot%_bindir/${n%%.sh}; done
# Install wrappers
for n in lo4*.sh; do m="lo${n##lo4}"; install -m755 -D $n %buildroot%_bindir/${m%%.sh}; done

# Install renamed icons
for n in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	m=libreoffice%version-`basename "$n"`
	d=`dirname "$n"`
	install -D sysui/desktop/icons/$n %buildroot%_iconsdir/$d/$m
done
# install unrenamed icons
for n in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	d=`dirname "$n"`
	install -D sysui/desktop/icons/$n %buildroot%_iconsdir/$d/$n
done

# TODO icon-themes/

mkdir -p %buildroot%_desktopdir
for n in writer impress calc base draw math qstart; do
	ln -s %lodir/share/xdg/$n.desktop %buildroot%_desktopdir/libreoffice%version-$n.desktop
	ln -s %lodir/share/xdg/$n.desktop %buildroot%_desktopdir/$n.desktop
done

# TODO some other hack with .mime (?)
mkdir -p %buildroot%_datadir/mime-info %buildroot%_datadir/mimelnk/application %buildroot%_datadir/application-registry
install sysui/desktop/mimetypes/*.keys %buildroot%_datadir/mime-info/
install sysui/desktop/mimetypes/*.mime %buildroot%_datadir/mime-info/
install sysui/desktop/mimetypes/*.desktop %buildroot%_datadir/mimelnk/application/
install sysui/desktop/mimetypes/*.applications %buildroot%_datadir/application-registry/

# Config file
install -D libreoffice.config %buildroot%conffile

%files

%files full

%files common -f files.nolang
%exclude /gid_Module*
%config %conffile
%lodir/share/extensions/package.txt
%lodir/share/extensions/presentation-minimizer
%lodir/share/extensions/report-builder

%files standalone
%_bindir/lo4*
%_desktopdir/libreoffice%{version}-*
%_iconsdir/*/*/apps/libreoffice%{version}-*.*g

%files integrated
%_bindir/*
%exclude %_bindir/lo4*
%_desktopdir/*
%exclude %_desktopdir/libreoffice%{version}-*
%_iconsdir/*/*/mimetypes/*
%_iconsdir/*/*/apps/*
%exclude %_iconsdir/*/*/apps/libreoffice%{version}-*.*g

%files gnome -f files.gnome

%files kde4 -f files.kde4

%files extensions
%lodir/share/extensions/*
%exclude %lodir/share/extensions/package.txt
%exclude %lodir/share/extensions/presentation-minimizer
%exclude %lodir/share/extensions/report-builder

%files mimetypes
%_datadir/mime-info/*
%_datadir/mimelnk/application/*
%_datadir/application-registry/*

%langpack -l ru -n Russian
%langpack -l de -n German
%langpack -l fr -n French
%langpack -l uk -n Ukrainian
%langpack -l pt-BR -n Brazilian Portuguese
%langpack -l es -n Espanian

%changelog
* Tue Mar 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt4
- Fix conflicts with LO3
- Introduce "full" package (without langpacks and GNOMe/KDE stuff)

* Wed Mar 06 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt3
- Update to 4.0.2.1
- Introduce extra extensions
- Separate %name-standalone and %name-integrated packages
- Introduce %name-mimetype

* Tue Mar 05 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt2
- Separate KDE4 plugins
- Apply Firefox certificates import patch

* Tue Feb 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt1
Initial test build

