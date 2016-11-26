Summary: The New Moon browser, an unofficial branding of the Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon

Name: palemoon
Version: 26.5.0
Release: alt1_git.1.edd5
License: MPL/GPL/LGPL
Group: Networking/WWW
Url: https://github.com/MoonchildProductions/Pale-Moon
Epoch: 2

%define sname palemoon
%define bname newmoon

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

# %%ifarch x86_64
# %%def_enable gst1   // Enable gstreamer 1.0
# %%else
# %%def_disable gst1   // Disable gstreamer 1.0
# %%endif

%def_enable gst1   // Enable gstreamer 1.0


%define palemoon_cid                    \{8de7fcbb-c55c-4fbe-bfc5-fc555c87dbc4\}

%define palemoon_prefix                 %_libdir/%bname
%define palemoon_datadir                %_datadir/%sname
%define palemoon_arch_extensionsdir     %palemoon_prefix/extensions
%define palemoon_noarch_extensionsdir   %palemoon_datadir/extensions


Source: %sname-source-%version-%release.tar
Source1: rpm-build.tar
Source2: searchplugins.tar
Source4: %sname-mozconfig
Source6: %bname.desktop
Source7: firefox.c
Source8: firefox-prefs.js
Source9: HISTORY_GIT
Source10: Changelog

#Patch1: palemoon_google_add-26.4.0.patch

Patch5: firefox-duckduckgo.patch
Patch6: firefox3-alt-disable-werror.patch
#Patch14:	firefox-fix-install.patch
Patch16: firefox-cross-desktop.patch
#Patch17:	mozilla-disable-installer.patch
Patch18: mozilla_palimoon-bug-1153109-enable-stdcxx-compat.patch
Patch20: mozilla_palimoon-bug-1025605-GLIBCXX-26.0.0.patch

Patch21: cpp_check.patch
Patch23: palemoon_version-26.4.0.1.patch
Patch25: palemoon-26.5.0-ui_picker_false.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): browser-plugins-npapi-devel

# Automatically added by buildreq on Sat Aug 13 2016
# optimized out: alternatives fontconfig fontconfig-devel glib2-devel gstreamer1.0-devel libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel libwayland-client libwayland-server perl pkg-config python-base python-devel python-module-PyStemmer python-module-cssselect python-module-ferari python-module-fiat python-module-instant python-module-mpmath python-module-numpy python-module-pyasn1 python-module-pyparsing python-module-ufl python-module-uflacs python-modules python-modules-compiler python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python3 xorg-kbproto-devel xorg-renderproto-devel xorg-scrnsaverproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: doxygen gcc-c++ imake java-devel libGConf-devel libXScrnSaver-devel libXt-devel libalsa-devel libgtk+2-devel libpulseaudio-devel libsocket libvpx-devel 
BuildRequires: python-module-cmd2 python-module-contextlib2 python-module-dns python-module-docutils python-module-ecdsa python-module-ed25519 python-module-ffc python-module-greenlet python-module-html5lib python-module-kerberos
BuildRequires: python-module-libcf python-module-mimeparse python-module-netaddr python-module-nss python-module-paste python-module-pbr python-module-polib python-module-psycopg2 python-module-pycrypto
BuildRequires: python-module-pycurl python-module-pyev python-module-pygobject3 python-module-pyinotify python-module-pysnmp4 python-module-pytz python-module-sidl python-module-sidlx python-module-snappy
BuildRequires: python-module-snowballstemmer python-module-wrapt python-module-yaml python-module-zope python-modules-wsgiref python3-base 
BuildRequires: unzip wget xorg-cf-files xsltproc yasm zip

BuildPreReq: bzlib-devel fontconfig-devel gcc-c++-common glib2-devel libSM-devel libX11-devel libXcomposite-devel libXext-devel libcairo-devel libdbus-devel libdbus-glib-devel libevent-devel libffi-devel libfreetype-devel
BuildPreReq: libgio-devel libgnomeui-devel libgraphite2-devel libgtk+3-devel libhunspell-devel libjpeg-devel libnspr libpango-devel libpixman-devel libpng-devel libproxy-devel libqt4-devel libreadline-devel
BuildPreReq: libsqlite3-devel libssl-devel libstartup-notification-devel libunwind-devel libwebp-devel libwine-devel
BuildPreReq: perl perl-Archive-Zip perl-CGI perl-DBI perl-GD perl-GD-Graph perl-HTTP-Message perl-XML-LibXML perl-XML-LibXSLT perl-devel perl-libwww python-base python-devel
BuildPreReq: qt4-mobility-devel qt5-base-devel texinfo wcslib-devel xsltproc zlib-devel gst-transcoder-devel

