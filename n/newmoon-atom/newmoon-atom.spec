Summary: The Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер Pale Moon

Name: newmoon-atom
Version: 26.5.0
Release: alt1
License: MPL/GPL/LGPL
Group: Networking/WWW
Url: https://github.com/MoonchildProductions/Pale-Moon


Packager: Hihin Ruslan <ruslandh@altlinux.ru>

%define	sname palemoon
%define	bname newmoon

%define palemoon_cid                    \{8de7fcbb-c55c-4fbe-bfc5-fc555c87dbc4\}

%define palemoon_prefix                 %_libdir/%name
%define spalemoon_prefix		%_libdir/%sname
%define palemoon_datadir                %_datadir/%name
%define palemoon_arch_extensionsdir     %palemoon_prefix/extensions
%define palemoon_noarch_extensionsdir   %palemoon_datadir/extensions


Source: %name-source.tar
# Source1: rpm-build.tar
# Source2: searchplugins.tar
Source4: %sname-mozconfig
Source6: %bname.desktop
Source7: firefox.c
Source8: firefox-prefs.js
Source9: HISTORY_GIT
Source10: Changelog

Patch5: firefox-duckduckgo.patch
Patch6: firefox3-alt-disable-werror.patch
#Patch14:	firefox-fix-install.patch
Patch16: firefox-cross-desktop.patch
#Patch17:	mozilla-disable-installer.patch
Patch18: mozilla_palimoon-bug-1153109-enable-stdcxx-compat.patch
Patch20: mozilla_palimoon-bug-1025605-GLIBCXX-26.0.0.patch
Patch21: cpp_check.patch
Patch23: newmoon_atom_version-26.5.0.patch
Patch25: palemoon-26.5.0-ui_picker_false.patch

%set_gcc_version 4.9
%set_autoconf_version 2.13

# Automatically added by buildreq on Sat Aug 19 2017
# optimized out: alternatives fontconfig fontconfig-devel glib2-devel glibc-kernheaders-x86 gstreamer1.0-devel libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libXt-devel libatk-devel libcairo-devel libcloog-isl4 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins1.0 libpango-devel libstdc++-devel libwayland-client libwayland-server perl pkg-config python-base python-devel python-module-PyStemmer python-module-ferari python-module-fiat python-module-instant python-module-mpmath python-module-numpy python-module-pyasn1 python-module-ufl python-module-uflacs python-modules python-modules-compiler python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python3 xorg-kbproto-devel xorg-renderproto-devel xorg-scrnsaverproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: doxygen gcc-c++ glibc-kernheaders-generic gst-plugins1.0-devel imake java-devel libGConf-devel libXScrnSaver-devel libalsa-devel libgtk+2-devel libpulseaudio-devel libsocket libvpx-devel
BuildRequires: python-module-cmd2 python-module-contextlib2 python-module-cssselect python-module-dns python-module-docutils python-module-ecdsa python-module-ed25519 python-module-ffc python-module-greenlet
BuildRequires: python-module-kerberos python-module-libcf python-module-mimeparse python-module-nss python-module-paste python-module-pbr python-module-polib python-module-psycopg2
BuildRequires: python-module-pycrypto python-module-pycurl python-module-pyev python-module-pygobject3 python-module-pyinotify python-module-pysnmp4 python-module-pytz python-module-sidl
BuildRequires: python-module-sidlx python-module-snappy python-module-snowballstemmer python-module-wrapt python-module-yaml python-module-zope python-modules-wsgiref python3-base
BuildRequires: unzip wget xorg-cf-files xsltproc yasm zip

BuildRequires: gcc%_gcc_version-c++

ExclusiveArch: %ix86

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildPreReq: gstreamer1.0-devel gst-plugins1.0-devel

BuildPreReq: chrpath


BuildPreReq: autoconf_%_autoconf_version



BuildRequires: libpixman-devel


# Protection against fraudulent DigiNotar certificates
Requires: libnss

Provides: palemoon
Provides: webclient

%set_autoconf_version 2.13

BuildPreReq: python3-base unzip xorg-cf-files

BuildPreReq: chrpath

