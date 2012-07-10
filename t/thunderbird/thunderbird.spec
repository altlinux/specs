%def_with	enigmail
%def_with	lightning

Summary:	Thunderbird is Mozilla's e-mail client
Name:		thunderbird
Version:	13.0.1
Release:	alt1
License:	MPL/GPL
Group:		Networking/Mail
URL:		http://www.mozillamessaging.com

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	thunderbird-source.tar
Source1:	enigmail-source.tar
Source2:	rpm-build.tar
Source3:	thunderbird.desktop
Source4:	thunderbird-mozconfig
Source5:	thunderbird-default-prefs.js

Patch1:		xulrunner-gio-protocol-handler.patch
#Patch2:	xulrunner-lighting-version.patch
Patch6:		01_locale.patch
Patch7:		xulrunner-noarch-extensions.patch
#Patch8:	thunderbird-asm-directive.patch
Patch9:		thunderbird-install-paths.patch
Patch10:	mozilla-check-libvpx.patch

# https://bugzilla.mozilla.org/show_bug.cgi?id=537089
Patch15:	thunderbird-with-system-mozldap.patch

# https://bugzilla.mozilla.org/show_bug.cgi?id=296453
#Patch16:	bug296453-fix-mfb-teardown-2.patch
#Patch17:	bug296453-folder-binding-bugfixes-2.patch
#Patch28:	thunderbird-use-mozsqlite.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: doxygen gcc-c++ imake libIDL-devel makedepend
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel
BuildRequires: libcurl-devel libgtk+2-devel libhunspell-devel libjpeg-devel
BuildRequires: xorg-cf-files chrpath alternatives yasm
BuildRequires: python-modules-compiler python-modules-logging
BuildRequires: bzlib-devel zlib-devel
BuildRequires: mozldap-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libGL-devel
BuildRequires: libwireless-devel
BuildRequires: libalsa-devel
BuildRequires: libnotify-devel
BuildRequires: libevent-devel
BuildRequires: zip unzip
BuildRequires: libvpx-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: libffi-devel

BuildRequires:	libnspr-devel       >= 4.9.0-alt1
BuildRequires:	libnss-devel        >= 3.13.4-alt1
BuildRequires:	libnss-devel-static >= 3.13.4-alt1
BuildRequires:	xulrunner-devel     >= 13.0.2-alt1

Provides:	mailclient
Obsoletes:	thunderbird-calendar

Provides:	thunderbird-gnome-support = %version-%release
Obsoletes:	thunderbird-gnome-support

Requires:	hunspell-en
Requires:	browser-plugins-npapi

# Protection against fraudulent DigiNotar certificates
Requires:	libnss >= 3.13.1-alt1

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

%define tbird_cid                    \{3550f703-e582-4d05-9a08-453d09bdfdc6\}
%define tbird_prefix                 %_libdir/%name
%define tbird_datadir                %_datadir/%name
%define tbird_idldir                 %_datadir/idl/%name
%define tbird_includedir             %_includedir/%name
%define tbird_develdir               %tbird_prefix-devel

%define tbird_arch_extensionsdir     %tbird_prefix/extensions
%define tbird_noarch_extensionsdir   %tbird_datadir/extensions

%description
Thunderbird is Mozilla's next generation e-mail client.
Thunderbird makes emailing safer, faster and easier than
ever before and can also scale to meet the most sophisticated
organizational needs.

%if_with enigmail
%package enigmail
%define enigmail_ciddir %mozilla_arch_extdir/%tbird_cid/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
Summary: Enigmail - GPG support for Mozilla Thunderbird
Group: Networking/Mail
Url: http://enigmail.mozdev.org/

Provides: %name-enigmail = 1.4.1
Requires: %name = %version-%release

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

Provides: %name-lightning = 1.3b1
Requires: %name = %version-%release

%description lightning
An integrated calendar for Thunderbird.

%package google-calendar
%define google_calendar_ciddir %mozilla_noarch_extdir/%tbird_cid/\{a62ef8ec-5fdc-40c2-873c-223b8a6925cc\}
#Version: 0.8pre
Summary: Provider for Google Calendar
Group: Office
Url: http://www.mozilla.org/projects/calendar/lightning/

