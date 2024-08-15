# git commit  1d5a6adf5f1e970041aad0b227cbc9f1cfe2ca72

Summary: The New Moon browser, an unofficial branding of the Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon

Name: palemoon
Version: 33.3.0

Release: alt1

License: MPL-2.0 GPL-3.0 and LGPL-2.1+
Group: Networking/WWW

Url: https://github.com/MoonchildProductions/Pale-Moon
Epoch: 2

ExclusiveArch: x86_64 aarch64
# ppc64le

%define sname palemoon
%define bname newmoon

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

%define palemoon_cid                    \{8de7fcbb-c55c-4fbe-bfc5-fc555c87dbc4\}

%define newmoon_prefix                  %_libdir/%bname
#define newmoon_datadir                 %%_datadir/%%sname
%define newmoon_datadir                 %_datadir/%bname
%define newmoon_bindir                  %_libdir/%bname
%define palemoon_arch_extensionsdir     %_newmoon_datadir/extensions
#define palemoon_noarch_extensionsdir   %%newmoon_datadir/extensions

Source: %sname-source-%version-%release.tar

Source1: rpm-build.tar
Source2: defaults-%bname.tar

Source4: %sname-mozconfig
Source6: %bname.desktop
Source7: firefox.c
#Source8: firefox-prefs.js
Source9: HISTORY_GIT
Source10: Changelog
Source11: content.tar

#Source12: xulstore.json
#Source13: kde.js

Patch10: palemoon-33.0.1-compatversion.patch

#Patch15: palemoon-32.0.1-ppc64le-alt1.patch


#Patch1: palemoon_google_add-26.4.0.patch
Patch16: mozilla_palimoon-29.4.6-cross-desctop.patch

Patch18: mozilla_palimoon-29.4.6-bug-1153109-enable-stdcxx-compat.patch

#Patch21: palemoon-build-el5-nss.patch

Patch22: palemoon_rpath-29.4.6.patch

Patch23: palemoon_version-33.0.1.patch
Patch24: palemoon-31.0.0-ui_picker_false.patch
#Patch25: palemoon-31.3.0.1-lock_impl_posix.patch

# Patch from Rosa
Patch103: palemoon-29.4.6-disable-check-default-browser.patch
Patch105: palemoon-29.4.6-default-mail-handler.patch
Patch106: palemoon-29.4.6-enable-addons.patch
#Patch107: palemoon-29.4.6-user-agent-overrides.patch

# Patches for KDE integration of New Moon
Patch111: palemoon-29.4.6-firefox-kde.patch
Patch112: palemoon-29.4.6-mozilla-kde.patch
Patch113: palemoon-29.4.6-kde-background.patch

Patch115: palemoon-32.4.0-mathops.patch
Patch116: palemoon-32.4.0-hunspell.patch
#Patch117: palemoon-32.5.1-locale.patch

Patch200: %bname-33.0.1-branding.patch

%set_autoconf_version 2.13

BuildPreReq: gstreamer1.0-devel gst-plugins1.0-devel libpixman-devel
BuildPreReq: python3-base unzip xorg-cf-files libsndfile-devel

# Automatically added by buildreq on Wed Mar 27 2024
# optimized out: alt-os-release alternatives fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcrypt-devel libctf-nobfd0 libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libpango-devel libstdc++-devel libxcb-devel perl pkg-config python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-distutils python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing python-modules-xml python2-base python3 python3-base python3-dev sh5 xorg-proto-devel zlib-devel
BuildRequires: doxygen gcc-c++ libGConf-devel libXt-devel libalsa-devel libdbus-glib-devel libgtk+2-devel
BuildRequires: libgtk+3-devel libhunspell-devel libpulseaudio-devel libsocket
BuildRequires: python-devel python-modules-json python-modules-wsgiref python3-module-setuptools
BuildRequires: unzip yasm zip


