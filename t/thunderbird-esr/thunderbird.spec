%def_with	enigmail
%def_with	lightning
%define 	r_name thunderbird

Summary:	Thunderbird is Mozilla's e-mail client
Name:		%r_name-esr
Version:	38.5.0
Release:	alt1
License:	MPL/GPL
Group:		Networking/Mail
URL:		http://www.mozillamessaging.com

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	thunderbird-source.tar
Source1:	enigmail-source.tar
Source2:	rpm-build.tar
Source3:	thunderbird.desktop
Source4:	thunderbird-mozconfig
Source5:	thunderbird-default-prefs.js

Patch6:		01_locale.patch
Patch8:		thunderbird-timezoes.patch
Patch9:		thunderbird-install-paths.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: doxygen gcc-c++ imake libIDL-devel makedepend
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel
BuildRequires: libcurl-devel libgtk+2-devel libhunspell-devel libjpeg-devel
BuildRequires: xorg-cf-files chrpath alternatives yasm
BuildRequires: bzlib-devel zlib-devel
BuildRequires: mozldap-devel
BuildRequires: zip unzip
BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libGL-devel
BuildRequires: libwireless-devel
BuildRequires: libalsa-devel
BuildRequires: libnotify-devel
BuildRequires: libevent-devel
BuildRequires: libvpx-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libffi-devel
BuildRequires: libproxy-devel
BuildRequires: libopus-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel

# Python requires
BuildRequires: python-module-distribute
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3
BuildRequires: python-modules-json

# Mozilla requires
BuildRequires:	libnspr-devel
BuildRequires:	libnss-devel
BuildRequires:	libnss-devel-static

Provides:	mailclient
Obsoletes:	thunderbird-calendar
Obsoletes:	thunderbird-calendar-timezones

Conflicts:	thunderbird
Provides:	thunderbird-gnome-support = %version-%release
Obsoletes:	thunderbird-gnome-support

Requires:	hunspell-en
Requires:	browser-plugins-npapi

# Protection against fraudulent DigiNotar certificates
Requires:	libnss >= 3.13.1-alt1

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

%define tbird_cid                    \{3550f703-e582-4d05-9a08-453d09bdfdc6\}
%define tbird_prefix                 %_libdir/%r_name
%define tbird_datadir                %_datadir/%r_name
%define tbird_idldir                 %_datadir/idl/%r_name
%define tbird_includedir             %_includedir/%r_name
%define tbird_develdir               %tbird_prefix-devel

%description
Thunderbird is Mozilla's next generation e-mail client.
Thunderbird makes emailing safer, faster and easier than
ever before and can also scale to meet the most sophisticated
organizational needs.

%if_with enigmail
%package enigmail
%define engimail_version 1.7
%define enigmail_ciddir %mozilla_arch_extdir/%tbird_cid/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
Summary: Enigmail - GPG support for Mozilla Thunderbird
Group: Networking/Mail
Url: http://enigmail.mozdev.org/

Provides: %name-enigmail = %engimail_version
Requires: %name = %version-%release
Conflicts: %r_name-enigmail

Obsoletes: thunderbird-enigmail < 0.95.7-alt2

%description enigmail
Enigmail is an extension to the mail client of Mozilla / Netscape 7.x 
which allows users to access the authentication and encryption features 
provided by the popular GnuPG software.
%endif

%if_with lightning
%package lightning
%define lightning_ciddir %mozilla_arch_extdir/%tbird_cid/\{e2fda1a4-762b-4020-b5ad-a41df1933103\}
Summary: An integrated calendar for Thunderbird
Group: Office
Url: http://www.mozilla.org/projects/calendar/lightning/

Provides: %name-lightning = 1.9b1
Requires: %name = %version-%release
Conflicts: %r_name-lightning

%description lightning
An integrated calendar for Thunderbird.

%package google-calendar
%define google_calendar_ciddir %mozilla_noarch_extdir/%tbird_cid/\{a62ef8ec-5fdc-40c2-873c-223b8a6925cc\}
#Version: 0.8pre
Summary: Provider for Google Calendar
Group: Office
Url: http://www.mozilla.org/projects/calendar/lightning/