Requires: %name = %version-%release
Requires: thunderbird-lightning

Provides: gdata-provider = %version-%release

%description google-calendar
Allows bidirectional access to Google Calendar

%package calendar-timezones
%define calendar_timezones_ciddir %mozilla_noarch_extdir/%tbird_cid/calendar-timezones@mozilla.org
#Version: 1.2011b
Summary: Timezone Definitions for Mozilla Calendar
Group: Office
Url: http://www.mozilla.org/projects/calendar/lightning/

Requires: %name = %version-%release

%description calendar-timezones
Timezone definitions required by Sunbird and Lightning
%endif

%package devel
Summary:	Thunderbird development kit.
Group:		Development/C++
Requires:	%name = %version-%release

Requires:	python-base
AutoReq:	yes, nopython

%description devel
Thunderbird development kit.

%package -n rpm-build-thunderbird
Summary: 	RPM helper macros to rebuild thunderbird packages
Group:		Development/Other
BuildArch:	noarch

Requires:	mozilla-common-devel
Requires:	rpm-build-mozilla.org

%description -n rpm-build-thunderbird
These helper macros provide possibility to rebuild
thunderbird packages by some Alt Linux Team Policy compatible way.

%prep
%setup -q -n %name-%version -c
cd mozilla

%if_with enigmail
tar -xf %SOURCE1 -C mailnews/extensions/
%endif

tar -xf %SOURCE2

#patch1 -p1
#patch2 -p2
%patch6 -p1
%patch7 -p1
#patch8 -p1
%patch9 -p1
%patch10 -p1 -b .fix10
%patch15 -p1 -b .mozldap
#patch16 -p1
#patch17 -p1

#echo %version > mail/config/version.txt

cp -f %SOURCE4 .mozconfig

%if_with lightning
echo 'ac_add_options --enable-calendar' >> .mozconfig
%endif

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

export PREFIX="%_prefix"
export LIBDIR="%_libdir"
export XULSDK="%xulr_develdir"
export srcdir="$PWD"
export MOZILLA_SRCDIR="$srcdir/mozilla"

%__autoconf

MOZ_SMP_FLAGS=-j1
# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
%ifarch %ix86 x86_64
[ "%__nprocs" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "%__nprocs" -ge 4 ] && MOZ_SMP_FLAGS=-j4
%endif

%make_build -f client.mk build \
	mozappdir=%tbird_prefix \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS"

%if_with enigmail
cd mailnews/extensions/enigmail
	./makemake -r
cd -

dir="$PWD/objdir"

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
%endif

%install
cd mozilla

dir="$PWD/objdir"

%__mkdir_p \
	%buildroot/%_bindir \
	%buildroot/%tbird_arch_extensionsdir \
	%buildroot/%tbird_noarch_extensionsdir \
	%buildroot/%mozilla_arch_extdir/%tbird_cid \
	%buildroot/%mozilla_noarch_extdir/%tbird_cid \
	%buildroot/%_datadir/applications \
	#

%makeinstall -C objdir \
	idldir=%buildroot/%tbird_idldir \
	includedir=%buildroot/%tbird_includedir \
	mozappdir=%buildroot/%tbird_prefix \
	#

ln -sf -- $(relative "%tbird_noarch_extensionsdir" "%tbird_prefix/") \
	%buildroot/%tbird_prefix/extensions-noarch

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

ver=%version
sed -i \
	-e "s,^\\(MaxVersion\\)=.*,\\1=${ver%%.*}.*,g" \
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

cp -a rpm-build/rpm.macros %buildroot/%_sysconfdir/rpm/macros.d/%name

sed -i \
	-e 's,@tbird_version@,%version,' \
	-e 's,@tbird_release@,%release,' \
	%buildroot/%_sysconfdir/rpm/macros.d/%name

%if_with enigmail
mkdir -p %buildroot/%enigmail_ciddir
unzip -q -u -d %buildroot/%enigmail_ciddir -- \
	$dir/mozilla/dist/xpi-stage/enigmail.xpi
%endif