# BEGIN SourceDeps(oneline):
BuildRequires: gobject-introspection-devel libssl-devel perl(Archive/Zip.pm) perl(CGI.pm) perl(LWP/Simple.pm)
BuildRequires: perl(XML/LibXML.pm) perl(XML/LibXSLT.pm) perl(diagnostics.pm) perl(fastcwd.pl) swig texinfo
BuildRequires: bzlib-devel gobject-introspection-devel libgtest-devel libpng-devel libssl-devel swig texinfo zlib-devel
# END SourceDeps(oneline)

BuildPreReq: %_bindir/python2.7 python2-base
BuildPreReq: libXcomposite-devel libXdamage-devel

%ifarch x86_64
BuildRequires: libcpuid-devel
%endif

BuildRequires(pre): mozilla-common-devel rpm-macros-alternatives mozilla-common
BuildRequires(pre): browser-plugins-npapi-devel

BuildPreReq: python-module-future python-modules-json python-modules-wsgiref

BuildPreReq: alsa-plugins libx264-devel libsox-devel transfig alsa-oss alsa-tools alsa-utils libogg-devel liboggz-devel xorg-proto-devel
BuildPreReq: gstreamer-devel

# set_gcc_version 4.9
# BuildRequires: gcc%%{_gcc_version}-c++

BuildPreReq: chrpath
BuildPreReq: autoconf_%_autoconf_version

BuildRequires: libhunspell-devel
# BuildRequires: wayland-devel libwaylandpp-devel libwayland-egl-devel libEGL-devel
 
%description
The %sname project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер %sname - кроссплатформенная модификация браузера Mozilla Firefox ,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n %bname
Summary: The New Moon browser, an unofficial branding of the Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер New Moon - неофициальная сборка браузера Pale Moon
Group: Networking/WWW

Provides: palemoon = %EVR
Provides: webclient

Conflicts: %bname < 31.0.0

# Requires: gst-plugins-bad1.0 
# Requires: gst-plugins-good1.0 
# Requires: gst-plugins-ugly1.0 
# Requires: gst-plugins1.0-tools
# Requires: gstreamer1.0-utils 

# Requires: libgstreamer1.0 gst-libav
# Requires: gst-plugins-base1.0

# Protection against fraudulent DigiNotar certificates
# Requires: libnss

%description -n %bname
The New Moon browser, an unofficial branding of the Pale Moon project browser
The %sname project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -n %bname -l ru_RU.UTF8
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

#cd UXP-PM%{version}_Release
# patch to move files directly to /usr/lib No more symlinks
pushd platform
sed -e 's;$(libdir)/$(MOZ_APP_NAME)-$(MOZ_APP_VERSION);$(libdir)/$(MOZ_APP_NAME);g' -i config/baseconfig.mk
sed -e 's;$(libdir)/$(MOZ_APP_NAME)-devel-$(MOZ_APP_VERSION);$(libdir)/$(MOZ_APP_NAME)-devel;g' -i config/baseconfig.mk
popd

%setup -T -D -a 2
%setup -T -D -a 11

%patch10 -p1

%patch24 -p1
#patch25 -p1

#patch21 -p1

%patch16 -p1

%patch18 -p1

%patch22 -p1

tar -xf %SOURCE1

%patch23 -p1

#Pach from Rosa
##patch101 -p1 -b .lang
%patch103  -p1 -b .disable-software-update
%patch105  -p1 -b .default-mail-handler
%patch106 -p1 -b .addons
#patch107 -p1 -b .ua

# KDE integration
#patch111 -p1 -b .kdepatch
#patch112 -p1 -b .kdemoz
#patch113 -p1 -b .kdebackground

%patch115 -p1
%patch116 -p1
#patch117 -p1

#patch114 -p1

%patch200 -p1

cd %sname
# icons
for s in 16 22 24 32 48 256; do
	install -D -m 644 \
		../defaults-%bname/default$s.png \
		branding/unofficial/