BuildPreReq: autoconf_2.13


%description
The %name project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер %name - кроссплатформенная модификация браузера Mozilla Firefox ,
созданная с использованием языка XUL для описания интерфейса пользователя.


%prep
%setup -n %name-%version -c
%patch21 -p1
%patch20 -p1

#tar -xf %%SOURCE1
cd %sname


pushd browser/locales/en-US/

popd

#%%patch1  -p1
%patch6  -p1
%patch16 -p1
%patch18 -p1
%patch23 -p1


cat >> browser/confvars.sh <<EOF
MOZ_UPDATER=
MOZ_JAVAXPCOM=
MOZ_EXTENSIONS_DEFAULT=' gio'
MOZ_CHROME_FILE_FORMAT=jar
EOF

echo %version > browser/config/version.txt

%__subst s~'$(MOZ_APP_NAME)-$(MOZ_APP_VERSION)'~'$(MOZ_APP_NAME)$(MOZ_APP_VERSION)'~g  ./config/baseconfig.mk
#subst s~'Moonchild Productions'~'Moonchild_Productions'~g  ./build/application.ini
#subst s~'Pale Moon'~'Pale_Moon'~g  ./build/application.ini

%__subst s~'"Moonchild Productions"'~'"Moonchild_Productions"'~g  ./build/application.ini
%__subst s~'"Pale Moon"'~'"Pale_Moon"'~g  ./build/application.ini

cp -f %SOURCE4 .mozconfig
echo "ac_add_options --enable-rpath"  >> .mozconfig


echo "ac_add_options --disable-methodjit" >> .mozconfig
echo "ac_add_options --disable-monoic" >> .mozconfig
echo "ac_add_options --disable-polyic" >> .mozconfig
echo "ac_add_options --disable-tracejit" >> .mozconfig

echo 'ac_add_options --enable-optimize=" -march=i586 -msse2 -mfpmath=sse"' >> .mozconfig

echo "ac_add_options --disable-static" >> .mozconfig
echo "ac_add_options --enable-media-plugins --disable-elf-hack --enable-media-plugins --enable-media-navigator" >> .mozconfig
echo "ac_add_options --with-system-libvpx --enable-wave --enable-alsa --enable-pulseaudio" >> .mozconfig


# Add  Ofiicial Options:
#  --enable-shared-js --enable-jemalloc --enable-jemalloc-lib --with-pthreads --x-libraries=/usr/lib/X11
echo "ac_add_options --with-pthreads" >> .mozconfig
echo "ac_add_options --enable-shared-js"  >> .mozconfig
echo "ac_add_options --enable-jemalloc --enable-jemalloc-lib" >> .mozconfig
echo "ac_add_options --x-libraries=/usr/lib/X11" >> .mozconfig

echo "ac_add_options --enable-gstreamer=1.0" >> .mozconfig

%build
cd %sname

%add_optflags %optflags_shared
%add_findprov_lib_path %palemoon_prefix
export MOZ_BUILD_APP=browser

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | \
                sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS -Wmaybe-uninitialized -Wreorder -D_GNUC_"

# Add fake RPATH
rpath="/$(printf %%s '%palemoon_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"
export LDFLAGS="-Wl,-rpath,%palemoon_prefix"

export RPATH_PATH="$rpath"     

#make -f client.mk build STRIP="/bin/true" MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"

export PREFIX="%prefix"
export LIBDIR="%_libdir"
export LIBIDL_CONFIG=%_bindir/libIDL-config-2
export srcdir="$PWD"
export SHELL=/bin/sh

%__autoconf
# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
MOZ_SMP_FLAGS=-j1
%ifarch %ix86 x86_64
[ "%__nprocs" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "%__nprocs" -ge 4 ] && MOZ_SMP_FLAGS=-j4
%endif

make -f client.mk \
	MAKENSISU= \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
	mozappdir=%buildroot/%palemoon_prefix \
	clobber

make -f client.mk \
	MAKENSISU= \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
	mozappdir=%buildroot/%palemoon_prefix \
	build


#	MOZ_APP_VERSION="" \