BuildPreReq: python3-base unzip xorg-cf-files

BuildPreReq: chrpath

BuildPreReq: autoconf_2.13

%set_autoconf_version 2.13

%if_enabled gst1
BuildPreReq: gstreamer1.0-devel gst-plugins1.0-devel
%else
BuildRequires(pre): gst-plugins-devel
BuildPreReq: gstreamer-devel gst-plugins-devel
%endif

%description
The %sname project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер %sname - кроссплатформенная модификация браузера Mozilla Firefox ,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n newmoon
Summary: The New Moon browser, an unofficial branding of the Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon
Group: Networking/WWW

Obsoletes: palemoon  <= 26.2.2
Provides: palemoon = %version-%release
Conflicts: palemoon

%if_enabled gst1
Requires: libgstreamer1.0 gst-libav
Requires: gst-plugins-base1.0
%else
Requires: libgstreamer gst-ffmpeg
Requires: gst-plugins-base gst-plugins-good
%endif
# Protection against fraudulent DigiNotar certificates
Requires: libnss

%description -n newmoon
The New Moon browser, an unofficial branding of the Pale Moon project browser
The %sname project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -n newmoon -l ru_RU.UTF8
Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon
Интернет-браузер %sname - кроссплатформенная модификация браузера Mozilla Firefox ,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n rpm-build-palemoon
Summary: RPM helper macros to rebuild %name packages
Group: Development/Other
BuildArch: noarch

Requires: mozilla-common-devel
Requires: rpm-build-mozilla.org

%description -n rpm-build-palemoon
These helper macros provide possibility to rebuild
%sname packages by some Alt Linux Team Policy compatible way.

%prep
%setup -n %sname-%version -c

%patch21 -p1
%patch20 -p1
%patch23 -p1
##patch25 -p1

cd %sname

#%%patch1  -p1
%patch6  -p1
%patch16 -p1
%patch18 -p1

tar -xf %SOURCE1

pushd browser/locales/en-US/
 tar -xf %SOURCE2
popd

#patch5  -p1
#patch14 -p1
#patch17 -p1



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

%ifnarch %ix86 x86_64
echo "ac_add_options --disable-methodjit" >> .mozconfig
echo "ac_add_options --disable-monoic" >> .mozconfig
echo "ac_add_options --disable-polyic" >> .mozconfig
echo "ac_add_options --disable-tracejit" >> .mozconfig
%endif

echo "ac_add_options --disable-static" >> .mozconfig
echo "ac_add_options --enable-media-plugins --disable-elf-hack --enable-media-plugins --enable-media-navigator" >> .mozconfig
echo "ac_add_options --with-system-libvpx --enable-wave --enable-alsa --enable-pulseaudio" >> .mozconfig


# Add  Ofiicial Options:
#  --enable-shared-js --enable-jemalloc --enable-jemalloc-lib --with-pthreads --x-libraries=/usr/lib/X11
echo "ac_add_options --with-pthreads" >> .mozconfig
echo "ac_add_options --enable-shared-js"  >> .mozconfig
echo "ac_add_options --enable-jemalloc --enable-jemalloc-lib" >> .mozconfig
echo "ac_add_options --x-libraries=/usr/lib/X11" >> .mozconfig

%ifarch %ix86
echo "ac_add_options --with-arch=i586" >> .mozconfig
echo 'ac_add_options --enable-optimize="-O2 -msse2 -mfpmath=sse" ' >> .mozconfig
%endif

echo "ac_add_options --enable-gstreamer" >> .mozconfig

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
export CXXFLAGS="$MOZ_OPT_FLAGS -D_GNUC_"

