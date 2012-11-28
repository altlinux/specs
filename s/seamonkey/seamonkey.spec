%def_with	lightning

%define sm_prefix	%_libdir/%name
%define sm_datadir	%_datadir/%name
%define sm_version	%name-%version
%define sm_arch_extensionsdir	%sm_prefix/extensions
%define sm_noarch_extensionsdir	%sm_datadir/extensions
%define sm_cid			\{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a}
%define enigmail_ciddir		%sm_arch_extensionsdir/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
%define sm_idldir                 %_datadir/idl/%name
%define sm_includedir             %_includedir/%name
%define sm_develdir               %sm_prefix-devel

Name: seamonkey
Version: 2.14
Release: alt1
Serial: 1
Summary: Web browser and mail reader
License: MPL/NPL
Group: Networking/WWW
Packager: Radik Usupov <radik@altlinux.org>
Url: http://www.mozilla.org/projects/seamonkey/

Source0:	%name-source.tar
Source2:	mozilla-searchplugins.tar
Source3:	seamonkey-alt-browser.desktop
Source4:	seamonkey-alt-mail.desktop
Source5:	seamonkey-prefs.js
Source6:	enigmail.tar
Source7:	seamonkey-mozconfig
Source8:	rpm-build.tar

Patch:		thunderbird-install-paths.patch
Patch1:		seamonkey-2.2-alt-machOS-fix.patch
Patch2:		seamonkey-2.0.14-alt-fix-plugin-path.patch
Patch3:		xulrunner-noarch-extensions.patch
Patch4:		thunderbird-asm-directive.patch
Patch5:		thunderbird-with-system-mozldap.patch
Patch6:		seamonkey-2.13.2-alt-fix-build.patch

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

BuildRequires(pre): rpm-build-seamonkey
BuildRequires(pre): rpm-macros-alternatives
BuildRequires(pre): browser-plugins-npapi-devel

# Automatically added by buildreq on Sun Jul 16 2006
BuildPreReq: mozldap-devel
BuildRequires: gcc-c++ libdnet-devel libgtk+2-devel libIDL-devel wget libarchive lbzip2 libpixman-devel
BuildRequires: libjpeg-devel libpng-devel libXinerama-devel libXext-devel
BuildRequires: libXp-devel libXt-devel makedepend net-tools unzip libalsa-devel yasm libwireless-devel
BuildRequires: xorg-cf-files zip libXft-devel libvpx-devel
BuildRequires: desktop-file-utils libcurl-devel libhunspell-devel libsqlite3-devel
BuildRequires: autoconf_2.13 chrpath alternatives libGL-devel
BuildRequires: libstartup-notification-devel libfreetype-devel fontconfig-devel libnotify-devel
BuildRequires: libffi-devel libgio-devel

# Mozilla requires
BuildRequires:	libnspr-devel       >= 4.9.2-alt1
BuildRequires:	libnss-devel        >= 3.13.6-alt1
BuildRequires:	libnss-devel-static >= 3.13.6-alt1

# Python requires
BuildRequires: python-module-distribute
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3

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

%package devel
Summary:	Seamonkey development kit.
Group:		Development/C++
Requires: %name = %version-%release

Requires:	python-base
AutoReq:	yes, nopython

%description devel
Seamonkey development kit.

%package -n rpm-build-seamonkey
Summary: 	RPM helper macros to rebuild seamonkey packages
Group:		Development/Other
BuildArch:	noarch

Requires:	mozilla-common-devel
Requires:	rpm-build-mozilla.org

%description -n rpm-build-seamonkey
These helper macros provide possibility to rebuild
seamonkey packages by some Alt Linux Team Policy compatible way.

%prep
%setup -q -n %name-%version -c
cd mozilla

### Moved enigmail to mailnews
tar -xf %SOURCE6 -C mailnews/extensions/

%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1 -b .mozldap
%patch6 -p2

### Copying .mozconfig to build directory
cp -f %SOURCE7 .mozconfig

%if_with lightning
echo 'ac_add_options --enable-calendar' >> .mozconfig
%endif

%build
cd mozilla

%add_optflags %optflags_shared
%add_findprov_lib_path %sm_prefix

sed -i -e 's|AC_CONFIG_AUX_DIR(\${MOZILLA_SRCDIR}/build/autoconf)|AC_CONFIG_AUX_DIR(mozilla/build/autoconf)|' configure.in
autoconf

sed -i -e 's|AC_CONFIG_AUX_DIR(\${srcdir}/build/autoconf)|AC_CONFIG_AUX_DIR(build/autoconf)|' configure.in
ln -s "$PWD/configure" build/autoconf/configure
autoconf

# Add fake RPATH
rpath="/$(printf %%s '%sm_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2

export MOZ_BUILD_APP=suite

# -fpermissive is needed to build with gcc 4.6+ which has become stricter
#
# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo "%optflags -fpermissive" | \
sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"

%ifarch x86_64
export CFLAGS="$CFLAGS -DHAVE_USR_LIB64_DIR=1"
%endif

export PREFIX="%_prefix"
export LIBDIR="%_libdir"
export srcdir="$PWD"
export MOZILLA_SRCDIR="$srcdir/mozilla"

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

cd mailnews/extensions/enigmail
    ./makemake -r
cd -

dir="$PWD"

cd $dir/mailnews/extensions/enigmail
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
cd mozilla

dir="$PWD"

mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%sm_prefix/plugins \
	%buildroot/%sm_arch_extensionsdir \
	%buildroot/%sm_noarch_extensionsdir \
	%buildroot/%_datadir/applications \
	#

%makeinstall \
	idldir=%buildroot/%sm_idldir \
	includedir=%buildroot/%sm_includedir \
	mozappdir=%buildroot/%sm_prefix \
	#

