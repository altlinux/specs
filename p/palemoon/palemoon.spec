Summary: The New Moon browser, an unofficial branding of the Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon

Name: palemoon
Version: 27.1.2
Release: alt1.0
License: MPL/GPL/LGPL
Group: Networking/WWW
Url: https://github.com/MoonchildProductions/Pale-Moon
Epoch: 2

%define sname palemoon
%define bname newmoon

Packager: Hihin Ruslan <ruslandh@altlinux.ru>


%def_enable gst1   // Enable gstreamer 1.0


%define palemoon_cid                    \{8de7fcbb-c55c-4fbe-bfc5-fc555c87dbc4\}

%define palemoon_prefix                 %_datadir/%bname
%define palemoon_datadir                %_datadir/%bname
%define palemoon_bindir                 %_libdir/%bname
%define palemoon_arch_extensionsdir     %palemoon_prefix/extensions
%define palemoon_noarch_extensionsdir   %palemoon_datadir/extensions


Source: %sname-source-%version-%release.tar
Source1: rpm-build.tar

Source4: %sname-mozconfig
Source6: %bname.desktop
Source7: firefox.c
Source8: firefox-prefs.js
Source9: HISTORY_GIT
Source10: Changelog
Source11: content.tar

#Patch1: palemoon_google_add-26.4.0.patch

Patch5: firefox-duckduckgo.patch
Patch6: firefox3-alt-disable-werror.patch
#Patch14:	firefox-fix-install.patch
Patch16: firefox-cross-desktop.patch
#Patch17:	mozilla-disable-installer.patch
# Patch18: mozilla_palimoon-bug-1153109-enable-stdcxx-compat.patch
Patch20: mozilla_palimoon-bug-1025605-GLIBCXX-26.0.0.patch
Patch21: palemoon-build-el5-nss.patch
Patch22: palemoon_rpath-27.0.2.patch
#Patch22: palemoon_version-26.4.0.1.patch
Patch24: palemoon-27.0.2-ui_picker_false.patch
Patch23: palemoon_version-27.0.3.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): browser-plugins-npapi-devel

%set_autoconf_version 2.13
%set_gcc_version 4.9

BuildRequires: gcc%_gcc_version-c++


# Automatically added by buildreq on Fri Feb 10 2017
# optimized out: alternatives ca-certificates fontconfig fontconfig-devel glib2-devel gstreamer1.0-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins1.0 libpango-devel libstdc++-devel perl pkg-config python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-xml python3 xorg-kbproto-devel xorg-renderproto-devel xorg-scrnsaverproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: doxygen glibc-devel-static gst-plugins1.0-devel imake java-devel libGConf-devel libXScrnSaver-devel libXt-devel libalsa-devel libgtk+2-devel libpixman-devel 
BuildRequires: libpulseaudio-devel libsocket libvpx-devel 
BuildRequires: python-module-future python-module-yaml python-modules-json python-modules-wsgiref python3-base 
BuildRequires: unzip wget xorg-cf-files xsltproc yasm zip


# BEGIN SourceDeps(oneline):
#  BuildRequires: /usr/bin/widl at-spi2-atk-devel bzlib-devel fontconfig-devel glib2-devel gobject-introspection-devel libSM-devel libX11-devel libXext-devel
#  BuildRequires: libcairo-devel libdbus-devel libdbus-glib-devel libevent-devel libfreetype-devel libgio-devel libgnomeui-devel libgtk+3-devel libhunspell-devel 
#  BuildRequires: libjpeg-devel libpango-devel libpixman-devel libpng-devel libproxy-devel libqt4-devel libsqlite3-devel libstartup-notification-devel libwebp-devel 
#  BuildRequires: perl(Archive/Zip.pm) perl(CGI.pm) perl(Carp.pm) perl(English.pm) perl(Errno.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(FileHandle.pm) perl(FindBin.pm) 
#  BuildRequires: perl(IO/File.pm) perl(IO/Handle.pm) perl(LWP/Simple.pm) perl(List/Util.pm) perl(Time/Local.pm) perl(Time/localtime.pm) perl(XML/LibXML.pm) 
#  BuildRequires: perl(XML/LibXSLT.pm) perl(diagnostics.pm) perl(open.pm) perl(strict.pm) perl(subs.pm)
#  BuildRequires: qt4-mobility-devel qt5-base-devel qt5-declarative-devel qt5-location-devel swig texinfo
# END SourceDeps(oneline)


BuildPreReq: python3-base unzip xorg-cf-files libssl-devel

BuildPreReq: chrpath

BuildPreReq: autoconf_2.13  


BuildPreReq: gstreamer1.0-devel gst-plugins1.0-devel

%description
The %sname project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер %sname - кроссплатформенная модификация браузера Mozilla Firefox ,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n newmoon-base
Summary: The New Moon browser, an unofficial branding of the Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon
Group: Networking/WWW

Obsoletes: palemoon  <= 26.2.2
Provides: palemoon = %version-%release

Conflicts: newmoon < %epoch:%version-%release
Obsoletes: newmoon < %epoch:%version-%release
Provides: newmoon = %epoch:%version-%release