# Add fake RPATH
rpath="/$(printf %%s '%palemoon_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"
#export LDFLAGS="-Wl,-rpath,%palemoon_prefix"
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
	%SOURCE7 -o %sname

%install
cd %sname

mkdir -p \
	%buildroot/%mozilla_arch_extdir/%palemoon_cid \
	%buildroot/%mozilla_noarch_extdir/%palemoon_cid \
	#

pushd objdir

%makeinstall_std MOZ_APP_VERSION=
popd

if [ -f %buildroot/%_bindir/%sname ];then
    rm  -f %buildroot/%_bindir/%sname
fi

install  %sname  %buildroot/%_bindir/%sname

#mv -f %buildroot%palemoon_prefix-%version %buildroot%palemoon_prefix

#cp  %buildroot/%palemoon_prefix/%name-bin  %buildroot%_bindir/%name

# icons
for s in 16 32 48; do
	install -D -m 644 \
		browser/branding/unofficial/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/%bname.png
done

# install rpm-build-%sname
mkdir -p -- \
	%buildroot/%_rpmmacrosdir
sed \
	-e 's,@palemoon_version@,%version,' \
	-e 's,@palemoon_release@,%release,' \
	rpm-build/rpm.macros.%sname.standalone > %buildroot/%_rpmmacrosdir/%sname

pushd %buildroot

# Remove devel files
rm -rf -- \
	%buildroot%_includedir/%sname-%version \
	%buildroot%_datadir/idl/%sname-%version \
	%buildroot%_libdir/%sname-devel-%version \
	%buildroot%_libdir/%sname-devel- \