Requires: %name = %version-%release
Requires: %name-lightning = %version-%release
Conflicts: %r_name-google-calendar

Provides: gdata-provider = %version-%release

%description google-calendar
Allows bidirectional access to Google Calendar
%endif

%package devel
Summary:	Thunderbird development kit.
Group:		Development/C++
Requires:	%name = %version-%release
Conflicts:      %r_name-devel

Requires:	python-base
AutoReq:	yes, nopython

%description devel
Thunderbird development kit.

%package -n rpm-build-%name
Summary: 	RPM helper macros to rebuild thunderbird packages
Group:		Development/Other
BuildArch:	noarch

Requires:	mozilla-common-devel
Requires:	rpm-build-mozilla.org
Conflicts:      rpm-build-%r_name

%description -n rpm-build-%name
These helper macros provide possibility to rebuild
thunderbird packages by some Alt Linux Team Policy compatible way.

%prep
%setup -q -n %name-%version -c
cd mozilla

%if_with enigmail
tar -xf %SOURCE1
%endif

tar -xf %SOURCE2

%patch6 -p1
#patch8 -p2
%patch9 -p0

#echo %version > mail/config/version.txt

cp -f %SOURCE4 .mozconfig

%if_with lightning
echo 'ac_add_options --enable-calendar' >> .mozconfig
%endif

%ifnarch %{ix86} x86_64 armh
echo "ac_add_options --disable-methodjit" >> .mozconfig
echo "ac_add_options --disable-monoic"    >> .mozconfig
echo "ac_add_options --disable-polyic"    >> .mozconfig
echo "ac_add_options --disable-tracejit"  >> .mozconfig
%endif

sed -i -e '\,hyphenation/,d' mail/installer/removed-files.in

%build
cd mozilla

%add_optflags %optflags_shared
%add_findprov_lib_path %tbird_prefix

# Add fake RPATH
rpath="/$(printf %%s '%tbird_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2

export MOZ_BUILD_APP=mail

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

export PREFIX='%_prefix'
export LIBDIR='%_libdir'
export INCLUDEDIR='%_includedir'
export LIBIDL_CONFIG='/usr/bin/libIDL-config-2'
export srcdir="$PWD"
export SHELL=/bin/sh
export MOZILLA_OBJDIR="$PWD"

%__autoconf

MOZ_SMP_FLAGS=-j1
# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
%ifarch %ix86 x86_64 armh
[ "%__nprocs" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "%__nprocs" -ge 4 ] && MOZ_SMP_FLAGS=-j4
%endif

mkdir objdir mozilla/objdir

make -f client.mk \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
	mozappdir=%buildroot/%tbird_prefix \
	build

%if_with enigmail
dir="$PWD/objdir"

cd enigmail
	./configure
	make \
		STRIP="/bin/true" \
		MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"
	mkdir -p -- \
		$dir/mozilla/dist
	mv -f -- \
		build/dist \
		$dir/mozilla/dist/enigmail
cd -
%endif

%install
cd mozilla

mkdir -p \
	%buildroot/%_bindir \
	%buildroot/%mozilla_arch_extdir/%tbird_cid \
	%buildroot/%mozilla_noarch_extdir/%tbird_cid \
	%buildroot/%_datadir/applications \
	#

%makeinstall -C objdir \
	idldir=%buildroot/%tbird_idldir \
	includedir=%buildroot/%tbird_includedir \
	mozappdir=%buildroot/%tbird_prefix \
	#

#(set +x
#	for l in libldap60.so libldif60.so libprldap60.so; do
#		[ -f .%xulr_prefix/$l ] ||
#			continue
#		mv -f -- .%tbird_prefix/$l .%_libdir/$l
#		ln -vs -- "$(relative %_libdir/$l %tbird_prefix/$l)" .%tbird_prefix/$l
#	done
#)