Requires: libgstreamer1.0 gst-libav
Requires: gst-plugins-base1.0
Requires: newmoon-data = %epoch:%version-%release

# Protection against fraudulent DigiNotar certificates
Requires: libnss

%description -n newmoon-base
The New Moon browser, an unofficial branding of the Pale Moon project browser
The %sname project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -n newmoon-base -l ru_RU.UTF8
Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon
Интернет-браузер %sname - кроссплатформенная модификация браузера Mozilla Firefox ,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n newmoon-data
Summary: The New Moon browser, an unofficial branding of the Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon
Group: Networking/WWW
BuildArch: noarch

#Provides: newmoon = %epoch:%version-%release
Conflicts: newmoon < %epoch:%version-%release
Obsoletes: newmoon <  %epoch:%version-%release



%description -n newmoon-data
The New Moon browser, an unofficial branding of the Pale Moon project browser
The %sname project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -n newmoon-data -l ru_RU.UTF8
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
# Add fake RPATH
#export LDFLAGS="-Wl,-rpath,%palemoon_prefix"
#export LD_LIBRARY_PATH="-Wl,-rpath,%palemoon_prefix"
rpath="/$(printf %%s '%palemoon_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"

# for  palemoon_rpath-27.0.2.patch
export RPATH_PATH="$rpath"     

%setup -n %sname-%version -c

%patch20 -p1
%patch24 -p1
#patch26 -p1
%patch23 -p1

%patch21 -p1
%patch22 -p1

cd %sname


tar -xf %SOURCE1

pushd browser/branding/unofficial
    tar --overwrite  -xf %SOURCE11
popd

#patch5  -p1
#patch14 -p1
#patch17 -p1

%patch6  -p1
%patch16 -p1

#patch18 -p1


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

%ifnarch %ix86 x86_64
echo "ac_add_options --disable-methodjit" >> .mozconfig
echo "ac_add_options --disable-monoic" >> .mozconfig
echo "ac_add_options --disable-polyic" >> .mozconfig
echo "ac_add_options --disable-tracejit" >> .mozconfig
%endif

echo "ac_add_options --disable-static" >> .mozconfig
echo "ac_add_options --enable-media-plugins --disable-elf-hack --enable-media-plugins --enable-media-navigator" >> .mozconfig
echo "ac_add_options --with-system-libvpx --enable-wave --enable-alsa --enable-pulseaudio" >> .mozconfig
echo "ac_add_options --enable-system-cairo" >> .mozconfig
# echo "ac_add_options --with-qtdir=%%_qt5_datadir"


# Add  Ofiicial Options:
#  --enable-shared-js --enable-jemalloc --enable-jemalloc-lib --with-pthreads --x-libraries=/usr/lib/X11
echo "ac_add_options --with-pthreads" >> .mozconfig
echo "ac_add_options --enable-shared-js"  >> .mozconfig
echo "ac_add_options --enable-jemalloc --enable-jemalloc-lib" >> .mozconfig
echo "ac_add_options --x-libraries=/usr/lib/X11" >> .mozconfig
# echo "ac_add_options --sharedstatedir=%_datadir" >> .mozconfig
# echo "ac_add_options --datadir=%_datadir" >> .mozconfig

# echo "ac_add_options --with-system-nss"  >> .mozconfig

echo "ac_add_options --with-nss-prefix=$RPATH_PATH" >> .mozconfig

# echo "ac_add_options --with-nss-prefix=%_libdir" >> .mozconfig

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
#export LDFLAGS="-Wl,-rpath,%palemoon_prefix"
#export LD_LIBRARY_PATH="-Wl,-rpath,%palemoon_prefix"
rpath="/$(printf %%s '%palemoon_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"

# for  palemoon_rpath-27.0.2.patch
export RPATH_PATH="$rpath"     

#make -f client.mk build STRIP="/bin/true" MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"


# for  palemoon_rpath-27.0.2.patch
export RPATH_PATH="$rpath"     

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
	-DMOZ_PROGRAM=\"%palemoon_bindir/%sname-bin\" \
	%SOURCE7 -o %sname

%install
#set_verify_elf_method unresolved=strict

cd %sname

mkdir -p \
	%buildroot/%mozilla_arch_extdir/%palemoon_cid \
	%buildroot/%mozilla_noarch_extdir/%palemoon_cid \
	#

pushd objdir
%makeinstall_std MOZ_APP_VERSION=
popd

# icons
for s in 16 32 48; do
	install -D -m 644 \
		browser/branding/unofficial/content/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/%bname.png
done


if [ -f %buildroot/%_bindir/%sname ];then
    rm  -f %buildroot/%_bindir/%sname
fi

install  %sname  %buildroot/%_bindir/%sname

#mv -f %buildroot%palemoon_prefix-%version %buildroot%palemoon_prefix

#cp  %buildroot/%palemoon_prefix/%name-bin  %buildroot%_bindir/%name


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


install -d  %buildroot%palemoon_bindir/components/
install -d  %buildroot%palemoon_bindir/browser/components/

