%def_with	lightning

%define sm_prefix	%_libdir/%name
%define sm_datadir	%_datadir/%name
%define sm_version	%name-%version
%define sm_arch_extensionsdir	%sm_prefix/extensions
%define sm_noarch_extensionsdir	%sm_datadir/extensions
%define enigmail_ciddir		%sm_arch_extensionsdir/\{847b3a00-7ab1-11d4-8f02-006008948af5\}

Name: seamonkey
Version: 2.8
Release: alt1
Serial: 1
Summary: Web browser and mail reader
License: MPL/NPL
Group: Networking/WWW
Packager: Radik Usupov <radik@altlinux.org>
Url: http://www.mozilla.org/projects/seamonkey/

Source0:	%name-%version.tar
Source2:	mozilla-searchplugins.tar
Source3:	seamonkey-alt-browser.desktop
Source4:	seamonkey-alt-mail.desktop

Patch:		thunderbird-install-paths.patch
Patch1:		seamonkey-2.2-alt-machOS-fix.patch
Patch2:		seamonkey-2.0.14-alt-fix-plugin-path.patch

PreReq:		urw-fonts

#Obsoletes
Obsoletes:	seamonkey-dom-inspector
Provides:	seamonkey-dom-inspector
Obsoletes:	seamonkey-enigmail
Provides:	seamonkey-enigmail
Obsoletes:	seamonkey-irc
Provides:	seamonkey-irc
Obsoletes:	seamonkey-js-debugger
Provides:	seamonkey-js-debugger
Obsoletes:	seamonkey-mail
Provides:	seamonkey-mail
Obsoletes:	seamonkey-plugins-common
Provides:	seamonkey-plugins-common
Obsoletes:	seamonkey-psm
Provides:	seamonkey-psm
Obsoletes:	seamonkey-spellchecker
Provides:	seamonkey-spellchecker
Obsoletes:	seamonkey-devel
Provides:	seamonkey-devel

BuildRequires(pre): rpm-build-seamonkey
BuildRequires(pre): rpm-macros-alternatives
BuildRequires(pre): browser-plugins-npapi-devel

# Automatically added by buildreq on Sun Jul 16 2006
BuildPreReq: mozldap-devel
BuildRequires: gcc-c++ libdnet-devel libgtk+2-devel libIDL-devel wget libarchive lbzip2 libpixman-devel
BuildRequires: libjpeg-devel libnspr-devel libpng-devel libXinerama-devel libXext-devel
BuildRequires: libXp-devel libXt-devel makedepend net-tools unzip libalsa-devel yasm libwireless-devel
BuildRequires: xorg-cf-files zip libnss-devel libnss-devel-static libXft-devel libvpx-devel
BuildRequires: desktop-file-utils libcurl-devel libhunspell-devel libsqlite3-devel
BuildRequires: autoconf_2.13 python-modules-logging chrpath alternatives libGL-devel
BuildRequires: libstartup-notification-devel libfreetype-devel fontconfig-devel libnotify-devel

%set_autoconf_version 2.13
%add_findprov_lib_path %sm_prefix

%description
SeaMonkey is an open-source web browser, designed for standards
compliance, performance and portability.

%if_with lightning
%package lightning
%define lightning_ciddir %sm_arch_extensionsdir/\{e2fda1a4-762b-4020-b5ad-a41df1933103\}
Summary: An integrated calendar for Seamonkey
Group: Office
Url: http://www.mozilla.org/projects/calendar/lightning/
Requires: %name = %version-%release

%description lightning
An integrated calendar for Seamonkey.
%endif

%prep
%setup

### Moved enigmail to mailnews
mv -f rpm/enigmail mailnews/extensions/enigmail

### Copying .mozconfig to build directory
cp -f rpm/seamonkey-mozconfig .mozconfig

%patch -p1
%patch1 -p1
%patch2 -p1

%if_with lightning
echo 'ac_add_options --enable-calendar' >> .mozconfig
%endif

%build
%add_optflags %optflags_shared
%add_findprov_lib_path %sm_prefix

sed -i -e 's|AC_CONFIG_AUX_DIR(\${MOZILLA_SRCDIR}/build/autoconf)|AC_CONFIG_AUX_DIR(mozilla/build/autoconf)|' configure.in
%__autoconf

cd mozilla
sed -i -e 's|AC_CONFIG_AUX_DIR(\${srcdir}/build/autoconf)|AC_CONFIG_AUX_DIR(build/autoconf)|' configure.in
ln -s "$PWD/configure" build/autoconf/configure
%__autoconf
cd -

cd mozilla/js/src
sed -i -e 's|AC_CONFIG_AUX_DIR(\${srcdir}/build/autoconf)|AC_CONFIG_AUX_DIR(build/autoconf)|' configure.in
ln -s "$PWD/configure" build/autoconf/configure
%__autoconf
cd -

# Add fake RPATH
export MOZ_BUILD_APP=suite
rpath_link=`pwd`/dist/lib
export PREFIX="%_prefix"
export LIBDIR="%_libdir"
export LDFLAGS="$LDFLAGS -Wl,-rpath,%sm_prefix -Wl,-rpath-link,$rpath_link"
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2
export MOZILLA_SRCDIR="$PWD"

%__autoconf

# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
%ifarch %ix86 x86_64
[ "%__nprocs" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "%__nprocs" -ge 4 ] && MOZ_SMP_FLAGS=-j4
%endif

%make_build -f client.mk build \
	mozappdir=%sm_prefix \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"

