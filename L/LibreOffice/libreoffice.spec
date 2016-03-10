# 5.1.1.3
%def_without forky
%def_with parallelism
%def_without fetch
%def_without lto

Name: LibreOffice
Version: 5.1
%define urelease 1.3
%define uversion %version.%urelease
%define lodir %_libdir/%name
%define uname libreoffice5
%define conffile %_sysconfdir/sysconfig/%uname
Release: alt2
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
Obsoletes: libreoffice < 3.99
Obsoletes: %name-full < %version-%release
Obsoletes: LibreOffice4

%define with_lang ru be de fr uk pt-BR es kk tt
#Requires: java xdg-utils hunspell-en hyphen-en mythes-en
#Requires: gst-plugins-bad1.0 gst-plugins-good1.0 gst-plugins-nice1.0 gst-plugins-ugly1.0 gst-plugins-base1.0
Requires: gst-libav

Source:		libreoffice-%uversion.tar.xz
Source1:	libreoffice-dictionaries-%uversion.tar.xz
Source2:	libreoffice-help-%uversion.tar.xz
Source3:	libreoffice-translations-%uversion.tar.xz


Source10:	libreoffice-ext_sources.%uversion.tar
Source100:	forky.c
Source200:	oasis-master-document-template.icns
Source300:	update_from_fc

## FC patches

## Long-term FC patches

## ALT patches
Patch401: alt-001-MOZILLA_CERTIFICATE_FOLDER.patch
Patch402: libreoffice-4-alt-drop-gnome-open.patch
Patch403: alt-002-tmpdir.patch
Patch404: alt-004-isnan.patch