%if_with lightning
mkdir -p %buildroot/%lightning_ciddir
unzip -q -u -d %buildroot/%lightning_ciddir -- \
	$dir/mozilla/dist/xpi-stage/lightning.xpi

mkdir -p %buildroot/%google_calendar_ciddir
unzip -q -u -d %buildroot/%google_calendar_ciddir -- \
	$dir/mozilla/dist/xpi-stage/gdata-provider.xpi

mkdir -p %buildroot/%calendar_timezones_ciddir
unzip -q -u -d %buildroot/%calendar_timezones_ciddir -- \
	$dir/mozilla/dist/xpi-stage/calendar-timezones.xpi

rm -rf -- %buildroot/%tbird_arch_extensionsdir/calendar-timezones@mozilla.org
rm -f -- %buildroot/%lightning_ciddir/application.ini
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
%tbird_arch_extensionsdir
%tbird_noarch_extensionsdir
%mozilla_arch_extdir/%tbird_cid
%mozilla_noarch_extdir/%tbird_cid
%defattr(0644,root,root,0755)
%_datadir/applications/%name.desktop
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
%exclude %calendar_timezones_ciddir
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

%files calendar-timezones
%calendar_timezones_ciddir
%endif

%files devel
%tbird_idldir
%tbird_includedir
%tbird_develdir

%files -n rpm-build-thunderbird
%_sysconfdir/rpm/macros.d/%name

%changelog
* Thu Jul 05 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New version (13.0.1).
- Fixed:
  + MFSA 2012-40 Buffer overflow and use-after-free issues found using Address Sanitizer
  + MFSA 2012-39 NSS parsing errors with zero length items
  + MFSA 2012-38 Use-after-free while replacing/inserting a node in a document
  + MFSA 2012-37 Information disclosure though Windows file shares and shortcut files
  + MFSA 2012-36 Content Security Policy inline-script bypass
  + MFSA 2012-35 Privilege escalation through Mozilla Updater and Windows Updater Service
  + MFSA 2012-34 Miscellaneous memory safety hazards

* Wed May 09 2012 Alexey Gladkov <legion@altlinux.ru> 12.0.1-alt1
- New version (12.0.1).
- Use internal libcairo.
- Fixed:
  + MFSA 2012-33 Potential site identity spoofing when loading RSS and Atom feeds
  + MFSA 2012-32 HTTP Redirections and remote content can be read by javascript errors
  + MFSA 2012-31 Off-by-one error in OpenType Sanitizer
  + MFSA 2012-30 Crash with WebGL content using textImage2D
  + MFSA 2012-29 Potential XSS through ISO-2022-KR/ISO-2022-CN decoding issues
  + MFSA 2012-28 Ambiguous IPv6 in Origin headers may bypass webserver access restrictions
  + MFSA 2012-27 Page load short-circuit can lead to XSS
  + MFSA 2012-26 WebGL.drawElements may read illegal video memory due to FindMaxUshortElement error
  + MFSA 2012-25 Potential memory corruption during font rendering using cairo-dwrite
  + MFSA 2012-24 Potential XSS via multibyte content processing errors
  + MFSA 2012-23 Invalid frees causes heap corruption in gfxImageSurface
  + MFSA 2012-22 use-after-free in IDBKeyRange
  + MFSA 2012-20 Miscellaneous memory safety hazards (rv:12.0/ rv:10.0.4)

* Fri Apr 20 2012 Alexey Gladkov <legion@altlinux.ru> 11.0.1-alt1
- New version (11.0.1).
- Fixed:
  + MFSA 2012-19 Miscellaneous memory safety hazards (rv:11.0/ rv:10.0.3 / rv:1.9.2.28)
  + MFSA 2012-18 window.fullScreen writeable by untrusted content
  + MFSA 2012-17 Crash when accessing keyframe cssText after dynamic modification
  + MFSA 2012-16 Escalation of privilege with Javascript: URL as home page
  + MFSA 2012-15 XSS with multiple Content Security Policy headers
  + MFSA 2012-14 SVG issues found with Address Sanitizer
  + MFSA 2012-13 XSS with Drag and Drop and Javascript: URL

