%define rname firefox
%set_verify_elf_method unresolved=strict

%define firefox_cid     \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define firefox_prefix  %_libdir/firefox
%define firefox_datadir %_datadir/firefox

%define gst_version 1.0
%define nspr_version 4.15
%define nss_version 3.31.0

Summary:              The Mozilla Firefox project is a redesign of Mozilla's browser
Summary(ru_RU.UTF-8): Интернет-браузер Mozilla Firefox

Name:           firefox-esr
Version:        52.6.0
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

Patch6:         firefox-alt-disable-werror.patch
#Patch7:         firefox-alt-disable-profiler.patch
Patch14:        firefox-fix-install.patch
Patch16:        firefox-cross-desktop.patch
Patch17:        firefox-mediasource-crash.patch

# Upstream
Patch200:       mozilla-bug-256180.patch
Patch201:       mozilla-bug-1196777.patch

# Red Hat
Patch301:       rhbz-1291190-appchooser-crash.patch
Patch302:       rhbz-966424.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: rpm-macros-alternatives
BuildRequires: doxygen gcc-c++ imake libIDL-devel makedepend glibc-kernheaders
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: libcurl-devel libgtk+2-devel libgtk+3-devel libhunspell-devel libjpeg-devel
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
#BuildRequires: libicu-devel
BuildRequires: libdbus-devel libdbus-glib-devel

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

# ALT#30732
Requires:	gst-plugins-ugly%gst_version

# Require fresh nss for correct https open
Requires: libnss >= %nss_version

%description
The Mozilla Firefox project is a redesign of Mozilla's browser
component, written using the XUL user interface language and designed to
be cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер Mozilla Firefox - кроссплатформенная модификация
браузера Mozilla, созданная с использованием языка XUL для описания
интерфейса пользователя.

%prep
%setup -q -n firefox-%version -c
cd mozilla

tar -xf %SOURCE1
tar -xf %SOURCE2

%patch6  -p1
#patch7  -p1
%patch14 -p1
%patch16 -p1
%patch17 -p2

%patch200 -p1
%patch201 -p1

%patch301 -p1
%patch302 -p1

cp -f %SOURCE4 .mozconfig

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

MOZ_OPT_FLAGS="$RPM_OPT_FLAGS"

# PIE, full relro
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -fPIC -Wl,-z,relro -Wl,-z,now"

# add -fno-delete-null-pointer-checks and -fno-inline-small-functions for gcc6
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -fno-delete-null-pointer-checks -fno-inline-small-functions"

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo $MOZ_OPT_FLAGS | \
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
[ "${NPROCS:+0}" -ge 6 ] && MOZ_SMP_FLAGS=-j6
%endif

make -f client.mk \
	MAKENSISU= \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
	mozappdir=%buildroot/%firefox_prefix \
	libdir=%_libdir \
	build

%__cc %optflags \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DMOZ_PROGRAM=\"%firefox_prefix/firefox-bin\" \
	-DMOZ_DIST_BIN=\"%firefox_prefix\"\
	%SOURCE7 -o firefox


%install
cd mozilla

export SHELL=/bin/sh

%__mkdir_p \
	%buildroot/%mozilla_arch_extdir/%firefox_cid \
	%buildroot/%mozilla_noarch_extdir/%firefox_cid \
	#

make -C objdir \
	DESTDIR=%buildroot \
	INSTALL="/bin/install -p" \
	mozappdir=%firefox_prefix \
	libdir=%_libdir \
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
* Mon Jan 22 2018 Andrey Cherepanov <cas@altlinux.org> 52.6.0-alt1
- New ESR version (52.6.0)

* Wed Jan 10 2018 Andrey Cherepanov <cas@altlinux.org> 52.5.3-alt1
- New ESR version (52.5.3)
- Fixes:
  + Speculative execution side-channel attack ("Spectre")

* Sun Dec 10 2017 Andrey Cherepanov <cas@altlinux.org> 52.5.2-alt1
- New ESR version (52.5.2)
- Fixes:
  + CVE-2017-7843 Web worker in Private Browsing mode can write IndexedDB data
