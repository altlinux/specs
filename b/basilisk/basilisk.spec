Summary: The Basilisk web browser
Summary(ru_RU.UTF-8): Интернет-браузер Baselisk - неофициальная сборка браузера palemoon

Name: basilisk
Version:  52.9.0

Release: alt1

License: MPL-2.0 GPL-3.0 and LGPL-2.1+
Group: Networking/WWW

Url: https://repo.palemoon.org/Basilisk-Dev/Basilisk.git

ExclusiveArch: x86_64 aarch64

Packager: Hihin Ruslan <ruslandh@altlinux.ru>
Source:  %name-%version.tar
Source1: rpm-build.tar

Source4: %name-mozconfig
Source6: %name.desktop

Source7: firefox.c

Patch1:  mozilla-%name-52.9.0-bug-1153109-enable-stdcxx-compat.patch
Patch22: basilisk_rpath-52.9.0.patch

#Obsoletes: palemoon  < 29.4.6
Provides: palemoon
Provides: webclient

%define basilisk_cid                    \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

%define basilisk_datadir                %_datadir/%name
%define basilisk_bindir                 %_libdir/%name
%define basilisk_arch_extensionsdir     %_basilisk_datadir/extensions

%set_autoconf_version 2.13


BuildRequires: doxygen gcc-c++ libGConf-devel libXcomposite-devel libXdamage-devel libXt-devel libalsa-devel libdbus-glib-devel libgtk+2-devel
BuildRequires: libgtk+3-devel libhunspell-devel libpulseaudio-devel libsocket python-modules-distutils python-modules-json
BuildRequires: python-modules-wsgiref unzip yasm zip


# BEGIN SourceDeps(oneline):
BuildRequires: gobject-introspection-devel libssl-devel perl(Archive/Zip.pm) perl(CGI.pm) perl(LWP/Simple.pm)
BuildRequires: perl(XML/LibXML.pm) perl(XML/LibXSLT.pm) perl(diagnostics.pm) perl(fastcwd.pl) swig texinfo
# END SourceDeps(oneline)

BuildPreReq: %_bindir/python2.7 python2-base
BuildPreReq: libXcomposite-devel libXdamage-devel

%ifarch x86_64
BuildRequires: libcpuid-devel
%endif

# BEGIN SourceDeps(oneline):
BuildRequires: bzlib-devel gobject-introspection-devel libgtest-devel libpng-devel libssl-devel swig texinfo zlib-devel
# END SourceDeps(oneline)

BuildRequires(pre): mozilla-common-devel rpm-macros-alternatives mozilla-common
BuildRequires(pre): browser-plugins-npapi-devel

BuildPreReq: python-module-future python-modules-json python-modules-wsgiref

#BuildRequires: gcc%%{_gcc_version}-c++

BuildPreReq: chrpath
BuildPreReq: autoconf_%_autoconf_version

BuildRequires: libhunspell-devel

%description
The %name project is a redesign of Mozilla's  Firefox browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер %name - кроссплатформенная модификация браузера Mozilla Firefox ,
созданная с использованием языка XUL для описания интерфейса пользователя.




# Protection against fraudulent DigiNotar certificates
#Requires: libnss

%package -n rpm-build-basilisk
Summary: RPM helper macros to rebuild %name packages
Group: Development/Other
BuildArch: noarch

Requires: mozilla-common-devel
Requires: rpm-build-mozilla.org

%description -n rpm-build-basilisk
These helper macros provide possibility to rebuild
%name packages by some Alt Linux Team Policy compatible way.

%prep
%setup -n %name-%version -c
cp -f %SOURCE4 .mozconfig

%ifarch x86_64
echo 'ac_add_options --enable-optimize="-O3 -march=x86-64 -w -msse2 -mfpmath=sse"' >> .mozconfig
%endif

echo "mk_add_options MOZ_OBJDIR=obj-%_arch" >> .mozconfig

%patch1 -p1
%patch22 -p1

tar -xf %SOURCE1

%build
%add_optflags %optflags_shared

%add_findprov_lib_path %basilisk_datadir

export MOZ_BUILD_APP=%name

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
rpath="/$(printf %%s '%basilisk_bindir' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"

# for  basilisk_rpath-27.0.2.patch
export RPATH_PATH="$rpath"

echo '%basilisk_bindir'
echo "$rpath"

export PREFIX="%prefix"
export LIBDIR="%_libdir"
export LIBIDL_CONFIG=%_bindir/libIDL-config-2
export srcdir="$PWD"
export SHELL=/bin/sh


%__autoconf
MOZ_SMP_FLAGS=%_smp_mflags

TOPSRCDIR=$pwd

make -f client.mk \
 	MAKENSISU= \
 	STRIP="/bin/true" \
 	MOZ_APP_VERSION=%version \
 	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
	mozappdir=%buildroot%basilisk_bindir \
 	clobber

%make_build -f client.mk \
 	MAKENSISU= \
 	STRIP="/bin/true" \
 	MOZ_APP_VERSION=%version \
 	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
 	mozappdir=%buildroot%basilisk_bindir \
  	build


gcc %optflags \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DMOZ_PROGRAM=\"%basilisk_bindir/%name-bin\" \
	%SOURCE7 -o %name-bin

#./mach build

