%def_without system_nss
#set_verify_elf_method relaxed
%define rname firefox

%define firefox_cid                    \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define firefox_prefix                 %_libdir/firefox
%define firefox_datadir                %_datadir/firefox
%define firefox_noarch_extensionsdir   %mozilla_noarch_extdir/%firefox_cid

Summary:              The Mozilla Firefox project is a redesign of Mozilla's browser
Summary(ru_RU.UTF-8): Интернет-браузер Mozilla Firefox

Name:           firefox-gost
Version:        38.8.0
Release:        alt1
License:        MPL/GPL/LGPL
Group:          Networking/WWW
URL:            http://www.mozilla.org/projects/firefox/

Packager:	Andrey Cherepanov <cas@altlinux.ru>

Source0:	firefox-source.tar
Source1:	rpm-build.tar
Source2:	searchplugins.tar
Source4:	firefox-mozconfig
Source6:	firefox.desktop
Source7:	firefox.c
Source8:	firefox-prefs.js
Source9:	ru.xpi

Patch5:		firefox-duckduckgo.patch
Patch6:		firefox3-alt-disable-werror.patch
Patch14:	firefox-fix-install.patch
Patch16:	firefox-cross-desktop.patch
#Patch17:	firefox-disable-installer.patch
Patch18:	mozilla-bug-1153109-enable-stdcxx-compat.patch
Patch19:	firefox-gost_patch38.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: rpm-macros-alternatives
BuildRequires: doxygen gcc-c++ imake libIDL-devel makedepend glibc-kernheaders
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libcurl-devel libgtk+2-devel libhunspell-devel libjpeg-devel
BuildRequires: xorg-cf-files chrpath alternatives yasm
BuildRequires: zip unzip
BuildRequires: bzlib-devel zlib-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libGL-devel
BuildRequires: libwireless-devel
BuildRequires: libalsa-devel
BuildRequires: libnotify-devel
BuildRequires: libevent-devel
BuildRequires: libproxy-devel
BuildRequires: libshell
BuildRequires: libvpx-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libffi-devel
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel
BuildRequires: libopus-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libicu-devel
BuildRequires: hunspell-ru

# Python requires
BuildRequires: python-module-distribute
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3
BuildRequires: python-modules-json

# Mozilla requires
BuildRequires: libnspr-devel       >= 4.10.10
%if_with system_nss
BuildRequires: libnss-devel        >= 3.22.0
BuildRequires: libnss-devel-static >= 3.22.0
%endif

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

Obsoletes:	firefox-3.6 firefox-4.0 firefox-5.0
Conflicts:	firefox-settings-desktop

Conflicts:	firefox
Conflicts:	firefox-esr
Conflicts:	firefox-ru
Conflicts:	firefox-esr-ru

Provides:	webclient
Requires:	mozilla-common
Requires:	gst-plugins-ugly1.0
Requires: 	hunspell-ru

Provides:	%name-ru = %version-%release
Obsoletes:	%name-ru < %version-%release

# Protection against fraudulent DigiNotar certificates
%if_with system_nss
Requires: libnss >= 3.12.11-alt3
%endif

%description
The Mozilla Firefox project is a redesign of Mozilla's browser component,
written using the XUL user interface language and designed to be
cross-platform.

This package supports GOST encryption by CryptoPro.
See https://www.cryptopro.ru/products/cpfox for details.

%description -l ru_RU.UTF8
Интернет-браузер Mozilla Firefox - кроссплатформенная модификация браузера Mozilla,
созданная с использованием языка XUL для описания интерфейса пользователя.

Этот пакет поддерживает шифрование по ГОСТ с помощью КриптоПро.
Подробости: https://www.cryptopro.ru/products/cpfox


%prep
%setup -q -n firefox-%version -c
cd mozilla

tar -xf %SOURCE1
tar -xf %SOURCE2

%patch5  -p1
%patch6  -p1
%patch14 -p1
%patch16 -p1
#patch17 -p1
%patch18 -p1
%patch19 -p1

#echo firefox_version > browser/config/version.txt

cp -f %SOURCE4 .mozconfig

%if_without system_nss
subst 's/with-system-nss/without-system-nss/' .mozconfig
%endif

%ifnarch %{ix86} x86_64 armh
echo "ac_add_options --disable-methodjit" >> .mozconfig
echo "ac_add_options --disable-monoic" >> .mozconfig
echo "ac_add_options --disable-polyic" >> .mozconfig
echo "ac_add_options --disable-tracejit" >> .mozconfig
%endif

%build
cd mozilla

%add_optflags %optflags_shared
%add_findprov_lib_path %firefox_prefix

export MOZ_BUILD_APP=browser

cat >> browser/confvars.sh <<EOF
MOZ_UPDATER=
MOZ_JAVAXPCOM=
MOZ_EXTENSIONS_DEFAULT=' gio'
MOZ_CHROME_FILE_FORMAT=jar
EOF

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | \
                sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"

# Add fake RPATH
rpath="/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"