- Build with DBUS support (ALT #34302)

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 52.5.0-alt1
- New ESR version (52.5.0)
- Fixes:
  + CVE-2017-7828 Use-after-free of PressShell while restyling layout
  + CVE-2017-7830 Cross-origin URL information leak through Resource
  + CVE-2017-7826 Memory safety bugs fixed in Firefox 57 and Firefox ESR

* Fri Sep 29 2017 Andrey Cherepanov <cas@altlinux.org> 52.4.0-alt1
- New ESR version (52.4.0)
- Fixes:
  + CVE-2017-7793 Use-after-free with Fetch API
  + CVE-2017-7818 Use-after-free during ARIA array manipulation
  + CVE-2017-7819 Use-after-free while resizing images in design mode
  + CVE-2017-7824 Buffer overflow when drawing and validating elements with ANGLE
  + CVE-2017-7805 Use-after-free in TLS 1.2 generating handshake hashes
  + CVE-2017-7814 Blob and data URLs bypass phishing and malware protection warnings
  + CVE-2017-7825 OS X fonts render some Tibetan and Arabic unicode characters as spaces
  + CVE-2017-7823 CSP sandbox directive did not create a unique origin
  + CVE-2017-7810 Memory safety bugs fixed in Firefox 56 and Firefox ESR 52.4

* Tue Aug 08 2017 Andrey Cherepanov <cas@altlinux.org> 52.3.0-alt1
- New ESR version (52.3.0)
- Security fixes:
  + CVE-2017-7798: XUL injection in the style editor in devtools
  + CVE-2017-7800: Use-after-free in WebSockets during disconnection
  + CVE-2017-7801: Use-after-free with marquee during window resizing
  + CVE-2017-7809: Use-after-free while deleting attached editor DOM node
  + CVE-2017-7784: Use-after-free with image observers
  + CVE-2017-7802: Use-after-free resizing image elements
  + CVE-2017-7785: Buffer overflow manipulating ARIA attributes in DOM
  + CVE-2017-7786: Buffer overflow while painting non-displayable SVG
  + CVE-2017-7753: Out-of-bounds read with cached style data and pseudo-elements
  + CVE-2017-7787: Same-origin policy bypass with iframes through page reloads
  + CVE-2017-7807: Domain hijacking through AppCache fallback
  + CVE-2017-7792: Buffer overflow viewing certificates with an extremely long OID
  + CVE-2017-7804: Memory protection bypass through WindowsDllDetourPatcher
  + CVE-2017-7791: Spoofing following page navigation with data: protocol and modal alerts
  + CVE-2017-7782: WindowsDllDetourPatcher allocates memory without DEP protections
  + CVE-2017-7803: CSP containing 'sandbox' improperly applied
  + CVE-2017-7779: Memory safety bugs fixed in Firefox 55 and Firefox ESR 52.3

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 52.2.1-alt1
- New ESR version (52.2.1)

* Wed Jun 21 2017 Andrey Cherepanov <cas@altlinux.org> 52.2.0-alt1
- New ESR version (52.2.0)
- Security fixes:
  + CVE-2017-5472: Use-after-free using destroyed node when regenerating trees
  + CVE-2017-7749: Use-after-free during docshell reloading
  + CVE-2017-7750: Use-after-free with track elements
  + CVE-2017-7751: Use-after-free with content viewer listeners
  + CVE-2017-7752: Use-after-free with IME input
  + CVE-2017-7754: Out-of-bounds read in WebGL with ImageInfo object
  + CVE-2017-7755: Privilege escalation through Firefox Installer with same directory DLL files
  + CVE-2017-7756: Use-after-free and use-after-scope logging XHR header errors
  + CVE-2017-7757: Use-after-free in IndexedDB
  + CVE-2017-7778: Vulnerabilities in the Graphite 2 library
  + CVE-2017-7758: Out-of-bounds read in Opus encoder
  + CVE-2017-7760: File manipulation and privilege escalation via callback parameter in Mozilla Windows Updater and Maintenance Service
  + CVE-2017-7761: File deletion and privilege escalation through Mozilla Maintenance Service helper.exe application
  + CVE-2017-7763: Mac fonts render some unicode characters as spaces
  + CVE-2017-7764: Domain spoofing with combination of Canadian Syllabics and other unicode blocks
  + CVE-2017-7765: Mark of the Web bypass when saving executable files
  + CVE-2017-7766: File execution and privilege escalation through updater.ini, Mozilla Windows Updater, and Mozilla Maintenance Service
  + CVE-2017-7767: Privilege escalation and arbitrary file overwrites through Mozilla Windows Updater and Mozilla Maintenance Service
  + CVE-2017-7768: 32 byte arbitrary file read through Mozilla Maintenance Service
  + CVE-2017-5470: Memory safety bugs fixed in Firefox 54 and Firefox ESR 52.2

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 52.1.1-alt1
- New ESR version (52.1.1)
- Set plugin.load_flash_only setting to false to allow use all NPAPI plugins
- Security fixes since 52.0:
  + CVE-2016-10196: Vulnerabilities in Libevent library
  + CVE-2017-5031: Use after free in ANGLE
  + CVE-2017-5428: integer overflow in createImageBitmap()
  + CVE-2017-5429: Memory safety bugs fixed in Firefox 53, Firefox ESR
  + CVE-2017-5430: Memory safety bugs fixed in Firefox 53 and Firefox ESR
  + CVE-2017-5435: Use-after-free during transaction processing in the
  + CVE-2017-5439: Use-after-free in nsTArray Length() during XSLT
  + CVE-2017-5440: Use-after-free in txExecutionState destructor during
  + CVE-2017-5444: Buffer overflow while parsing
  + CVE-2017-5446: Out-of-bounds read when HTTP/2 DATA frames are sent
  + CVE-2017-5451: Addressbar spoofing with onblur event
  + CVE-2017-5454: Sandbox escape allowing file system read access through
  + CVE-2017-5455: Sandbox escape through internal feed reader APIs
  + CVE-2017-5456: Sandbox escape allowing local file system access
  + CVE-2017-5464: Memory corruption with accessibility and DOM
  + CVE-2017-5466: Origin confusion when reloading isolated data:text/html
  + CVE-2017-5467: Memory corruption when drawing Skia content

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 52.0-alt1
- New release (52.0) based on legion@ build.
- Built with internal icu.
- Fixed:
  + CVE-2017-5400: asm.js JIT-spray bypass of ASLR and DEP
  + CVE-2017-5401: Memory Corruption when handling ErrorResult
  + CVE-2017-5402: Use-after-free working with events in FontFace objects
  + CVE-2017-5403: Use-after-free using addRange to add range to an incorrect root object
  + CVE-2017-5404: Use-after-free working with ranges in selections
  + CVE-2017-5406: Segmentation fault in Skia with canvas operations
  + CVE-2017-5407: Pixel and history stealing via floating-point timing side channel with SVG filters
  + CVE-2017-5410: Memory corruption during JavaScript garbage collection incremental sweeping
  + CVE-2017-5411: Use-after-free in Buffer Storage in libGLES
  + CVE-2017-5409: File deletion via callback parameter in Mozilla Windows Updater and Maintenance Service
  + CVE-2017-5408: Cross-origin reading of video captions in violation of CORS
  + CVE-2017-5412: Buffer overflow read in SVG filters
  + CVE-2017-5413: Segmentation fault during bidirectional operations
  + CVE-2017-5414: File picker can choose incorrect default directory
  + CVE-2017-5415: Addressbar spoofing through blob URL
  + CVE-2017-5416: Null dereference crash in HttpChannel
  + CVE-2017-5417: Addressbar spoofing by draging and dropping URLs
  + CVE-2017-5425: Overly permissive Gecko Media Plugin sandbox regular expression access
  + CVE-2017-5426: Gecko Media Plugin sandbox is not started if seccomp-bpf filter is running
  + CVE-2017-5427: Non-existent chrome.manifest file loaded during startup
  + CVE-2017-5418: Out of bounds read when parsing HTTP digest authorization responses
  + CVE-2017-5419: Repeated authentication prompts lead to DOS attack
  + CVE-2017-5420: Javascript: URLs can obfuscate addressbar location
  + CVE-2017-5405: FTP response codes can cause use of uninitialized values for ports
  + CVE-2017-5421: Print preview spoofing
  + CVE-2017-5422: DOS attack by using view-source: protocol repeatedly in one hyperlink
  + CVE-2017-5399: Memory safety bugs fixed in Firefox 52
  + CVE-2017-5398: Memory safety bugs fixed in Firefox 52 and Firefox ESR 45.8

* Thu Apr 20 2017 Andrey Cherepanov <cas@altlinux.org> 45.9.0-alt1
- New ESR version
- Security fixes:
  + CVE-2017-5429: Memory safety bugs fixed in Firefox 53, Firefox ESR 45.9,
  + CVE-2017-5462: DRBG flaw in NSS
  + CVE-2017-5445: Uninitialized values used while parsing
  + CVE-2017-5469: Potential Buffer overflow in flex-generated code
  + CVE-2017-5437: Vulnerabilities in Libevent library
  + CVE-2017-5448: Out-of-bounds write in ClearKeyDecryptor
  + CVE-2017-5465: Out-of-bounds read in ConvolvePixel
  + CVE-2017-5447: Out-of-bounds read during glyph processing
  + CVE-2017-5446: Out-of-bounds read when HTTP/2 DATA frames are sent with
  + CVE-2017-5444: Buffer overflow while parsing application/http-index-format
  + CVE-2017-5443: Out-of-bounds write during BinHex decoding
  + CVE-2017-5464: Memory corruption with accessibility and DOM manipulation
  + CVE-2017-5442: Use-after-free during style changes
  + CVE-2017-5441: Use-after-free with selection during scroll events
  + CVE-2017-5440: Use-after-free in txExecutionState destructor during XSLT
  + CVE-2017-5439: Use-after-free in nsTArray Length() during XSLT processing
  + CVE-2017-5438: Use-after-free in nsAutoPtr during XSLT processing
  + CVE-2017-5460: Use-after-free in frame selection
  + CVE-2017-5432: Use-after-free in text input selection
  + CVE-2017-5434: Use-after-free during focus handling
  + CVE-2017-5459: Buffer overflow in WebGL
  + CVE-2017-5461: Out-of-bounds write in Base64 encoding in NSS
  + CVE-2017-5436: Out-of-bounds write with malicious font in Graphite 2
  + CVE-2017-5435: Use-after-free during transaction processing in the editor
  + CVE-2017-5433: Use-after-free in SMIL animation functions

* Tue Mar 07 2017 Andrey Cherepanov <cas@altlinux.org> 45.8.0-alt1
- New ESR version
- Require fresh libnss for correct https open

* Wed Jan 25 2017 Andrey Cherepanov <cas@altlinux.org> 45.7.0-alt1
- New ESR version

* Fri Jan 20 2017 Andrey Cherepanov <cas@altlinux.org> 45.6.0-alt2
- Fix build with GCC 6.1

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
  + 2015-19 Out-of-bounds read and write while rendering SVG content
  + 2015-16 Use-after-free in IndexedDB
  + 2015-12 Invoking Mozilla updater will load locally stored DLL files

* Sun Feb 08 2015 Andrey Cherepanov <cas@altlinux.org> 31.4.0-alt1
- Package ESR version as firefox-esr
- Fixed:
  + MFSA 2015-06 Read-after-free in WebRTC
  + MFSA 2015-04 Cookie injection through Proxy Authenticate responses
  + MFSA 2015-03 sendBeacon requests lack an Origin header