* Thu Feb 23 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- New version (10.0.2).
- Fixed:
  + MFSA 2012-11 libpng integer overflow
  + MFSA 2012-10 use after free in nsXBLDocumentInfo::ReadPrototypeBindings
  + MFSA 2012-08 Crash with malformed embedded XSLT stylesheets
  + MFSA 2012-07 Potential Memory Corruption When Decoding Ogg Vorbis files
  + MFSA 2012-06 Uninitialized memory appended when encoding icon images may cause information disclosure
  + MFSA 2012-05 Frame scripts calling into untrusted objects bypass security checks
  + MFSA 2012-04 Child nodes from nsDOMAttribute still accessible after removal of nodes
  + MFSA 2012-03 <iframe> element exposed across domains via name attribute
  + MFSA 2012-01 Miscellaneous memory safety hazards (rv:10.0/ rv:1.9.2.26)
  + MFSA 2011-58 Crash scaling <video> to extreme sizes
  + MFSA 2011-57 Crash when plugin removes itself on Mac OS X
  + MFSA 2011-56 Key detection without JavaScript via SVG animation
  + MFSA 2011-55 nsSVGValue out-of-bounds access
  + MFSA 2011-54 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-53 Miscellaneous memory safety hazards (rv:9.0)

* Tue Jan 31 2012 Alexey Gladkov <legion@altlinux.ru> 8.0-alt2
- Rebuilt with libvpx.

* Tue Nov 15 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New version (8.0).
- Fixed:
  + MFSA 2011-52 Code execution via NoWaiverWrapper
  + MFSA 2011-51 Cross-origin image theft on Mac with integrated Intel GPU
  + MFSA 2011-50 Cross-origin data theft using canvas and Windows D2D
  + MFSA 2011-49 Memory corruption while profiling using Firebug
  + MFSA 2011-48 Miscellaneous memory safety hazards (rv:8.0)
  + MFSA 2011-47 Potential XSS against sites using Shift-JIS
  + MFSA 2011-44 Use after free reading OGG headers
  + MFSA 2011-42 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-40 Code installation through holding down Enter
  + MFSA 2011-39 Defense against multiple Location headers due to CRLF Injection
  + MFSA 2011-36 Miscellaneous memory safety hazards (rv:7.0 / rv:1.9.2.23)

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.1-alt1
- New version (6.0.1).
- Fixed:
  + MFSA 2011-34 Protection against fraudulent DigiNotar certificates