export PREFIX="%_prefix"
export LIBDIR="%_libdir"
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2
export srcdir="$PWD"
export SHELL=/bin/sh

%__autoconf

# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
MOZ_SMP_FLAGS=-j1
%ifarch %{ix86} x86_64
[ "${NPROCS:+0}" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "${NPROCS:+0}" -ge 4 ] && MOZ_SMP_FLAGS=-j4
%endif

make -f client.mk \
	MAKENSISU= \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
	mozappdir=%buildroot/%firefox_prefix \
	build

%__cc %optflags \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DMOZ_PROGRAM=\"%firefox_prefix/firefox-bin\" \
	%SOURCE7 -o firefox


%install
cd mozilla

%__mkdir_p \
	%buildroot/%mozilla_arch_extdir/%firefox_cid \
	%buildroot/%mozilla_noarch_extdir/%firefox_cid \
	#

make -C objdir \
    DESTDIR=%buildroot \
    INSTALL="/bin/install -p" \
    mozappdir=%firefox_prefix \
    install

# install altlinux-specific configuration
install -D -m 644 %SOURCE8 %buildroot/%firefox_prefix/browser/defaults/preferences/all-altlinux.js

cat > %buildroot/%firefox_prefix/browser/defaults/preferences/firefox-l10n.js <<EOF
pref("intl.locale.matchOS",		true);
pref("general.useragent.locale",	"chrome://global/locale/intl.properties");
EOF

# icons
for s in 16 22 24 32 48 256; do
	install -D -m 644 \
		browser/branding/official/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/firefox.png
done

# install rpm-build-firefox
mkdir -p -- \
	%buildroot/%_rpmmacrosdir
sed \
	-e 's,@firefox_version@,%version,' \
	-e 's,@firefox_release@,%release,' \
	rpm-build/rpm.macros.firefox.standalone > %buildroot/%_rpmmacrosdir/firefox

install -m755 firefox %buildroot/%_bindir/firefox

cd %buildroot

#sed -i \
#	-e 's,\(MinVersion\)=.*,\1=5.0.1,g' \
#	-e 's,\(MaxVersion\)=.*,\1=5.0.1,g' \
#	./%firefox_prefix/application.ini

mv -f ./%firefox_prefix/application.ini ./%firefox_prefix/browser/application.ini

# install menu file
%__install -D -m 644 %SOURCE6 ./%_datadir/applications/firefox.desktop

# Add alternatives
mkdir -p ./%_altdir
printf '%_bindir/xbrowser\t%_bindir/firefox\t100\n' >./%_altdir/firefox

rm -f -- \
	./%firefox_prefix/firefox \
	./%firefox_prefix/removed-files

# Remove devel files
rm -rf -- \
	./%_includedir/%rname \
	./%_datadir/idl/%rname \
	./%_libdir/%rname-devel \
#

# Add real RPATH
(set +x
	rpath="/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"

	find \
		%buildroot/%firefox_prefix \
	-type f |
	while read f; do
		t="$(readlink -ev "$f")"

		file "$t" | fgrep -qs ELF || continue

		if chrpath -l "$t" | fgrep -qs "RPATH=$rpath"; then
			chrpath -r "%firefox_prefix" "$t"
		fi
	done
)

# Install Russian localization
mkdir -p %buildroot%firefox_noarch_extensionsdir \
         %buildroot%firefox_prefix/dictionaries
cp %SOURCE9 %buildroot%firefox_noarch_extensionsdir/langpack-ru@firefox.mozilla.org.xpi
ln -s %_datadir/myspell/ru_RU.dic %buildroot%firefox_prefix/dictionaries/ru.dic
ln -s %_datadir/myspell/ru_RU.aff %buildroot%firefox_prefix/dictionaries/ru.aff

%pre
for n in defaults browserconfig.properties; do
	[ ! -L "%firefox_prefix/$n" ] || rm -f "%firefox_prefix/$n"
done

%files
%_altdir/firefox
%_bindir/firefox
%firefox_prefix
%mozilla_arch_extdir/%firefox_cid
%mozilla_noarch_extdir/%firefox_cid
%_datadir/applications/firefox.desktop
%_iconsdir/hicolor/16x16/apps/firefox.png
%_iconsdir/hicolor/22x22/apps/firefox.png
%_iconsdir/hicolor/24x24/apps/firefox.png
%_iconsdir/hicolor/32x32/apps/firefox.png
%_iconsdir/hicolor/48x48/apps/firefox.png
%_iconsdir/hicolor/256x256/apps/firefox.png
%firefox_noarch_extensionsdir/langpack-*
%firefox_prefix/dictionaries/*

%changelog
* Tue Jun 14 2016 Andrey Cherepanov <cas@altlinux.org> 38.8.0-alt1
- New ESR version
- Package Russian localization (instead of separate firefox-gost-ru)

* Fri May 20 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.0-alt1
- New package with support GOST encryption [firefox-gost_patch38.patch]
- Build with bundled nss