%install
cd obj-%_arch
%makeinstall MOZ_APP_VERSION=%version SHELL=/bin/sh  \

mv %buildroot%_libdir/basilisk-%version \
   %buildroot%_libdir/basilisk

#makeinstall_std MOZ_APP_VERSION=%version COMSPEC=rpm SHELL=/bin/sh
# MOZILLABUILD SHELL=/bin/sh COMSPEC=rpm

rm -f %buildroot%basilisk_bindir/%name
mkdir -p \
	%buildroot/%mozilla_arch_extdir/%basilisk_cid \
	%buildroot/%mozilla_noarch_extdir/%basilisk_cid
cd ..


# icons
for s in 16 32 48; do
	install -D -m 644 \
		%name/branding/unofficial/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/%name.png
done


if [ -f %buildroot/%_bindir/%name ];then
    rm  -f %buildroot/%_bindir/%name
fi

install  %name-bin  %buildroot/%_bindir/%name

mkdir -p -- \
	%buildroot/%_rpmmacrosdir

#sed \
#	-e 's,@basilisk_version@,%version,' \
#	-e 's,@basilisk_release@,%release,' \
#	 rpm-build/rpm.macros.%name.standalone > %buildroot/%_rpmmacrosdir/%name

install -D -m 644 rpm-build/rpm.macros.%name.standalone  %buildroot/%_rpmmacrosdir/%name

pushd %buildroot

# Remove devel files
rm -rf -- \
 	%buildroot%_libdir/basilisk-devel-%version \
 	%buildroot%_libdir/basilisk-devel \
 	%buildroot%_datadir/idl/%name-%version

# install menu file
install -D -m 644 %SOURCE6 ./%_desktopdir/%name.desktop
install -d -m 755 %buildroot/%basilisk_bindir/browser/defaults/preferences/

# cat > %buildroot/%basilisk_bindir/browser/defaults/preferences/%name-l10n.js <<EOF
# pref("intl.locale.matchOS",		true);
# pref("general.useragent.locale",	"chrome://global/locale/intl.properties");
# pref("extensions.getAddons.cache.enabled", false);
# EOF

# cat << EOF >> %buildroot%basilisk_bindir/defaults/pref/prefs.js
# user_pref("browser.EULA.override", true);
# user_pref("browser.ctrlTab.previews", true);
# user_pref("browser.tabs.insertRelatedAfterCurrent", false);
# user_pref("browser.tabs.onTop", true);
# user_pref("browser.startup.homepage", "file://%_docdir/HTML/index.html");
# user_pref("browser.backspace_action", 2);
# user_pref("browser.display.use_system_colors", true);
# user_pref("browser.download.folderList", 1);
# user_pref("browser.link.open_external", 3);
# user_pref("app.update.auto", false);
# user_pref("app.update.enabled", false);
# user_pref("app.update.autoInstallEnabled", false);
# user_pref("dom.ipc.plugins.enabled.nswrapper*", false);
# user_pref("extensions.autoDisableScopes", 0);
# user_pref("extensions.shownSelectionUI", true);
# user_pref("network.manage-offline-status", true);
# user_pref("browser.urlbar.decodeURLsOnCopy", true);
# EOF

echo %_builddir
ls -d %_builddir/%name-%version/%name/branding/*
ls -l %_builddir/%name-%version/%name/branding/unofficial/default48.png

install -m 644 %_builddir/%name-%version/%name/branding/unofficial/default48.png %buildroot%basilisk_bindir/browser/chrome/icons/default/PMaboutDialog48.png

set -x

# Add alternatives
mkdir -p ./%_altdir
printf '%_bindir/xbrowser\t%_bindir/%name\t98\n' >./%_altdir/%name

# Add real RPATH
(set -x
 	rpath="/$(printf %%s '%basilisk_bindir' |tr '[:print:]' '_')"

 	find \
 		%buildroot/%basilisk_bindir \
 	-type f |
 	while read f; do
 		t="$(readlink -ev "$f")"
 		echo $t
 		file "$t" | grep -Fqs ELF || continue
 		if chrpath -l "$t" | grep -Fqs "PATH=$rpath"; then
 			chrpath -r "%basilisk_bindir" "$t"
 			echo cmp Ok
 		else
 			echo cmp No
 			chrpath -l "$t"
 			echo PATH=$rpath
 			echo
 		fi
 	done
     )

install -d  %buildroot/%_docdir/%name-%version/
# Add Doc
install -D -m 644 %_builddir/basilisk-%version/AUTHORS %buildroot/%_docdir/%name-%version/
install -D -m 644 %_builddir/basilisk-%version/LICENSE %buildroot/%_docdir/%name-%version/
install -D -m 644 %_builddir/basilisk-%version/README.md %buildroot/%_docdir/%name-%version/

%files -n %name
%dir %basilisk_bindir
%basilisk_bindir/

%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%doc AUTHORS LICENSE README.md
%_altdir/%name
%_bindir/%name

%mozilla_arch_extdir/%basilisk_cid
%mozilla_noarch_extdir/%basilisk_cid

%files -n rpm-build-%name
%_rpmmacrosdir/%name
%exclude %_includedir/*

%changelog
* Thu Nov 23 2023 Hihin Ruslan <ruslandh@altlinux.ru> 52.9.0-alt1
- Init Build