ln -sf -- $(relative "%sm_noarch_extensionsdir" "%sm_prefix/") \
    %buildroot/%sm_prefix/extensions-noarch

(set +x
    for f in %buildroot/%sm_develdir/*; do
	[ -L "$f" ] || continue

	t="$(readlink "$f")"
	r="$(relative "${t#%buildroot}" "${f#%buildroot}")"

	ln -vnsf -- "$r" "$f"
    done
)

(set +x
    rm -vrf -- %buildroot/%sm_prefix/dictionaries/*
    for suf in aff dic; do
	t="$(relative %_datadir/myspell/en_US.$suf %sm_prefix/dictionaries/)"
	ln -vs "$t" %buildroot/%sm_prefix/dictionaries/en-US.$suf
    done
)

rm -rf -- \
	%buildroot/%_bindir/seamonkey \
	%buildroot/%sm_prefix/js \
	%buildroot/%sm_prefix/regxpcom \
	%buildroot/%sm_prefix/xpcshell \
	%buildroot/%sm_prefix/xpidl \
	%buildroot/%sm_prefix/xpt_dump \
	%buildroot/%sm_prefix/xpt_link \
	%buildroot/%sm_prefix/nsinstall \
	%buildroot/%sm_prefix/removed-files \
	%buildroot/%sm_prefix/seamonkey \
	%buildroot/%sm_prefix/run-mozilla.sh \
	%buildroot/%sm_prefix/README.txt \
	#

###From Enigmail
mkdir -p %buildroot/%enigmail_ciddir
unzip -q -u -d %buildroot/%enigmail_ciddir -- \
    $dir/mozilla/dist/xpi-stage/enigmail.xpi

###From Lightning
%if_with lightning
mkdir -p %buildroot/%lightning_ciddir
unzip -q -u -d %buildroot/%lightning_ciddir -- \
    $dir/mozilla/dist/xpi-stage/lightning.xpi

rm -f -- %buildroot/%lightning_ciddir/application.ini
%endif

# rpm-build-seamonkey files
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
tar -xf %SOURCE8
cp -a rpm-build/rpm.macros.seamonkey %buildroot/%_sysconfdir/rpm/macros.d/%name


# install altlinux-specific configuration
install -D -m 644 %SOURCE5 %buildroot/%sm_prefix/defaults/preferences/all-altlinux.js

# install icons
	install -D suite/branding/nightly/icons/gtk/default16.png \
	%buildroot%_miconsdir/%name.png
	install -D suite/branding/nightly/icons/gtk/default.png \
	%buildroot%_niconsdir/%name.png
	install -D suite/branding/nightly/icons/gtk/%name.png \
	%buildroot%_iconsdir/hicolor/128x128/apps/%name.png

# install search plugins
tar -C %buildroot%sm_prefix -xf %SOURCE2

# install browser menu file
install -D -m 644 %SOURCE3 %buildroot%_datadir/applications/seamonkey-alt-browser.desktop
# install mail menu file
install -D -m 644 %SOURCE4 %buildroot%_datadir/applications/seamonkey-alt-mail.desktop

# main startup script
cat>%buildroot/%_bindir/seamonkey<<-EOF
#!/bin/sh -e
    export MOZ_APP_LAUNCHER="\${MOZ_APP_LAUNCHER:-\$0}"
    export MOZ_PLUGIN_PATH="%browser_plugins_path\${MOZ_PLUGIN_PATH:+:\$MOZ_PLUGIN_PATH}"
    export NSS_SSL_ENABLE_RENEGOTIATION=1
    %sm_prefix/seamonkey-bin \${1:+"\$@"}
EOF


chmod 755 %buildroot/%_bindir/seamonkey

# Add alternatives
mkdir -p %buildroot%_altdir
printf '%_bindir/xbrowser\t%_bindir/%name\t100\n' > %buildroot%_altdir/%name

# Add real RPATH
(set +x
    rpath="/$(printf %%s '%sm_prefix' |tr '[:print:]' '_')"

    find \
	%buildroot/%sm_prefix \
	%buildroot/%sm_develdir \
	%buildroot/%sm_arch_extensionsdir \
    -type f |
    while read f; do
	t="$(readlink -ev "$f")"

	file "$t" | fgrep -qs ELF || continue

	if chrpath -l "$t" | fgrep -qs "RPATH=$rpath"; then
	chrpath -r "%sm_prefix" "$t"
	fi
    done
)

%files
%dir %sm_datadir
%_altdir/%name
%_bindir/%name
%_datadir/applications/*.desktop
%sm_prefix
%sm_noarch_extensionsdir
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

%files devel
%dir %sm_idldir
%sm_idldir
%sm_includedir
%sm_develdir

%files -n rpm-build-seamonkey
%_sysconfdir/rpm/macros.d/%name

%changelog
* Fri Nov 23 2012 Radik Usupov <radik@altlinux.org> 1:2.14-alt1
- New version seamonkey (2.14)
- New version enigmail (1.4.6)

* Wed Oct 31 2012 Radik Usupov <radik@altlinux.org> 1:2.13.2-alt1
- New version seamonkey (2.13.2) (Closes: 27764)

* Thu Oct 18 2012 Radik Usupov <radik@altlinux.org> 1:2.13.1-alt1
- New version seamonkey (2.13.1) (tnx legion@)
- New version enigmail (1.4.5)
- Build with rpm-build-seamonkey (external build macros)
- Added devel packages

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:2.8-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for seamonkey
  * postclean-03-private-rpm-macros for the spec file

* Sun Feb 19 2012 Radik Usupov <radik@altlinux.org> 1:2.8-alt1
- New version seamonkey (2.8)
- Fixed automatic install from specific locations (tnx legion@)
- New version enigmail (1.4)

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