done

cd -

cat >> confvars.sh <<EOF
MOZ_UPDATER=
MOZ_JAVAXPCOM=
MOZ_EXTENSIONS_DEFAULT=' gio'
MOZ_CHROME_FILE_FORMAT=jar
EOF

echo %version > config/version.txt

rpath="/$(printf %%s '%newmoon_bindir' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"

# for  palemoon_rpath-27.0.2.patch
export RPATH_PATH="$rpath"

# %__subst s~'$(MOZ_APP_NAME)-$(MOZ_APP_VERSION)'~'$(MOZ_APP_NAME)$(MOZ_APP_VERSION)'~g  ./platform/config/baseconfig.mk

%__subst s~'"Moonchild Productions"'~'"Moonchild_Productions"'~g  ./platform/build/application.ini
%__subst s~'"Pale Moon"'~'"Pale_Moon"'~g  ./platform/build/application.ini

cp -f %SOURCE4 .mozconfig

echo "mk_add_options MOZ_OBJDIR=obj-%_arch" >> .mozconfig

# echo "mk_add_options MOZ_MAKE_FLAGS=-j${NPROCS:-4}" >> .mozconfig
echo "mk_add_options MOZ_MAKE_FLAGS=%_smp_mflags" >> .mozconfig

echo "ac_add_options --disable-elf-hack" >> .mozconfig
echo "ac_add_options --enable-alsa" >> .mozconfig 
echo "ac_add_options --enable-pulseaudio" >> .mozconfig
echo "ac_add_options --enable-raw" >> .mozconfig
echo "ac_add_options --enable-ffmpeg" >> .mozconfig
echo "ac_add_options --enable-fmp4" >> .mozconfig

echo "ac_add_options --enable-system-hunspell" >> .mozconfig

echo "ac_add_options --x-libraries=%_libdir/X11" >> .mozconfig
echo "ac_add_options --with-nss-prefix=%_libdir/nss" >> .mozconfig

echo "ac_add_options  --with-system-jpeg" >> .mozconfig
echo "ac_add_options  --with-system-zlib" >> .mozconfig


# echo "ac_add_options  --enable-perf" >> .mozconfig
# echo "ac_add_options  --with-system-ffi" >> .mozconfig

%ifarch x86_64
 echo "ac_add_options --with-arch=x86-64" >> .mozconfig
 echo 'ac_add_options --enable-optimize=" -march=x86-64 -msse2 -mfpmath=sse"' >> .mozconfig
%endif



cat << EOF >> palemoon/app/profile/%sname.js
// -----------  Build Add   ------------------------
pref("browser.EULA.override", true);
pref("app.update.auto", false);
pref("app.update.enabled", false);
pref("app.update.autoInstallEnabled", false);
pref("browser.display.use_system_colors", true);
pref("browser.helperApps.deleteTempFileOnExit", false);
pref("browser.link.open_external", 3);
pref("browser.urlbar.decodeURLsOnCopy", true);
pref("extensions.autoDisableScopes", 3);
pref("ui.allow_platform_file_picker", "false");
pref("media.gstreamer.enabled", true);
user_pref("general.useragent.locale",	"chrome://global/locale/intl.properties");
user_pref("extensions.getAddons.cache.enabled", false);
user_pref("intl.locale.matchOS",  true);
user_pref("general.useragent.locale", "C");
EOF


%build
%add_optflags %optflags_shared

%add_findprov_lib_path %newmoon_prefix

export MOZ_BUILD_APP=%sname

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | \
                sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')

export CFLAGS="$MOZ_OPT_FLAGS"
#export CXXFLAGS="$MOZ_OPT_FLAGS -Wno-error=format-overflow -Wmaybe-uninitialized -Wreorder -fno-rtti -ffunction-sections -fdata-sections -D_GNUC_"
export CXXFLAGS="$MOZ_OPT_FLAGS -Wno-error=format-overflow -Wmaybe-uninitialized -Wreorder -D_GNUC_"