%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist %lodir/share/config/webcast/*

# Automatically added by buildreq on Mon Nov 10 2014
# optimized out: ant-testutil apache-commons-codec apache-commons-logging boost-devel boost-devel-headers boost-interprocess-devel boost-intrusive-devel cppunit flute fontconfig fontconfig-devel fonts-type1-xorg glib2-devel gstreamer1.0-devel icu-utils java java-devel jpackage-utils junit4 kde4libs libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXext-devel libXinerama-devel libXrandr-devel libXrender-devel libXt-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcloog-isl4 libclucene-contribs-lib libclucene-core libclucene-shared libcurl-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-xlib libgio-devel libgpg-error libgraphite2-devel libgst-plugins1.0 libharfbuzz-icu libicu-devel libnspr-devel libpango-devel libpng-devel libpoppler-devel libpq-devel libqt4-core libqt4-devel libqt4-gui libqt4-network librasqal-devel librevenge-devel libsasl2-3 libssl-devel libstdc++-devel libunixODBC-devel libwayland-client libwayland-server libxml2-devel pentaho-libxml perl-Compress-Raw-Zlib pkg-config poppler-data python-base python-devel python-modules python3 python3-base raptor2-devel sac tzdata tzdata-java xerces-j2 xml-common xml-commons-jaxp-1.4-apis xml-utils xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel xsltproc xz zlib-devel
BuildRequires: ant apache-commons-httpclient apache-commons-lang bsh cppunit-devel flex fonts-ttf-liberation gcc-c++ git-core gperf gst-plugins1.0-devel hunspell-en imake kde4libs-devel libGConf-devel libGLEW-devel libabw-devel libbluez-devel libcdr-devel libclucene-core-devel libcmis-devel libcups-devel libdbus-glib-devel libetonyek-devel libexpat-devel libexttextcat-devel libfreehand-devel libglm-devel libgtk+2-devel libgtk+3-devel libharfbuzz-devel libhunspell-devel libhyphen-devel libjpeg-devel liblangtag-devel liblcms2-devel libldap-devel liblpsolve-devel libmspub-devel libmwaw-devel libmythes-devel libneon-devel libnss-devel libodfgen-devel liborcus-devel libpoppler-cpp-devel libredland-devel libsane-devel libvigra-devel libvisio-devel libwpd9-devel libwpg-devel libwps-devel libxslt-devel mdds-devel pentaho-reporting-flow-engine perl-Archive-Zip postgresql-devel python3-dev unzip xorg-cf-files zip

# 4.4
BuildRequires: libavahi-devel libpagemaker-devel boost-signals-devel
BuildRequires: libe-book-devel
# 5.1
BuildRequires: junit xsltproc java-1.8.0-openjdk-devel

%description
LibreOffice is a productivity suite that is compatible with other major
office suites.

This package provides maximum possible installation of %name along winth
other office packages, except of language packs and GNOME/KDE bindings.

%package common
Summary: Basic installation of %name
Group: Office
Obsoletes: LibreOffice4-common
AutoReqProv: yes, noshell, nopython
%description common
Common part of %name that does not interfere with other packages

%package integrated
Summary: Binaries, icons and desktop files for %name
Group: Office
Provides: %uname = %version-%release
Obsoletes: LibreOffice4-integrated
Requires: %name-common = %version-%release
%description integrated
Wrapper scripts, icons and desktop files for running %name

%package gnome
Summary: GNOME Extensions for %name
Group:  Office
Requires: %uname = %version-%release
Requires: %name-common = %version-%release
Obsoletes: LibreOffice4-gnome
%description gnome
GNOME extensions for %name

%package kde4
Summary: KDE4 Extensions for %name
Group:  Office
Requires: %uname = %version-%release
Requires: %name-common = %version-%release
Obsoletes: LibreOffice4-kde4
%description kde4
KDE4 extensions for %name

%package extensions
Summary: Additional extensions for %name
Group:  Office
Requires: %uname = %version-%release
AutoReqProv: yes, noshell, nopython
Obsoletes: LibreOffice4-extensions
%description extensions
Additional extensions for %name.
One can choose either to install this package at once,
or to download and install (possibly newer) extensions manually.

%package mimetypes
Summary: Mimetype keys support for %name
Group: Office
BuildArch: noarch
Obsoletes: LibreOffice4-mimetypes
%description mimetypes
%name is distributed along with some mimetype settings and files.
This package installs them.

# TODO redefine %%lang adding corr langpack
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
Obsoletes: LibreOffice4-%{pkgname} \
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

## FC apply patches

## Long-term FC patches applying

## ALT apply patches
%patch401 -p0
##patch402 -p1
%patch403 -p2
%patch404 -p1

# Hacked git binary patch
cp %SOURCE300 sysui/desktop/icons/

# Unhack liborcus version from configure
# TODO check after 5.0.2.1
#sed -Ei 's/(libo_CHECK_SYSTEM_MODULE.*liborcus)-[0-9.]+/\1/' configure.ac

rm -fr %name-tnslations/git-hooks

install -D %SOURCE100 forky.c

# create shell wrappers
for n in office writer impress calc base draw math qstart; do
	oname=lo$n
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
export CC=%_target_platform-gcc
export CXX=%_target_platform-g++
./autogen.sh \
        --with-vendor="ALT Linux Team" \
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
	--without-system-npapi-headers \
	\
        --with-external-dict-dir=%_datadir/myspell \
        --with-external-hyph-dir=%_datadir/hyphen \
        --with-external-thes-dir=%_datadir/mythes \
        --with-lang="en-US %with_lang" \
        --with-external-tar=`pwd`/ext_sources \
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
	--disable-ext-languagetool \
  \
	--enable-release-build \
	--with-help \
  \
	--enable-kde4 \
	--enable-gtk3 \
	--disable-gstreamer-0-10 \
  \
  	--enable-avahi \
%if_with lto
  	--enable-lto \
%endif
%if_with parallelism
	--with-parallelism \
%else   
        --without-parallelism \
%endif
%if_with fetch
	--enable-python=internal \
	--enable-fetch-external
%else
	--with-system-libs \
	--enable-python=internal \
	--disable-fetch-external
%endif

#        --disable-gnome-vfs \

%if_with forky
# Make forky
gcc -g -DHAVE_CONFIG_H -shared -O3 -fomit-frame-pointer -fPIC forky.c -oforky.so -ldl
%endif

%make bootstrap

%if_with parallelism
export _JAVA_OPTIONS="-XX:ParallelGCThreads=4 $_JAVA_OPTIONS"
%endif

%if_with forky
# TODO prefect forky_max tune
echo Using forky
export forky_divider=21
export forky_max_procs=`awk '/^Max processes/{print int(5*$3/'$forky_divider')}' < /proc/self/limits`
export forky_max_rss=6400000
export forky_max_vsz=9600000
export forky_verbose=1
echo "max_procs $forky_max_procs / max_vsz $forky_max_vsz / max_rss $forky_max_rss" | tee $HOME/forky.log
export LD_PRELOAD=`pwd`/forky.so

%make build-nocheck || { tail -100 $HOME/forky.log; head -1 $HOME/forky.log; wc $HOME/forky.log; false; }
test -r $HOME/forky.log && echo "Fork() was `wc -l $HOME/forky.log` times delayed" || :
%else
%make build-nocheck
%endif

%install
%makeinstall DESTDIR=%buildroot INSTALLDIR=%lodir
# Ignore dull /usr/local/bin/python hack
chmod -x %buildroot%lodir/program/python-core*/lib/cgi.py

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