install -m 644 %buildroot%palemoon_prefix/components/* %buildroot%palemoon_bindir/components/
install -m 644 %buildroot%palemoon_prefix/browser/components/* %buildroot%palemoon_bindir/browser/components/

rm -f %buildroot%palemoon_prefix/components/*
rmdir  %buildroot%palemoon_prefix/components/

rm -f %buildroot%palemoon_prefix/browser/components/*
rmdir %buildroot%palemoon_prefix/browser/components/


mv %buildroot/%palemoon_prefix/{palemoon,palemoon-bin,plugin-container,run-mozilla.sh} %buildroot%palemoon_bindir/
mv %buildroot/%palemoon_prefix/*.so* %buildroot%palemoon_bindir/
mv %buildroot/%palemoon_prefix/*.manifest %buildroot%palemoon_bindir/


ln -s %palemoon_prefix/{chrome,defaults,dictionaries,hyphenation,modules,res} %buildroot/%palemoon_bindir/
ln -s %palemoon_prefix/{dependentlibs.list,greprefs.js,libfreebl3.chk,libnssdbm3.chk,libsoftokn3.chk,platform.ini} %buildroot/%palemoon_bindir/
ln -s %palemoon_prefix/browser/{application.ini,blocklist.xml,chrome,chrome.manifest,defaults,extensions,icons,modules,searchplugins} %buildroot/%palemoon_bindir/browser/


rm -f -- \
	./%palemoon_prefix/%bname \
	./%palemoon_prefix/removed-files

# Add real RPATH
(set +x
	rpath="/$(printf %%s '%palemoon_bindir' |tr '[:print:]' '_')"

	find \
		%buildroot/%palemoon_bindir \
	-type f |
	while read f; do
		t="$(readlink -ev "$f")"

		file "$t" | fgrep -qs ELF || continue

		if chrpath -l "$t" | fgrep -qs "PATH=$rpath"; then
			chrpath -r "%palemoon_bindir" "$t"
		fi
	done
    )
popd

install -d %buildroot%palemoon_prefix/browser/chrome/icons/default/
install -m 644 browser/branding/unstable/content/icon48.png %buildroot%palemoon_prefix/browser/chrome/icons/default/PMaboutDialog48.png

# Add Docdir
install -D -m 644 %SOURCE9 ../
install -D -m 644 %SOURCE10 ../
install -D -m 644 AUTHORS ../
install -D -m 644 LICENSE ../


%pre
for n in defaults browserconfig.properties; do
	[ ! -L "%palemoon_prefix/$n" ] || rm -f "%palemoon_prefix/$n"
done

%files -n %bname-base
%doc AUTHORS LICENSE HISTORY_GIT Changelog
%_altdir/%bname
%_bindir/%sname
%dir %palemoon_bindir
%palemoon_bindir/*
%mozilla_arch_extdir/%palemoon_cid
%mozilla_noarch_extdir/%palemoon_cid

%files -n %bname-data
%dir %palemoon_prefix
%palemoon_prefix/*
%_desktopdir/%bname.desktop
%_miconsdir/%bname.png
%_niconsdir/%bname.png
%_liconsdir/%bname.png


%files -n rpm-build-%sname
%_rpmmacrosdir/%sname
%exclude %_includedir/*
%exclude %_datadir/idl/*

%changelog
* Sat Mar 04 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.2-alt1.0
- Version 27.1.2

* Thu Mar 02 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.1-alt3.1.git_869d77f
- update from git

* Thu Mar 02 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.1-alt3.0
- Rename from newmoon to newmoon-base

* Sat Feb 25 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.1-alt2.0
- Add norch package newmoon-data

* Fri Feb 24 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.1-alt1.2
- Correct searchplugins.tar

* Wed Feb 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.1-alt1.1
- Remove searchplugins.tar

* Wed Feb 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.1-alt1.0
- Version 27.1.1

* Fri Feb 10 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.0-alt3.0
- Built on gcc-4.9

* Thu Feb 09 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.0-alt3
- Correct BuildRequires

* Wed Feb 08 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.0-alt2
- Version 27.1.0

* Mon Feb 06 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.0-alt1.git_g1_76513
- Update from git

* Sun Jan 29 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.0-alt1.git_g0_76044
- Update from git

* Sat Jan 14 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.0-alt1.git_9bc65
- Update from git

* Sun Jan 01 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.0-alt0.git_c2e6
- Update from git

* Sat Dec 24 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.1.0-alt0.git_8392
- Update from git

* Sun Dec 18 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.0.3-alt1
- Version 27.0.3

* Mon Dec 05 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.0.2-alt4_git.1.6e62
- Update from git

* Sun Dec 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.0.2-alt3
- Add palemoon-build-el5-nss.patch

* Fri Dec 02 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.0.2-alt2
- Add patch`s 

* Wed Nov 30 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.0.2-alt1
- Version 27.0.2

* Tue Nov 29 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2:26.5.0-alt1_git.2.edd5
- Fix BuildRequires

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
