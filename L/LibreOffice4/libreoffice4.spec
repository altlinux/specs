# 4.3.0.0.beta2-buildfix1
%def_with forky
%def_with parallelism
%def_without fetch

Name: LibreOffice4
Version: 4.3
%define urelease 0.0.beta2-buildfix1
%define uversion %version.%urelease
%define oopfx lo4
%define lodir %_libdir/%name
%define uname libreoffice4
%define conffile %_sysconfdir/sysconfig/%uname
Release: alt0.beta2.buildfix1
Summary: LibreOffice Productivity Suite
License: LGPL
Group: Office
URL: http://www.libreoffice.org

Requires: %name-integrated = %version-%release
Requires: %name-common = %version-%release
Requires: %name-mimetypes = %version-%release
Requires: %name-extensions = %version-%release

Provides: %name-full = %version-%release
Provides: libreoffice = %version-%release
Obsoletes: %name-full < %version-%release

%define with_lang ru de fr uk pt-BR es kk
#Requires: java xdg-utils hunspell-en hyphen-en mythes-en
#Requires: gst-plugins-bad1.0 gst-plugins-good1.0 gst-plugins-nice1.0 gst-plugins-ugly1.0 gst-plugins-base1.0
Requires: gst-libav

Source:		libreoffice-%uversion.tar.xz
Source1:	libreoffice-dictionaries-%uversion.tar.xz
Source2:	libreoffice-help-%uversion.tar.xz
Source3:	libreoffice-translations-%uversion.tar.xz


Source10:	libreoffice-ext_sources.%uversion.tar
Source100:	forky.c
Source200:	update_from_fc

Patch401:	alt-001-MOZILLA_CERTIFICATE_FOLDER.patch
Patch402: libreoffice-4-alt-drop-gnome-open.patch
Patch403: alt-002-tmpdir.patch

# FC patches files

Patch12: 0001-Resolves-rhbz-1035092-no-shortcut-key-for-Italian-To.patch
Patch13: 0001-disable-firebird-unit-test.patch
Patch14: 0001-never-run-autogen.sh.patch
Patch15: 0001-add-X-TryExec-entries-to-desktop-files.patch
Patch16: 0001-disable-PSD-import-test-which-deadlocks-on-ARM.patch
Patch44: 0001-deb-749592-mysql-connector-doesn-t-work-with-remote-.patch

# Long-term FC patches
Patch300: openoffice.org-2.0.2.rh188467.printingdefaults.patch
Patch301: openoffice.org-3.0.0.ooo88341.sc.verticalboxes.patch
Patch302: openoffice.org-3.1.0.ooo101274.opening-a-directory.patch

BuildRequires: ant-testutil imake junit4 xorg-cf-files zenity
BuildRequires: sac pentaho-libxml flute pentaho-reporting-flow-engine liblayout libloader libformula librepository libserializer libbase apache-commons-codec apache-commons-lang apache-commons-httpclient apache-commons-logging bsh rhino

BuildRequires: bc
BuildRequires: binutils
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: findutils
BuildRequires: libicu-devel
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: git
BuildRequires: gperf
BuildRequires: perl-Archive-Zip
BuildRequires: zip unzip

# libs / headers - common
BuildRequires: libcups-devel
BuildRequires: libexpat-devel
BuildRequires: fonts-ttf-liberation
BuildRequires: libhyphen-devel
BuildRequires: libicu-devel
BuildRequires: liblpsolve-devel
BuildRequires: pkgconfig(cppunit) >= 1.12.0
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(evolution-data-server-1.2)
BuildRequires: pkgconfig(fontconfig) >= 2.4.1
BuildRequires: pkgconfig(freetype2) >= 9.9.3
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(gtk+-2.0) >= 2.10.0 pkgconfig(gdk-pixbuf-xlib-2.0) >= 2.2 pkgconfig(gtk+-unix-print-2.0) >= 2.10.0 pkgconfig(gio-2.0) >= 2.26
BuildRequires: pkgconfig(telepathy-glib) >= 0.18.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.2 pkgconfig(gtk+-unix-print-3.0) pkgconfig(gmodule-no-export-2.0) pkgconfig(cairo)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libcurl) >= 7.19.4
BuildRequires: pkgconfig(libidn)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(neon)
BuildRequires: pkgconfig(nss) >= 3.9.3 pkgconfig(nspr) >= 4.8
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(redland) >= 1.0.8 pkgconfig(raptor2) >= 2.0.7
BuildRequires: pkgconfig(sane-backends)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(zlib)
BuildRequires: libvigra-devel