# Install wrappers
for n in lo*.sh; do install -m755 -D $n %buildroot%_bindir/${n%%.sh}; done
install -m755 -D libreoffice%version.sh %buildroot%_bindir/loffice
install -m755 libreoffice%version.sh %buildroot%_bindir/libreoffice%version

# install icons
for f in `( cd sysui/desktop/icons; find hicolor -type f )`; do
	d=`dirname "$f"`; n=`basename "$f"`
	install -D sysui/desktop/icons/$f %buildroot%_iconsdir/$d/$n
	ln -sr %buildroot%_iconsdir/$d/$n %buildroot%_iconsdir/$d/libreoffice%version-$n
done

# TODO icon-themes/

mkdir -p %buildroot%_desktopdir
for n in writer impress calc base draw math qstart; do
	ln -sr %buildroot%lodir/share/xdg/$n.desktop %buildroot%_desktopdir/$n.desktop
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

%files integrated
%_bindir/*
%exclude %_bindir/libreoffice%version
%_desktopdir/*
%_iconsdir/*/*/mimetypes/*
%_iconsdir/*/*/apps/*
%exclude %_iconsdir/*/*/apps/libreoffice%{version}-*.*g

%files gnome -f files.gnome

%files kde4 -f files.kde4

%files extensions
%lodir/share/extensions/*
%exclude %lodir/share/extensions/package.txt

%files mimetypes
%_datadir/mime-info/*
%_datadir/mimelnk/application/*
%_datadir/application-registry/*

%langpack -l ru -n Russian
%langpack -l be -n Belorussian
%langpack -l de -n German
%langpack -l fr -n French
%langpack -l uk -n Ukrainian
%langpack -l pt-BR -n Brazilian Portuguese
%langpack -l es -n Espanian
%langpack -l kk -n Kazakh
%langpack -l tt -n Tatar

%changelog
* Thu Mar 10 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt2
- Update to 5.1.1.3
- Build without forky (turns out -XX:ParallelGCThreads=2 fixes OOM)

* Wed Feb 10 2016 Fr. Br. George <george@altlinux.ru> 5.1-alt1
- Update to 5.1.1.1
- Build with internal Python3

* Wed Nov 04 2015 Fr. Br. George <george@altlinux.ru> 5.0-alt2
- Update to 5.0.3.2

* Wed Sep 16 2015 Fr. Br. George <george@altlinux.ru> 5.0-alt1
- Update to 5.0.3.1
- Rename package
- Remove -standalone package

* Tue Feb 24 2015 Fr. Br. George <george@altlinux.ru> 4.4-alt2
- Update to 4.4.1.2

* Thu Feb 05 2015 Fr. Br. George <george@altlinux.ru> 4.4-alt1
- Update to 4.4.0.3
- Turn tt and be langpacks on

* Mon Dec 01 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt3
- Update to 4.3.5.1

* Wed Nov 19 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt2
- Update to 4.3.4.1

* Wed Nov 12 2014 Fr. Br. George <george@altlinux.ru> 4.3-alt1
- Update to 4.3.3.2
- Provide loffice binary (Closes: #30044)
- Reqiure gst-libav (Closes: #30015)

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

