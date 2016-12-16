%define rname firefox
%set_verify_elf_method unresolved=strict
%def_without gtk3

%define firefox_cid     \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define firefox_prefix  %_libdir/firefox
%define firefox_datadir %_datadir/firefox

%define gst_version 1.0
%define nspr_version 4.12.0
%define nss_version 3.23.0

Summary:              The Mozilla Firefox project is a redesign of Mozilla's browser
Summary(ru_RU.UTF-8): Интернет-браузер Mozilla Firefox

Name:           firefox-esr
Version:        45.6.0
Release:        alt1
License:        MPL/GPL/LGPL
Group:          Networking/WWW
URL:            http://www.mozilla.org/projects/firefox/

Packager:	Andrey Cherepanov <cas@altlinux.ru>

Source0:        firefox-source.tar
Source1:        rpm-build.tar
Source2:        searchplugins.tar
Source4:        firefox-mozconfig
Source6:        firefox.desktop
Source7:        firefox.c
Source8:        firefox-prefs.js

Patch5:         firefox-duckduckgo.patch
Patch6:         firefox3-alt-disable-werror.patch
Patch14:        firefox-fix-install.patch
Patch16:        firefox-cross-desktop.patch
Patch17:        firefox-mediasource-crash.patch

# Upstream
Patch200:       mozilla-bug-1205199.patch

# Red Hat
Patch300:       rhbz-1219542-s390-build.patch
Patch301:       rhbz-1291190-appchooser-crash.patch
Patch302:       rhbz-966424.patch
%if_with gtk3
Patch303:       rh-firefox-gtk3-20.patch
%endif

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: rpm-macros-alternatives
BuildRequires: doxygen gcc-c++ imake libIDL-devel makedepend glibc-kernheaders
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libcurl-devel libgtk+2-devel libhunspell-devel libjpeg-devel
%if_with gtk3
BuildRequires: libgtk+3-devel
%endif
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
BuildRequires: gstreamer%gst_version-devel gst-plugins%gst_version-devel
BuildRequires: libopus-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libicu-devel

# Python requires
BuildRequires: python-module-distribute
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3
BuildRequires: python-modules-json

# Mozilla requires
BuildRequires: pkgconfig(nspr) >= %nspr_version
BuildRequires: pkgconfig(nss) >= %nss_version
BuildRequires: libnss-devel-static

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

Obsoletes:	firefox-3.6 firefox-4.0 firefox-5.0
Conflicts:	firefox-settings-desktop

Provides:	webclient
Provides:	firefox = %EVR
Conflicts:	firefox
Requires:	mozilla-common
Requires:	gst-plugins-ugly1.0

# ALT#30732
Requires:	gst-plugins-ugly%gst_version

# Protection against fraudulent DigiNotar certificates
Requires: libnss >= 3.12.11-alt3

%description
The Mozilla Firefox project is a redesign of Mozilla's browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер Mozilla Firefox - кроссплатформенная модификация браузера Mozilla,
созданная с использованием языка XUL для описания интерфейса пользователя.

%prep
%setup -q -n firefox-%version -c
cd mozilla

tar -xf %SOURCE1
tar -xf %SOURCE2

%patch5  -p1
%patch6  -p1
%patch14 -p1
%patch16 -p1
%patch17 -p2

%patch200 -p1

%patch300 -p1
%patch301 -p1
%patch302 -p1
%if_with gtk3
%patch303 -p1
%endif

cp -f %SOURCE4 .mozconfig
%if_without gtk3
subst 's/cairo-gtk3/cairo-gtk2/' .mozconfig
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
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS -fPIC -Wl,-z,relro -Wl,-z,now | \
                sed \
                    -e 's/-Wall//' \
                    -e 's/-fexceptions/-fno-exceptions/g'
)
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"
# Add fake RPATH
rpath="/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"
export LDFLAGS="$LDFLAGS -Wl,-rpath,$rpath"
%if_without system_nss
# see mozilla/security/nss/coreconf/Linux.mk:203
export RPATH="-Wl,-rpath,$rpath"
%endif

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

# ALT#30572
if [ ! -e "%buildroot/%firefox_prefix/plugins" ]; then
	what="$(relative %browser_plugins_path %firefox_prefix/plugins)"
	ln -s -- "$what" %buildroot/%firefox_prefix/plugins