# Add fake RPATH
rpath="/$(printf %%s '%newmoon_bindir' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"

# for  palemoon_rpath-27.0.2.patch
export RPATH_PATH="$rpath"

echo '%newmoon_bindir'
echo "$rpath"

export PREFIX="%prefix"
export LIBDIR="%_libdir"
export LIBIDL_CONFIG=%_bindir/libIDL-config-2
export srcdir="$PWD"
export SHELL=/bin/sh

#./mach build

%__autoconf

MOZ_SMP_FLAGS=%_smp_mflags

TOPSRCDIR=$pwd

%make -f client.mk \
 	MAKENSISU= \
 	STRIP="/bin/true" \
 	MOZ_APP_VERSION=%version \
 	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
 	mozappdir=%buildroot%newmoon_bindir \
 	clobber

%make -f client.mk \
 	MAKENSISU= \
 	STRIP="/bin/true" \
 	MOZ_APP_VERSION=%version \
 	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
 	mozappdir=%buildroot%newmoon_bindir \
 	build

gcc %optflags \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DMOZ_PROGRAM=\"%newmoon_bindir/%bname-bin\" \
	%SOURCE7 -o %bname

%install
## ? install -D -m644 %%SOURCE12 obj-%_arch/dist/bin/browser/defaults/profile/xulstore.json
# нужен только с патчами KDE
#install -D -m644 %%SOURCE13 obj-%_arch/dist/bin/defaults/pref/kde.js

#cd palemoon
cd obj-%_arch
%makeinstall MOZ_APP_VERSION=%version SHELL=/bin/sh


#makeinstall_std MOZ_APP_VERSION=%version COMSPEC=rpm SHELL=/bin/sh
# MOZILLABUILD SHELL=/bin/sh COMSPEC=rpm

rm -f %buildroot%newmoon_bindir/%bname

mkdir -p \
	%buildroot/%mozilla_arch_extdir/%palemoon_cid \
	%buildroot/%mozilla_noarch_extdir/%palemoon_cid

# icons
for s in 16 32 48; do
	install -D -m 644 \
		../defaults-%bname/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/%bname.png
done

if [ -f %buildroot/%_bindir/%sname ];then
    rm  -f %buildroot/%_bindir/%sname
fi

cd ..

install  %bname  %buildroot/%_bindir/%bname

mkdir -p -- \
	%buildroot/%_rpmmacrosdir

sed \
	-e 's,@palemoon_version@,%version,' \
	-e 's,@palemoon_release@,%release,' \
	 rpm-build/rpm.macros.%sname.standalone > %buildroot/%_rpmmacrosdir/%sname

install -D -m 644 rpm-build/rpm.macros.%sname.standalone  %buildroot/%_rpmmacrosdir/%sname

pushd %buildroot

# Remove devel files
rm -rf -- \
 	%buildroot%_libdir/%bname-devel-%version \
 	%buildroot%_libdir/%bname-devel \
 	%buildroot%_datadir/idl/%bname-%version

# install menu file
install -D -m 644 %SOURCE6 ./%_desktopdir/%bname.desktop
install -d -m 755 %buildroot/%newmoon_bindir/browser/defaults/preferences/




install -m 644 %_builddir/palemoon-%version/defaults-%bname/default48.png %buildroot%newmoon_bindir/browser/chrome/icons/default/PMaboutDialog48.png

set -x

# Add alternatives
mkdir -p ./%_altdir
printf '%_bindir/xbrowser\t%_bindir/%bname\t99\n' >./%_altdir/%bname