* Thu Aug 25 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New version (6.0).
- Add GIO support (ALT#11503).
- Fixed:
  + MFSA 2011-31 Security issues addressed in Thunderbird 6

* Thu Jul 21 2011 Alexey Gladkov <legion@altlinux.ru> 5.0-alt1
- New version (5.0).
- Remove gnome-support subpackage.

* Sat Apr 09 2011 Alexey Gladkov <legion@altlinux.ru> 3.1.9-alt1.20110409
- New snapshot (3.1.9 20110409).
- Use xdg-open (ALT#25403).

* Tue Mar 08 2011 Alexey Gladkov <legion@altlinux.ru> 3.1.9-alt1.20110308
- New version (3.1.9 20110308).
- Fixed:
  + MFSA 2011-09 Crash caused by corrupted JPEG image
  + MFSA 2011-08 ParanoidFragmentSink allows javascript: URLs in chrome documents
  + MFSA 2011-01 Miscellaneous memory safety hazards (rv:1.9.2.14/ 1.9.1.17)

* Sun Jan 23 2011 Alexey Gladkov <legion@altlinux.ru> 3.1.7-alt1.20110123
- New snapshot (3.1.7 20110123)
- Fix update request (ALT#23867)

* Sun Aug 15 2010 Alexey Gladkov <legion@altlinux.ru> 3.1.2-alt1.20100815
- New snapshot (3.1.2 20100810)
- Fixed:
  + MFSA 2010-47 Cross-origin data leakage from script filename in error messages
  + MFSA 2010-46 Cross-domain data theft using CSS
  + MFSA 2010-44 Characters mapped to U+FFFD in 8 bit encodings cause subsequent character to vanish
  + MFSA 2010-43 Same-origin bypass using canvas context
  + MFSA 2010-42 Cross-origin data disclosure via Web Workers and importScripts
  + MFSA 2010-41 Remote code execution using malformed PNG image
  + MFSA 2010-40 nsTreeSelection dangling pointer remote code execution vulnerability
  + MFSA 2010-39 nsCSSValue::Array index integer overflow
  + MFSA 2010-38 Arbitrary code execution using SJOW and fast native function
  + MFSA 2010-34 Miscellaneous memory safety hazards (rv:1.9.2.7/ 1.9.1.11)

* Tue Jun 29 2010 Alexey Gladkov <legion@altlinux.ru> 3.1.1-alt1.20100626
- New snapshot

* Mon Apr 05 2010 Alexey Gladkov <legion@altlinux.ru> 3.0.4-alt1.20100404
- New snapshot (3.0.4 20100404)
- Add gnome support.
- Fixed:
  + MFSA 2010-24 XMLDocument::load() doesn't check nsIContentPolicy
  + MFSA 2010-22 Update NSS to support TLS renegotiation indication
  + MFSA 2010-18 Dangling pointer vulnerability in nsTreeContentView
  + MFSA 2010-17 Remote code execution with use-after-free in nsTreeSelection
  + MFSA 2010-16 Crashes with evidence of memory corruption (rv:1.9.2.2/ 1.9.1.9/ 1.9.0.19)

* Thu Jan 28 2010 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt1.20100128
- New snapshot (3.0.1 20100128)

* Thu Nov 26 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20091126
- New snapshot (3.0 20091126)

* Sun Oct 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20091018
- New snapshot (3.0 20091018)

* Sun Oct 11 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20091010
- New snapshot (3.0 20091010)

* Tue Sep 29 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090929
- New snapshot (3.0 20090929)

* Tue Sep 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090917
- New snapshot (3.0 20090917)

* Mon Aug 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090817
- New snapshot (3.0 20090817)

* Wed Jul 29 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090729
- New snapshot (3.0 20090729)

* Mon Jun 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090601
- New snapshot (3.0 20090601)

* Sun Apr 26 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090424
- New snapshot (3.0 20090424)

* Thu Mar 12 2009 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20090312
- New snapshot (3.0 20090312)
- Use system mozsqlite3 (sqlite3 unsupported)

* Mon Nov 24 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.18-alt1
- New version (2.0.0.18)
- Fixed:
    + MFSA 2008-59 Script access to .documentURI and .textContent in mail
    + MFSA 2008-58 Parsing error in E4X default namespace
    + MFSA 2008-56 nsXMLHttpRequest::NotifyEventListeners() same-origin violation
    + MFSA 2008-55 Crash and remote code execution in nsFrameManager
    + MFSA 2008-52 Crashes with evidence of memory corruption (rv:1.9.0.4/1.8.1.18)
    + MFSA 2008-50 Crash and remote code execution via __proto__ tampering
    + MFSA 2008-48 Image stealing via canvas and HTTP redirect

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.17-alt1
- New version (2.0.0.17)
- Fixed:
    + MFSA 2008-46 Heap overflow when canceling newsgroup message
    + MFSA 2008-44 resource: traversal vulnerabilities
    + MFSA 2008-43 BOM characters stripped from JavaScript before execution
    + MFSA 2008-42 Crashes with evidence of memory corruption (rv:1.9.0.2/1.8.1.17)
    + MFSA 2008-41 Privilege escalation via XPCnativeWrapper pollution
    + MFSA 2008-38 nsXMLDocument::OnChannelRedirect() same-origin violation
    + MFSA 2008-37 UTF-8 URL stack buffer overflow
    + MFSA 2008-34 Remote code execution by overflowing CSS reference counter
    + MFSA 2008-33 Crash and remote code execution in block reflow
    + MFSA 2008-31 Peer-trusted certs can use alt names to spoof
    + MFSA 2008-29 Faulty .properties file results in uninitialized memory being used
    + MFSA 2008-26 Buffer length checks in MIME processing
    + MFSA 2008-25 Arbitrary code execution in mozIJSSubScriptLoader.loadSubScript()
    + MFSA 2008-24 Chrome script loading from fastload file
    + MFSA 2008-21 Crashes with evidence of memory corruption (rv:1.8.1.15)

* Thu Jul 17 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.14-alt2
- Bugfix build.
- Dont use LD_LIBRARY_PATH in startup scripts.

* Sun May 11 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.14-alt1
- New version (2.0.0.14)
- Fixed:
    + MFSA 2008-15 Crashes with evidence of memory corruption (rv:1.8.1.13)
    + MFSA 2008-14 JavaScript privilege escalation and arbitrary code execution

* Sun Mar 02 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0.12-alt1
- New version (2.0.0.12)
- Fixed:
    + MFSA 2008-12 Heap buffer overflow in external MIME bodies
    + MFSA 2008-05 Directory traversal via chrome: URI
    + MFSA 2008-03 Privilege escalation, XSS, Remote Code Execution
    + MFSA 2008-01 Crashes with evidence of memory corruption (rv:1.8.1.12)
    + MFSA 2007-36 URIs with invalid %-encoding mishandled by Windows
    + MFSA 2007-29 Crashes with evidence of memory corruption (rv:1.8.1.8)
    + MFSA 2007-27 Unescaped URIs passed to external programs
    + MFSA 2007-26 Privilege escalation through chrome-loaded about:blank windows

* Thu Aug 02 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.6-alt1
- New version (2.0.0.6)
- Fixed:
    + MFSA 2007-27 Unescaped URIs passed to external programs
    + MFSA 2007-26 Privilege escalation through chrome-loaded about:blank windows

* Fri Jul 20 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.5-alt1
- New version (2.0.0.5)
- Fixed:
    + MFSA 2007-23 Remote code execution by launching Firefox from Internet Explorer
    + MFSA 2007-18 Crashes with evidence of memory corruption

* Fri Jun 29 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.4-alt1
- New version (2.0.0.4)
- Fix normal icons.
- Fixed:
    + MFSA 2007-15 Security Vulnerability in APOP Authentication
    + MFSA 2007-12 Crashes with evidence of memory corruption (rv:1.8.0.12/1.8.1.4)

* Sun Apr 22 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.0-alt1
- New version (2.0.0.0)
- Many bugfixes (see http://weblogs.mozillazine.org/rumblingedge/archives/2007/03/tb_2.html).
- Add RSS files (again).

* Tue Feb 27 2007 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1.b2
- New version (2.0 Beta 2)

* Thu Nov 23 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.8-alt1
- New version (1.5.0.8)
- Remove version specific paths.
- Add %%pre script.
- Improvements to product stability.
- Fixed:
    + MFSA 2006-67 Running Script can be recompiled
    + MFSA 2006-66 RSA signature forgery (variant)
    + MFSA 2006-65 Crashes with evidence of memory corruption (rv:1.8.0.8)
    + MFSA 2006-64 Crashes with evidence of memory corruption (rv:1.8.0.7)
    + MFSA 2006-63 JavaScript execution in mail via XBL
    + MFSA 2006-60 RSA Signature Forgery
    + MFSA 2006-59 Concurrency-related vulnerability
    + MFSA 2006-58 Auto-Update compromise through DNS and SSL spoofing
    + MFSA 2006-57 JavaScript Regular Expression Heap Corruption

* Thu Aug 17 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.5-alt1
- New version (1.5.0.5)
- Build with MozLDAP support.
- Improvements to product stability.
- Fixed:
    + MFSA 2006-55 Crashes with evidence of memory corruption (rv:1.8.0.5)
    + MFSA 2006-54 XSS with XPCNativeWrapper(window).Function(...)
    + MFSA 2006-53 UniversalBrowserRead privilege escalation
    + MFSA 2006-52 PAC privilege escalation using Function.prototype.call
    + MFSA 2006-51 Privilege escalation using named-functions and redefined "new Object()"
    + MFSA 2006-50 JavaScript engine vulnerabilities
    + MFSA 2006-49 Heap buffer overwrite on malformed VCard
    + MFSA 2006-48 JavaScript new Function race condition
    + MFSA 2006-47 Native DOM methods can be hijacked across domains
    + MFSA 2006-46 Memory corruption with simultaneous events
    + MFSA 2006-44 Code execution through deleted frame reference

* Tue May 02 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.2-alt1
- New bugfix version.
- Improvements to product stability.
- Fixed:
    + MFSA 2006-28 Security check of js_ValueToFunctionObject() can be circumvented;
    + MFSA 2006-27 Table Rebuilding Code Execution Vulnerability;
    + MFSA 2006-26 Mail Multiple Information Disclosure;
    + MFSA 2006-25 Privilege escalation through Print Preview;
    + MFSA 2006-24 Privilege escalation using crypto.generateCRMFRequest;
    + MFSA 2006-22 CSS Letter-Spacing Heap Overflow Vulnerability;
    + MFSA 2006-21 JavaScript execution in mail when forwarding in-line;
    + MFSA 2006-20 Crashes with evidence of memory corruption (rv:1.8.0.2);
    + MFSA 2006-08 "AnyName" entrainment and access control hazard;
    + MFSA 2006-07 Read beyond buffer while parsing XML;
    + MFSA 2006-06 Integer overflows in E4X, SVG and Canvas;
    + MFSA 2006-05 Localstore.rdf XML injection through XULDocument.persist();
    + MFSA 2006-04 Memory corruption via QueryInterface on Location, Navigator objects;
    + MFSA 2006-02 Changing postion:relative to static corrupts memory;
    + MFSA 2006-01 JavaScript garbage-collection hazards.

* Fri Mar 24 2006 Alexey Gladkov <legion@altlinux.ru> 1.5-alt2
- bugfix build.
- share extension directory fix.

* Tue Feb 21 2006 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- new version 1.5
- build with rpm-build-thunderbird (external build macros)
- Build with system NSS and NSPR.
- Buildrequires updated for xorg-7.0 
- directory /usr/share/thunderbird-@version@/extensions was added to extensions search path .
  * this location is controled by the option extensions.dir.extensions .
- Startup script rewritten. Now it is single script.
  * command line shortcut added: altmail:MAILLIST 
    (example: "altmail:devel" -> mailto:devel@list.altlinux.org).
- LDAP support disabled.
- firsttime script removed
- NoX patch removed

* Wed Aug 24 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt2
- packaging bugfix.
- rpm mascros bugfix.
- The script is added for switching language after installation/removal 
  of a localization package.
- Bug: #6204, #6254 fixed.

* Mon Aug 15 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt1
- new version.
- firsttime script added.

* Wed May 11 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.2-alt1
- new version;
- RSS missing files add;

* Tue Feb 01 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt4
- update patch thunderbird-1.0-20050201-alt-nox.patch 
  * uninstall-global-theme command-line option was added;
  * update-register command-line option was added;
- thunderbird-1.0-alt-rpm-scripts.tar.bz2 bugfix;

* Thu Jan 27 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt3
- fix crush when comiling with gcc3.4 .

* Wed Jan 19 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2
- Rebuilt with libstdc++.so.6.

* Thu Jan 06 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- new version;
- new extension load scheme;
- uninstall-global-extension option fixed;
- add RPATH=%%_libdir/%%fullname to the all binares;
- rpm macros was updated;
- %%post_ldconfig and %%postun_ldconfig was removed.
- icons updated (thx shrek@);

* Tue Jul 16 2004 Alexey Morozov <morozov@altlinux.org> 0.7.2-alt2
- new version (0.7.2)
- rpm macros file is splitted to base and devel parts
- Russian spec translation
- A patch to handle external URLs w/ url_handler
- Requirements cleanup

* Fri May 07 2004 Alexey Gladkov <legion@altlinux.ru> 0.6-alt1
- New version;
- Splash screen added;
- Default userContent.css added;
- Offline extension added by default;
- Confilct between mozilla-like devel packages was removed.

* Wed Feb 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.5-alt1
- New version.

* Tue Jan 13 2004 Alexey Gladkov <legion@altlinux.ru> 0.4-alt4
- Spec changes.

* Fri Dec 26 2003 Alexey Gladkov <legion@altlinux.ru> 0.4-alt3
- first build for ALT Linux.
- rpm macro added.
- new scheme loading extensions added (thx force@)
- Spec modifications.