# libs / headers - conditional
#BuildRequires: firebird-devel
#BuildRequires: firebird-libfbembed
BuildRequires: libglm-devel
BuildRequires: kde4libs-devel
BuildRequires: pkgconfig(glew) >= 1.10.0
BuildRequires: pkgconfig(libabw-0.1)
BuildRequires: pkgconfig(libcdr-0.1)
BuildRequires: pkgconfig(libcmis-0.4) >= 0.4.0
BuildRequires: pkgconfig(libe-book-0.1) >= 0.1.1
BuildRequires: pkgconfig(libeot) >= 0.01
BuildRequires: pkgconfig(libetonyek-0.1) >= 0.1.1
BuildRequires: pkgconfig(libfreehand-0.1)
BuildRequires: pkgconfig(libmspub-0.1)
BuildRequires: pkgconfig(libmwaw-0.3) >= 0.3.1
BuildRequires: pkgconfig(libodfgen-0.1)
BuildRequires: pkgconfig(liborcus-0.8) >= 0.7.0
BuildRequires: pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires: pkgconfig(libvisio-0.1)
BuildRequires: pkgconfig(libwpd-0.10)
BuildRequires: pkgconfig(libwpg-0.3)
BuildRequires: pkgconfig(libwps-0.3)
BuildRequires: pkgconfig(mdds) >= 0.10.3

BuildRequires: boost-devel
BuildRequires: pkgconfig(graphite2) >= 0.9.3
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libclucene-core)
BuildRequires: pkgconfig(libexttextcat)
BuildRequires: pkgconfig(liblangtag)
BuildRequires: pkgconfig(mythes)
BuildRequires: pkgconfig(poppler-cpp)

BuildRequires: libldap-devel
BuildRequires: libunixODBC-devel
BuildRequires: postgresql-devel
BuildRequires: libmysqlclient-devel
BuildRequires: libbluez-devel
BuildRequires: python3-devel
BuildRequires: xulrunner-devel

# libs / headers - special cases
BuildRequires: pkgconfig(gstreamer-1.0) pkgconfig(gstreamer-plugins-base-1.0) pkgconfig(gstreamer-video-1.0)
BuildRequires: libjpeg-devel


# to remove in 4.2
BuildRequires: tomcat-servlet-3.0-api

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*

%description
LibreOffice is a productivity suite that is compatible with other major
office suites.

This package provides maximum possible installation of %name along winth
other office packages, except of language packs and GNOME/KDE bindings.

%package common
Summary: Basic installation of %name
Group: Office
AutoReqProv: yes, noshell, nopython
%description common
Common part of %name that does not interfere with other packages

%package standalone
Summary: Renamed binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %version-%release
Conflicts: %name-integrated
Requires: %name-common = %version-%release
%description standalone
Wrapper scripts, icons and desktop files for running renamed version of %name
as lo4write, lo4draw etc.

%package integrated
Summary: Binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %version-%release
Conflicts: %name-standalone
Requires: %name-common = %version-%release
%description integrated
Wrapper scripts, icons and desktop files for running %name

%package gnome
Summary: GNOME Extensions for %name
Group:  Office
Requires: %uname = %version-%release
Requires: %name-common = %version-%release
%description gnome
GNOME extensions for %name

%package kde4
Summary: KDE4 Extensions for %name
Group:  Office
Requires: %uname = %version-%release
Requires: %name-common = %version-%release
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
%if_with forky
echo Using forky
%else
echo Direct build
%endif
%setup -q -n libreoffice-%uversion -a10 -b1 -b2 -b3
%patch401 -p0
%patch402 -p1
%patch403 -p2

# FC patches applying (## -- unsuccsessful but seems meaningful)
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch44 -p1

# Long-term FC patches applying
#%patch300 -p1
#%patch301 -p1
#%patch302 -p1

# Hack GCC_VERSION usage
sed -i '
s/\(GCC_VERSION=`echo $_gcc_version\)[^`]*`/\1|cut -d. -f1-2`/
/if test "\${*GCC_VERSION}*" -lt 0401/,/fi/d
/elif test "\${GCC_VERSION\?}" -ge 0403; then/d
' configure.ac

rm -fr %name-tnslations/git-hooks

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
./autogen.sh \
        --with-vendor="ALT Linux Team" \
        --disable-gnome-vfs \
        --disable-odk \
        --disable-systray \
	--disable-firebird-sdbc \
	--disable-gltf \
	--disable-coinmp \
        --enable-dbus \
        --enable-evolution2 \
        --enable-gio \
        --with-alloc=system \
        --without-fonts \
        --without-myspell-dicts \
        --without-ppds \
	\
        --with-external-dict-dir=%_datadir/myspell \
        --with-external-hyph-dir=%_datadir/hyphen \
        --with-external-thes-dir=%_datadir/mythes \
        --with-lang="en-US %with_lang" \
        --with-external-tar=`pwd`/ext_sources \
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
  \
	--enable-release-build \
	--with-help \
  \
	--enable-gtk3 \
	--enable-gstreamer \
	--disable-gstreamer-0-10 \