# Add real RPATH
(set -x
 	rpath="/$(printf %%s '%newmoon_bindir' |tr '[:print:]' '_')"

 	find \
 		%buildroot/%newmoon_bindir \
 	-type f |
 	while read f; do
 		t="$(readlink -ev "$f")"
 		echo $t
 		file "$t" | grep -Fqs ELF || continue
 		if chrpath -l "$t" | grep -Fqs "PATH=$rpath"; then
 			chrpath -r "%newmoon_bindir" "$t"
 			echo cmp Ok
 		else
 			echo cmp No
 			chrpath -l "$t"
 			echo PATH=$rpath
 			echo
 		fi
 	done
     )




#install -d   %buildroot/%_docdir/%bname-%version/
# Add Doc
install -D -m 644 %SOURCE9  %_builddir/%sname-%version
install -D -m 644 %SOURCE10 %_builddir/%sname-%version
# install -D -m 644 %_builddir/palemoon-%version/AUTHORS %_builddir/%sname-%version
# install -D -m 644 %_builddir/palemoon-%version/LICENSE %_builddir/%sname-%version
# install -D -m 644 %_builddir/palemoon-%version/README.md %_builddir/%sname-%version

# cat > %buildroot/%newmoon_bindir/browser/defaults/preferences/%sname-l10n.js <<EOF
# pref("general.useragent.locale",	"chrome://global/locale/intl.properties");
# pref("extensions.getAddons.cache.enabled", false);
# pref("general.useragent.locale", "en-GB");
# EOF




%files -n %bname
%dir %newmoon_bindir
%newmoon_bindir/

%_desktopdir/%bname.desktop
%_miconsdir/%bname.png
%_niconsdir/%bname.png
%_liconsdir/%bname.png

%doc AUTHORS LICENSE HISTORY_GIT Changelog README.md
%_altdir/%bname
%_bindir/%bname

%mozilla_arch_extdir/%palemoon_cid
%mozilla_noarch_extdir/%palemoon_cid