(set +x
	for f in %buildroot/%tbird_develdir/*; do
		[ -L "$f" ] || continue

		t="$(readlink "$f")"
		r="$(relative "${t#%buildroot}" "${f#%buildroot}")"

		ln -vnsf -- "$r" "$f"
	done
)

(set +x
	rm -vrf -- %buildroot/%tbird_prefix/dictionaries/*
	for suf in aff dic; do
		t="$(relative %_datadir/myspell/en_US.$suf %tbird_prefix/dictionaries/)"
		ln -vs "$t" %buildroot/%tbird_prefix/dictionaries/en-US.$suf
	done
)

rm -rf -- \
	%buildroot/%_bindir/thunderbird \
	%buildroot/%tbird_prefix/js \
	%buildroot/%tbird_prefix/regxpcom \
	%buildroot/%tbird_prefix/xpcshell \
	%buildroot/%tbird_prefix/xpidl \
	%buildroot/%tbird_prefix/xpt_dump \
	%buildroot/%tbird_prefix/xpt_link \
	%buildroot/%tbird_prefix/nsinstall \
	%buildroot/%tbird_prefix/removed-files \
	%buildroot/%tbird_prefix/thunderbird \
	%buildroot/%tbird_prefix/run-mozilla.sh \
	%buildroot/%tbird_prefix/README.txt \
	#

#ver=%version
minver='24.0'
maxver='%xulr_version'
maxver="${maxver%%.*}.*"
sed -i \
	-e "s,^\\(MaxVersion\\)=.*,\\1=$maxver,g" \
	-e "s,^\\(MinVersion\\)=.*,\\1=$minver,g" \
	%buildroot/%tbird_prefix/application.ini

# desktop file
install -D -m 644 %SOURCE3 %buildroot/%_datadir/applications/thunderbird.desktop

# install altlinux-specific configuration
install -D -m 644 %SOURCE5 %buildroot/%tbird_prefix/defaults/pref/all-altlinux.js

# icons
for s in 16 22 24 32 48 256; do
	install -D -m 644 \
		other-licenses/branding/thunderbird/mailicon$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/thunderbird.png
done

# main startup script
cat>%buildroot/%_bindir/thunderbird<<-EOF
	#!/bin/sh -e
	export MOZ_APP_LAUNCHER="\${MOZ_APP_LAUNCHER:-\$0}"
	export MOZ_PLUGIN_PATH="%browser_plugins_path\${MOZ_PLUGIN_PATH:+:\$MOZ_PLUGIN_PATH}"
	export NSS_SSL_ENABLE_RENEGOTIATION=1
	%tbird_prefix/thunderbird-bin \${1:+"\$@"}
EOF
chmod 755 %buildroot/%_bindir/thunderbird

# rpm-build-thunderbird files
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d

cp -a rpm-build/rpm.macros %buildroot/%_sysconfdir/rpm/macros.d/%r_name

sed -i \
	-e 's,@tbird_version@,%version,' \
	-e 's,@tbird_release@,%release,' \
	%buildroot/%_sysconfdir/rpm/macros.d/%r_name

dir="$PWD/objdir"

%if_with enigmail
mkdir -p %buildroot/%enigmail_ciddir
unzip -q -u -d %buildroot/%enigmail_ciddir -- \
	enigmail/build/enigmail*.xpi
%endif

%if_with lightning
mkdir -p %buildroot/%lightning_ciddir
unzip -q -u -d %buildroot/%lightning_ciddir -- \
	$dir/dist/xpi-stage/lightning*.xpi

mkdir -p %buildroot/%google_calendar_ciddir
unzip -q -u -d %buildroot/%google_calendar_ciddir -- \
	$dir/dist/xpi-stage/gdata-provider*.xpi
%endif

# Add real RPATH
(set +x
	rpath="/$(printf %%s '%tbird_prefix' |tr '[:print:]' '_')"

	find \
		%buildroot/%tbird_prefix \
		%buildroot/%tbird_develdir \
		%buildroot/%mozilla_arch_extdir/%tbird_cid \
	-type f |
	while read f; do
		t="$(readlink -ev "$f")"

		file "$t" | fgrep -qs ELF || continue

		if chrpath -l "$t" | fgrep -qs "RPATH=$rpath"; then
			chrpath -r "%tbird_prefix" "$t"
		fi
	done
)


%files 
%_bindir/*
%tbird_prefix
%mozilla_arch_extdir/%tbird_cid
%mozilla_noarch_extdir/%tbird_cid
%defattr(0644,root,root,0755)
%_datadir/applications/%r_name.desktop
%_iconsdir/hicolor/16x16/apps/thunderbird.png
%_iconsdir/hicolor/22x22/apps/thunderbird.png
%_iconsdir/hicolor/24x24/apps/thunderbird.png
%_iconsdir/hicolor/32x32/apps/thunderbird.png
%_iconsdir/hicolor/48x48/apps/thunderbird.png
%_iconsdir/hicolor/256x256/apps/thunderbird.png

%if_with enigmail
%exclude %enigmail_ciddir
%endif
%if_with lightning
%exclude %lightning_ciddir
%exclude %google_calendar_ciddir
%endif

%if_with enigmail
%files enigmail
%enigmail_ciddir
%endif

%if_with lightning
%files lightning
%lightning_ciddir

%files google-calendar
%google_calendar_ciddir
%endif

%files devel
%tbird_idldir
%tbird_includedir
%tbird_develdir

%files -n rpm-build-%name
%_sysconfdir/rpm/macros.d/%r_name

%changelog
* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 38.5.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-149 Cross-site reading attack through data and view-source URIs
  + MFSA 2015-146 Integer overflow in MP4 playback in 64-bit versions
  + MFSA 2015-145 Underflow through code inspection
  + MFSA 2015-139 Integer overflow allocating extremely large textures

* Thu Nov 26 2015 Andrey Cherepanov <cas@altlinux.org> 38.4.0-alt1
- New ESR version

* Fri Oct 02 2015 Andrey Cherepanov <cas@altlinux.org> 38.3.0-alt2
- Use GStreamer 1.0

* Thu Oct 01 2015 Andrey Cherepanov <cas@altlinux.org> 38.3.0-alt1
- New ESR version

* Mon Aug 17 2015 Andrey Cherepanov <cas@altlinux.org> 38.2.0-alt1
- New ESR version

* Thu Jul 16 2015 Andrey Cherepanov <cas@altlinux.org> 38.1.0-alt1
- New ESR version
  + MFSA NSS incorrectly permits skipping of ServerKeyExchange
  + MFSA 2015-70 NSS accepts export-length DHE keys with regular DHE cipher suites
  + MFSA 2015-67 Key pinning is ignored when overridable errors are encountered
  + MFSA 2015-66 Vulnerabilities found through code inspection
  + MFSA 2015-63 Use-after-free in Content Policy due to microtask execution error

* Sat Jun 13 2015 Andrey Cherepanov <cas@altlinux.org> 38.0.1-alt1
- New ESR version

* Mon Jun 08 2015 Andrey Cherepanov <cas@altlinux.org> 31.7.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-57 Privilege escalation through IPC channel messages
  + MFSA 2015-54 Buffer overflow when parsing compressed XML
  + MFSA 2015-51 Use-after-free during text processing with vertical
    text enabled
  + MFSA 2015-48 Buffer overflow with SVG content and CSS
  + MFSA 2015-47 Buffer overflow parsing H.264 video with Linux
    Gstreamer
- Enigmail 1.8.2

* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 31.6.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-40 Same-origin bypass through anchor navigation
  + MFSA 2015-37 CORS requests should not follow 30x redirections after
    preflight
  + MFSA 2015-33 resource:// documents can load privileged pages
  + MFSA 2015-31 Use-after-free when using the Fluendo MP3 GStreamer
    plugin

* Wed Feb 25 2015 Andrey Cherepanov <cas@altlinux.org> 31.5.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-24 Reading of local files through manipulation of form
    autocomplete
  + MFSA 2015-19 Out-of-bounds read and write while rendering SVG
    content
  + MFSA 2015-16 Use-after-free in IndexedDB
  + MFSA 2015-12 Invoking Mozilla updater will load locally stored DLL
    files

* Sun Feb 08 2015 Andrey Cherepanov <cas@altlinux.org> 31.4.0-alt1
- Package ESR version as thunderbird-esr