%if_with parallelism
	--with-parallelism \
%endif
%if_with fetch
	--enable-fetch-external
%else
        --with-system-libs \
	--disable-fetch-external
%endif

%if_with forky
# Make forky
gcc -g -DHAVE_CONFIG_H -shared -O3 -fomit-frame-pointer -fPIC forky.c -oforky.so -ldl
%endif

%make bootstrap

%if_with forky
# TODO prefect forky_max tune
echo Using forky
export forky_divider=16
export forky_max_procs=`awk '/^Max processes/{print int(5*$3/'$forky_divider')}' < /proc/self/limits`
##export forky_max_vsz=`awk '/^CommitLimit/{print int(5*$2/'$forky_divider')}' < /proc/meminfo`
##export forky_max_rss=$(($forky_max_vsz/3))
export forky_max_rss=6000000
export forky_max_vsz=$((3*$forky_max_rss))
export forky_verbose=1
echo "max_procs $forky_max_procs / max_vsz $forky_max_vsz / max_rss $forky_max_rss" | tee $HOME/forky.log
export LD_PRELOAD=`pwd`/forky.so

%make || { tail -100 $HOME/forky.log; head -1 $HOME/forky.log; wc $HOME/forky.log; false; }
test -r $HOME/forky.log && echo "Fork() was `wc -l $HOME/forky.log` times delayed" || :
%else
%make
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
find .%lodir/program/*gconf*
find .%lodir/program/*gtk*.so
find .%lodir/share/registry/gnome.xcd
) | sed 's/^[.]//' > files.gnome

# Create kde plugin list
(
cd %buildroot
find .%lodir/program/*kde*
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

%files common -f files.nolang
%exclude /gid_Module*
%_bindir/libreoffice%version
%config %conffile
%lodir/share/extensions/package.txt
#lodir/share/extensions/presentation-minimizer
%_iconsdir/*/*/apps/libreoffice%{version}-*.*g

%files standalone
%_bindir/lo4*
%exclude %_bindir/libreoffice%version
%_desktopdir/libreoffice%{version}-*
%exclude %_iconsdir/*/*/apps/libreoffice%{version}-*.*g

%files integrated
%_bindir/*
%exclude %_bindir/lo4*
%exclude %_bindir/libreoffice%version
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
#exclude %lodir/share/extensions/presentation-minimizer

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
%langpack -l kk -n Kazakh

%changelog
* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 4.3-alt0.beta2.buildfix1
- 4.3.0.0.beta2-buildfix1
- update BR:
- switch to librevenge-based import libs

* Wed Apr 30 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt3
- Version up to 4.2.4.1

* Wed Apr 16 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt2
- Version up to 4.2.3.3

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 4.2-alt1
- Version up

* Tue Feb 04 2014 Fr. Br. George <george@altlinux.ru> 4.1-alt9
- Merge -full package into general one
- Buld with help (closes: #29735)
- Require gst1.0 plugins to install (closes: #29782)

* Thu Dec 26 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt8
- Build with --enable-release-build

* Thu Dec 19 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt7
- Version up to officially corporative stable 4.1.4.2
- Disable applied patches

* Mon Nov 25 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt6
- Version up to officially stable 4.1.3.2
- More accurate forky utilization

* Tue Oct 01 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt5
- Version up to 4.1.2.3

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt4
- rebuild against libharfbuzz-icu

* Wed Sep 04 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt3
- Version up to 4.1.1.2
- Refresh FC patchset
- Un-hardcode /tmp usage (Closes: 29267)

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 4.1-alt2
- fixed gnome file list
- fixed kde file list
- drop use gnome-open in gnome-open-url.sh
- build with gstreamer-1.0
- build with system libraries (libodfgen,libcdr,libmspub,libmwaw,libvisio,libcmis,libexttextcat)
- build with system jar files
- changed configure options --with-system-* to --with-system-libs

* Tue Jul 30 2013 Fr. Br. George <george@altlinux.ru> 4.1-alt1
- Version up to 4.1.0.4
- Renew FC patchset (previous ones are pushed to upstream)

*  Wed May 15 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt8
- Version up to 4.0.3.3
- Drop some RH patches accepted by upstream

* Wed Apr 24 2013 Sergey V Turchin <zerg@altlinux.org> 4.0-alt7.1
- NMU: rebuilt with new poppler

* Mon Apr 22 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt7
- Closes: 28883
- Drop some internal libraries build

* Thu Apr 18 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt6
- Version up to 4.0.2.2
- Incoprporate useful RH patches

* Thu Mar 21 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt5
- Introduce Kazakh locale
- Fix common binary displacement

* Tue Mar 19 2013 Fr. Br. George <george@altlinux.ru> 4.0-alt4
- Fix conflicts with LO3
- Introduce "full" package (without langpacks and GNOME/KDE stuff)

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