%files -n rpm-build-%sname
%_rpmmacrosdir/%sname
%exclude %_includedir/*

%changelog
* Thu Aug 15 2024 Hihin Ruslan <ruslandh@altlinux.ru> 2:33.3.0-alt1
- New Version (CVE-2024-7531)

* Tue Jul 16 2024 Hihin Ruslan <ruslandh@altlinux.ru> 2:33.2.1-alt1
- New Version
(CVE-2024-6611, CVE-2024-6612, CVE-2024-5699, CVE-2024-5702 DiD, CVE-2024-5690, CVE-2024-5698 DiD, CVE-2024-5688 DiD, CVE-2024-5692, CVE-2024-4772 DiD, CVE-2024-4771, CVE-2024-4769,  CVE-2024-4770)

* Sun May 05 2024 Hihin Ruslan <ruslandh@altlinux.ru> 2:33.1.0-alt1
- New Version
(CVE-2024-3863, CVE-2024-3302, CVE-2024-3857 DiD, CVE-2024-3859 and CVE-2024-3861)

* Tue Mar 26 2024 Hihin Ruslan <ruslandh@altlinux.ru> 2:33.0.2-alt1
- New Version

* Sun Mar 24 2024 Hihin Ruslan <ruslandh@altlinux.ru> 2:33.0.1-alt2
- Changed patches

* Wed Mar 20 2024 Hihin Ruslan <ruslandh@altlinux.ru> 2:33.0.1-alt1
- Release 33.0.1
(CVE-2024-1551)

* Wed Jan 31 2024 Hihin Ruslan <ruslandh@altlinux.ru> 2:33.0.0-alt1
- Release 33.0.0
(CVE-2024-0746, CVE-2024-0741, CVE-2024-0743 DiD, CVE-2024-0750 DiD, and CVE-2024-0753)

* Sun Dec 31 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.5.2-alt1
- Update Version 
(CVE-2023-6863, CVE-2023-6858)

* Sat Dec 16 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.5.1-alt2.1
- Update spec and mozconfig

* Sun Dec 03 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.5.1-alt1
- Release 32.5.1
(CVE-2023-6204, CVE-2023-6210, CVE-2023-6209 and CVE-2023-6205)

* Wed Nov 22 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.5.0-alt3
- Add palemoon_version-32.5.0.patch and  palemoon-32.5.0-locale.patch

* Wed Nov 22 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.5.0-alt2.1
- Changed palemoon-mozconfig

* Mon Nov 20 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.5.0-alt2
- Release 32.5.0

* Thu Nov 16 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.5.0-alt1_1_git_30b19d3eb
- Version 32.5.0 (git commit 30b19d3eb)
(CVE-2023-5722, CVE-2023-5723, CVE-2023-5724, CVE-2023-5727)

* Wed Oct 18 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.4.1-alt1.1
- Update Changelog

* Mon Sep 18 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.4.1-alt1
- Version 32.4.1 (CVE 2023-4863)

* Tue Sep 05 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.4.0-alt1
- Version 32.4.0 (CVE-2023-37208)

* Sat Sep 02 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.4.0-alt0_1_rc1
- Version 32.4.0 RC1

* Sun Jun 04 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.2.0-alt1
- Version 32.2.0

* Sun Jun 04 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.1.2-alt1
- Add palemoon-32.0.1-ppc64le-alt.patch.
  Thanks to ximper@ for the patch ;-)

* Sat Apr 22 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.1.1-alt1
- Version 32.1.1 (CVE-2023-29545, CVE-2023-29539)

* Fri Mar 31 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.1.0-alt1
- Version 32.1.0 (CVE-2023-25751, CVE-2023-28163)

* Sat Mar 11 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.0.1-alt1
- Version 32.0.1  (CVE-2023-25733, CVE-2023-25739, CVE-2023-0767)

* Mon Jan 30 2023 Hihin Ruslan <ruslandh@altlinux.ru> 2:32.0.0-alt1
- Version 32.0.0

* Wed Dec 21 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.4.2-alt1
- Version 31.4.2

* Sun Dec 11 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.4.1.1-alt1
- Version 31.4.1.1

* Mon Nov 28 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.4.0-alt1
- Version 31.4.0

* Sat Oct 29 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.3.1-alt0_git1_89e277
- Version 31.3.1_RC1

* Tue Oct 25 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.3.0.1-alt2.2
- Build with gcc10

* Sun Oct 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.3.0.1-alt2
- Add palemoon-31.3.0.1-lock_impl_posix.patch

* Sun Oct 02 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.3.0.1-alt1
- Version 31.3.0.1

* Thu Sep 01 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.2.0.1-alt2
- Remove palemoon-l10n.js

* Fri Aug 12 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.2.0.1-alt1
- Version 31.2.0.1

* Thu Jul 21 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.1.1-alt3
- Fix rpm-build-palemoon

* Sat Jul 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.1.1-alt2
- Add BuildArch aarch64, ppc64le

* Wed Jul 13 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.1.1-alt1
- Version 31.1.1

* Wed Jul 13 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.1.1-alt0_1
- New Version (test buld)

* Mon May 30 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.0.0-alt0.5
- Add nemoon_branding-31.0.0.patch

* Fri May 27 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.0.0-alt0.4
- Beta build

* Fri May 13 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:31.0.0-alt0.1
- Version - Release 31.0.0

* Tue Apr 26 2022 Hihin Ruslan <ruslandh@altlinux.ru> 2:29.4.6-alt1
- Version - Release 29.4.6

* Mon Feb 11 2019 Hihin Ruslan <ruslandh@altlinux.ru> 2:28.3.1-alt1
- Version - Release 28.3.1

* Sat Apr 14 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.9.0-alt1
- New Version - Release 27.9.0

* Fri Mar 30 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.8.3-alt2
- New Version - Release 27.8.3

* Wed Mar 28 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.8.2-alt2
- New Version - Release 27.8.2

* Sun Mar 18 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.8.1-alt2
- Fix Changelog

* Sun Mar 11 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.8.1-alt1
- New Version - Release 27.8.1

* Mon Feb 05 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.7.2-alt1.2
- Fix Changelog

* Thu Feb 01 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.7.2-alt1.1
- Correct BuildPreReq

* Wed Jan 31 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.7.2-alt1
- New Version - Release 27.7.2

* Thu Jan 18 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.7.1-alt1
- New Version - Release 27.7.1

* Tue Jan 16 2018 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.7.0-alt1
- New Version - Release 27.7.0

* Sat Dec 02 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.6.2-alt1
- New Version - Release 27.6.2
- Fixed CVE-2017-7832, CVE-2017-7835, CVE-2017-7840. See Changelog 

* Mon Nov 20 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.6.1-alt1
- New Version - Release 27.6.1 width "fix Linux loading throbber to be properly encoded"

* Sat Oct 21 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.1-alt1
- New Version - Release 27.5.1

* Wed Sep 27 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt1.git_1_74d4e5e
- Update from github commit 74d4e5eac9d69983373a05f8c0aa3d47091d54b5

* Sat Sep 23 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt1
- New Version - Release 27.5.0

* Thu Sep 07 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt0.git_7_b2fca2a
- Update from github commit b2fca2a567fe2b824e2a90a8a522fc62c061d408

* Thu Sep 07 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt0.git_6_41fdbc8.1
- Rebuild with new Enviroment

* Sun Sep 03 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt0.git_6_41fdbc8
- Update from github commit 41fdbc840ff86cdba0240dbab72effbc8e124925

* Sun Aug 13 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt0.git_5_71cf8e6
- Update from github commit 71cf8e6633388614fe4c4a103d6b2f988ee6cd2e

* Sat Aug 05 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt0.git_4_d77a2a4
- Update from github commit d77a2a4c912b843ec320c8899cfc548a3c6bf01b

* Wed Aug 02 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt0.git_3_0505aac
- add  provides webclient ( Bug #33709 )

* Tue Aug 01 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt0.git_2_0505aac
- Update from github commit 0505aac66844b9579d1c1a53e00ba6147dfbdfd1

* Sun Jul 23 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.5.0-alt0.git_1_9a0d28e
- Update from github commit 9a0d28e130fb4d2fb48d5acfac2b80c3cea35ba7

* Sat Jul 15 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.4.0-alt2
- enable-system-sqlite

* Wed Jul 12 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.4.0-alt1
- New Version - Release 27.4.0

* Mon Jul 10 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.4.0-alt0.pre
- Pre Release 27.4.0
- add palemoon-27.4.0-blocklist.patch
- Update from github commit d2b9f74ba8fd962bb4ef8b0c6cc56bb75d784fdc

* Sat Jun 17 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.4.0-alt0.git_3_7556ee3
- Update from github commit 7556ee3e53e5ce9c14dfc7982068af6beb86da32

* Thu May 11 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.4.0-alt0.git_2_88954fe
- Update from github commit 88954fe39705269da876fc25f9d2470fae980ae8

* Mon May 01 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.4.0-alt0.git_1_e110eb1
- Update from github commit e110eb1756e5f417c036e3d25d3ffdbfb39951b7

* Sun Apr 30 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.3.0-alt2
- new Buildreq

* Sat Apr 29 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.3.0-alt1
- Version 27.3.0

* Sun Apr 23 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.3.0-alt0.git_f269589
- Update from github branch b27.3 commit f2695891c96250bfde630acdf2f5babe31c750f5

* Mon Apr 10 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.2.1-alt2.0
- Change %%palemoon_prefix, %%palemoon_bindir

* Sat Apr 08 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.2.1-alt1.1
- Add Rosa patch`s

* Sat Mar 25 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.2.1-alt1.0
- Version 27.2.1

* Sat Mar 18 2017 Hihin Ruslan <ruslandh@altlinux.ru> 2:27.2.0-alt1.0
- Version 27.2.0

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