fi

# install rpm-build-firefox
mkdir -p -- \
	%buildroot/%_rpmmacrosdir
sed \
	-e 's,@firefox_version@,%version,' \
	-e 's,@firefox_release@,%release,' \
	rpm-build/rpm.macros.firefox.standalone > %buildroot/%_rpmmacrosdir/firefox

install -m755 firefox %buildroot/%_bindir/firefox

cd %buildroot

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
rpath="/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"
find \
     %buildroot/%firefox_prefix \
-type f -print0 |
(set +x
        while read -r -d '' f; do
              t="$(readlink -ev -- "$f")"

              file -- "$t" | fgrep -qs ELF || continue

              if chrpath -l "$t" | fgrep -qs "PATH=$rpath"; then
                 chrpath -r "%firefox_prefix" "$t"
              fi
        done
)

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

%changelog
* Fri Dec 16 2016 Andrey Cherepanov <cas@altlinux.org> 45.6.0-alt1
- New ESR version

* Tue Dec  6 2016 Ivan Zakharyaschev <imz@altlinux.org> 45.5.1-alt2
- Make it pass strict verification of unresolved ELF symbols; this will also
  protect us from missing dependencies on libgtk symbols. (Thx legion@ for
  the original hack, removed in 44.0.2-alt3, but found to be restorable by
  ruslandh@'s work on strict unresolved symbols verification in palemoon.)

* Thu Dec 01 2016 Andrey Cherepanov <cas@altlinux.org> 45.5.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-92 Firefox SVG Animation Remote Code Execution

* Thu Nov 17 2016 Andrey Cherepanov <cas@altlinux.org> 45.5.0-alt1
- New ESR version

* Tue Sep 20 2016 Andrey Cherepanov <cas@altlinux.org> 45.4.0-alt1
- New ESR version

* Tue Aug 02 2016 Andrey Cherepanov <cas@altlinux.org> 45.3.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-80 Same-origin policy violation using local HTML file and saved shortcut file
  + MFSA 2016-79 Use-after-free when applying SVG effects
  + MFSA 2016-78 Type confusion in display transformation
  + MFSA 2016-77 Buffer overflow in ClearKey Content Decryption Module (CDM) during video playback
  + MFSA 2016-76 Scripts on marquee tag can execute in sandboxed iframes
  + MFSA 2016-73 Use-after-free in service workers with nested sync events
  + MFSA 2016-72 Use-after-free in DTLS during WebRTC session shutdown
  + MFSA 2016-70 Use-after-free when using alt key and toplevel menus
  + MFSA 2016-67 Stack underflow during 2D graphics rendering
  + MFSA 2016-65 Cairo rendering crash due to memory allocation issue with FFmpeg 0.10
  + MFSA 2016-64 Buffer overflow rendering SVG with bidirectional content
  + MFSA 2016-63 Favicon network connection can persist when page is closed


* Sun Jun 12 2016 Andrey Cherepanov <cas@altlinux.org> 45.2.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-58 Entering fullscreen and persistent pointerlock without user permission
  + MFSA 2016-56 Use-after-free when textures are used in WebGL operations after recycle pool destruction
  + MFSA 2016-55 File overwrite and privilege escalation through Mozilla Windows updater
  + MFSA 2016-53 Out-of-bounds write with WebGL shader
  + MFSA 2016-52 Addressbar spoofing though the SELECT element
  + MFSA 2016-51 Use-after-free deleting tables from a contenteditable document
  + MFSA 2016-50 Buffer overflow parsing HTML5 fragments

* Tue May 24 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.1-alt2
- Build with GTK+ 2.x (ALT #32120)

* Wed May 04 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.1-alt1
- New ESR version

* Mon May 02 2016 Andrey Cherepanov <cas@altlinux.org> 45.1.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-47 Write to invalid HashMap entry through JavaScript.watch()
  + MFSA 2016-44 Buffer overflow in libstagefright with CENC offsets
  + MFSA 2016-39 Miscellaneous memory safety hazards

* Fri Apr 15 2016 Andrey Cherepanov <cas@altlinux.org> 45.0.2-alt1
- New ESR version (switch to 45.x)

* Thu Mar 24 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.1-alt1
- New ESR version

* Thu Mar 10 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.0-alt2
- Rebuild with new rpm

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 38.7.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-37 Font vulnerabilities in the Graphite 2 library
  + MFSA 2016-35 Buffer overflow during ASN.1 decoding in NSS
  + MFSA 2016-34 Out-of-bounds read in HTML parser following a failed allocation
  + MFSA 2016-31 Memory corruption with malicious NPAPI plugin
  + MFSA 2016-28 Addressbar spoofing though history navigation and Location protocol property
  + MFSA 2016-27 Use-after-free during XML transformations
  + MFSA 2016-25 Use-after-free when using multiple WebRTC data channels
  + MFSA 2016-24 Use-after-free in SetBody
  + MFSA 2016-23 Use-after-free in HTML5 string parser
  + MFSA 2016-21 Displayed page address can be overridden
  + MFSA 2016-20 Memory leak in libstagefright when deleting an array during MP4 processing
  + MFSA 2016-17 Local file overwriting and potential privilege escalation through CSP reports
  + MFSA 2016-16 Miscellaneous memory safety hazards
  + MFSA 2015-136 Same-origin policy violation using performance.getEntries and history navigation
  + MFSA 2015-81 Use-after-free in MediaStream playback

* Fri Feb 12 2016 Andrey Cherepanov <cas@altlinux.org> 38.6.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-14 Vulnerabilities in Graphite 2

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 38.6.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2016-03 Buffer overflow in WebGL after out of memory allocation
  + MFSA 2016-01 Miscellaneous memory safety hazards (rv:44.0 / rv:38.6)
  + MFSA 2015-150 MD5 signatures accepted within TLS 1.2 ServerKeyExchange in server signature

* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 38.5.2-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-150 MD5 signatures accepted within TLS 1.2 ServerKeyExchange in server signature

* Tue Dec 22 2015 Andrey Cherepanov <cas@altlinux.org> 38.5.1-alt1
- New ESR version

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 38.5.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-149 Cross-site reading attack through data and view-source URIs
  + MFSA 2015-147 Integer underflow and buffer overflow processing MP4 metadata in libstagefright
  + MFSA 2015-146 Integer overflow in MP4 playback in 64-bit versions
  + MFSA 2015-145 Underflow through code inspection
  + MFSA 2015-139 Integer overflow allocating extremely large textures
  + MFSA 2015-138 Use-after-free in WebRTC when datachannel is used after being destroyed

* Wed Nov 04 2015 Andrey Cherepanov <cas@altlinux.org> 38.4.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-133 NSS and NSPR memory corruption issues
  + MFSA 2015-132 Mixed content WebSocket policy bypass through workers
  + MFSA 2015-131 Vulnerabilities found through code inspection
  + MFSA 2015-130 JavaScript garbage collection crash with Java applet
  + MFSA 2015-128 Memory corruption in libjar through zip files
  + MFSA 2015-127 CORS preflight is bypassed when non-standard Content-Type headers are received
  + MFSA 2015-123 Buffer overflow during image interactions in canvas
  + MFSA 2015-122 Trailing whitespace in IP address hostnames can bypass same-origin policy

* Mon Sep 28 2015 Andrey Cherepanov <cas@altlinux.org> 38.3.0-alt2
- Use GStreamer 1.0 (ALT #31305)

* Wed Sep 23 2015 Andrey Cherepanov <cas@altlinux.org> 38.3.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-113 Memory safety errors in libGLES in the ANGLE graphics library
  + MFSA 2015-112 Vulnerabilities found through code inspection
  + MFSA 2015-111 Errors in the handling of CORS preflight request headers
  + MFSA 2015-110 Dragging and dropping images exposes final URL after redirects
  + MFSA 2015-106 Use-after-free while manipulating HTML media content
  + MFSA 2015-105 Buffer overflow while decoding WebM video
  + MFSA 2015-101 Buffer overflow in libvpx while parsing vp9 format video
  + MFSA 2015-100 Arbitrary file manipulation by local user through Mozilla updater

* Fri Aug 28 2015 Andrey Cherepanov <cas@altlinux.org> 38.2.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-95 Add-on notification bypass through data URLs
  + MFSA 2015-94 Use-after-free when resizing canvas element during restyling

* Wed Aug 12 2015 Andrey Cherepanov <cas@altlinux.org> 38.2.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-92 Use-after-free in XMLHttpRequest with shared workers
  + MFSA 2015-90 Vulnerabilities found through code inspection
  + MFSA 2015-89 Buffer overflows on Libvpx when decoding WebM video
  + MFSA 2015-88 Heap overflow in gdk-pixbuf when scaling bitmap images
  + MFSA 2015-87 Crash when using shared memory in JavaScript
  + MFSA 2015-85 Out-of-bounds write with Updater and malicious MAR file
  + MFSA 2015-84 Arbitrary file overwriting through Mozilla Maintenance
    Service with hard links
  + MFSA 2015-83 Overflow issues in libstagefright
  + MFSA 2015-82 Redefinition of non-configurable JavaScript object
    properties
  + MFSA 2015-80 Out-of-bounds read with malformed MP3 file

* Sat Aug 08 2015 Andrey Cherepanov <cas@altlinux.org> 38.1.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-78 Same origin violation and local file stealing via PDF reader

* Thu Jul 16 2015 Andrey Cherepanov <cas@altlinux.org> 38.1.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-70 NSS accepts export-length DHE keys with regular DHE cipher suites
  + MFSA 2015-69 Privilege escalation through internal workers
  + MFSA 2015-67 Key pinning is ignored when overridable errors are encountered
  + MFSA 2015-66 Vulnerabilities found through code inspection
  + MFSA 2015-65 Use-after-free in workers while using XMLHttpRequest
  + MFSA 2015-64 ECDSA signature validation fails to handle some signatures correctly
  + MFSA 2015-63 Use-after-free in Content Policy due to microtask execution error
  + MFSA 2015-62 Out-of-bound read while computing an oscillator rendering range in Web Audio
  + MFSA 2015-61 Type confusion in Indexed Database Manager
  + MFSA 2015-60 Local files or privileged URLs in pages can be opened into new tabs

* Mon May 25 2015 Andrey Cherepanov <cas@altlinux.org> 38.0.1-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-58 Mozilla Windows updater can be run outside of application directory
  + MFSA 2015-57 Privilege escalation through IPC channel messages
  + MFSA 2015-56 Untrusted site hosting trusted page can intercept webchannel responses
  + MFSA 2015-55 Buffer overflow and out-of-bounds read while parsing MP4 video metadata
  + MFSA 2015-54 Buffer overflow when parsing compressed XML
  + MFSA 2015-53 Use-after-free due to Media Decoder Thread creation during shutdown
  + MFSA 2015-52 Sensitive URL encoded information written to Android logcat
  + MFSA 2015-51 Use-after-free during text processing with vertical text enabled
  + MFSA 2015-50 Out-of-bounds read and write in asm.js validation
  + MFSA 2015-49 Referrer policy ignored when links opened by middle-click and context menu
  + MFSA 2015-48 Buffer overflow with SVG content and CSS
  + MFSA 2015-47 Buffer overflow parsing H.264 video with Linux Gstreamer

* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 31.6.0-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-40 Same-origin bypass through anchor navigation
  + MFSA 2015-37 CORS requests should not follow 30x redirections after
    preflight
  + MFSA 2015-33 resource:// documents can load privileged pages
  + MFSA 2015-31 Use-after-free when using the Fluendo MP3 GStreamer
    plugin

* Sun Mar 22 2015 Andrey Cherepanov <cas@altlinux.org> 31.5.3-alt1
- New ESR version
- Security fixes:
  + MFSA 2015-28 Privilege escalation through SVG navigation
  + MFSA 2015-29 Code execution through incorrect JavaScript bounds
    checking elimination

* Wed Feb 25 2015 Andrey Cherepanov <cas@altlinux.org> 31.5.0-alt1
- New ESR version
- Fixed:
  + 2015-24 Reading of local files through manipulation of form
    autocomplete
  + 2015-19 Out-of-bounds read and write while rendering SVG content
  + 2015-16 Use-after-free in IndexedDB
  + 2015-12 Invoking Mozilla updater will load locally stored DLL files

* Sun Feb 08 2015 Andrey Cherepanov <cas@altlinux.org> 31.4.0-alt1
- Package ESR version as firefox-esr
- Fixed:
  + MFSA 2015-06 Read-after-free in WebRTC
  + MFSA 2015-04 Cookie injection through Proxy Authenticate responses
  + MFSA 2015-03 sendBeacon requests lack an Origin header
