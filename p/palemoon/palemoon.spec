Summary: The Pale Moon project browser
Summary(ru_RU.UTF-8): Интернет-браузер Pale Moon

Name: palemoon
Version: 26.0.0.0
Release: alt1
License: MPL/GPL/LGPL
Group: Networking/WWW
Url: https://github.com/MoonchildProductions/Pale-Moon
Epoch: 1

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

%define palemoon_cid                    \{8de7fcbb-c55c-4fbe-bfc5-fc555c87dbc4\}

%define palemoon_prefix                 %_libdir/%name
%define palemoon_datadir                %_datadir/%name
%define palemoon_arch_extensionsdir     %palemoon_prefix/extensions
%define palemoon_noarch_extensionsdir   %palemoon_datadir/extensions

Source: %name-source.tar
Source1: rpm-build.tar
Source2: searchplugins.tar
Source4: %name-mozconfig
Source6: %name.desktop
Source7: firefox.c
Source8: firefox-prefs.js

Patch5: firefox-duckduckgo.patch
Patch6: firefox3-alt-disable-werror.patch
#Patch14:	firefox-fix-install.patch
Patch16: firefox-cross-desktop.patch
#Patch17:	mozilla-disable-installer.patch
Patch18: mozilla_palimoon-bug-1153109-enable-stdcxx-compat.patch
Patch20: mozilla_palimoon-bug-1025605-GLIBCXX-26.0.0.patch
Patch21: cpp_check.patch


BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

# Automatically added by buildreq on Sun Jul 12 2015
# optimized out: alternatives fontconfig fontconfig-devel glib2-devel gstreamer-devel libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXrender-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgst-plugins libpango-devel libstdc++-devel libwayland-client libwayland-server libxml2-devel pkg-config python-base python-devel python-modules python-modules-compiler python-modules-curses python-modules-email python-modules-encodings python-modules-logging python-modules-multiprocessing xorg-kbproto-devel xorg-renderproto-devel xorg-scrnsaverproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: doxygen gcc-c++ glibc-devel-static gst-plugins-devel imake libXScrnSaver-devel libXt-devel libalsa-devel libgtk+2-devel python-modules-json unzip xorg-cf-files yasm zip

BuildRequires: autoconf_2.13
BuildRequires: libpixman-devel

%set_autoconf_version 2.13

# Protection against fraudulent DigiNotar certificates
Requires: libnss

%description
The %name project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер %name - кроссплатформенная модификация браузера Mozilla Firefox ,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n rpm-build-%name
Summary: RPM helper macros to rebuild %name packages
Group: Development/Other
BuildArch: noarch

Requires: mozilla-common-devel
Requires: rpm-build-mozilla.org

%description -n rpm-build-%name
These helper macros provide possibility to rebuild
%name packages by some Alt Linux Team Policy compatible way.

%prep
%setup -n %name-%version -c
%patch21 -p1
%patch20 -p1

cd %name

tar -xf %SOURCE1
pushd browser/locales/en-US/
tar -xf %SOURCE2
#pushd searchplugins
#> ./list.txt
#for fil in *.xml
#do
#    bn=`basename $fil .xml`
#    echo $bn >> ./list.txt
#done
#popd
popd


#patch5  -p1
%patch6  -p1
#patch14 -p1
%patch16 -p1
#patch17 -p1
%patch18 -p1

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


%ifnarch %ix86 x86_64 armh
echo "ac_add_options --disable-methodjit" >> .mozconfig
echo "ac_add_options --disable-monoic" >> .mozconfig
echo "ac_add_options --disable-polyic" >> .mozconfig
echo "ac_add_options --disable-tracejit" >> .mozconfig
%endif

%ifarch %ix86
#ac_add_options --disable-cairo
#echo 'ac_add_options --enable-optimize="-O3 -msse2 -mfpmath=sse"' >> .mozconfig
echo 'ac_add_options --enable-optimize=" -march=i586 -msse2 -mfpmath=sse"' >> .mozconfig
%endif

%build
cd %name

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
export LDFLAGS="-Wl,-rpath,%palemoon_prefix"
#make -f client.mk build STRIP="/bin/true" MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"

export PREFIX="%prefix"
export LIBDIR="%_libdir"
export LIBIDL_CONFIG=%_bindir/libIDL-config-2
export srcdir="$PWD"
export SHELL=/bin/sh

#__autoconf
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
	build

#	MOZ_APP_VERSION="" \

gcc %optflags \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DMOZ_PROGRAM=\"%palemoon_prefix/%name-bin\" \
	%SOURCE7 -o %name

%install
cd %name

echo %palemoon_prefix

mkdir -p \
	%buildroot/%mozilla_arch_extdir/%palemoon_cid \
	%buildroot/%mozilla_noarch_extdir/%palemoon_cid \
	#

#install -d %buildroot%palemoon_prefix

#install -d %buildroot%palemoon_prefix

pushd objdir
#install -d %buildroot%palemoon_prefix/bin
#cp -RfLp  dist/bin/* %buildroot%palemoon_prefix/bin
%makeinstall_std MOZ_APP_VERSION=
popd

rm  -f %buildroot/%_bindir/%name

install  %name  %buildroot/%_bindir/%name

#mv -f %buildroot%palemoon_prefix-%version %buildroot%palemoon_prefix

#cp  %buildroot/%palemoon_prefix/%name-bin  %buildroot%_bindir/%name

# install altlinux-specific configuration
install -D -m 644 %SOURCE8 %buildroot/%palemoon_prefix/browser/defaults/preferences/all-altlinux.js

cat > %buildroot/%palemoon_prefix/browser/defaults/preferences/%name-l10n.js <<EOF
pref("intl.locale.matchOS",		true);
pref("general.useragent.locale",	"chrome://global/locale/intl.properties");
EOF

# icons
for s in 16 22 24 32 48 256; do
	install -D -m 644 \
		browser/branding/official/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/%name.png
done

# install rpm-build-%name
mkdir -p -- \
	%buildroot/%_rpmmacrosdir
sed \
	-e 's,@palemoon_version@,%version,' \
	-e 's,@palemoon_release@,%release,' \
	rpm-build/rpm.macros.%name.standalone > %buildroot/%_rpmmacrosdir/%name

#install -m755 %name %buildroot/%_bindir/%name

cd %buildroot

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
	./%palemoon_prefix/removed-files

# Remove devel files
rm -rf -- \
	./%_includedir/%name-%version \
	./%_datadir/idl/%name-%version \
	./%_libdir/%name-devel-%version \

#

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

%files -n rpm-build-%name
%_rpmmacrosdir/%name

%changelog
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