gcc %optflags \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DMOZ_PROGRAM=\"%palemoon_prefix/%sname-bin\" \
	%SOURCE7 -o %name

%install
cd %sname

echo %palemoon_prefix



mkdir -p \
	%buildroot/%mozilla_arch_extdir/%palemoon_cid \
	%buildroot/%mozilla_noarch_extdir/%palemoon_cid \
	#


pushd objdir
#install -d %buildroot%palemoon_prefix/bin
#cp -RfLp  dist/bin/* %buildroot%palemoon_prefix/bin
%makeinstall_std MOZ_APP_VERSION=
popd

mv -f %buildroot/%spalemoon_prefix/ %buildroot/%palemoon_prefix/


install  %name  %buildroot/%_bindir/%name

install -D -m 644 %SOURCE8 %buildroot/%palemoon_prefix/browser/defaults/preferences/all-altlinux.js

# icons
for s in 16 22 24 32 48 256; do
	install -D -m 644 \
		browser/branding/official/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/%name.png
done

# install rpm-build-%name
#mkdir -p -- \
#	%buildroot/%_rpmmacrosdir
#sed \
#	-e 's,@palemoon_version@,%version,' \
#	-e 's,@palemoon_release@,%release,' \
#	rpm-build/rpm.macros.%bname.standalone > %buildroot/%_rpmmacrosdir/%bname

#install -m755 %bname %buildroot/%_bindir/%bname

pwd

pushd %buildroot

# Remove devel files
rm -rf -- \
	%buildroot%_includedir/%sname-%version \
	%buildroot%_datadir/idl/%sname-%version \
	%buildroot%_libdir/%sname-devel-%version \
	%buildroot%_libdir/%sname-devel- \

#sed -i \
#	-e 's,\(MinVersion\)=.*,\1=5.0.1,g' \
#	-e 's,\(MaxVersion\)=.*,\1=5.0.1,g' \
#	./%palemoon_prefix/application.ini

mv -f %buildroot%palemoon_prefix/application.ini %buildroot%palemoon_prefix/browser/application.ini

# install menu file
install -D -m 644 %SOURCE6 ./%_desktopdir/%name.desktop

# Add alternatives
mkdir -p ./%_altdir
printf '%_bindir/xbrowser\t%_bindir/%name\t100\n' >./%_altdir/%name

rm -f -- \
	./%palemoon_prefix/%name \
	./%palemoon_prefix/removed-files \

# Add real RPATH
(set +x
	rpath="/$(printf %%s '%palemoon_prefix' |tr '[:print:]' '_')"

	find \
		%buildroot/%palemoon_prefix \
	-type f |
	while read f; do
		t="$(readlink -ev "$f")"

		file "$t" | fgrep -qs ELF || continue

		if chrpath -l "$t" | fgrep -qs "RPATH=$rpath"; then
			chrpath -r "%palemoon_prefix" "$t"
		fi
	done
)


popd

pwd

# Add Docdir
install -D -m 644 %SOURCE9 ./
install -D -m 644 %SOURCE10 ./
#install -D -m 644 AUTHORS ./
#install -D -m 644 LICENSE ./

if [ -x %buildroot/%_bindir/%bname ];then
    rm  -f %buildroot/%_bindir/%bname
fi

rm  -f %buildroot/%_bindir/%sname

%pre
for n in defaults browserconfig.properties; do
	[ ! -L "%palemoon_prefix/$n" ] || rm -f "%palemoon_prefix/$n"
done

%files
%_altdir/%name
%_bindir/%name
%dir %palemoon_prefix
%palemoon_prefix/*

%mozilla_arch_extdir/%palemoon_cid
%mozilla_noarch_extdir/%palemoon_cid

%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_iconsdir/hicolor/22x22/apps/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png

%exclude %_includedir/%sname/*
%exclude %_datadir/idl/%sname/*

%changelog
* Fri Aug 18 2017 Hihin Ruslan <ruslandh@altlinux.ru> 26.5.0-alt1
- Version 26.5.0-Atom

* Sat Jan 16 2016 Hihin Ruslan <ruslandh@altlinux.ru> 25.8.1-alt1
- Version palemon to Atom