dir="$PWD"
cd mailnews/extensions/enigmail
    ./makemake -r
	%make_build
	%make_build xpi
	mv -f -- \
		$dir/mozilla/dist/bin/enigmail-*.xpi \
		$dir/mozilla/dist/xpi-stage/enigmail.xpi
	%make_build clean
cd -
# everybody lie ... 'make clean' lie!
(set +x
    for f in \
	components/enigprefs-service.js \
	components/enigMsgCompFields.js \
	components/enigmail.js \
	components/enigmail.xpt \
	components/ipc.xpt \
	components/enigmime.xpt \
	components/libipc.so \
	components/libenigmime.so \
	defaults/preferences/enigmail.js \
	defaults/pref/enigmail.js \
	chrome/enigmail.jar \
	chrome/enigmail-skin.jar \
	chrome/enigmail-en-US.jar \
	chrome/enigmime.jar \
	platform/*/components/libenigmime*.so \
	platform/*/components/libipc*.so \
	wrappers/gpg-wrapper.sh;
    do
	t="$dir/mozilla/dist/bin/$f"

	[ -L "$t" -o -f "$t" ] || continue

	rm -vf -- "$t"

	t="${t%%/*}"
	while [ "$t" != "$dir/mozilla/dist/bin" ]; do
	    rmdir -v -- "$t" ||:
	    t="${t%%/*}"
	done
    done
)

%install

%__mkdir_p \
	%buildroot/%sm_prefix/plugins \
	%buildroot/%sm_arch_extensionsdir \
	%buildroot/%sm_noarch_extensionsdir \
	#

%makeinstall_std STRIP=/bin/true \
	mozappdir=%buildroot%sm_prefix \
	#

###From Enigmail
%__mkdir_p %buildroot/%enigmail_ciddir
unzip -q -u -d %buildroot/%enigmail_ciddir -- \
    mozilla/dist/xpi-stage/enigmail.xpi

###From Lightning
%if_with lightning
mkdir -p %buildroot/%lightning_ciddir
unzip -q -u -d %buildroot/%lightning_ciddir -- \
    mozilla/dist/xpi-stage/lightning.xpi

rm -f -- %buildroot/%lightning_ciddir/application.ini
%endif

rm -rf -- \
	%buildroot%sm_prefix/js \
	%buildroot%sm_prefix/regxpcom \
	%buildroot%sm_prefix/xpcshell \
	%buildroot%sm_prefix/xpidl \
	%buildroot%sm_prefix/xpt_dump \
	%buildroot%sm_prefix/xpt_link \
	%buildroot%sm_prefix/nsinstall \
	#

# install icons
	%__install -D suite/branding/nightly/icons/gtk/default16.png \
	%buildroot%_miconsdir/%name.png
	%__install -D suite/branding/nightly/icons/gtk/default.png \
	%buildroot%_niconsdir/%name.png
	%__install -D suite/branding/nightly/icons/gtk/%name.png \
	%buildroot%_iconsdir/hicolor/128x128/apps/%name.png

# install search plugins
tar -C %buildroot%sm_prefix -xf %SOURCE2

# install browser menu file
%__install -D -m 644 %SOURCE3 %buildroot%_datadir/applications/seamonkey-alt-browser.desktop
# install mail menu file
%__install -D -m 644 %SOURCE4 %buildroot%_datadir/applications/seamonkey-alt-mail.desktop

# Add alternatives
%__mkdir_p %buildroot%_altdir
printf '%_bindir/xbrowser\t%_bindir/%name\t100\n' > %buildroot%_altdir/%name

# Fixed plugins path
sed -i -e 's,@PLUGIN_PATH@,%browser_plugins_path,g' %buildroot%sm_prefix/seamonkey

%files
%_altdir/%name
%_bindir/%name
%_datadir/applications/*.desktop
%sm_prefix
%_miconsdir/%name.png
%_niconsdir/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%if_with lightning
%exclude %lightning_ciddir
%endif

%if_with lightning
%files lightning
%lightning_ciddir
%endif

%changelog
* Sun Feb 19 2012 Radik Usupov <radik@altlinux.org> 1:2.8-alt1
- New version seamonkey (2.8b3)

* Thu Feb 09 2012 Radik Usupov <radik@altlinux.org> 1:2.7-alt1
- New version seamonkey (2.7)
- New version enigmail (1.3.5)
- Added seamonkey-lightning package

* Thu Feb 02 2012 Dmitry V. Levin <ldv@altlinux.org> 1:2.5-alt1.qa1
- Rebuilt with libvpx.so.1.

* Wed Nov 23 2011 Radik Usupov <radik@altlinux.org> 1:2.5-alt1
- New version seamonkey (2.5)
- New version enigmail (1.3.3)

* Fri Sep 30 2011 Radik Usupov <radik@altlinux.org> 1:2.4.1-alt1
- New version (2.4.1)

* Wed Sep 07 2011 Radik Usupov <radik@altlinux.org> 1:2.3.3-alt1
- New version (2.3.3)

* Thu Sep 01 2011 Radik Usupov <radik@altlinux.org> 1:2.3.2-alt1
- New version (2.3.2)

* Sun Aug 28 2011 Radik Usupov <radik@altlinux.org> 1:2.3.1-alt1
- New version (2.3.1)
- Provides: seamonkey-devel

* Wed Aug 17 2011 Radik Usupov <radik@altlinux.org> 1:2.3-alt1
- New version (2.3)

* Fri Jul 22 2011 Radik Usupov <radik@altlinux.org> 1:2.2-alt1
- New version (2.2)

* Thu Mar 17 2011 Radik Usupov <radik@altlinux.org> 1:2.0.14-alt1
- New version (2.0.14)
- Thanks legion@!