install -d %buildroot%palemoon_prefix
mv -f %buildroot/%_libdir/%sname/* %buildroot%palemoon_prefix

mv -f %buildroot%palemoon_prefix/application.ini %buildroot%palemoon_prefix/browser/application.ini

# install altlinux-specific configuration
install -D -m 644 %SOURCE8 %buildroot/%palemoon_prefix/browser/defaults/preferences/all-altlinux.js

cat > %buildroot/%palemoon_prefix/browser/defaults/preferences/%sname-l10n.js <<EOF
pref("intl.locale.matchOS",		true);
pref("general.useragent.locale",	"chrome://global/locale/intl.properties");
EOF

# install menu file
install -D -m 644 %SOURCE6 ./%_desktopdir/%bname.desktop

# Add alternatives
mkdir -p ./%_altdir
printf '%_bindir/xbrowser\t%_bindir/%bname\t100\n' >./%_altdir/%bname

rm -f -- \
	./%palemoon_prefix/%bname \
	./%palemoon_prefix/removed-files

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

# Add Docdir
install -D -m 644 %SOURCE9 ../
install -D -m 644 %SOURCE10 ../
install -D -m 644 AUTHORS ../
install -D -m 644 LICENSE ../

%pre
for n in defaults browserconfig.properties; do
	[ ! -L "%palemoon_prefix/$n" ] || rm -f "%palemoon_prefix/$n"
done

%files -n %bname
%doc AUTHORS LICENSE HISTORY_GIT Changelog
%_altdir/%bname
%_bindir/%sname
%dir %palemoon_prefix
%palemoon_prefix/*
%mozilla_arch_extdir/%palemoon_cid
%mozilla_noarch_extdir/%palemoon_cid
%_desktopdir/%bname.desktop
%_miconsdir/%bname.png
%_niconsdir/%bname.png
%_liconsdir/%bname.png

%files -n rpm-build-%sname
%_rpmmacrosdir/%sname
%exclude %_includedir/*
%exclude %_datadir/idl/*

%changelog
* Sat Nov 26 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.5.0-alt1_git.1.edd5
- Update from git

* Mon Oct 03 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.5.0-alt1
- Version 26.5.0 Release

* Mon Sep 12 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.1-alt1
- Version 26.4.1 Release

* Sun Sep 11 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0.1-alt1.007a
- Update from git

* Sun Sep 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0.1-alt1.ae71
- Update from git

* Sun Aug 28 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0.1-alt1
- Version 26.4.0.1 (2016-08-23) - Linux only

* Wed Aug 17 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0-alt2.1
- Update Changelog

* Wed Aug 17 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0-alt2.0
- Version 26.4.0 Release

* Sat Aug 13 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0-alt1.3.1841
- Update from git

* Sat Aug 06 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0-alt1.2.1fd9
- Fix Version

* Fri Aug 05 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0-alt0.2.1fd9
- Update from git

* Fri Aug 05 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0-alt0.2.1de4
- Update from git

* Mon Jul 18 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.4.0-alt0.1.d177
- Update from git

* Sat Jun 25 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.3.1-alt1
- Version 26.3.1 Release

* Thu Jun 16 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.3.0-alt2
- Version 26.3.0 Release

* Tue Jun 14 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.3.0-alt1.0.b333
- Update from git

* Sun May 08 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.2.2-alt1
- Version 26.2.2 Release

* Tue May 03 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.2.1-alt5.5c81
- add Docdir
- Correct Buildreq

* Sat Apr 30 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.2.1-alt4.5c81
- Update from git

* Mon Apr 11 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.2.1-alt2.0f44
- New Branding - New Moon

* Fri Apr 08 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.2.1-alt1.0f44
- Update from git

* Wed Apr 06 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.2.0-alt2
- Version 26.2 Release

* Sat Apr 02 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.2.0-alt1.RC3
- Version 26.2-RC3

* Thu Mar 31 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.2.0-alt1.RC2
- Version 26.2-RC2

* Tue Mar 29 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.1-alt5.d870
- Update from upstream/master git

* Wed Mar 23 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.1-alt4.46aa4
- Update from upstream/master git

* Wed Mar 16 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.1-alt3.ec88
- Version from https://github.com/trav90/Pale-Moon/tree/gstreamer1.x
- Add Buildreq

* Sun Mar 13 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.1-alt2.09e4
- Update from git

* Tue Mar 08 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.1-alt1.4e6e
- Update from git

* Thu Mar 03 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.1-alt1
- Version 26.1.1.

* Mon Feb 22 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.0-alt5
- Fix media.gstreamer.enabled
- Update from git

* Mon Feb 15 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.0-alt4
- Closes: Bug #31791

* Sun Feb 14 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.0-alt3
- Add option enable-gstreamer

* Sat Feb 13 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.0-alt2
- New Version

* Fri Feb 12 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.1.0-alt1.1.fc37
- Update from git
= Remove rpm-build-mozilla.org from deps

* Fri Feb 05 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.0.3-alt1.1.5e83
- Update from git

* Tue Feb 02 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:26.01-alt1.1
- Fix Build

* Mon Feb 01 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:26.01-alt1
- New Version

* Tue Jan 26 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:26.0r-alt1
- New Version

* Sat Jan 23 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:26.0b-alt1.1.dab2
- Update from git

* Sun Jan 10 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:26.0.0.0-alt1.1.c20fb
- Update from git

* Tue Dec 22 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1:26.0.0.0-alt1
- New Version

* Sun Dec 06 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1:26.0.0.0-alt0.b4
- New Version
- Removed support for palemoon-ru

* Tue Dec 01 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1:25.8.0.0-alt3
- Rollback to 25.8.0

* Mon Nov 30 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.8.1.0-alt1
- New Version
* Fri Nov 27 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.8.0.0-alt2
- add BuildRequires libpixman-devel
- add cpp_check.patch

* Sat Nov 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.8.0.0-alt1
- New Version

* Thu Oct 15 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.7.3.0-alt1
- New Version

* Sun Oct 11 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.7.2-alt2
- Fix searchplugins

* Mon Oct 05 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.7.2-alt1
- New Version

* Sat Aug 29 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.7.0.rel-alt1
- New Version

* Sun Jul 26 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0.rel-alt1.1
- Fix x86 version

* Sat Jul 25 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0.rel-alt1
- New version

* Sat Jul 18 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0b3-alt2
- Update from upstream

* Tue Jul 14 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0b3-alt1
- New Version

* Tue Jul 14 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0b2-alt0.2
- merge from p7

* Thu Jul 09 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0b2-alt0.1
- New Version

* Sun Jun 28 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.5.01-alt0.1
- initial build for ALT Linux Sisyphus
