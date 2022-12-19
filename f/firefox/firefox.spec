Summary:              The Mozilla Firefox project is a redesign of Mozilla's browser
Summary(ru_RU.UTF-8): Интернет-браузер Mozilla Firefox

Name: firefox
Version: 108.0.1
Release: alt1
License: MPL-2.0
Group: Networking/WWW
URL: https://www.mozilla.org/firefox/

Source0: firefox-source.tar

### Start Patches
Patch001: 0001-FEDORA-build-arm-libopus.patch
Patch002: 0002-FEDORA-build-arm.patch
Patch003: 0003-ALT-Fix-aarch64-build.patch
Patch004: 0004-MOZILLA-1196777-GTK3-keyboard-input-focus-sticks-on-.patch
Patch005: 0005-MOZILLA-1170092-Search-for-default-preferences-in-et.patch
Patch006: 0006-use-floats-for-audio-on-arm-too.patch
Patch007: 0007-bmo-847568-Support-system-harfbuzz.patch
Patch008: 0008-bmo-847568-Support-system-graphite2.patch
Patch009: 0009-bmo-1559213-Support-system-av1.patch
Patch010: 0010-Revert-Bug-1712947-Don-t-pass-neon-flags-to-rustc-wh.patch
Patch011: 0011-ALT-fix-double_t-redefinition.patch
Patch012: 0012-build-Disable-Werror.patch
Patch013: 0013-glxtest-delay-terminating-the-EGLDisplay.patch
### End Patches

%define _unpackaged_files_terminate_build 1
%set_verify_elf_method relaxed

%ifndef build_parallel_jobs
%global build_parallel_jobs %__nprocs
%endif

%define gst_version   1.0
%define nspr_version  4.35
%define nss_version   3.86
%define rust_version  1.65.0
%define cargo_version 1.65.0
%define llvm_version  15.0

ExcludeArch: ppc64le

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-firefox
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: clang%llvm_version
BuildRequires: clang%llvm_version-devel
BuildRequires: llvm%llvm_version-devel
BuildRequires: lld%llvm_version-devel
BuildRequires: libstdc++-devel
BuildRequires: glibc-kernheaders-generic
BuildRequires: rpm-macros-alternatives
BuildRequires: rust >= %rust_version
BuildRequires: rust-cargo >= %cargo_version
BuildRequires: node
BuildRequires: nasm yasm
BuildRequires: zip unzip
BuildRequires: libshell
BuildRequires: libwireless-devel
BuildRequires: libnss-devel-static
BuildRequires: xorg-cf-files chrpath alternatives
BuildRequires: gstreamer%gst_version-devel gst-plugins%gst_version-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(aom)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(dav1d)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(dri)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(graphite2)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libproxy-1.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(nspr) >= %nspr_version
BuildRequires: pkgconfig(nss) >= %nss_version
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(vpx)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(zlib)

# Python requires
BuildRequires: /dev/shm

BuildRequires: python3-base
BuildRequires: python3(curses)
BuildRequires: python3(hamcrest)
BuildRequires: python3(pip)
BuildRequires: python3(setuptools)
BuildRequires: python3(sqlite3)

# Rust requires
BuildRequires: /proc

Provides: webclient
Requires: mozilla-common

Obsoletes: firefox-ru <= 70.0.1
Obsoletes: firefox-uk <= 70.0.1
Obsoletes: firefox-kk <= 70.0.1
Obsoletes: firefox-wayland <= 104.0.2

Provides: firefox-ru = %EVR
Provides: firefox-uk = %EVR
Provides: firefox-kk = %EVR
Provides: firefox-wayland = %EVR

# ALT#30732
Requires: gst-plugins-ugly%gst_version

Requires: libnspr >= %nspr_version
Requires: libnss >= %nss_version

%description
The Mozilla Firefox project is a redesign of Mozilla's browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF-8
Интернет-браузер Mozilla Firefox - кроссплатформенная модификация браузера Mozilla,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n firefox-config-privacy
Summary:	Firefox configuration with the paranoid privacy settings
Group:		System/Configuration/Networking
BuildArch:	noarch

Requires: %name >= %version-%release

%description -n firefox-config-privacy
Settings disable:
* obsolete ssl protocols;
* safebrowsing, trackingprotection and other requests to third-party services;
* telemetry;
* webrtc;
* the social features;
* dns and network predictors/prefetch;
* and some more...

Most likely you don't need to use this package.

%prep
%setup -q -n firefox-%version -c
%autopatch -p1

mv -- .rpm/l10n .
cp -f .rpm/firefox-mozconfig .mozconfig

tee -a .mozconfig <<'EOF'
ac_add_options --prefix="%_prefix"
ac_add_options --libdir="%_libdir"
%ifnarch %{ix86} ppc64le
ac_add_options --enable-linker=lld
%ifnarch armh
ac_add_options --enable-lto=thin
%endif
%endif
%ifarch %{ix86} armh ppc64le
ac_add_options --disable-webrtc
%endif
%ifarch %{ix86} armh x86_64
ac_add_options --disable-elf-hack
%endif
%ifarch %{ix86} armh
%ifarch %{ix86}
ac_add_options --disable-av1
%endif
ac_add_options --enable-strip
ac_add_options --enable-install-strip
ac_add_options --disable-rust-debug
ac_add_options --disable-debug-symbols
%else
ac_add_options --disable-strip
ac_add_options --disable-install-strip
%endif
mk_add_options MOZ_MAKE_FLAGS="-j%build_parallel_jobs --no-print-directory"
EOF

find third_party \
	-type f \( -name '*.so' -o -name '*.o' -o -name '*.a' \) \
	-delete

# Error: relocation R_386_GOTOFF against undefined hidden symbol
# `tabs_4d51_TabsBridgedEngine_reset' can not be used when making a shared
# object
# https://bugzilla.mozilla.org/show_bug.cgi?id=1805809
%ifarch armh %{ix86}
find toolkit/components/uniffi-js -type f |
	xargs sed -ri.poff 's,_4d51_,_1c79_,g'
%endif

rm -rf -- obj-x86_64-pc-linux-gnu
rm -rf -- third_party/python/setuptools/setuptools*


%build
%add_findprov_lib_path %firefox_prefix

export MOZ_BUILD_APP=browser
export MOZ_CHROME_MULTILOCALE="$(tr '\n' ' ' < .rpm/firefox-l10n.txt)"

MOZ_OPT_FLAGS="-pipe -O2 -g0"
%ifarch armh
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -march=armv7-a -mthumb"
%endif

# PIE, full relro
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -DPIC -fPIC -Wl,-z,relro -Wl,-z,now"

# Add fake RPATH
MOZ_OPT_FLAGS="$MOZ_OPT_FLAGS -Wl,-rpath,/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"

# If MOZ_DEBUG_FLAGS is empty, firefox's build will default it to "-g" which
# overrides the -g0 from line above and breaks building on s390
# (OOM when linking, rhbz#1238225)
export MOZ_DEBUG_FLAGS=" "

export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"

export MOZ_PARALLEL_BUILD=%build_parallel_jobs
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export RANLIB="llvm-ranlib"
export LLVM_PROFDATA="llvm-profdata"
export ALTWRAP_LLVM_VERSION="%llvm_version"

export LIBIDL_CONFIG=/usr/bin/libIDL-config-2
export SHELL=/bin/sh

export RUST_BACKTRACE=1
%ifarch armh %{ix86}
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=0"
%else
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=2"
%endif

CBINDGEN_HOME="$PWD/.rpm/cbindgen-vendor"
CBINDGEN_BINDIR="$CBINDGEN_HOME/bin"

if [ ! -x "$CBINDGEN_BINDIR/cbindgen" ]; then
	cat > "$CBINDGEN_HOME/config" <<-EOF
	[source.crates-io]
	replace-with = "vendored-sources"

	[source.vendored-sources]
	directory = "$CBINDGEN_HOME"
	EOF

	env CARGO_HOME="$CBINDGEN_HOME" \
		cargo install cbindgen

	export PATH="$CBINDGEN_BINDIR:$PATH"
fi

#export WASM_SANDBOXED_LIBRARIES=graphite,ogg
#export WASM_CC="$CC --target=wasm32-wasi"
#export WASM_CXX="$CXX --target=wasm32-wasi"

export srcdir="$PWD"
export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=system

python3 ./mach build

while read -r loc; do
	python3 ./mach build chrome-$loc
done < .rpm/firefox-l10n.txt

make -C objdir/browser/installer multilocale.txt

$CC $CFLAGS \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DMOZ_PROGRAM=\"%firefox_prefix/firefox\" \
	-DMOZ_DIST_BIN=\"%firefox_prefix\"\
	.rpm/firefox.c -o firefox


%install
export SHELL=/bin/sh
export MOZ_CHROME_MULTILOCALE="$(tr '\n' ' ' < .rpm/firefox-l10n.txt)"

mkdir -p \
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
install -D -m 644 .rpm/firefox-prefs.js %buildroot/%firefox_prefix/browser/defaults/preferences/all-altlinux.js
install -D -m 644 .rpm/firefox-privacy-prefs.js %buildroot/%_sysconfdir/firefox/pref/all-privacy.js

sed -i \
	-e 's#@VERSION@#%{version}#g' \
	%buildroot/%_sysconfdir/firefox/pref/all-privacy.js

cat > %buildroot/%firefox_prefix/browser/defaults/preferences/firefox-l10n.js <<EOF
pref("intl.locale.matchOS", true);
pref("intl.locale.requested", "");
pref("general.useragent.locale", "chrome://global/locale/intl.properties");
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

install -m755 firefox %buildroot/%_bindir/firefox
ln -s firefox %buildroot/%_bindir/firefox-wayland

install -D -m 644 .rpm/distribution.ini \
	%buildroot/%firefox_prefix/distribution/distribution.ini

install -D -m 644 .rpm/firefox.desktop \
	%buildroot/%_datadir/applications/firefox.desktop

install -D -m 644 .rpm/firefox-search-provider.ini \
	%buildroot/%_datadir/gnome-shell/search-providers/firefox-search-provider.ini

# Add alternatives
mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/firefox <<EOF
%_bindir/xbrowser	%_bindir/firefox	200
%_bindir/x-www-browser	%_bindir/firefox	200
EOF

rm -f -- \
	%buildroot/%firefox_prefix/removed-files

# Remove devel files
rm -rf -- \
	%buildroot/%_includedir/%name \
	%buildroot/%_datadir/idl/%name \
	%buildroot/%_libdir/%name-devel \
#


# Add real RPATH
(set +x
	rpath="/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"
	find %buildroot -type f |
	while read f; do
		t="$(readlink -ev "$f")"
		file "$t" | fgrep -qs ELF ||
			continue
		chrpath -l "$t" |
			fgrep -qs \
				-e "RPATH=$rpath" \
				-e "RUNPATH=$rpath" ||
			continue
		chrpath -r "%firefox_prefix" "$t"
	done
)

%files
%dir %_sysconfdir/firefox
%dir %_sysconfdir/firefox/pref
%_altdir/firefox
%_bindir/firefox
%_bindir/firefox-wayland
%firefox_prefix
%mozilla_arch_extdir/%firefox_cid
%mozilla_noarch_extdir/%firefox_cid
%_datadir/applications/firefox.desktop
%_datadir/gnome-shell/search-providers/firefox-search-provider.ini
%_iconsdir/hicolor/16x16/apps/firefox.png
%_iconsdir/hicolor/22x22/apps/firefox.png
%_iconsdir/hicolor/24x24/apps/firefox.png
%_iconsdir/hicolor/32x32/apps/firefox.png
%_iconsdir/hicolor/48x48/apps/firefox.png
%_iconsdir/hicolor/256x256/apps/firefox.png

%files -n firefox-config-privacy
%config(noreplace) %_sysconfdir/firefox/pref/all-privacy.js

%changelog
* Mon Dec 19 2022 Alexey Gladkov <legion@altlinux.ru> 108.0.1-alt1
- New release (108.0.1).

* Wed Dec 14 2022 Alexey Gladkov <legion@altlinux.ru> 108.0-alt1
- New release (108.0).
- Security fixes:
  + CVE-2022-46871: libusrsctp library out of date
  + CVE-2022-46872: Arbitrary file read from a compromised content process
  + CVE-2022-46873: Firefox did not implement the CSP directive unsafe-hashes
  + CVE-2022-46874: Drag and Dropped Filenames could have been truncated to malicious extensions
  + CVE-2022-46875: Download Protections were bypassed by .atloc and .ftploc files on Mac OS
  + CVE-2022-46877: Fullscreen notification bypass
  + CVE-2022-46878: Memory safety bugs fixed in Firefox 108 and Firefox ESR 102.6
  + CVE-2022-46879: Memory safety bugs fixed in Firefox 108

* Sat Dec 10 2022 Alexey Gladkov <legion@altlinux.ru> 107.0.1-alt2
- glxtest: Add patch to delay terminating the EGLDisplay.

* Fri Dec 02 2022 Alexey Gladkov <legion@altlinux.ru> 107.0.1-alt1
- New release (107.0.1).

* Tue Nov 15 2022 Alexey Gladkov <legion@altlinux.ru> 107.0-alt1
- New release (107.0).
- Security fixes:
  + CVE-2022-45403: Service Workers might have learned size of cross-origin media files
  + CVE-2022-45404: Fullscreen notification bypass
  + CVE-2022-45405: Use-after-free in InputStream implementation
  + CVE-2022-45406: Use-after-free of a JavaScript Realm
  + CVE-2022-45407: Loading fonts on workers was not thread-safe
  + CVE-2022-45408: Fullscreen notification bypass via windowName
  + CVE-2022-45409: Use-after-free in Garbage Collection
  + CVE-2022-45410: ServiceWorker-intercepted requests bypassed SameSite cookie policy
  + CVE-2022-45411: Cross-Site Tracing was possible via non-standard override headers
  + CVE-2022-45412: Symlinks may resolve to partially uninitialized buffers
  + CVE-2022-45413: SameSite=Strict cookies could have been sent cross-site via intent URLs
  + CVE-2022-40674: Use-after-free vulnerability in expat
  + CVE-2022-45415: Downloaded file may have been saved with malicious extension
  + CVE-2022-45416: Keystroke Side-Channel Leakage
  + CVE-2022-45417: Service Workers in Private Browsing Mode may have been written to disk
  + CVE-2022-45418: Custom mouse cursor could have been drawn over browser UiI
  + CVE-2022-45419: Deleting a security exception did not take effect immediately
  + CVE-2022-45420: Iframe contents could be rendered outside the iframe
  + CVE-2022-45421: Memory safety bugs fixed in Firefox 107 and Firefox ESR 102.5

* Sat Nov 05 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.5-alt1
- New release (106.0.5).

* Thu Oct 27 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.2-alt1
- New release (106.0.2).

* Fri Oct 21 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.1-alt1
- New release (106.0.1).

* Tue Oct 18 2022 Alexey Gladkov <legion@altlinux.ru> 106.0-alt1
- New release (106.0).
- Security fixes:
  + CVE-2022-42927: Same-origin policy violation could have leaked cross-origin URLs
  + CVE-2022-42928: Memory Corruption in JS Engine
  + CVE-2022-42929: Denial of Service via window.print
  + CVE-2022-42930: Race condition in DOM Workers
  + CVE-2022-42931: Username saved to a plaintext file on disk
  + CVE-2022-42932: Memory safety bugs fixed in Firefox 106 and Firefox ESR 102.4

* Sat Oct 08 2022 Alexey Gladkov <legion@altlinux.ru> 105.0.3-alt1
- New release (105.0.3).

* Thu Oct 06 2022 Alexey Gladkov <legion@altlinux.ru> 105.0.2-alt1
- New release (105.0.2).

* Fri Sep 23 2022 Alexey Gladkov <legion@altlinux.ru> 105.0.1-alt1
- New release (105.0.1).

* Wed Sep 21 2022 Alexey Gladkov <legion@altlinux.ru> 105.0-alt1
- New release (105.0).
- Security fixes:
  + CVE-2022-40959: Bypassing FeaturePolicy restrictions on transient pages
  + CVE-2022-40960: Data-race when parsing non-UTF-8 URLs in threads
  + CVE-2022-40958: Bypassing Secure Context restriction for cookies with __Host and __Secure prefix
  + CVE-2022-40961: Stack-buffer overflow when initializing Graphics
  + CVE-2022-40956: Content-Security-Policy base-uri bypass
  + CVE-2022-40957: Incoherent instruction cache when building WASM on ARM64
  + CVE-2022-40962: Memory safety bugs fixed in Firefox 105 and Firefox ESR 102.3

* Thu Sep 08 2022 Alexey Gladkov <legion@altlinux.ru> 104.0.2-alt2
- Merge firefox-wayland to firefox (ALT#43733).
- Drop gtk2 support.

* Wed Sep 07 2022 Alexey Gladkov <legion@altlinux.ru> 104.0.2-alt1
- New release (104.0.2).
- Use LLVM 14.

* Wed Aug 31 2022 Alexey Gladkov <legion@altlinux.ru> 104.0.1-alt1
- New release (104.0.1).

* Tue Aug 16 2022 Alexey Gladkov <legion@altlinux.ru> 104.0-alt1
- New release (104.0).
- Security fixes:
  + CVE-2022-38472: Address bar spoofing via XSLT error handling
  + CVE-2022-38473: Cross-origin XSLT Documents would have inherited the parent's permissions
  + CVE-2022-38474: Recording notification not shown when microphone was recording on Android
  + CVE-2022-38475: Attacker could write a value to a zero-length array
  + CVE-2022-38477: Memory safety bugs fixed in Firefox 104 and Firefox ESR 102.2
  + CVE-2022-38478: Memory safety bugs fixed in Firefox 104, Firefox ESR 102.2, and Firefox ESR 91.13

* Mon Aug 01 2022 Alexey Gladkov <legion@altlinux.ru> 103.0.1-alt1
- New release (103.0.1).

* Tue Jul 26 2022 Alexey Gladkov <legion@altlinux.ru> 103.0-alt1
- New release (103.0).
- Security fixes:
  + CVE-2022-36319: Mouse Position spoofing with CSS transforms
  + CVE-2022-36317: Long URL would hang Firefox for Android
  + CVE-2022-36318: Directory indexes for bundled resources reflected URL parameters
  + CVE-2022-36314: Opening local <code>.lnk</code> files could cause unexpected network loads
  + CVE-2022-36315: Preload Cache Bypasses Subresource Integrity
  + CVE-2022-36316: Performance API leaked whether a cross-site resource is redirecting
  + CVE-2022-36320: Memory safety bugs fixed in Firefox 103
  + CVE-2022-2505: Memory safety bugs fixed in Firefox 103 and 102.1

* Wed Jun 29 2022 Alexey Gladkov <legion@altlinux.ru> 102.0-alt1
- New release (102.0).
- Use internal libevent.
- Security fixes:
  + CVE-2022-34479: A popup window could be resized in a way to overlay the address bar with web content
  + CVE-2022-34470: Use-after-free in nsSHistory
  + CVE-2022-34468: CSP sandbox header without `allow-scripts` can be bypassed via retargeted javascript: URI
  + CVE-2022-34482: Drag and drop of malicious image could have led to malicious executable and potential code execution
  + CVE-2022-34483: Drag and drop of malicious image could have led to malicious executable and potential code execution
  + CVE-2022-34476: ASN.1 parser could have been tricked into accepting malformed ASN.1
  + CVE-2022-34481: Potential integer overflow in ReplaceElementsAt
  + CVE-2022-34474: Sandboxed iframes could redirect to external schemes
  + CVE-2022-34469: TLS certificate errors on HSTS-protected domains could be bypassed by the user on Firefox for Android
  + CVE-2022-34471: Compromised server could trick a browser into an addon downgrade
  + CVE-2022-34472: Unavailable PAC file resulted in OCSP requests being blocked
  + CVE-2022-34478: Microsoft protocols can be attacked if a user accepts a prompt
  + CVE-2022-2200: Undesired attributes could be set as part of prototype pollution
  + CVE-2022-34480: Free of uninitialized pointer in lg_init
  + CVE-2022-34477: MediaError message property leaked information on cross-origin same-site pages
  + CVE-2022-34475: HTML Sanitizer could have been bypassed via same-origin script via use tags
  + CVE-2022-34473: HTML Sanitizer could have been bypassed via use tags
  + CVE-2022-34484: Memory safety bugs fixed in Firefox 102 and Firefox ESR 91.11
  + CVE-2022-34485: Memory safety bugs fixed in Firefox 102

* Fri Jun 10 2022 Alexey Gladkov <legion@altlinux.ru> 101.0.1-alt1
- New release (101.0.1).

* Thu Jun 02 2022 Alexey Gladkov <legion@altlinux.ru> 101.0-alt2
- Wayland: Add fix for utility popups (MOZ#1771104).
- Use LLVM12 again.

* Wed Jun 01 2022 Alexey Gladkov <legion@altlinux.ru> 101.0-alt1
- New release (101.0).
- Use internal cbindgen again.
- Security fixes:
  + CVE-2022-31736: Cross-Origin resource's length leaked
  + CVE-2022-31737: Heap buffer overflow in WebGL
  + CVE-2022-31738: Browser window spoof using fullscreen mode
  + CVE-2022-31739: Attacker-influenced path traversal when saving downloaded files
  + CVE-2022-31740: Register allocation problem in WASM on arm64
  + CVE-2022-31741: Uninitialized variable leads to invalid memory read
  + CVE-2022-31742: Querying a WebAuthn token with a large number of allowCredential entries may have leaked cross-origin information
  + CVE-2022-31743: HTML Parsing incorrectly ended HTML comments prematurely
  + CVE-2022-31744: CSP bypass enabling stylesheet injection
  + CVE-2022-31745: Incorrect Assertion caused by unoptimized array shift operations
  + CVE-2022-1919: Memory Corruption when manipulating webp images
  + CVE-2022-31747: Memory safety bugs fixed in Firefox 101 and Firefox ESR 91.10
  + CVE-2022-31748: Memory safety bugs fixed in Firefox 101

* Sat May 21 2022 Alexey Gladkov <legion@altlinux.ru> 100.0.2-alt1
- New release (100.0.2).
- Security fixes:
  + CVE-2022-1802: Prototype pollution in Top-Level Await implementation
  + CVE-2022-1529: Untrusted input used in JavaScript object indexing, leading to prototype pollution

* Tue May 03 2022 Alexey Gladkov <legion@altlinux.ru> 100.0-alt1
- New release (100.0).
- Security fixes:
  + CVE-2022-29914: Fullscreen notification bypass using popups
  + CVE-2022-29909: Bypassing permission prompt in nested browsing contexts
  + CVE-2022-29916: Leaking browser history with CSS variables
  + CVE-2022-29911: iframe Sandbox bypass
  + CVE-2022-29912: Reader mode bypassed SameSite cookies
  + CVE-2022-29910: Firefox for Android forgot HTTP Strict Transport Security settings
  + CVE-2022-29915: Leaking cross-origin redirect through the Performance API
  + CVE-2022-29917: Memory safety bugs fixed in Firefox 100 and Firefox ESR 91.9
  + CVE-2022-29918: Memory safety bugs fixed in Firefox 100

* Fri Apr 15 2022 Alexey Gladkov <legion@altlinux.ru> 99.0.1-alt1
- New release (99.0.1).

* Tue Apr 05 2022 Alexey Gladkov <legion@altlinux.ru> 99.0-alt1
- New release (99.0).
- Stop shipping user-installed search plugins (MOZ#1643679, MOZ#1203167).
- Exclude arch ppc64le.
- Security fixes:
  + CVE-2022-1097: Use-after-free in NSSToken objects
  + CVE-2022-28281: Out of bounds write due to unexpected WebAuthN Extensions
  + CVE-2022-28282: Use-after-free in DocumentL10n::TranslateDocument
  + CVE-2022-28283: Missing security checks for fetching sourceMapURL
  + CVE-2022-28284: Script could be executed via svg's use element
  + CVE-2022-28285: Incorrect AliasSet used in JIT Codegen
  + CVE-2022-28286: iframe contents could be rendered outside the border
  + CVE-2022-28287: Text Selection could crash Firefox
  + CVE-2022-24713: Denial of Service via complex regular expressions
  + CVE-2022-28289: Memory safety bugs fixed in Firefox 99 and Firefox ESR 91.8
  + CVE-2022-28288: Memory safety bugs fixed in Firefox 99

* Thu Mar 24 2022 Alexey Gladkov <legion@altlinux.ru> 98.0.2-alt1
- New release (98.0.2).

* Thu Mar 17 2022 Alexey Gladkov <legion@altlinux.ru> 98.0.1-alt1
- New release (98.0.1).
- Update localization.
- Prevented exclusion some of Russian extensions and bookmarks.

* Tue Mar 08 2022 Alexey Gladkov <legion@altlinux.ru> 98.0-alt1
- New release (98.0).
- Security fixes:
  + CVE-2022-26383: Browser window spoof using fullscreen mode
  + CVE-2022-26384: iframe allow-scripts sandbox bypass
  + CVE-2022-26387: Time-of-check time-of-use bug when verifying add-on signatures
  + CVE-2022-26381: Use-after-free in text reflows
  + CVE-2022-26382: Autofill Text could be exfiltrated via side-channel attacks
  + CVE-2022-26385: Use-after-free in thread shutdown
  + CVE-2022-0843: Memory safety bugs fixed in Firefox 98

* Sun Mar 06 2022 Alexey Gladkov <legion@altlinux.ru> 97.0.2-alt1
- New release (97.0.2).
- Security fixes:
  + CVE-2022-26485: Use-after-free in XSLT parameter processing
  + CVE-2022-26486: Use-after-free in WebGPU IPC Framework

* Fri Feb 18 2022 Alexey Gladkov <legion@altlinux.ru> 97.0.1-alt1
- New release (97.0.1).

* Wed Feb 09 2022 Alexey Gladkov <legion@altlinux.ru> 97.0-alt1
- New release (97.0).
- Security fixes:
  + CVE-2022-22753: Privilege Escalation to SYSTEM on Windows via Maintenance Service
  + CVE-2022-22754: Extensions could have bypassed permission confirmation during update
  + CVE-2022-22755: XSL could have allowed JavaScript execution after a tab was closed
  + CVE-2022-22756: Drag and dropping an image could have resulted in the dropped object being an executable
  + CVE-2022-22757: Remote Agent did not prevent local websites from connecting
  + CVE-2022-22758: tel: links could have sent USSD codes to the dialer on Firefox for Android
  + CVE-2022-22759: Sandboxed iframes could have executed script if the parent appended elements
  + CVE-2022-22760: Cross-Origin responses could be distinguished between script and non-script content-types
  + CVE-2022-22761: frame-ancestors Content Security Policy directive was not enforced for framed extension pages
  + CVE-2022-22762: JavaScript Dialogs could have been displayed over other domains on Firefox for Android
  + CVE-2022-22764: Memory safety bugs fixed in Firefox 97 and Firefox ESR 91.6
  + CVE-2022-0511: Memory safety bugs fixed in Firefox 97

* Tue Feb 01 2022 Alexey Gladkov <legion@altlinux.ru> 96.0.3-alt1
- New release (96.0.3).
- Enable debuginfo on 64-bit architectures.
- Privacy config:
  + Disable merino service.
  + Disable more suggests in the urlbar.

* Fri Jan 21 2022 Alexey Gladkov <legion@altlinux.ru> 96.0.2-alt2
- Add forgotten source code updates.

* Thu Jan 20 2022 Alexey Gladkov <legion@altlinux.ru> 96.0.2-alt1
- New release (96.0.2).

* Sat Jan 15 2022 Alexey Gladkov <legion@altlinux.ru> 96.0.1-alt1
- New release (96.0.1).

* Wed Jan 12 2022 Alexey Gladkov <legion@altlinux.ru> 96.0-alt1
- New release (96.0).
- Disable webrtc for armh, ppc64le.
- Security fixes:
  + CVE-2022-22746: Calling into reportValidity could have lead to fullscreen window spoof
  + CVE-2022-22743: Browser window spoof using fullscreen mode
  + CVE-2022-22742: Out-of-bounds memory access when inserting text in edit mode
  + CVE-2022-22741: Browser window spoof using fullscreen mode
  + CVE-2022-22740: Use-after-free of ChannelEventQueue::mOwner
  + CVE-2022-22738: Heap-buffer-overflow in blendGaussianBlur
  + CVE-2022-22737: Race condition when playing audio files
  + CVE-2021-4140: Iframe sandbox bypass with XSLT
  + CVE-2022-22750: IPC passing of resource handles could have lead to sandbox bypass
  + CVE-2022-22749: Lack of URL restrictions when scanning QR codes
  + CVE-2022-22748: Spoofed origin on external protocol launch dialog
  + CVE-2022-22745: Leaking cross-origin URLs through securitypolicyviolation event
  + CVE-2022-22744: The 'Copy as curl' feature in DevTools did not fully escape website-controlled data, potentially leading to command injection
  + CVE-2022-22747: Crash when handling empty pkcs7 sequence
  + CVE-2022-22736: Potential local privilege escalation when loading modules from the install directory.
  + CVE-2022-22739: Missing throttling on external protocol launch dialog
  + CVE-2022-22751: Memory safety bugs fixed in Firefox 96 and Firefox ESR 91.5
  + CVE-2022-22752: Memory safety bugs fixed in Firefox 96

* Fri Dec 17 2021 Alexey Gladkov <legion@altlinux.ru> 95.0.1-alt1
- New release (95.0.1).

* Wed Dec 08 2021 Alexey Gladkov <legion@altlinux.ru> 95.0-alt1
- New release (95.0).
- Security fixes:
  + CVE-2021-43536: URL leakage when navigating while executing asynchronous function
  + CVE-2021-43537: Heap buffer overflow when using structured clone
  + CVE-2021-43538: Missing fullscreen and pointer lock notification when requesting both
  + CVE-2021-43539: GC rooting failure when calling wasm instance methods
  + MOZ-2021-0010: Use-after-free in fullscreen objects on MacOS
  + CVE-2021-43540: WebExtensions could have installed persistent ServiceWorkers
  + CVE-2021-43541: External protocol handler parameters were unescaped
  + CVE-2021-43542: XMLHttpRequest error codes could have leaked the existence of an external protocol handler
  + CVE-2021-43543: Bypass of CSP sandbox directive when embedding
  + CVE-2021-43544: Receiving a malicious URL as text through a SEND intent could have led to XSS
  + CVE-2021-43545: Denial of Service when using the Location API in a loop
  + CVE-2021-43546: Cursor spoofing could overlay user interface when native cursor is zoomed
  + MOZ-2021-0009: Memory safety bugs fixed in Firefox 95 and Firefox ESR 91.4

* Fri Nov 19 2021 Alexey Gladkov <legion@altlinux.ru> 94.0.2-alt1
- New release (94.0.2).

* Tue Nov 02 2021 Alexey Gladkov <legion@altlinux.ru> 94.0-alt1
- New release (94.0).
- Security fixes:
  + CVE-2021-38503: iframe sandbox rules did not apply to XSLT stylesheets
  + CVE-2021-38504: Use-after-free in file picker dialog
  + CVE-2021-38505: Windows 10 Cloud Clipboard may have recorded sensitive user data
  + CVE-2021-38506: Firefox could be coaxed into going into fullscreen mode without notification or warning
  + CVE-2021-38507: Opportunistic Encryption in HTTP2 could be used to bypass the Same-Origin-Policy on services hosted on other ports
  + MOZ-2021-0003: Universal XSS in Firefox for Android via QR Code URLs
  + CVE-2021-38508: Permission Prompt could be overlaid, resulting in user confusion and potential spoofing
  + MOZ-2021-0004: Web Extensions could access pre-redirect URL when their context menu was triggered by a user
  + CVE-2021-38509: Javascript alert box could have been spoofed onto an arbitrary domain
  + CVE-2021-38510: Download Protections were bypassed by .inetloc files on Mac OS
  + MOZ-2021-0005: 'Copy Image Link' context menu action could have been abused to see authentication tokens
  + MOZ-2021-0006: URL Parsing may incorrectly parse internationalized domains
  + MOZ-2021-0007: Memory safety bugs fixed in Firefox 94 and Firefox ESR 91.3

* Wed Oct 06 2021 Alexey Gladkov <legion@altlinux.ru> 93.0-alt1
- New release (93.0).
- Security fixes:
  + CVE-2021-38496: Use-after-free in MessageTask
  + CVE-2021-38497: Validation message could have been overlaid on another origin
  + CVE-2021-38498: Use-after-free of nsLanguageAtomService object
  + CVE-2021-32810: Data race in crossbeam-deque
  + CVE-2021-38500: Memory safety bugs fixed in Firefox 93, Firefox ESR 78.15, and Firefox ESR 91.2
  + CVE-2021-38501: Memory safety bugs fixed in Firefox 93 and Firefox ESR 91.2
  + CVE-2021-38499: Memory safety bugs fixed in Firefox 93

* Tue Sep 28 2021 Alexey Gladkov <legion@altlinux.ru> 92.0.1-alt1
- New release (92.0.1).

* Tue Sep 07 2021 Alexey Gladkov <legion@altlinux.ru> 92.0-alt1
- New release (92.0).
- Security fixes:
  + CVE-2021-29993: Handling custom intents could lead to crashes and UI spoofs
  + CVE-2021-38491: Mixed-Content-Blocking was unable to check opaque origins
  + CVE-2021-38492: Navigating to `mk:` URL scheme could load Internet Explorer
  + CVE-2021-38493: Memory safety bugs fixed in Firefox 92, Firefox ESR 78.14 and Firefox ESR 91.1
  + CVE-2021-38494: Memory safety bugs fixed in Firefox 92

* Tue Sep 07 2021 Alexey Gladkov <legion@altlinux.ru> 91.0.2-alt2
- Rebuild with llvm12.0.

* Wed Aug 25 2021 Alexey Gladkov <legion@altlinux.ru> 91.0.2-alt1
- New release (91.0.2).

* Wed Aug 18 2021 Alexey Gladkov <legion@altlinux.ru> 91.0.1-alt1
- New release (91.0.1).
- Security fixes:
  + CVE-2021-29991: Header Splitting possible with HTTP/3 Responses

* Tue Aug 10 2021 Alexey Gladkov <legion@altlinux.ru> 91.0-alt1
- New release (91.0).
- Security fixes:
  + CVE-2021-29986: Race condition when resolving DNS names could have led to memory corruption
  + CVE-2021-29981: Live range splitting could have led to conflicting assignments in the JIT
  + CVE-2021-29988: Memory corruption as a result of incorrect style treatment
  + CVE-2021-29983: Firefox for Android could get stuck in fullscreen mode
  + CVE-2021-29984: Incorrect instruction reordering during JIT optimization
  + CVE-2021-29980: Uninitialized memory in a canvas object could have led to memory corruption
  + CVE-2021-29987: Users could have been tricked into accepting unwanted permissions on Linux
  + CVE-2021-29985: Use-after-free media channels
  + CVE-2021-29982: Single bit data leak due to incorrect JIT optimization and type confusion
  + CVE-2021-29989: Memory safety bugs fixed in Firefox 91 and Firefox ESR 78.13
  + CVE-2021-29990: Memory safety bugs fixed in Firefox 91

* Fri Jul 23 2021 Alexey Gladkov <legion@altlinux.ru> 90.0.2-alt1
- New release (90.0.2).

* Tue Jul 20 2021 Alexey Gladkov <legion@altlinux.ru> 90.0.1-alt1
- New release (90.0.1).

* Tue Jul 13 2021 Alexey Gladkov <legion@altlinux.ru> 90.0-alt1
- New release (90.0).
- Move rpm-build-firefox from firefox to separate package.
- Security fixes:
  + CVE-2021-29970: Use-after-free in accessibility features of a document
  + CVE-2021-29971: Granted permissions only compared host; omitting scheme and port on Android
  + CVE-2021-30547: Out of bounds write in ANGLE
  + CVE-2021-29972: Use of out-of-date library included use-after-free vulnerability
  + CVE-2021-29973: Password autofill on HTTP websites was enabled without user interaction on Android
  + CVE-2021-29974: HSTS errors could be overridden when network partitioning was enabled
  + CVE-2021-29975: Text message could be overlaid on top of another website
  + CVE-2021-29976: Memory safety bugs fixed in Firefox 90 and Firefox ESR 78.12
  + CVE-2021-29977: Memory safety bugs fixed in Firefox 90

* Fri Jul 09 2021 Alexey Gladkov <legion@altlinux.ru> 89.0.2-alt2
- Enable searching system- and account-global directories for extensions (ALT#40364).

* Tue Jun 29 2021 Alexey Gladkov <legion@altlinux.ru> 89.0.2-alt1
- New release (89.0.2).

* Thu Jun 17 2021 Alexey Gladkov <legion@altlinux.ru> 89.0.1-alt1
- New release (89.0.1).
- Security fixes:
  + CVE-2021-29968: Out of bounds read when drawing text characters onto a Canvas

* Thu Jun 03 2021 Alexey Gladkov <legion@altlinux.ru> 89.0-alt1
- New release (89.0).
- Security fixes:
  + CVE-2021-29965: Password Manager on Firefox for Android susceptible to domain spoofing
  + CVE-2021-29960: Filenames printed from private browsing mode incorrectly retained in preferences
  + CVE-2021-29961: Firefox UI spoof using `<select>` elements and CSS scaling
  + CVE-2021-29963: Shared cookies for search suggestions in private browsing mode
  + CVE-2021-29964: Out of bounds-read when parsing a `WM_COPYDATA` message
  + CVE-2021-29959: Devices could be re-enabled without additional permission prompt
  + CVE-2021-29962: No rate-limiting for popups on Firefox for Android
  + CVE-2021-29967: Memory safety bugs fixed in Firefox 89 and Firefox ESR 78.11
  + CVE-2021-29966: Memory safety bugs fixed in Firefox 89

* Fri May 07 2021 Alexey Gladkov <legion@altlinux.ru> 88.0.1-alt1
- New release (88.0.1).
- Security fixes:
  + CVE-2021-29953: Universal Cross-Site Scripting
  + CVE-2021-29952: Race condition in Web Render Components

* Mon Apr 19 2021 Alexey Gladkov <legion@altlinux.ru> 88.0-alt1
- New release (88.0).
- Security fixes:
  + CVE-2021-23994: Out of bound write due to lazy initialization
  + CVE-2021-23995: Use-after-free in Responsive Design Mode
  + CVE-2021-23996: Content rendered outside of webpage viewport
  + CVE-2021-23997: Use-after-free when freeing fonts from cache
  + CVE-2021-23998: Secure Lock icon could have been spoofed
  + CVE-2021-23999: Blob URLs may have been granted additional privileges
  + CVE-2021-24000: requestPointerLock() could be applied to a tab different from the visible tab
  + CVE-2021-24001: Testing code could have enabled session history manipulations by a compromised content process
  + CVE-2021-24002: Arbitrary FTP command execution on FTP servers using an encoded URL
  + CVE-2021-29945: Incorrect size computation in WebAssembly JIT could lead to null-reads
  + CVE-2021-29944: HTML injection vulnerability in Firefox for Android's Reader View
  + CVE-2021-29946: Port blocking could be bypassed
  + CVE-2021-29947: Memory safety bugs fixed in Firefox 88

* Wed Mar 24 2021 Alexey Gladkov <legion@altlinux.ru> 87.0-alt1
- New release (87.0).
- Security fixes:
  + CVE-2021-23981: Texture upload into an unbound backing buffer resulted in an out-of-bound read
  + CVE-2021-23982: Internal network hosts could have been probed by a malicious webpage
  + CVE-2021-23983: Transitions for invalid ::marker properties resulted in memory corruption
  + CVE-2021-23984: Malicious extensions could have spoofed popup information
  + CVE-2021-23985: Devtools remote debugging feature could have been enabled without indication to the user
  + CVE-2021-23986: A malicious extension could have performed credential-less same origin policy violations
  + CVE-2021-23987: Memory safety bugs fixed in Firefox 87 and Firefox ESR 78.9
  + CVE-2021-23988: Memory safety bugs fixed in Firefox 87

* Mon Mar 01 2021 Alexey Gladkov <legion@altlinux.ru> 86.0-alt1
- New release (86.0).
- Security fixes:
  + CVE-2021-23969: Content Security Policy violation report could have contained the destination of a redirect
  + CVE-2021-23970: Multithreaded WASM triggered assertions validating separation of script domains
  + CVE-2021-23968: Content Security Policy violation report could have contained the destination of a redirect
  + CVE-2021-23974: noscript elements could have led to an HTML Sanitizer bypass
  + CVE-2021-23971: A website's Referrer-Policy could have been be overridden, potentially resulting in the full URL being sent as a Referrer
  + CVE-2021-23976: Local spoofing of web manifests for arbitrary pages in Firefox for Android
  + CVE-2021-23977: Malicious application could read sensitive data from Firefox for Android's application directories
  + CVE-2021-23972: HTTP Auth phishing warning was omitted when a redirect is cached
  + CVE-2021-23975: about:memory Measure function caused an incorrect pointer operation
  + CVE-2021-23973: MediaError message property could have leaked information about cross-origin resources
  + CVE-2021-23978: Memory safety bugs fixed in Firefox 86 and Firefox ESR 78.8
  + CVE-2021-23979: Memory safety bugs fixed in Firefox 86

* Tue Feb 09 2021 Alexey Gladkov <legion@altlinux.ru> 85.0.2-alt1
- New release (85.0.2).

* Fri Feb 05 2021 Alexey Gladkov <legion@altlinux.ru> 85.0.1-alt1
- New release (85.0.1).
- Security fixes:
  + MOZ-2021-0001: Buffer overflow in depth pitch calculations for compressed textures

* Tue Jan 26 2021 Alexey Gladkov <legion@altlinux.ru> 85.0-alt1
- New release (85.0).
- Security fixes:
  + CVE-2021-23953: Cross-origin information leakage via redirected PDF requests
  + CVE-2021-23954: Type confusion when using logical assignment operators in JavaScript switch statements
  + CVE-2021-23955: Clickjacking across tabs through misusing requestPointerLock
  + CVE-2021-23956: File picker dialog could have been used to disclose a complete directory
  + CVE-2021-23957: Iframe sandbox could have been bypassed on Android via the intent URL scheme
  + CVE-2021-23958: Screen sharing permission leaked across tabs
  + CVE-2021-23959: Cross-Site Scripting in error pages on Firefox for Android
  + CVE-2021-23960: Use-after-poison for incorrectly redeclared JavaScript variables during GC
  + CVE-2021-23961: More internal network hosts could have been probed by a malicious webpage
  + CVE-2021-23962: Use-after-poison in <code>nsTreeBodyFrame::RowCountChanged</code>
  + CVE-2021-23963: Permission prompt inaccessible after asking for additional permissions
  + CVE-2021-23964: Memory safety bugs fixed in Firefox 85 and Firefox ESR 78.7
  + CVE-2021-23965: Memory safety bugs fixed in Firefox 85

* Wed Jan 06 2021 Alexey Gladkov <legion@altlinux.ru> 84.0.2-alt1
- New release (84.0.2).
- Security fixes:
  + CVE-2020-16044: Use-after-free write when handling a malicious COOKIE-ECHO SCTP chunk
- Add firefox GNOME Shell search provider.
- Enable smooth scrolling option.

* Sat Dec 26 2020 Alexey Gladkov <legion@altlinux.ru> 84.0.1-alt1
- New release (84.0.1).
- No longer requires autoconf_2.13 to build.

* Thu Dec 17 2020 Alexey Gladkov <legion@altlinux.ru> 84.0-alt1
- New release (84.0).
- Security fixes:
  + CVE-2020-16042: Operations on a BigInt could have caused uninitialized memory to be exposed
  + CVE-2020-26971: Heap buffer overflow in WebGL
  + CVE-2020-26972: Use-After-Free in WebGL
  + CVE-2020-26973: CSS Sanitizer performed incorrect sanitization
  + CVE-2020-26974: Incorrect cast of StyleGenericFlexBasis resulted in a heap use-after-free
  + CVE-2020-26975: Malicious applications on Android could have induced Firefox for Android into sending arbitrary attacker-specified headers
  + CVE-2020-26976: HTTPS pages could have been intercepted by a registered service worker when they should not have been
  + CVE-2020-26977: URL spoofing via unresponsive port in Firefox for Android
  + CVE-2020-26978: Internal network hosts could have been probed by a malicious webpage
  + CVE-2020-26979: When entering an address in the address or search bars, a website could have redirected the user before they were navigated to the intended url
  + CVE-2020-35111: The proxy.onRequest API did not catch view-source URLs
  + CVE-2020-35112: Opening an extension-less download may have inadvertently launched an executable instead
  + CVE-2020-35113: Memory safety bugs fixed in Firefox 84 and Firefox ESR 78.6
  + CVE-2020-35114: Memory safety bugs fixed in Firefox 84

* Wed Nov 25 2020 Alexey Gladkov <legion@altlinux.ru> 83.0-alt2
- Fix alternatives.

* Tue Nov 17 2020 Alexey Gladkov <legion@altlinux.ru> 83.0-alt1
- New release (83.0).
- Security fixes:
  + CVE-2020-26951: Parsing mismatches could confuse and bypass security sanitizer for chrome privileged code
  + CVE-2020-26952: Out of memory handling of JITed, inlined functions could lead to a memory corruption
  + CVE-2020-16012: Variable time processing of cross-origin images during drawImage calls
  + CVE-2020-26953: Fullscreen could be enabled without displaying the security UI
  + CVE-2020-26954: Local spoofing of web manifests for arbitrary pages in Firefox for Android
  + CVE-2020-26955: Cookies set during file downloads are shared between normal and Private Browsing Mode in Firefox for Android
  + CVE-2020-26956: XSS through paste (manual and clipboard API)
  + CVE-2020-26957: OneCRL was not working in Firefox for Android
  + CVE-2020-26958: Requests intercepted through ServiceWorkers lacked MIME type restrictions
  + CVE-2020-26959: Use-after-free in WebRequestService
  + CVE-2020-26960: Potential use-after-free in uses of nsTArray
  + CVE-2020-15999: Heap buffer overflow in freetype
  + CVE-2020-26961: DoH did not filter IPv4 mapped IP Addresses
  + CVE-2020-26962: Cross-origin iframes supported login autofill
  + CVE-2020-26963: History and Location interfaces could have been used to hang the browser
  + CVE-2020-26964: Firefox for Android's Remote Debugging via USB could have been abused by untrusted apps on older versions of Android
  + CVE-2020-26965: Software keyboards may have remembered typed passwords
  + CVE-2020-26966: Single-word search queries were also broadcast to local network
  + CVE-2020-26967: Mutation Observers could break or confuse Firefox Screenshots feature
  + CVE-2020-26968: Memory safety bugs fixed in Firefox 83 and Firefox ESR 78.5
  + CVE-2020-26969: Memory safety bugs fixed in Firefox 83

* Tue Nov 10 2020 Alexey Gladkov <legion@altlinux.ru> 82.0.3-alt1
- New release (82.0.3).
- Security fixes:
  + CVE-2020-26950: Write side effects in MCallGetProperty opcode not accounted for

* Wed Oct 28 2020 Alexey Gladkov <legion@altlinux.ru> 82.0.1-alt1
- New release (82.0.1).

* Thu Oct 22 2020 Alexey Gladkov <legion@altlinux.ru> 82.0-alt1
- New release (82.0).
- Security fixes:
  + CVE-2020-15969: Use-after-free in usersctp
  + CVE-2020-15254: Undefined behavior in bounded channel of crossbeam rust crate
  + CVE-2020-15680: Presence of external protocol handlers could be determined through image tags
  + CVE-2020-15681: Multiple WASM threads may have overwritten each others' stub table entries
  + CVE-2020-15682: The domain associated with the prompt to open an external protocol could be spoofed to display the incorrect origin
  + CVE-2020-15683: Memory safety bugs fixed in Firefox 82 and Firefox ESR 78.4
  + CVE-2020-15684: Memory safety bugs fixed in Firefox 82

* Wed Oct 14 2020 Alexey Gladkov <legion@altlinux.ru> 81.0.2-alt1
- New release (81.0.2).

* Sun Oct 04 2020 Alexey Gladkov <legion@altlinux.ru> 81.0.1-alt1
- New release (81.0.1).

* Sun Sep 27 2020 Alexey Gladkov <legion@altlinux.ru> 81.0-alt1
- New release (81.0).
- Build on all architectures.
- Security fixes:
  + CVE-2020-15675: Use-After-Free in WebGL
  + CVE-2020-15677: Download origin spoofing via redirect
  + CVE-2020-15676: XSS when pasting attacker-controlled data into a contenteditable element
  + CVE-2020-15678: When recursing through layers while scrolling, an iterator may have become invalid, resulting in a potential use-after-free scenario
  + CVE-2020-15673: Memory safety bugs fixed in Firefox 81 and Firefox ESR 78.3
  + CVE-2020-15674: Memory safety bugs fixed in Firefox 81

* Tue Sep 08 2020 Alexey Gladkov <legion@altlinux.ru> 80.0.1-alt1
- New release (80.0.1).

* Thu Aug 27 2020 Alexey Gladkov <legion@altlinux.ru> 80.0-alt1
- New release (80.0).
- Security fixes:
  + CVE-2020-15663: Downgrade attack on the Mozilla Maintenance Service could have resulted in escalation of privilege
  + CVE-2020-15664: Attacker-induced prompt for extension installation
  + CVE-2020-12401: Timing-attack on ECDSA signature generation
  + CVE-2020-6829: P-384 and P-521 vulnerable to an electro-magnetic side channel attack on signature generation
  + CVE-2020-12400: P-384 and P-521 vulnerable to a side channel attack on modular inversion
  + CVE-2020-15665: Address bar not reset when choosing to stay on a page after the beforeunload dialog is shown
  + CVE-2020-15666: MediaError message property leaks cross-origin response status
  + CVE-2020-15667: Heap overflow when processing an update file
  + CVE-2020-15668: Data Race when reading certificate information
  + CVE-2020-15670: Memory safety bugs fixed in Firefox 80 and Firefox ESR 78.2

* Mon Aug 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 79.0-alt2
- rebuilt for armh

* Thu Jul 30 2020 Alexey Gladkov <legion@altlinux.ru> 79.0-alt1
- New release (79.0).
- ExcludeArch armh ppc64le
- Security fixes:
  + CVE-2020-15652: Potential leak of redirect targets when loading scripts in a worker
  + CVE-2020-6514: WebRTC data channel leaks internal address to peer
  + CVE-2020-15655: Extension APIs could be used to bypass Same-Origin Policy
  + CVE-2020-15653: Bypassing iframe sandbox when allowing popups
  + CVE-2020-6463: Use-after-free in ANGLE gl::Texture::onUnbindAsSamplerTexture
  + CVE-2020-15656: Type confusion for special arguments in IonMonkey
  + CVE-2020-15658: Overriding file type when saving to disk
  + CVE-2020-15657: DLL hijacking due to incorrect loading path
  + CVE-2020-15654: Custom cursor can overlay user interface
  + CVE-2020-15659: Memory safety bugs fixed in Firefox 79

* Mon Jul 13 2020 Alexey Gladkov <legion@altlinux.ru> 78.0.2-alt1
- New release (78.0.2).
- Security fixes:
  + MFSA-2020-0003: X-Frame-Options bypass using object or embed tags

* Sat Jul 04 2020 Alexey Gladkov <legion@altlinux.ru> 78.0.1-alt1
- New release (78.0.1).
- Security fixes:
  + CVE-2020-12415: AppCache manifest poisoning due to url encoded character processing
  + CVE-2020-12416: Use-after-free in WebRTC VideoBroadcaster
  + CVE-2020-12417: Memory corruption due to missing sign-extension for ValueTags on ARM64
  + CVE-2020-12418: Information disclosure due to manipulated URL object
  + CVE-2020-12419: Use-after-free in nsGlobalWindowInner
  + CVE-2020-12420: Use-After-Free when trying to connect to a STUN server
  + CVE-2020-12402: RSA Key Generation vulnerable to side-channel attack
  + CVE-2020-12421: Add-On updates did not respect the same certificate trust rules as software updates
  + CVE-2020-12422: Integer overflow in nsJPEGEncoder::emptyOutputBuffer
  + CVE-2020-12423: DLL Hijacking due to searching %%PATH%% for a library
  + CVE-2020-12424: WebRTC permission prompt could have been bypassed by a compromised content process
  + CVE-2020-12425: Out of bound read in Date.parse()
  + CVE-2020-12426: Memory safety bugs fixed in Firefox 78

* Tue Jun 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 77.0.1-alt2
- fixed packaging on so-called armh

* Thu Jun 04 2020 Alexey Gladkov <legion@altlinux.ru> 77.0.1-alt1
- New release (77.0.1).
- Security fixes:
  + CVE-2020-12399: Timing attack on DSA signatures in NSS library
  + CVE-2020-12405: Use-after-free in SharedWorkerService
  + CVE-2020-12406: JavaScript type confusion with NativeTypes
  + CVE-2020-12407: WebRender leaking GPU memory when using border-image CSS directive
  + CVE-2020-12408: URL spoofing when using IP addresses
  + CVE-2020-12409: URL spoofing with unicode characters
  + CVE-2020-12410: Memory safety bugs fixed in Firefox 77 and Firefox ESR 68.9
  + CVE-2020-12411: Memory safety bugs fixed in Firefox 77

* Fri May 08 2020 Alexey Gladkov <legion@altlinux.ru> 76.0.1-alt1
- New release (76.0.1).

* Wed May 06 2020 Alexey Gladkov <legion@altlinux.ru> 76.0-alt1
- New release (76.0).
- Security fixes:
  + CVE-2020-12387: Use-after-free during worker shutdown
  + CVE-2020-12388: Sandbox escape with improperly guarded Access Tokens
  + CVE-2020-12389: Sandbox escape with improperly separated process types
  + CVE-2020-6831: Buffer overflow in SCTP chunk input validation
  + CVE-2020-12390: Incorrect serialization of nsIPrincipal.origin for IPv6 addresses
  + CVE-2020-12391: Content-Security-Policy bypass using object elements
  + CVE-2020-12392: Arbitrary local file access with 'Copy as cURL'
  + CVE-2020-12393: Devtools' 'Copy as cURL' feature did not fully escape website-controlled data, potentially leading to command injection
  + CVE-2020-12394: URL spoofing in location bar when unfocussed
  + CVE-2020-12395: Memory safety bugs fixed in Firefox 76 and Firefox ESR 68.8
  + CVE-2020-12396: Memory safety bugs fixed in Firefox 76

* Wed Apr 08 2020 Alexey Gladkov <legion@altlinux.ru> 75.0-alt1
- New release (75.0).
- Security fixes:
  + CVE-2020-6821: Uninitialized memory could be read when using the WebGL copyTexSubImage method
  + CVE-2020-6822: Out of bounds write in GMPDecodeData when processing large images
  + CVE-2020-6823: Malicious Extension could obtain auth codes from OAuth login flows
  + CVE-2020-6824: Generated passwords may be identical on the same site between separate private browsing sessions
  + CVE-2020-6825: Memory safety bugs fixed in Firefox 75 and Firefox ESR 68.7
  + CVE-2020-6826: Memory safety bugs fixed in Firefox 75

* Thu Mar 12 2020 Alexey Gladkov <legion@altlinux.ru> 74.0-alt1
- New release (74.0).
- Security fixes:
  + CVE-2020-6805: Use-after-free when removing data about origins
  + CVE-2020-6806: BodyStream::OnInputStreamReady was missing protections against state confusion
  + CVE-2020-6807: Use-after-free in cubeb during stream destruction
  + CVE-2020-6808: URL Spoofing via javascript: URL
  + CVE-2020-6809: Web Extensions with the all-urls permission could access local files
  + CVE-2020-6810: Focusing a popup while in fullscreen could have obscured the fullscreen notification
  + CVE-2020-6811: Devtools' 'Copy as cURL' feature did not fully escape website-controlled data, potentially leading to command injection
  + CVE-2019-20503: Out of bounds reads in sctp_load_addresses_from_init
  + CVE-2020-6812: The names of AirPods with personally identifiable information were exposed to websites with camera or microphone permission
  + CVE-2020-6813: @import statements in CSS could bypass the Content Security Policy nonce feature
  + CVE-2020-6814: Memory safety bugs fixed in Firefox 74 and Firefox ESR 68.6
  + CVE-2020-6815: Memory and script safety bugs fixed in Firefox 74

* Wed Feb 19 2020 Alexey Gladkov <legion@altlinux.ru> 73.0.1-alt1
- New release (73.0.1).

* Mon Feb 17 2020 Alexey Gladkov <legion@altlinux.ru> 73.0-alt1
- New release (73.0).
- Security fixes:
  + CVE-2020-6796: Missing bounds check on shared memory read in the parent process
  + CVE-2020-6797: Extensions granted downloads.open permission could open arbitrary applications on Mac OSX
  + CVE-2020-6798: Incorrect parsing of template tag could result in JavaScript injection
  + CVE-2020-6799: Arbitrary code execution when opening pdf links from other applications, when Firefox is configured as default pdf reader
  + CVE-2020-6800: Memory safety bugs fixed in Firefox 73 and Firefox ESR 68.5
  + CVE-2020-6801: Memory safety bugs fixed in Firefox 73

* Thu Jan 23 2020 Alexey Gladkov <legion@altlinux.ru> 72.0.2-alt1
- New release (72.0.2).
- Security fixes:
  + CVE-2019-17015: Memory corruption in parent process during new content process initialization on Windows
  + CVE-2019-17016: Bypass of @namespace CSS sanitization during pasting
  + CVE-2019-17017: Type Confusion in XPCVariant.cpp
  + CVE-2019-17018: Windows Keyboard in Private Browsing Mode may retain word suggestions
  + CVE-2019-17019: Python files could be inadvertently executed upon opening a download
  + CVE-2019-17020: Content Security Policy not applied to XSL stylesheets applied to XML documents
  + CVE-2019-17021: Heap address disclosure in parent process during content process initialization on Windows
  + CVE-2019-17022: CSS sanitization does not escape HTML tags
  + CVE-2019-17023: NSS may negotiate TLS 1.2 or below after a TLS 1.3 HelloRetryRequest had been sent
  + CVE-2019-17024: Memory safety bugs fixed in Firefox 72 and Firefox ESR 68.4
  + CVE-2019-17025: Memory safety bugs fixed in Firefox 72
  + CVE-2019-17026: IonMonkey type confusion with StoreElementHole and FallibleStoreElement

* Thu Dec 05 2019 Alexey Gladkov <legion@altlinux.ru> 71.0-alt1
- New release (71.0).
- Update license tag.
- Security fixes:
  + CVE-2019-11756: Use-after-free of SFTKSession object
  + CVE-2019-17008: Use-after-free in worker destruction
  + CVE-2019-13722: Stack corruption due to incorrect number of arguments in WebRTC code
  + CVE-2019-11745: Out of bounds write in NSS when encrypting with a block cipher
  + CVE-2019-17014: Dragging and dropping a cross-origin resource, incorrectly loaded as an image, could result in information disclosure
  + CVE-2019-17009: Updater temporary files accessible to unprivileged processes
  + CVE-2019-17010: Use-after-free when performing device orientation checks
  + CVE-2019-17005: Buffer overflow in plain text serializer
  + CVE-2019-17011: Use-after-free when retrieving a document in antitracking
  + CVE-2019-17012: Memory safety bugs fixed in Firefox 71 and Firefox ESR 68.3
  + CVE-2019-17013: Memory safety bugs fixed in Firefox 71

* Thu Oct 31 2019 Alexey Gladkov <legion@altlinux.ru> 70.0.1-alt1
- New release (70.0.1).
- Builtin ru, kk, uk locales.

* Mon Oct 28 2019 Alexey Gladkov <legion@altlinux.ru> 70.0-alt1
- New release (70.0).
- Fixed:
  + CVE-2018-6156: Heap buffer overflow in FEC processing in WebRTC
  + CVE-2019-15903: Heap overflow in expat library in XML_GetCurrentLineNumber
  + CVE-2019-11757: Use-after-free when creating index updates in IndexedDB
  + CVE-2019-11759: Stack buffer overflow in HKDF output
  + CVE-2019-11760: Stack buffer overflow in WebRTC networking
  + CVE-2019-11761: Unintended access to a privileged JSONView object
  + CVE-2019-11762: document.domain-based origin isolation has same-origin-property violation
  + CVE-2019-11763: Incorrect HTML parsing results in XSS bypass technique
  + CVE-2019-11765: Incorrect permissions could be granted to a website
  + CVE-2019-17000: CSP bypass using object tag with data: URI
  + CVE-2019-17001: CSP bypass using object tag when script-src 'none' is specified
  + CVE-2019-17002: upgrade-insecure-requests was not being honored for links dragged and dropped
  + CVE-2019-11764: Memory safety bugs fixed in Firefox 70 and Firefox ESR 68.2

* Fri Oct 04 2019 Alexey Gladkov <legion@altlinux.ru> 69.0.2-alt1
- New release (69.0.2).

* Fri Sep 27 2019 Alexey Gladkov <legion@altlinux.ru> 69.0.1-alt1
- New release (69.0.1).
- Fixed:
  + CVE-2019-11754: Pointer Lock is enabled with no user notification

* Wed Sep 11 2019 Alexey Gladkov <legion@altlinux.ru> 69.0-alt1
- New release (69.0).
- Fixed:
  + CVE-2019-11751: Malicious code execution through command line parameters
  + CVE-2019-11746: Use-after-free while manipulating video
  + CVE-2019-11744: XSS by breaking out of title and textarea elements using innerHTML
  + CVE-2019-11742: Same-origin policy violation with SVG filters and canvas to steal cross-origin images
  + CVE-2019-11736: File manipulation and privilege escalation in Mozilla Maintenance Service
  + CVE-2019-11753: Privilege escalation with Mozilla Maintenance Service in custom Firefox installation location
  + CVE-2019-11752: Use-after-free while extracting a key value in IndexedDB
  + CVE-2019-9812: Sandbox escape through Firefox Sync
  + CVE-2019-11741: Isolate addons.mozilla.org and accounts.firefox.com
  + CVE-2019-11743: Cross-origin access to unload event attributes
  + CVE-2019-11748: Persistence of WebRTC permissions in a third party context
  + CVE-2019-11749: Camera information available without prompting using getUserMedia
  + CVE-2019-5849: Out-of-bounds read in Skia
  + CVE-2019-11750: Type confusion in Spidermonkey
  + CVE-2019-11737: Content security policy directives ignore port and path if host is a wildcard
  + CVE-2019-11738: Content security policy bypass through hash-based sources in directives
  + CVE-2019-11747: 'Forget about this site' removes sites from pre-loaded HSTS list
  + CVE-2019-11734: Memory safety bugs fixed in Firefox 69
  + CVE-2019-11735: Memory safety bugs fixed in Firefox 69 and Firefox ESR 68.1
  + CVE-2019-11740: Memory safety bugs fixed in Firefox 69, Firefox ESR 68.1, and Firefox ESR 60.9

* Thu Aug 01 2019 Alexey Gladkov <legion@altlinux.ru> 68.0.1-alt1
- New release (68.0.1).

* Thu Jul 11 2019 Alexey Gladkov <legion@altlinux.ru> 68.0-alt1
- New release (68.0).
- Fixed:
  + CVE-2019-9811: Sandbox escape via installation of malicious language pack
  + CVE-2019-11711: Script injection within domain through inner window reuse
  + CVE-2019-11712: Cross-origin POST requests can be made with NPAPI plugins by following 308 redirects
  + CVE-2019-11713: Use-after-free with HTTP/2 cached stream
  + CVE-2019-11714: NeckoChild can trigger crash when accessed off of main thread
  + CVE-2019-11729: Empty or malformed p256-ECDH public keys may trigger a segmentation fault
  + CVE-2019-11715: HTML parsing error can contribute to content XSS
  + CVE-2019-11716: globalThis not enumerable until accessed
  + CVE-2019-11717: Caret character improperly escaped in origins
  + CVE-2019-11718: Activity Stream writes unsanitized content to innerHTML
  + CVE-2019-11719: Out-of-bounds read when importing curve25519 private key
  + CVE-2019-11720: Character encoding XSS vulnerability
  + CVE-2019-11721: Domain spoofing through unicode latin 'kra' character
  + CVE-2019-11730: Same-origin policy treats all files in a directory as having the same-origin
  + CVE-2019-11723: Cookie leakage during add-on fetching across private browsing boundaries
  + CVE-2019-11724: Retired site input.mozilla.org has remote troubleshooting permissions
  + CVE-2019-11725: Websocket resources bypass safebrowsing protections
  + CVE-2019-11727: PKCS#1 v1.5 signatures can be used for TLS 1.3
  + CVE-2019-11728: Port scanning through Alt-Svc header
  + CVE-2019-11710: Memory safety bugs fixed in Firefox 68
  + CVE-2019-11709: Memory safety bugs fixed in Firefox 68 and Firefox ESR 60.8

* Mon Jul 01 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 67.0.4-alt2
- Added ppc64le support.
- spec: cleaned up rpm-build internal macros.

* Fri Jun 21 2019 Alexey Gladkov <legion@altlinux.ru> 67.0.4-alt1
- New release (67.0.4).
- Fixed:
 + CVE-2019-11708: sandbox escape using Prompt:Open

* Wed Jun 19 2019 Alexey Gladkov <legion@altlinux.ru> 67.0.3-alt1
- New release (67.0.3).
- Fixed:
  + CVE-2019-11707: Type confusion in Array.pop

* Tue Jun 18 2019 Alexey Gladkov <legion@altlinux.ru> 67.0.2-alt1
- New release (67.0.2).
- Fixed:
  + CVE-2019-11702: IE protocols can be used to open known local files

* Wed Jun 05 2019 Alexey Gladkov <legion@altlinux.ru> 67.0.1-alt1
- New release (67.0.1).

* Wed May 22 2019 Alexey Gladkov <legion@altlinux.ru> 67.0-alt1
- New release (67.0).
- Fixed:
  + CVE-2019-9815: Disable hyperthreading on content JavaScript threads on macOS
  + CVE-2019-9816: Type confusion with object groups and UnboxedObjects
  + CVE-2019-9817: Stealing of cross-domain images using canvas
  + CVE-2019-9818: Use-after-free in crash generation server
  + CVE-2019-9819: Compartment mismatch with fetch API
  + CVE-2019-9820: Use-after-free of ChromeEventHandler by DocShell
  + CVE-2019-9821: Use-after-free in AssertWorkerThread
  + CVE-2019-11691: Use-after-free in XMLHttpRequest
  + CVE-2019-11692: Use-after-free removing listeners in the event listener manager
  + CVE-2019-11693: Buffer overflow in WebGL bufferdata on Linux
  + CVE-2019-7317: Use-after-free in png_image_free of libpng library
  + CVE-2019-11694: Uninitialized memory memory leakage in Windows sandbox
  + CVE-2019-11695: Custom cursor can render over user interface outside of web content
  + CVE-2019-11696: Java web start .JNLP files are not recognized as executable files for download prompts
  + CVE-2019-11697: Pressing key combinations can bypass installation prompt delays and install extensions
  + CVE-2019-11698: Theft of user history data through drag and drop of hyperlinks to and from bookmarks
  + CVE-2019-11700: res: protocol can be used to open known local files
  + CVE-2019-11699: Incorrect domain name highlighting during page navigation
  + CVE-2019-11701: webcal: protocol default handler loads vulnerable web page
  + CVE-2019-9814: Memory safety bugs fixed in Firefox 67
  + CVE-2019-9800: Memory safety bugs fixed in Firefox 67 and Firefox ESR 60.7

* Wed May 08 2019 Alexey Gladkov <legion@altlinux.ru> 66.0.5-alt1
- New release (66.0.5).

* Fri Apr 12 2019 Alexey Gladkov <legion@altlinux.ru> 66.0.3-alt1
- New release (66.0.3).

* Tue Apr 02 2019 Alexey Gladkov <legion@altlinux.ru> 66.0.1-alt2
- Incease minimum version of nspr, nss.
- Improve firefox-wayland startup script.

* Wed Mar 27 2019 Alexey Gladkov <legion@altlinux.ru> 66.0.1-alt1
- New release (66.0.1).
- Use cairo-gtk3-wayland toolkit.
- Add firefox-wayland sub-package.
- Fixed:
  + CVE-2019-9790: Use-after-free when removing in-use DOM elements
  + CVE-2019-9791: Type inference is incorrect for constructors entered through on-stack replacement with IonMonkey
  + CVE-2019-9792: IonMonkey leaks JS_OPTIMIZED_OUT magic value to script
  + CVE-2019-9793: Improper bounds checks when Spectre mitigations are disabled
  + CVE-2019-9794: Command line arguments not discarded during execution
  + CVE-2019-9795: Type-confusion in IonMonkey JIT compiler
  + CVE-2019-9796: Use-after-free with SMIL animation controller
  + CVE-2019-9797: Cross-origin theft of images with createImageBitmap
  + CVE-2019-9798: Library is loaded from world writable APITRACE_LIB location
  + CVE-2019-9799: Information disclosure via IPC channel messages
  + CVE-2019-9801: Windows programs that are not 'URL Handlers' are exposed to web content
  + CVE-2019-9802: Chrome process information leak
  + CVE-2019-9803: Upgrade-Insecure-Requests incorrectly enforced for same-origin navigation
  + CVE-2019-9804: Code execution through 'Copy as cURL' in Firefox Developer Tools on macOS
  + CVE-2019-9805: Potential use of uninitialized memory in Prio
  + CVE-2019-9806: Denial of service through successive FTP authorization prompts
  + CVE-2019-9807: Text sent through FTP connection can be incorporated into alert messages
  + CVE-2019-9809: Denial of service through FTP modal alert error messages
  + CVE-2019-9808: WebRTC permissions can display incorrect origin with data: and blob: URLs
  + CVE-2019-9789: Memory safety bugs fixed in Firefox 66
  + CVE-2019-9788: Memory safety bugs fixed in Firefox 66 and Firefox ESR 60.6
  + CVE-2019-9810: IonMonkey MArraySlice has incorrect alias information
  + CVE-2019-9813: Ionmonkey type confusion with __proto__ mutations

* Sat Mar 02 2019 Alexey Gladkov <legion@altlinux.ru> 65.0.2-alt1
- New release (65.0.2).
- Use libvpx5.

* Tue Feb 19 2019 Alexey Gladkov <legion@altlinux.ru> 65.0.1-alt1
- New release (65.0.1).
- Fixed:
  + CVE-2018-18356: Use-after-free in Skia
  + CVE-2019-5785: Integer overflow in Skia
  + CVE-2018-18511: Cross-origin theft of images with ImageBitmapRenderingContext

* Thu Jan 31 2019 Alexey Gladkov <legion@altlinux.ru> 65.0-alt1
- New release (65.0).
- Fixed:
  + CVE-2018-18500: Use-after-free parsing HTML5 stream
  + CVE-2018-18503: Memory corruption with Audio Buffer
  + CVE-2018-18504: Memory corruption and out-of-bounds read of texture client buffer
  + CVE-2018-18505: Privilege escalation through IPC channel messages
  + CVE-2018-18506: Proxy Auto-Configuration file can define localhost access to be proxied
  + CVE-2018-18502: Memory safety bugs fixed in Firefox 65
  + CVE-2018-18501: Memory safety bugs fixed in Firefox 65 and Firefox ESR 60.5

* Mon Dec 31 2018 Alexey Gladkov <legion@altlinux.ru> 64.0-alt2
- Rebuilt with clang7.0.

* Thu Dec 20 2018 Alexey Gladkov <legion@altlinux.ru> 64.0-alt1
- New release (64.0).
- Fixed:
  + CVE-2018-12407: Buffer overflow with ANGLE library when using VertexBuffer11 module
  + CVE-2018-17466: Buffer overflow and out-of-bounds read in ANGLE library with TextureStorage11
  + CVE-2018-18492: Use-after-free with select element
  + CVE-2018-18493: Buffer overflow in accelerated 2D canvas with Skia
  + CVE-2018-18494: Same-origin policy violation using location attribute and performance.getEntries to steal cross-origin URLs
  + CVE-2018-18495: WebExtension content scripts can be loaded in about: pages
  + CVE-2018-18496: Embedded feed preview page can be abused for clickjacking
  + CVE-2018-18497: WebExtensions can load arbitrary URLs through pipe separators
  + CVE-2018-18498: Integer overflow when calculating buffer sizes for images
  + CVE-2018-12406: Memory safety bugs fixed in Firefox 64
  + CVE-2018-12405: Memory safety bugs fixed in Firefox 64 and Firefox ESR 60.4

* Fri Nov 23 2018 Alexey Gladkov <legion@altlinux.ru> 63.0.3-alt1
- New release (63.0.3).

* Tue Nov 13 2018 Alexey Gladkov <legion@altlinux.ru> 63.0.1-alt1
- New release (63.0.1).
- Fixed:
  + CVE-2018-12391: HTTP Live Stream audio data is accessible cross-origin
  + CVE-2018-12392: Crash with nested event loops
  + CVE-2018-12393: Integer overflow during Unicode conversion while loading JavaScript
  + CVE-2018-12395: WebExtension bypass of domain restrictions through header rewriting
  + CVE-2018-12396: WebExtension content scripts can execute in disallowed contexts
  + CVE-2018-12397: Missing warning prompt when WebExtension requests local file access
  + CVE-2018-12398: CSP bypass through stylesheet injection in resource URIs
  + CVE-2018-12399: Spoofing of protocol registration notification bar
  + CVE-2018-12400: Favicons are cached in private browsing mode on Firefox for Android
  + CVE-2018-12401: DOS attack through special resource URI parsing
  + CVE-2018-12402: SameSite cookies leak when pages are explicitly saved
  + CVE-2018-12403: Mixed content warning is not displayed when HTTPS page loads a favicon over HTTP
  + CVE-2018-12388: Memory safety bugs fixed in Firefox 63
  + CVE-2018-12390: Memory safety bugs fixed in Firefox 63 and Firefox ESR 60.3

* Thu Oct 04 2018 Alexey Gladkov <legion@altlinux.ru> 62.0.3-alt1
- New release (62.0.3).
- Fixed:
  + CVE-2018-12386: Type confusion in JavaScript
  + CVE-2018-12387: A vulnerability where the JavaScript JIT compiler
  + CVE-2018-12385: Crash in TransportSecurityInfo due to cached data
  + CVE-2018-12377: Use-after-free in refresh driver timers
  + CVE-2018-12378: Use-after-free in IndexedDB
  + CVE-2018-12379: Out-of-bounds write with malicious MAR file
  + CVE-2017-16541: Proxy bypass using automount and autofs
  + CVE-2018-12381: Dragging and dropping Outlook email message results in page navigation
  + CVE-2018-12382: Addressbar spoofing with javascript URI on Firefox for Android
  + CVE-2018-12383: Setting a master password post-Firefox 58 does not delete unencrypted previously stored passwords
  + CVE-2018-12375: Memory safety bugs fixed in Firefox 62
  + CVE-2018-12376: Memory safety bugs fixed in Firefox 62 and Firefox ESR 60.2

* Fri Jul 06 2018 Alexey Gladkov <legion@altlinux.ru> 61.0.1-alt1
- New release (61.0.1).

* Mon Jul 02 2018 Alexey Gladkov <legion@altlinux.ru> 61.0-alt1
- New release (61.0).
- Fixed:
  + CVE-2018-12359: Buffer overflow using computed size of canvas element
  + CVE-2018-12360: Use-after-free when using focus()
  + CVE-2018-12361: Integer overflow in SwizzleData
  + CVE-2018-12358: Same-origin bypass using service worker and redirection
  + CVE-2018-12362: Integer overflow in SSSE3 scaler
  + CVE-2018-5156: Media recorder segmentation fault when track type is changed during capture
  + CVE-2018-12363: Use-after-free when appending DOM nodes
  + CVE-2018-12364: CSRF attacks through 307 redirects and NPAPI plugins
  + CVE-2018-12365: Compromised IPC child process can list local filenames
  + CVE-2018-12371: Integer overflow in Skia library during edge builder allocation
  + CVE-2018-12366: Invalid data handling during QCMS transformations
  + CVE-2018-12367: Timing attack mitigation of PerformanceNavigationTiming
  + CVE-2018-12368: No warning when opening executable SettingContent-ms files
  + CVE-2018-12369: WebExtension security permission checks bypassed by embedded experiments
  + CVE-2018-12370: SameSite cookie protections bypassed when exiting Reader View
  + CVE-2018-5186: Memory safety bugs fixed in Firefox 61
  + CVE-2018-5187: Memory safety bugs fixed in Firefox 60 and Firefox ESR 60.1
  + CVE-2018-5188: Memory safety bugs fixed in Firefox 60, Firefox ESR 60.1, and Firefox ESR 52.9

* Thu Jun 07 2018 Alexey Gladkov <legion@altlinux.ru> 60.0.2-alt1
- New release (60.0.2).
- Fixed:
  + CVE-2018-6126: Heap buffer overflow rasterizing paths in SVG with Skia

* Thu May 17 2018 Alexey Gladkov <legion@altlinux.ru> 60.0.1-alt1
- New release (60.0.1).
- Fixed:
  + CVE-2018-5154: Use-after-free with SVG animations and clip paths
  + CVE-2018-5155: Use-after-free with SVG animations and text paths
  + CVE-2018-5157: Same-origin bypass of PDF Viewer to view protected PDF files
  + CVE-2018-5158: Malicious PDF can inject JavaScript into PDF Viewer
  + CVE-2018-5159: Integer overflow and out-of-bounds write in Skia
  + CVE-2018-5160: Uninitialized memory use by WebRTC encoder
  + CVE-2018-5152: WebExtensions information leak through webRequest API
  + CVE-2018-5153: Out-of-bounds read in mixed content websocket messages
  + CVE-2018-5163: Replacing cached data in JavaScript Start-up Bytecode Cache
  + CVE-2018-5164: CSP not applied to all multipart content sent with multipart/x-mixed-replace
  + CVE-2018-5166: WebExtension host permission bypass through filterReponseData
  + CVE-2018-5167: Improper linkification of chrome: and javascript: content in web console and JavaScript debugger
  + CVE-2018-5168: Lightweight themes can be installed without user interaction
  + CVE-2018-5169: Dragging and dropping link text onto home button can set home page to include chrome pages
  + CVE-2018-5172: Pasted script from clipboard can run in the Live Bookmarks page or PDF viewer
  + CVE-2018-5173: File name spoofing of Downloads panel with Unicode characters
  + CVE-2018-5174: Windows Defender SmartScreen UI runs with less secure behavior for downloaded files in Windows 10 April 2018 Update
  + CVE-2018-5175: Universal CSP bypass on sites using strict-dynamic in their policies
  + CVE-2018-5176: JSON Viewer script injection
  + CVE-2018-5177: Buffer overflow in XSLT during number formatting
  + CVE-2018-5165: Checkbox for enabling Flash protected mode is inverted in 32-bit Firefox
  + CVE-2018-5180: heap-use-after-free in mozilla::WebGLContext::DrawElementsInstanced
  + CVE-2018-5181: Local file can be displayed in noopener tab through drag and drop of hyperlink
  + CVE-2018-5182: Local file can be displayed from hyperlink dragged and dropped on addressbar
  + CVE-2018-5151: Memory safety bugs fixed in Firefox 60
  + CVE-2018-5150: Memory safety bugs fixed in Firefox 60 and Firefox ESR 52.8

* Fri Mar 30 2018 Alexey Gladkov <legion@altlinux.ru> 59.0.2-alt2
- Fix locale switch (ALT#34741)

* Tue Mar 27 2018 Alexey Gladkov <legion@altlinux.ru> 59.0.2-alt1
- New release (59.0.2).
- Fixed:
  + CVE-2018-5127: Buffer overflow manipulating SVG animatedPathSegList
  + CVE-2018-5128: Use-after-free manipulating editor selection ranges
  + CVE-2018-5129: Out-of-bounds write with malformed IPC messages
  + CVE-2018-5130: Mismatched RTP payload type can trigger memory corruption
  + CVE-2018-5131: Fetch API improperly returns cached copies of no-store/no-cache resources
  + CVE-2018-5132: WebExtension Find API can search privileged pages
  + CVE-2018-5133: Value of the app.support.baseURL preference is not properly sanitized
  + CVE-2018-5134: WebExtensions may use view-source: URLs to bypass content restrictions
  + CVE-2018-5135: WebExtension browserAction can inject scripts into unintended contexts
  + CVE-2018-5136: Same-origin policy violation with data: URL shared workers
  + CVE-2018-5137: Script content can access legacy extension non-contentaccessible resources
  + CVE-2018-5138: Android Custom Tab address spoofing through long domain names
  + CVE-2018-5140: Moz-icon images accessible to web content through moz-icon: protocol
  + CVE-2018-5141: DOS attack through notifications Push API
  + CVE-2018-5142: Media Capture and Streams API permissions display incorrect origin with data: and blob: URLs
  + CVE-2018-5143: Self-XSS pasting javascript: URL with embedded tab into addressbar
  + CVE-2018-5126: Memory safety bugs fixed in Firefox 59
  + CVE-2018-5125: Memory safety bugs fixed in Firefox 59 and Firefox ESR 52.7
  + CVE-2018-5146: Out of bounds memory write in libvorbis
  + CVE-2018-5147: Out of bounds memory write in libtremor
  + CVE-2018-5148: Use-after-free in compositor

* Thu Feb 22 2018 Alexey Gladkov <legion@altlinux.ru> 58.0.2-alt3
- Fix ALSA (ALT#34553).

* Mon Feb 19 2018 Alexey Gladkov <legion@altlinux.ru> 58.0.2-alt2
- Enable ALSA support.

* Sun Feb 11 2018 Alexey Gladkov <legion@altlinux.ru> 58.0.2-alt1
- New release (58.0.2).
- Fixed:
  + CVE-2018-5091: Use-after-free with DTMF timers
  + CVE-2018-5092: Use-after-free in Web Workers
  + CVE-2018-5093: Buffer overflow in WebAssembly during Memory/Table resizing
  + CVE-2018-5094: Buffer overflow in WebAssembly with garbage collection on uninitialized memory
  + CVE-2018-5095: Integer overflow in Skia library during edge builder allocation
  + CVE-2018-5097: Use-after-free when source document is manipulated during XSLT
  + CVE-2018-5098: Use-after-free while manipulating form input elements
  + CVE-2018-5099: Use-after-free with widget listener
  + CVE-2018-5100: Use-after-free when IsPotentiallyScrollable arguments are freed from memory
  + CVE-2018-5101: Use-after-free with floating first-letter style elements
  + CVE-2018-5102: Use-after-free in HTML media elements
  + CVE-2018-5103: Use-after-free during mouse event handling
  + CVE-2018-5104: Use-after-free during font face manipulation
  + CVE-2018-5105: WebExtensions can save and execute files on local file system without user prompts
  + CVE-2018-5106: Developer Tools can expose style editor information cross-origin through service worker
  + CVE-2018-5107: Printing process will follow symlinks for local file access
  + CVE-2018-5108: Manually entered blob URL can be accessed by subsequent private browsing tabs
  + CVE-2018-5109: Audio capture prompts and starts with incorrect origin attribution
  + CVE-2018-5110: Cursor can be made invisible on OS X
  + CVE-2018-5111: URL spoofing in addressbar through drag and drop
  + CVE-2018-5112: Extension development tools panel can open a non-relative URL in the panel
  + CVE-2018-5113: WebExtensions can load non-HTTPS pages with browser.identity.launchWebAuthFlow
  + CVE-2018-5114: The old value of a cookie changed to HttpOnly remains accessible to scripts
  + CVE-2018-5115: Background network requests can open HTTP authentication in unrelated foreground tabs
  + CVE-2018-5116: WebExtension ActiveTab permission allows cross-origin frame content access
  + CVE-2018-5117: URL spoofing with right-to-left text aligned left-to-right
  + CVE-2018-5118: Activity Stream images can attempt to load local content through file:
  + CVE-2018-5119: Reader view will load cross-origin content in violation of CORS headers
  + CVE-2018-5121: OS X Tibetan characters render incompletely in the addressbar
  + CVE-2018-5122: Potential integer overflow in DoCrypt
  + CVE-2018-5090: Memory safety bugs fixed in Firefox 58
  + CVE-2018-5089: Memory safety bugs fixed in Firefox 58 and Firefox ESR 52.6
  + CVE-2018-5124: Sanitize HTML fragments created for chrome-privileged documents

* Sat Jan 06 2018 Alexey Gladkov <legion@altlinux.ru> 57.0.4-alt1
- New release (57.0.4).
- Fixed:
  + Speculative execution side-channel attack ("Spectre")
  + CVE-2017-7845: Buffer overflow when drawing and validating elements with ANGLE library using Direct 3D 9

* Fri Dec 08 2017 Alexey Gladkov <legion@altlinux.ru> 57.0.1-alt2
- Enable dbus support (ALT#34275).
- Change chrome packaging format to omni (ALT#34285).

* Mon Dec 04 2017 Alexey Gladkov <legion@altlinux.ru> 57.0.1-alt1
- New release (57.0.1).

* Tue Nov 21 2017 Alexey Gladkov <legion@altlinux.ru> 57.0-alt1
- New release (57.0).
- Fixed:
  + CVE-2017-7828: Use-after-free of PressShell while restyling layout
  + CVE-2017-7830: Cross-origin URL information leak through Resource Timing API
  + CVE-2017-7831: Information disclosure of exposed properties on JavaScript proxy objects
  + CVE-2017-7832: Domain spoofing through use of dotless 'i' character followed by accent markers
  + CVE-2017-7833: Domain spoofing with Arabic and Indic vowel marker characters
  + CVE-2017-7834: data: URLs opened in new tabs bypass CSP protections
  + CVE-2017-7835: Mixed content blocking incorrectly applies with redirects
  + CVE-2017-7836: Pingsender dynamically loads libcurl on Linux and OS X
  + CVE-2017-7837: SVG loaded as <img> can use meta tags to set cookies
  + CVE-2017-7838: Failure of individual decoding of labels in international domain names triggers punycode display of entire IDN
  + CVE-2017-7839: Control characters before javascript: URLs defeats self-XSS prevention mechanism
  + CVE-2017-7840: Exported bookmarks do not strip script elements from user-supplied tags
  + CVE-2017-7842: Referrer Policy is not always respected for <link> elements
  + CVE-2017-7827: Memory safety bugs fixed in Firefox 57
  + CVE-2017-7826: Memory safety bugs fixed in Firefox 57 and Firefox ESR 52.5

* Sun Oct 08 2017 Alexey Gladkov <legion@altlinux.ru> 56.0-alt1
- New release (56.0).
- Fixed:
  + CVE-2017-7793: Use-after-free with Fetch API
  + CVE-2017-7817: Firefox for Android address bar spoofing through fullscreen mode
  + CVE-2017-7818: Use-after-free during ARIA array manipulation
  + CVE-2017-7819: Use-after-free while resizing images in design mode
  + CVE-2017-7824: Buffer overflow when drawing and validating elements with ANGLE
  + CVE-2017-7805: Use-after-free in TLS 1.2 generating handshake hashes
  + CVE-2017-7812: Drag and drop of malicious page content to the tab bar can open locally stored files
  + CVE-2017-7814: Blob and data URLs bypass phishing and malware protection warnings
  + CVE-2017-7813: Integer truncation in the JavaScript parser
  + CVE-2017-7825: OS X fonts render some Tibetan and Arabic unicode characters as spaces
  + CVE-2017-7815: Spoofing attack with modal dialogs on non-e10s installations
  + CVE-2017-7816: WebExtensions can load about: URLs in extension UI
  + CVE-2017-7821: WebExtensions can download and open non-executable files without user interaction
  + CVE-2017-7823: CSP sandbox directive did not create a unique origin
  + CVE-2017-7822: WebCrypto allows AES-GCM with 0-length IV
  + CVE-2017-7820: Xray wrapper bypass with new tab and web console
  + CVE-2017-7811: Memory safety bugs fixed in Firefox 56
  + CVE-2017-7810: Memory safety bugs fixed in Firefox 56 and Firefox ESR 52.4

* Tue Aug 29 2017 Alexey Gladkov <legion@altlinux.ru> 55.0.3-alt1
- New release (55.0.3).

* Sun Aug 13 2017 Alexey Gladkov <legion@altlinux.ru> 55.0.1-alt1
- New release (55.0.1).
- Fixed:
  + CVE-2017-7798: XUL injection in the style editor in devtools
  + CVE-2017-7800: Use-after-free in WebSockets during disconnection
  + CVE-2017-7801: Use-after-free with marquee during window resizing
  + CVE-2017-7809: Use-after-free while deleting attached editor DOM node
  + CVE-2017-7784: Use-after-free with image observers
  + CVE-2017-7802: Use-after-free resizing image elements
  + CVE-2017-7785: Buffer overflow manipulating ARIA attributes in DOM
  + CVE-2017-7786: Buffer overflow while painting non-displayable SVG
  + CVE-2017-7806: Use-after-free in layer manager with SVG
  + CVE-2017-7753: Out-of-bounds read with cached style data and pseudo-elements
  + CVE-2017-7787: Same-origin policy bypass with iframes through page reloads
  + CVE-2017-7807: Domain hijacking through AppCache fallback
  + CVE-2017-7792: Buffer overflow viewing certificates with an extremely long OID
  + CVE-2017-7804: Memory protection bypass through WindowsDllDetourPatcher
  + CVE-2017-7791: Spoofing following page navigation with data: protocol and modal alerts
  + CVE-2017-7808: CSP information leak with frame-ancestors containing paths
  + CVE-2017-7782: WindowsDllDetourPatcher allocates memory without DEP protections
  + CVE-2017-7781: Elliptic curve point addition error when using mixed Jacobian-affine coordinates
  + CVE-2017-7794: Linux file truncation via sandbox broker
  + CVE-2017-7803: CSP containing 'sandbox' improperly applied
  + CVE-2017-7799: Self-XSS XUL injection in about:webrtc
  + CVE-2017-7783: DOS attack through long username in URL
  + CVE-2017-7788: Sandboxed about:srcdoc iframes do not inherit CSP directives
  + CVE-2017-7789: Failure to enable HSTS when two STS headers are sent for a connection
  + CVE-2017-7790: Windows crash reporter reads extra memory for some non-null-terminated registry values
  + CVE-2017-7796: Windows updater can delete any file named update.log
  + CVE-2017-7797: Response header name interning leaks across origins
  + CVE-2017-7780: Memory safety bugs fixed in Firefox 55
  + CVE-2017-7779: Memory safety bugs fixed in Firefox 55 and Firefox ESR 52.3

* Wed Jul 12 2017 Alexey Gladkov <legion@altlinux.ru> 54.0.1-alt1
- New release (54.0.1).

* Sun Jun 25 2017 Alexey Gladkov <legion@altlinux.ru> 54.0-alt1
- New release (54.0).
- Fixed:
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
  + CVE-2017-7759: Android intent URLs can cause navigation to local file system
  + CVE-2017-7760: File manipulation and privilege escalation via callback parameter in Mozilla Windows Updater and Maintenance Service
  + CVE-2017-7761: File deletion and privilege escalation through Mozilla Maintenance Service helper.exe application
  + CVE-2017-7762: Addressbar spoofing in Reader mode
  + CVE-2017-7763: Mac fonts render some unicode characters as spaces
  + CVE-2017-7764: Domain spoofing with combination of Canadian Syllabics and other unicode blocks
  + CVE-2017-7765: Mark of the Web bypass when saving executable files
  + CVE-2017-7766: File execution and privilege escalation through updater.ini, Mozilla Windows Updater, and Mozilla Maintenance Service
  + CVE-2017-7767: Privilege escalation and arbitrary file overwrites through Mozilla Windows Updater and Mozilla Maintenance Service
  + CVE-2017-7768: 32 byte arbitrary file read through Mozilla Maintenance Service
  + CVE-2017-7770: Addressbar spoofing with JavaScript events and fullscreen mode
  + CVE-2017-5471: Memory safety bugs fixed in Firefox 54
  + CVE-2017-5470: Memory safety bugs fixed in Firefox 54 and Firefox ESR 52.2

* Sun May 07 2017 Alexey Gladkov <legion@altlinux.ru> 53.0.2-alt1
- New release (53.0.2).
- Fixed:
  + CVE-2017-5031: Use after free in ANGLE

* Mon May 01 2017 Alexey Gladkov <legion@altlinux.ru> 53.0-alt1
- New release (53.0).
- Built with internal hunspell.
- Fixed:
  + CVE-2017-5433: Use-after-free in SMIL animation functions
  + CVE-2017-5435: Use-after-free during transaction processing in the editor
  + CVE-2017-5436: Out-of-bounds write with malicious font in Graphite 2
  + CVE-2017-5461: Out-of-bounds write in Base64 encoding in NSS
  + CVE-2017-5459: Buffer overflow in WebGL
  + CVE-2017-5466: Origin confusion when reloading isolated data:text/html URL
  + CVE-2017-5434: Use-after-free during focus handling
  + CVE-2017-5432: Use-after-free in text input selection
  + CVE-2017-5460: Use-after-free in frame selection
  + CVE-2017-5438: Use-after-free in nsAutoPtr during XSLT processing
  + CVE-2017-5439: Use-after-free in nsTArray Length() during XSLT processing
  + CVE-2017-5440: Use-after-free in txExecutionState destructor during XSLT processing
  + CVE-2017-5441: Use-after-free with selection during scroll events
  + CVE-2017-5442: Use-after-free during style changes
  + CVE-2017-5464: Memory corruption with accessibility and DOM manipulation
  + CVE-2017-5443: Out-of-bounds write during BinHex decoding
  + CVE-2017-5444: Buffer overflow while parsing application/http-index-format content
  + CVE-2017-5446: Out-of-bounds read when HTTP/2 DATA frames are sent with incorrect data
  + CVE-2017-5447: Out-of-bounds read during glyph processing
  + CVE-2017-5465: Out-of-bounds read in ConvolvePixel
  + CVE-2017-5448: Out-of-bounds write in ClearKeyDecryptor
  + CVE-2016-10196: Vulnerabilities in Libevent library
  + CVE-2017-5454: Sandbox escape allowing file system read access through file picker
  + CVE-2017-5455: Sandbox escape through internal feed reader APIs
  + CVE-2017-5456: Sandbox escape allowing local file system access
  + CVE-2017-5469: Potential Buffer overflow in flex-generated code
  + CVE-2017-5445: Uninitialized values used while parsing application/http-index-format content
  + CVE-2017-5449: Crash during bidirectional unicode manipulation with animation
  + CVE-2017-5450: Addressbar spoofing using javascript: URI on Firefox for Android
  + CVE-2017-5451: Addressbar spoofing with onblur event
  + CVE-2017-5462: DRBG flaw in NSS
  + CVE-2017-5463: Addressbar spoofing through reader view on Firefox for Android
  + CVE-2017-5467: Memory corruption when drawing Skia content
  + CVE-2017-5452: Addressbar spoofing during scrolling with editable content on Firefox for Android
  + CVE-2017-5453: HTML injection into RSS Reader feed preview page through TITLE element
  + CVE-2017-5458: Drag and drop of javascript: URLs can allow for self-XSS
  + CVE-2017-5468: Incorrect ownership model for Private Browsing information
  + CVE-2017-5430: Memory safety bugs fixed in Firefox 53 and Firefox ESR 52.1
  + CVE-2017-5429: Memory safety bugs fixed in Firefox 53, Firefox ESR 45.9, and Firefox ESR 52.1

* Wed Mar 15 2017 Alexey Gladkov <legion@altlinux.ru> 52.0-alt1
- New release (52.0).
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

* Wed Feb 08 2017 Alexey Gladkov <legion@altlinux.ru> 51.0.1-alt2
- Remove RPATH but began to use LD_LIBRARY_PATH (ALT#33085).

* Mon Jan 30 2017 Alexey Gladkov <legion@altlinux.ru> 51.0.1-alt1
- New release (51.0.1).
- Fixed:
  + CVE-2017-5375: Excessive JIT code allocation allows bypass of ASLR and DEP
  + CVE-2017-5376: Use-after-free in XSL
  + CVE-2017-5377: Memory corruption with transforms to create gradients in Skia
  + CVE-2017-5378: Pointer and frame data leakage of Javascript objects
  + CVE-2017-5379: Use-after-free in Web Animations
  + CVE-2017-5380: Potential use-after-free during DOM manipulations
  + CVE-2017-5390: Insecure communication methods in Developer Tools JSON viewer
  + CVE-2017-5389: WebExtensions can install additional add-ons via modified host requests
  + CVE-2017-5396: Use-after-free with Media Decoder
  + CVE-2017-5381: Certificate Viewer exporting can be used to navigate and save to arbitrary filesystem locations
  + CVE-2017-5382: Feed preview can expose privileged content errors and exceptions
  + CVE-2017-5383: Location bar spoofing with unicode characters
  + CVE-2017-5384: Information disclosure via Proxy Auto-Config (PAC)
  + CVE-2017-5385: Data sent in multipart channels ignores referrer-policy response headers
  + CVE-2017-5386: WebExtensions can use data: protocol to affect other extensions
  + CVE-2017-5394: Android location bar spoofing using fullscreen and JavaScript events
  + CVE-2017-5391: Content about: pages can load privileged about: pages
  + CVE-2017-5392: Weak references using multiple threads on weak proxy objects lead to unsafe memory usage
  + CVE-2017-5393: Remove addons.mozilla.org CDN from whitelist for mozAddonManager
  + CVE-2017-5395: Android location bar spoofing during scrolling
  + CVE-2017-5387: Disclosure of local file existence through TRACK tag error messages
  + CVE-2017-5388: WebRTC can be used to generate a large amount of UDP traffic for DDOS attacks
  + CVE-2017-5374: Memory safety bugs fixed in Firefox 51
  + CVE-2017-5373: Memory safety bugs fixed in Firefox 51 and Firefox ESR 45.7

* Thu Dec 15 2016 Alexey Gladkov <legion@altlinux.ru> 50.1.0-alt1
- New release (50.1.0).
- Fixed:
  + CVE-2016-9894: Buffer overflow in SkiaGL
  + CVE-2016-9899: Use-after-free while manipulating DOM events and audio elements
  + CVE-2016-9895: CSP bypass using marquee tag
  + CVE-2016-9896: Use-after-free with WebVR
  + CVE-2016-9897: Memory corruption in libGLES
  + CVE-2016-9898: Use-after-free in Editor while manipulating DOM subtrees
  + CVE-2016-9900: Restricted external resources can be loaded by SVG images through data URLs
  + CVE-2016-9904: Cross-origin information leak in shared atoms
  + CVE-2016-9901: Data from Pocket server improperly sanitized before execution
  + CVE-2016-9902: Pocket extension does not validate the origin of events
  + CVE-2016-9903: XSS injection vulnerability in add-ons SDK
  + CVE-2016-9080: Memory safety bugs fixed in Firefox 50.1
  + CVE-2016-9893: Memory safety bugs fixed in Firefox 50.1 and Firefox ESR 45.6

* Tue Dec  6 2016 Ivan Zakharyaschev <imz@altlinux.org> 50.0.2-alt2
- Precise calculation of the dependency on libgtk symbols (ALT#32297) and
  strict verification of unresolved symbols. (Thx legion@ for the original
  hack, which had to be removed in 44.0.2-alt3, but found to be restorable
  by ruslandh@'s work on strict unresolved symbols verification in palemoon.)

* Fri Dec 02 2016 Alexey Gladkov <legion@altlinux.ru> 50.0.2-alt1
- New release (50.0.2).
- Fixed:
  + CVE-2016-9078: data: URL can inherit wrong origin after an HTTP redirect
  + CVE-2016-9079: Use-after-free in SVG Animation

* Wed Nov 23 2016 Alexey Gladkov <legion@altlinux.ru> 50.0-alt2
- Set "system colors" off by default (ALT#32787).

* Wed Nov 16 2016 Alexey Gladkov <legion@altlinux.ru> 50.0-alt1
- New release (50.0).
- Fixed:
  + CVE-2016-5296: Heap-buffer-overflow WRITE in rasterize_edges_1
  + CVE-2016-5292: URL parsing causes crash
  + CVE-2016-5293: Write to arbitrary file with Mozilla Updater and Maintenance Service using updater.log hardlink
  + CVE-2016-5294: Arbitrary target directory for result files of update process
  + CVE-2016-5297: Incorrect argument length checking in JavaScript
  + CVE-2016-9064: Add-ons update must verify IDs match between current and new versions
  + CVE-2016-9065: Firefox for Android location bar spoofing using fullscreen
  + CVE-2016-9066: Integer overflow leading to a buffer overflow in nsScriptLoadHandler
  + CVE-2016-9067: heap-use-after-free in nsINode::ReplaceOrInsertBefore
  + CVE-2016-9068: heap-use-after-free in nsRefreshDriver
  + CVE-2016-9072: 64-bit NPAPI sandbox isn't enabled on fresh profile
  + CVE-2016-9075: WebExtensions can access the mozAddonManager API and use it to gain elevated privileges
  + CVE-2016-9077: Canvas filters allow feDisplacementMaps to be applied to cross-origin images, allowing timing attacks on them
  + CVE-2016-5291: Same-origin policy violation using local HTML file and saved shortcut file
  + CVE-2016-5295: Mozilla Maintenance Service: Ability to read arbitrary files as SYSTEM
  + CVE-2016-5298: SSL indicator can mislead the user about the real URL visited
  + CVE-2016-5299: Firefox AuthToken in broadcast protected with signature-level permission can be accessed by an application installed beforehand that defines the same permissions
  + CVE-2016-9061: API key (glocation) in broadcast protected with signature-level permission can be accessed by an application installed beforehand that defines the same permissions
  + CVE-2016-9062: Private browsing browser traces (Android) in browser.db and wal file
  + CVE-2016-9070: Sidebar bookmark can have reference to chrome window
  + CVE-2016-9073: windows.create schema doesn't specify "format": "relativeUrl"
  + CVE-2016-9074: Insufficient timing side-channel resistance in divSpoiler
  + CVE-2016-9076: select dropdown menu can be used for URL bar spoofing on e10s
  + CVE-2016-9063: Possible integer overflow to fix inside XML_Parse in Expat
  + CVE-2016-9071: Probe browser history via HSTS/301 redirect + CSP
  + CVE-2016-5289: Memory safety bugs fixed in Firefox 50
  + CVE-2016-5290: Memory safety bugs fixed in Firefox 50 and Firefox ESR 45.5

* Fri Oct 21 2016 Alexey Gladkov <legion@altlinux.ru> 49.0.2-alt1
- New release (49.0.2).
- Fixed:
  + CVE-2016-5287: Crash in nsTArray_base<T>::SwapArrayElements
  + CVE-2016-5288: Web content can read cache entries

* Tue Oct 04 2016 Alexey Gladkov <legion@altlinux.ru> 49.0.1-alt2
- Fix scrolling.

* Tue Sep 27 2016 Alexey Gladkov <legion@altlinux.ru> 49.0.1-alt1
- New release (49.0.1).
- Fixed:
  + CVE-2016-2827: Out-of-bounds read in mozilla::net::IsValidReferrerPolicy
  + CVE-2016-5270: Heap-buffer-overflow in nsCaseTransformTextRunFactory::TransformString
  + CVE-2016-5271: Out-of-bounds read in PropertyProvider::GetSpacingInternal
  + CVE-2016-5272: Bad cast in nsImageGeometryMixin
  + CVE-2016-5273: crash in mozilla::a11y::HyperTextAccessible::GetChildOffset
  + CVE-2016-5276: Heap-use-after-free in mozilla::a11y::DocAccessible::ProcessInvalidationList
  + CVE-2016-5274: use-after-free in nsFrameManager::CaptureFrameState
  + CVE-2016-5277: Heap-use-after-free in nsRefreshDriver::Tick
  + CVE-2016-5275: A buffer overflow when working with empty filters during canvas rendering
  + CVE-2016-5278: Heap-buffer-overflow in nsBMPEncoder::AddImageFrame
  + CVE-2016-5279: Full local path of files is available to web pages after drag and drop
  + CVE-2016-5280: Use-after-free in mozilla::nsTextNodeDirectionalityMap::RemoveElementFromMap
  + CVE-2016-5281: use-after-free in DOMSVGLength
  + CVE-2016-5282: Don't allow content to request favicons from non-whitelisted schemes
  + CVE-2016-5283: Iframe src fragment timing attack can reveal cross-origin data
  + CVE-2016-5284: Add-on update site certificate pin expiration
  + CVE-2016-5256: Memory safety bugs fixed in Firefox 49
  + CVE-2016-5257: Memory safety bugs fixed in Firefox 49 and Firefox ESR 45.4

* Tue Sep 06 2016 Alexey Gladkov <legion@altlinux.ru> 48.0.2-alt1
- New release (48.0.2).

* Sun Aug 28 2016 Alexey Gladkov <legion@altlinux.ru> 48.0.1-alt1
- New release (48.0.1).

* Fri Aug 05 2016 Alexey Gladkov <legion@altlinux.ru> 48.0-alt1
- New release (48.0).
- Fixed:
  + 2016-84 Information disclosure through Resource Timing API during page navigation
  + 2016-83 Spoofing attack through text injection into internal error pages
  + 2016-82 Addressbar spoofing with right-to-left characters on Firefox for Android
  + 2016-81 Information disclosure and local file manipulation through drag and drop
  + 2016-80 Same-origin policy violation using local HTML file and saved shortcut file
  + 2016-79 Use-after-free when applying SVG effects
  + 2016-78 Type confusion in display transformation
  + 2016-77 Buffer overflow in ClearKey Content Decryption Module (CDM) during video playback
  + 2016-76 Scripts on marquee tag can execute in sandboxed iframes
  + 2016-75 Integer overflow in WebSockets during data buffering
  + 2016-74 Form input type change from password to text can store plain text password in session restore file
  + 2016-73 Use-after-free in service workers with nested sync events
  + 2016-72 Use-after-free in DTLS during WebRTC session shutdown
  + 2016-71 Crash in incremental garbage collection in JavaScript
  + 2016-70 Use-after-free when using alt key and toplevel menus
  + 2016-69 Arbitrary file manipulation by local user through Mozilla updater and callback application path parameter
  + 2016-68 Out-of-bounds read during XML parsing in Expat library
  + 2016-67 Stack underflow during 2D graphics rendering
  + 2016-66 Location bar spoofing via data URLs with malformed/invalid mediatypes
  + 2016-65 Cairo rendering crash due to memory allocation issue with FFmpeg 0.10
  + 2016-64 Buffer overflow rendering SVG with bidirectional content
  + 2016-63 Favicon network connection can persist when page is closed
  + 2016-62 Miscellaneous memory safety hazards (rv:48.0 / rv:45.3)

* Tue Jul 26 2016 Alexey Gladkov <legion@altlinux.ru> 47.0.1-alt1
- New release (47.0.1).

* Fri Jun 10 2016 Alexey Gladkov <legion@altlinux.ru> 47.0-alt1
- New release (47.0).
- Fixed:
  + 2016-61 Network Security Services (NSS) vulnerabilities
  + 2016-60 Java applets bypass CSP protections
  + 2016-59 Information disclosure of disabled plugins through CSS pseudo-classes
  + 2016-58 Entering fullscreen and persistent pointerlock without user permission
  + 2016-57 Incorrect icon displayed on permissions notifications
  + 2016-56 Use-after-free when textures are used in WebGL operations after recycle pool destruction
  + 2016-55 File overwrite and privilege escalation through Mozilla Windows updater
  + 2016-54 Partial same-origin-policy through setting location.host through data URI
  + 2016-53 Out-of-bounds write with WebGL shader
  + 2016-52 Addressbar spoofing though the SELECT element
  + 2016-51 Use-after-free deleting tables from a contenteditable document
  + 2016-50 Buffer overflow parsing HTML5 fragments
  + 2016-49 Miscellaneous memory safety hazards (rv:47.0 / rv:45.2)

* Tue May 31 2016 Alexey Gladkov <legion@altlinux.ru> 46.0.1-alt2
- New release (46.0.1).

* Fri Apr 29 2016 Alexey Gladkov <legion@altlinux.ru> 46.0-alt1
- New release (46.0).
- Fixed:
  + 2016-48 Firefox Health Reports could accept events from untrusted domains
  + 2016-47 Write to invalid HashMap entry through JavaScript.watch()
  + 2016-46 Elevation of privilege with chrome.tabs.update API in web extensions
  + 2016-45 CSP not applied to pages sent with multipart/x-mixed-replace
  + 2016-44 Buffer overflow in libstagefright with CENC offsets
  + 2016-43 Disclosure of user actions through JavaScript with motion and orientation sensors
  + 2016-42 Use-after-free and buffer overflow in Service Workers
  + 2016-41 Content provider permission bypass allows malicious application to access data
  + 2016-40 Privilege escalation through file deletion by Maintenance Service updater
  + 2016-39 Miscellaneous memory safety hazards (rv:46.0 / rv:45.1 / rv:38.8)

* Sat Apr 16 2016 Alexey Gladkov <legion@altlinux.ru> 45.0.2-alt1
- New release (45.0.2).

* Thu Mar 31 2016 Alexey Gladkov <legion@altlinux.ru> 45.0.1-alt2
- Add patch for Gtk 3.20.

* Tue Mar 22 2016 Alexey Gladkov <legion@altlinux.ru> 45.0.1-alt1
- New release (45.0.1).

* Wed Mar 16 2016 Alexey Gladkov <legion@altlinux.ru> 45.0-alt4
- New release (45.0).
- Fixed:
  + 2016-38 Out-of-bounds write with malicious font in Graphite 2
  + 2016-37 Font vulnerabilities in the Graphite 2 library
  + 2016-36 Use-after-free during processing of DER encoded keys in NSS
  + 2016-35 Buffer overflow during ASN.1 decoding in NSS
  + 2016-34 Out-of-bounds read in HTML parser following a failed allocation
  + 2016-33 Use-after-free in GetStaticInstance in WebRTC
  + 2016-32 WebRTC and LibVPX vulnerabilities found through code inspection
  + 2016-31 Memory corruption with malicious NPAPI plugin
  + 2016-30 Buffer overflow in Brotli decompression
  + 2016-29 Same-origin policy violation using performance.getEntries and history navigation with session restore
  + 2016-28 Addressbar spoofing though history navigation and Location protocol property
  + 2016-27 Use-after-free during XML transformations
  + 2016-26 Memory corruption when modifying a file being read by FileReader
  + 2016-25 Use-after-free when using multiple WebRTC data channels
  + 2016-24 Use-after-free in SetBody
  + 2016-23 Use-after-free in HTML5 string parser
  + 2016-22 Service Worker Manager out-of-bounds read in Service Worker Manager
  + 2016-21 Displayed page address can be overridden
  + 2016-20 Memory leak in libstagefright when deleting an array during MP4 processing
  + 2016-19 Linux video memory DOS with Intel drivers
  + 2016-18 CSP reports fail to strip location information for embedded iframe pages
  + 2016-17 Local file overwriting and potential privilege escalation through CSP reports
  + 2016-16 Miscellaneous memory safety hazards (rv:45.0 / rv:38.7)

* Fri Feb 19 2016 Alexey Gladkov <legion@altlinux.ru> 44.0.2-alt4
- Fix gst-plugins-ugly version.

* Tue Feb 16 2016 Alexey Gladkov <legion@altlinux.ru> 44.0.2-alt3
- Use GTK3 again.
- Add RedHat patches.
- Add require gst-plugins-ugly (ALT#30732).
- Fix javascript crash (ALT#31787).
- Fix flash player crash (ALT#31744).

* Mon Feb 15 2016 Alexey Gladkov <legion@altlinux.ru> 44.0.2-alt2
- Rollback to GTK2.

* Fri Feb 12 2016 Alexey Gladkov <legion@altlinux.ru> 44.0.2-alt1
- New release (44.0.2).
- Add symlink to browser-plugins from firefox home directory (ALT#30572)
- Fixed:
  + 2016-13 Same-origin-policy violation using Service Workers with plugins 

* Wed Feb 10 2016 Alexey Gladkov <legion@altlinux.ru> 44.0.1-alt1
- New release (44.0.1).
- Use system cairo.

* Wed Jan 27 2016 Alexey Gladkov <legion@altlinux.ru> 44.0-alt1
- New release (44.0).
- Use GTK3.
- Fixed:
  + 2016-12 Lightweight themes on Firefox for Android do not verify a secure connection
  + 2016-11 Application Reputation service disabled in Firefox 43
  + 2016-10 Unsafe memory manipulation found through code inspection
  + 2016-09 Addressbar spoofing attacks
  + 2016-08 Delay following click events in file download dialog too short on OS X
  + 2016-07 Errors in mp_div and mp_exptmod cryptographic functions in NSS
  + 2016-06 Missing delay following user click events in protocol handler dialog
  + 2016-05 Addressbar spoofing through stored data url shortcuts on Firefox for Android
  + 2016-04 Firefox allows for control characters to be set in cookie names
  + 2016-03 Buffer overflow in WebGL after out of memory allocation
  + 2016-02 Out of Memory crash when parsing GIF format images
  + 2016-01 Miscellaneous memory safety hazards (rv:44.0 / rv:38.6)

* Tue Jan 19 2016 Alexey Gladkov <legion@altlinux.ru> 43.0.4-alt2
- Fix crash in media source (thx: glebfm@).

* Fri Jan 08 2016 Alexey Gladkov <legion@altlinux.ru> 43.0.4-alt1
- New release (43.0.4).
- Fixed:
  + 2015-150 MD5 signatures accepted within TLS 1.2 ServerKeyExchange in server signature 

* Tue Dec 22 2015 Alexey Gladkov <legion@altlinux.ru> 43.0.1-alt1
- New release (43.0.1).
- Fixed:
  + 2015-149 Cross-site reading attack through data and view-source URIs
  + 2015-148 Privilege escalation vulnerabilities in WebExtension APIs
  + 2015-147 Integer underflow and buffer overflow processing MP4 metadata in libstagefright
  + 2015-146 Integer overflow in MP4 playback in 64-bit versions
  + 2015-145 Underflow through code inspection
  + 2015-144 Buffer overflows found through code inspection
  + 2015-143 Linux file chooser crashes on malformed images due to flaws in Jasper library
  + 2015-142 DOS due to malformed frames in HTTP/2
  + 2015-141 Hash in data URI is incorrectly parsed
  + 2015-140 Cross-origin information leak through web workers error events
  + 2015-139 Integer overflow allocating extremely large textures
  + 2015-138 Use-after-free in WebRTC when datachannel is used after being destroyed
  + 2015-137 Firefox allows for control characters to be set in cookies
  + 2015-136 Same-origin policy violation using perfomance.getEntries and history navigation
  + 2015-135 Crash with JavaScript variable assignment with unboxed objects
  + 2015-134 Miscellaneous memory safety hazards (rv:43.0 / rv:38.5)

* Thu Nov 05 2015 Alexey Gladkov <legion@altlinux.ru> 42.0-alt1
- New release (42.0).
- Fixed:
  + 2015-133 NSS and NSPR memory corruption issues
  + 2015-132 Mixed content WebSocket policy bypass through workers
  + 2015-131 Vulnerabilities found through code inspection
  + 2015-130 JavaScript garbage collection crash with Java applet
  + 2015-129 Certain escaped characters in host of Location-header are being treated as non-escaped
  + 2015-128 Memory corruption in libjar through zip files
  + 2015-127 CORS preflight is bypassed when non-standard Content-Type headers are received
  + 2015-126 Crash when accessing HTML tables with accessibility tools on OS X
  + 2015-125 XSS attack through intents on Firefox for Android
  + 2015-124 Android intents can be used on Firefox for Android to open privileged files
  + 2015-123 Buffer overflow during image interactions in canvas
  + 2015-122 Trailing whitespace in IP address hostnames can bypass same-origin policy
  + 2015-121 Disabling scripts in Add-on SDK panels has no effect
  + 2015-120 Reading sensitive profile files through local HTML file on Android
  + 2015-119 Firefox for Android addressbar can be removed after fullscreen mode
  + 2015-118 CSP bypass due to permissive Reader mode whitelist
  + 2015-117 Information disclosure through NTLM authentication
  + 2015-116 Miscellaneous memory safety hazards (rv:42.0 / rv:38.4)

* Tue Oct 20 2015 Alexey Gladkov <legion@altlinux.ru> 41.0.2-alt1
- New release (41.0.2).
- Fixed:
  + 2015-115 Cross-origin restriction bypass using Fetch 

* Sat Sep 26 2015 Alexey Gladkov <legion@altlinux.ru> 41.0-alt1
- New release (41.0).
- Fixed:
  + 2015-114 Information disclosure via the High Resolution Time API
  + 2015-113 Memory safety errors in libGLES in the ANGLE graphics library
  + 2015-112 Vulnerabilities found through code inspection
  + 2015-111 Errors in the handling of CORS preflight request headers
  + 2015-110 Dragging and dropping images exposes final URL after redirects
  + 2015-109 JavaScript immutable property enforcement can be bypassed
  + 2015-108 Scripted proxies can access inner window
  + 2015-107 Out-of-bounds read during 2D canvas display on Linux 16-bit color depth systems
  + 2015-106 Use-after-free while manipulating HTML media content
  + 2015-105 Buffer overflow while decoding WebM video
  + 2015-104 Use-after-free with shared workers and IndexedDB
  + 2015-103 URL spoofing in reader mode
  + 2015-102 Crash when using debugger with SavedStacks in JavaScript
  + 2015-101 Buffer overflow in libvpx while parsing vp9 format video
  + 2015-100 Arbitrary file manipulation by local user through Mozilla updater
  + 2015-99 Site attribute spoofing on Android by pasting URL with unknown scheme
  + 2015-98 Out of bounds read in QCMS library with ICC V4 profile attributes
  + 2015-97 Memory leak in mozTCPSocket to servers
  + 2015-96 Miscellaneous memory safety hazards (rv:41.0 / rv:38.3)
  + 2015-95 Add-on notification bypass through data URLs
  + 2015-94 Use-after-free when resizing canvas element during restyling

* Mon Aug 17 2015 Alexey Gladkov <legion@altlinux.ru> 40.0.2-alt1
- New release (40.0.2).
- Fixed:
  + 2015-92 Use-after-free in XMLHttpRequest with shared workers
  + 2015-91 Mozilla Content Security Policy allows for asterisk wildcards in violation of CSP specification
  + 2015-90 Vulnerabilities found through code inspection
  + 2015-89 Buffer overflows on Libvpx when decoding WebM video
  + 2015-88 Heap overflow in gdk-pixbuf when scaling bitmap images
  + 2015-87 Crash when using shared memory in JavaScript
  + 2015-86 Feed protocol with POST bypasses mixed content protections
  + 2015-85 Out-of-bounds write with Updater and malicious MAR file
  + 2015-84 Arbitrary file overwriting through Mozilla Maintenance Service with hard links
  + 2015-83 Overflow issues in libstagefright
  + 2015-82 Redefinition of non-configurable JavaScript object properties
  + 2015-81 Use-after-free in MediaStream playback
  + 2015-80 Out-of-bounds read with malformed MP3 file
  + 2015-79 Miscellaneous memory safety hazards (rv:40.0 / rv:38.2)

* Mon Aug 10 2015 Alexey Gladkov <legion@altlinux.ru> 39.0.3-alt1
- New release (39.0.3).
- Fixed:
  + 2015-78 Same origin violation and local file stealing via PDF reader
  + 2015-71 NSS incorrectly permits skipping of ServerKeyExchange
  + 2015-70 NSS accepts export-length DHE keys with regular DHE cipher suites
  + 2015-69 Privilege escalation through internal workers
  + 2015-68 OS X crash reports may contain entered key press information
  + 2015-67 Key pinning is ignored when overridable errors are encountered
  + 2015-66 Vulnerabilities found through code inspection
  + 2015-65 Use-after-free in workers while using XMLHttpRequest
  + 2015-64 ECDSA signature validation fails to handle some signatures correctly
  + 2015-63 Use-after-free in Content Policy due to microtask execution error
  + 2015-62 Out-of-bound read while computing an oscillator rendering range in Web Audio
  + 2015-61 Type confusion in Indexed Database Manager
  + 2015-60 Local files or privileged URLs in pages can be opened into new tabs
  + 2015-59 Miscellaneous memory safety hazards (rv:39.0 / rv:31.8 / rv:38.1)

* Sat Jun 13 2015 Alexey Gladkov <legion@altlinux.ru> 38.0.6-alt1
- New release (38.0.6).

* Tue May 19 2015 Alexey Gladkov <legion@altlinux.ru> 38.0.1-alt1
- New release (38.0.1).
- Fixed:
  + 2015-58 Mozilla Windows updater can be run outside of application directory
  + 2015-57 Privilege escalation through IPC channel messages
  + 2015-56 Untrusted site hosting trusted page can intercept webchannel responses
  + 2015-55 Buffer overflow and out-of-bounds read while parsing MP4 video metadata
  + 2015-54 Buffer overflow when parsing compressed XML
  + 2015-53 Use-after-free due to Media Decoder Thread creation during shutdown
  + 2015-52 Sensitive URL encoded information written to Android logcat
  + 2015-51 Use-after-free during text processing with vertical text enabled
  + 2015-50 Out-of-bounds read and write in asm.js validation
  + 2015-49 Referrer policy ignored when links opened by middle-click and context menu
  + 2015-48 Buffer overflow with SVG content and CSS
  + 2015-47 Buffer overflow parsing H.264 video with Linux Gstreamer
  + 2015-46 Miscellaneous memory safety hazards (rv:38.0 / rv:31.7)

* Sun Apr 26 2015 Alexey Gladkov <legion@altlinux.ru> 37.0.2-alt1
- New release (37.0.2).
- Fixed:
  + 2015-45 Memory corruption during failed plugin initialization 

* Mon Apr 06 2015 Alexey Gladkov <legion@altlinux.ru> 37.0.1-alt1
- New release (37.0.1).
- Fixed:
  + 2015-44 Certificate verification bypass through the HTTP/2 Alt-Svc header
  + 2015-43 Loading privileged content through Reader mode
  + 2015-42 Windows can retain access to privileged content on navigation to unprivileged pages
  + 2015-41 PRNG weakness allows for DNS poisoning on Android
  + 2015-40 Same-origin bypass through anchor navigation
  + 2015-39 Use-after-free due to type confusion flaws
  + 2015-38 Memory corruption crashes in Off Main Thread Compositing
  + 2015-37 CORS requests should not follow 30x redirections after preflight
  + 2015-36 Incorrect memory management for simple-type arrays in WebRTC
  + 2015-35 Cursor clickjacking with flash and images
  + 2015-34 Out of bounds read in QCMS library
  + 2015-33 resource:// documents can load privileged pages
  + 2015-32 Add-on lightweight theme installation approval bypassed through MITM attack
  + 2015-31 Use-after-free when using the Fluendo MP3 GStreamer plugin
  + 2015-30 Miscellaneous memory safety hazards (rv:37.0 / rv:31.6)

* Sun Mar 22 2015 Alexey Gladkov <legion@altlinux.ru> 36.0.4-alt1
- New release (36.0.4).
- Fixed:
  + 2015-28 Privilege escalation through SVG navigation
  + 2015-29 Code execution through incorrect JavaScript bounds checking elimination

* Sun Mar 08 2015 Alexey Gladkov <legion@altlinux.ru> 36.0.1-alt1
- New release (36.0.1).
- Fixed:
  + 2015-27 Caja Compiler JavaScript sandbox bypass
  + 2015-26 UI Tour whitelisted sites in background tab can spoof foreground tabs
  + 2015-25 Local files or privileged URLs in pages can be opened into new tabs
  + 2015-24 Reading of local files through manipulation of form autocomplete
  + 2015-23 Use-after-free in Developer Console date with OpenType Sanitiser
  + 2015-22 Crash using DrawTarget in Cairo graphics library
  + 2015-21 Buffer underflow during MP3 playback
  + 2015-20 Buffer overflow during CSS restyling
  + 2015-19 Out-of-bounds read and write while rendering SVG content
  + 2015-18 Double-free when using non-default memory allocators with a zero-length XHR
  + 2015-17 Buffer overflow in libstagefright during MP4 video playback
  + 2015-16 Use-after-free in IndexedDB
  + 2015-15 TLS TURN and STUN connections silently fail to simple TCP connections
  + 2015-14 Malicious WebGL content crash when writing strings
  + 2015-13 Appended period to hostnames can bypass HPKP and HSTS protections
  + 2015-12 Invoking Mozilla updater will load locally stored DLL files
  + 2015-11 Miscellaneous memory safety hazards (rv:36.0 / rv:31.5)

* Wed Jan 28 2015 Alexey Gladkov <legion@altlinux.ru> 35.0.1-alt1
- New release (35.0.1).

* Mon Jan 19 2015 Alexey Gladkov <legion@altlinux.ru> 35.0-alt1
- New release (35.0).
- Fixed:
  + 2015-09 XrayWrapper bypass through DOM objects
  + 2015-08 Delegated OCSP responder certificates failure with id-pkix-ocsp-nocheck extension
  + 2015-07 Gecko Media Plugin sandbox escape
  + 2015-06 Read-after-free in WebRTC
  + 2015-05 Read of uninitialized memory in Web Audio
  + 2015-04 Cookie injection through Proxy Authenticate responses
  + 2015-03 sendBeacon requests lack an Origin header
  + 2015-02 Uninitialized memory use during bitmap rendering
  + 2015-01 Miscellaneous memory safety hazards (rv:35.0 / rv:31.4)

* Thu Dec 18 2014 Alexey Gladkov <legion@altlinux.ru> 34.0.5-alt2
- Enable WebRTC.

* Tue Dec 02 2014 Alexey Gladkov <legion@altlinux.ru> 34.0.5-alt1
- New release (34.0.5).
- Fixed:
  + 2014-91 Privileged access to security wrapped protected objects
  + 2014-90 Apple CoreGraphics framework on OS X 10.10 logging input data to /tmp directory
  + 2014-89 Bad casting from the BasicThebesLayer to BasicContainerLayer
  + 2014-88 Buffer overflow while parsing media content
  + 2014-87 Use-after-free during HTML5 parsing
  + 2014-86 CSP leaks redirect data via violation reports
  + 2014-85 XMLHttpRequest crashes with some input streams
  + 2014-84 XBL bindings accessible via improper CSS declarations
  + 2014-83 Miscellaneous memory safety hazards (rv:34.0 / rv:31.3)

* Mon Nov 17 2014 Alexey Gladkov <legion@altlinux.ru> 33.1.1-alt1
- New release (33.1.1).

* Thu Oct 30 2014 Alexey Gladkov <legion@altlinux.ru> 33.0.2-alt1
- New release (33.0.2).

* Sun Oct 19 2014 Alexey Gladkov <legion@altlinux.ru> 33.0-alt1
- New release (33.0).
- Fixed:
  + MFSA 2014-82 Accessing cross-origin objects via the Alarms API
  + MFSA 2014-81 Inconsistent video sharing within iframe
  + MFSA 2014-80 Key pinning bypasses
  + MFSA 2014-79 Use-after-free interacting with text directionality
  + MFSA 2014-78 Further uninitialized memory use during GIF
  + MFSA 2014-77 Out-of-bounds write with WebM video
  + MFSA 2014-76 Web Audio memory corruption issues with custom waveforms
  + MFSA 2014-75 Buffer overflow during CSS manipulation
  + MFSA 2014-74 Miscellaneous memory safety hazards (rv:33.0 / rv:31.2)

* Wed Sep 24 2014 Alexey Gladkov <legion@altlinux.ru> 32.0.3-alt1
- New release (32.0.3).
- Fixed:
  + MFSA 2014-72 Use-after-free setting text directionality
  + MFSA 2014-71 Profile directory file access through file: protocol
  + MFSA 2014-70 Out-of-bounds read in Web Audio audio timeline
  + MFSA 2014-69 Uninitialized memory use during GIF rendering
  + MFSA 2014-68 Use-after-free during DOM interactions with SVG
  + MFSA 2014-67 Miscellaneous memory safety hazards (rv:32.0 / rv:31.1 / rv:24.8)

* Sun Jul 27 2014 Alexey Gladkov <legion@altlinux.ru> 31.0-alt1
- New release (31.0).
- Fixed:
  + MFSA 2014-66 IFRAME sandbox same-origin access through redirect
  + MFSA 2014-65 Certificate parsing broken by non-standard character encoding
  + MFSA 2014-64 Crash in Skia library when scaling high quality images
  + MFSA 2014-63 Use-after-free while when manipulating certificates in the trusted cache
  + MFSA 2014-62 Exploitable WebGL crash with Cesium JavaScript library
  + MFSA 2014-61 Use-after-free with FireOnStateChange event
  + MFSA 2014-60 Toolbar dialog customization event spoofing
  + MFSA 2014-59 Use-after-free in DirectWrite font handling
  + MFSA 2014-58 Use-after-free in Web Audio due to incorrect control message ordering
  + MFSA 2014-57 Buffer overflow during Web Audio buffering for playback
  + MFSA 2014-56 Miscellaneous memory safety hazards (rv:31.0 / rv:24.7)

* Tue Jul 01 2014 Alexey Gladkov <legion@altlinux.ru> 30.0-alt1
- New release (30.0).
- Built without xulrunner.
- Fixed:
  + MFSA 2014-54 Buffer overflow in Gamepad API
  + MFSA 2014-53 Buffer overflow in Web Audio Speex resampler
  + MFSA 2014-52 Use-after-free with SMIL Animation Controller
  + MFSA 2014-51 Use-after-free in Event Listener Manager
  + MFSA 2014-50 Clickjacking through cursor invisability after Flash interaction
  + MFSA 2014-49 Use-after-free and out of bounds issues found using Address Sanitizer
  + MFSA 2014-48 Miscellaneous memory safety hazards (rv:30.0 / rv:24.6)

* Sun May 11 2014 Alexey Gladkov <legion@altlinux.ru> 29.0.1-alt1
- New release (29.0.1).

* Sat May 10 2014 Alexey Gladkov <legion@altlinux.ru> 29.0-alt1
- New release (29.0).
- Fixed:
  + MFSA 2014-47 Debugger can bypass XrayWrappers with JavaScript
  + MFSA 2014-46 Use-after-free in nsHostResolve
  + MFSA 2014-45 Incorrect IDNA domain name matching for wildcard certificates
  + MFSA 2014-44 Use-after-free in imgLoader while resizing images
  + MFSA 2014-43 Cross-site scripting (XSS) using history navigations
  + MFSA 2014-42 Privilege escalation through Web Notification API
  + MFSA 2014-41 Out-of-bounds write in Cairo
  + MFSA 2014-40 Firefox for Android addressbar suppression
  + MFSA 2014-39 Use-after-free in the Text Track Manager for HTML video
  + MFSA 2014-38 Buffer overflow when using non-XBL object as XBL
  + MFSA 2014-37 Out of bounds read while decoding JPG images
  + MFSA 2014-36 Web Audio memory corruption issues
  + MFSA 2014-35 Privilege escalation through Mozilla Maintenance Service Installer
  + MFSA 2014-34 Miscellaneous memory safety hazards (rv:29.0 / rv:24.5)

* Sat Mar 22 2014 Alexey Gladkov <legion@altlinux.ru> 28.0-alt1
- New release (28.0).
- Fixed:
  + MFSA 2014-32 Out-of-bounds write through TypedArrayObject after neutering
  + MFSA 2014-31 Out-of-bounds read/write through neutering ArrayBuffer objects
  + MFSA 2014-30 Use-after-free in TypeObject
  + MFSA 2014-29 Privilege escalation using WebIDL-implemented APIs
  + MFSA 2014-28 SVG filters information disclosure through feDisplacementMap
  + MFSA 2014-27 Memory corruption in Cairo during PDF font rendering
  + MFSA 2014-26 Information disclosure through polygon rendering in MathML
  + MFSA 2014-25 Firefox OS DeviceStorageFile object vulnerable to relative path escape
  + MFSA 2014-24 Android Crash Reporter open to manipulation
  + MFSA 2014-23 Content Security Policy for data: documents not preserved by session restore
  + MFSA 2014-22 WebGL content injection from one domain to rendering in another
  + MFSA 2014-21 Local file access via Open Link in new tab
  + MFSA 2014-20 onbeforeunload and Javascript navigation DOS
  + MFSA 2014-19 Spoofing attack on WebRTC permission prompt
  + MFSA 2014-18 crypto.generateCRMFRequest does not validate type of key
  + MFSA 2014-17 Out of bounds read during WAV file decoding
  + MFSA 2014-16 Files extracted during updates are not always read only
  + MFSA 2014-15 Miscellaneous memory safety hazards (rv:28.0 / rv:24.4)

* Fri Feb 07 2014 Alexey Gladkov <legion@altlinux.ru> 27.0-alt1
- New release (27.0).
- Fixed:
  + MFSA 2014-13 Inconsistent JavaScript handling of access to Window objects
  + MFSA 2014-12 NSS ticket handling issues
  + MFSA 2014-11 Crash when using web workers with asm.js
  + MFSA 2014-10 Firefox default start page UI content invokable by script
  + MFSA 2014-09 Cross-origin information leak through web workers
  + MFSA 2014-08 Use-after-free with imgRequestProxy and image proccessing
  + MFSA 2014-07 XSLT stylesheets treated as styles in Content Security Policy
  + MFSA 2014-06 Profile path leaks to Android system log
  + MFSA 2014-05 Information disclosure with *FromPoint on iframes
  + MFSA 2014-04 Incorrect use of discarded images by RasterImage
  + MFSA 2014-03 UI selection timeout missing on download prompts
  + MFSA 2014-02 Clone protected content with XBL scopes
  + MFSA 2014-01 Miscellaneous memory safety hazards (rv:27.0 / rv:24.3)

* Mon Dec 23 2013 Alexey Gladkov <legion@altlinux.ru> 26.0-alt1
- New release (26.0).
- Fixed:
  + MFSA 2013-117 Mis-issued ANSSI/DCSSI certificate
  + MFSA 2013-116 JPEG information leak
  + MFSA 2013-115 GetElementIC typed array stubs can be generated outside observed typesets
  + MFSA 2013-114 Use-after-free in synthetic mouse movement
  + MFSA 2013-113 Trust settings for built-in roots ignored during EV certificate validation
  + MFSA 2013-112 Linux clipboard information disclosure though selection paste
  + MFSA 2013-111 Segmentation violation when replacing ordered list elements
  + MFSA 2013-110 Potential overflow in JavaScript binary search algorithms
  + MFSA 2013-109 Use-after-free during Table Editing
  + MFSA 2013-108 Use-after-free in event listeners
  + MFSA 2013-107 Sandbox restrictions not applied to nested object elements
  + MFSA 2013-106 Character encoding cross-origin XSS attack
  + MFSA 2013-105 Application Installation doorhanger persists on navigation
  + MFSA 2013-104 Miscellaneous memory safety hazards (rv:26.0 / rv:24.2)

* Thu Nov 21 2013 Alexey Gladkov <legion@altlinux.ru> 25.0.1-alt1
- New release (25.0.1).
- Fixed:
  + MFSA 2013-103 Miscellaneous Network Security Services (NSS) vulnerabilities

* Sun Nov 03 2013 Alexey Gladkov <legion@altlinux.ru> 25.0-alt1
- New release (25.0).
- Fixed:
  + MFSA 2013-102 Use-after-free in HTML document templates
  + MFSA 2013-101 Memory corruption in workers
  + MFSA 2013-100 Miscellaneous use-after-free issues found through ASAN fuzzing
  + MFSA 2013-99 Security bypass of PDF.js checks using iframes
  + MFSA 2013-98 Use-after-free when updating offline cache
  + MFSA 2013-97 Writing to cycle collected object during image decoding
  + MFSA 2013-96 Improperly initialized memory and overflows in some JavaScript functions
  + MFSA 2013-95 Access violation with XSLT and uninitialized data
  + MFSA 2013-94 Spoofing addressbar though SELECT element
  + MFSA 2013-93 Miscellaneous memory safety hazards (rv:25.0 / rv:24.1 / rv:17.0.10)

* Tue Oct 01 2013 Alexey Gladkov <legion@altlinux.ru> 24.0-alt1
- New release (24.0).
- Add gstreamer support (ALT#29454).
- Fixed:
  + MFSA 2013-92 GC hazard with default compartments and frame chain restoration
  + MFSA 2013-91 User-defined properties on DOM proxies get the wrong "this" object
  + MFSA 2013-90 Memory corruption involving scrolling
  + MFSA 2013-89 Buffer overflow with multi-column, lists, and floats
  + MFSA 2013-88 compartment mismatch re-attaching XBL-backed nodes
  + MFSA 2013-87 Shared object library loading from writable location
  + MFSA 2013-86 WebGL Information disclosure through OS X NVIDIA graphic drivers
  + MFSA 2013-85 Uninitialized data in IonMonkey
  + MFSA 2013-84 Same-origin bypass through symbolic links
  + MFSA 2013-83 Mozilla Updater does not lock MAR file after signature verification
  + MFSA 2013-82 Calling scope for new Javascript objects can lead to memory corruption
  + MFSA 2013-81 Use-after-free with select element
  + MFSA 2013-80 NativeKey continues handling key messages after widget is destroyed
  + MFSA 2013-79 Use-after-free in Animation Manager during stylesheet cloning
  + MFSA 2013-78 Integer overflow in ANGLE library
  + MFSA 2013-77 Improper state in HTML5 Tree Builder with templates
  + MFSA 2013-76 Miscellaneous memory safety hazards (rv:24.0 / rv:17.0.9)

* Mon Aug 12 2013 Alexey Gladkov <legion@altlinux.ru> 23.0-alt1
- New release (23.0).
- Fixed:
  + MFSA 2013-75 Local Java applets may read contents of local file system
  + MFSA 2013-74 Firefox full and stub installer DLL hijacking
  + MFSA 2013-73 Same-origin bypass with web workers and XMLHttpRequest
  + MFSA 2013-72 Wrong principal used for validating URI for some Javascript components
  + MFSA 2013-71 Further Privilege escalation through Mozilla Updater
  + MFSA 2013-70 Bypass of XrayWrappers using XBL Scopes
  + MFSA 2013-69 CRMF requests allow for code execution and XSS attacks
  + MFSA 2013-68 Document URI misrepresentation and masquerading
  + MFSA 2013-67 Crash during WAV audio file decoding
  + MFSA 2013-66 Buffer overflow in Mozilla Maintenance Service and Mozilla Updater
  + MFSA 2013-65 Buffer underflow when generating CRMF requests
  + MFSA 2013-64 Use after free mutating DOM during SetBody
  + MFSA 2013-63 Miscellaneous memory safety hazards (rv:23.0 / rv:17.0.8)

* Wed Jun 26 2013 Alexey Gladkov <legion@altlinux.ru> 22.0-alt1
- New release (22.0).
- Fixed:
  + MFSA 2013-62 Inaccessible updater can lead to local privilege escalation
  + MFSA 2013-61 Homograph domain spoofing in .com, .net and .name
  + MFSA 2013-60 getUserMedia permission dialog incorrectly displays location
  + MFSA 2013-59 XrayWrappers can be bypassed to run user defined methods in a privileged context
  + MFSA 2013-58 X-Frame-Options ignored when using server push with multi-part responses
  + MFSA 2013-57 Sandbox restrictions not applied to nested frame elements
  + MFSA 2013-56 PreserveWrapper has inconsistent behavior
  + MFSA 2013-55 SVG filters can lead to information disclosure
  + MFSA 2013-54 Data in the body of XHR HEAD requests leads to CSRF attacks
  + MFSA 2013-53 Execution of unmapped memory through onreadystatechange event
  + MFSA 2013-52 Arbitrary code execution within Profiler
  + MFSA 2013-51 Privileged content access and execution via XBL
  + MFSA 2013-50 Memory corruption found using Address Sanitizer
  + MFSA 2013-49 Miscellaneous memory safety hazards (rv:22.0 / rv:17.0.7)

* Sat Jun 01 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt1
- New release (21.0).
- Fixed:
  + MFSA 2013-48 Memory corruption found using Address Sanitizer
  + MFSA 2013-47 Uninitialized functions in DOMSVGZoomEvent
  + MFSA 2013-46 Use-after-free with video and onresize event
  + MFSA 2013-45 Mozilla Updater fails to update some Windows Registry entries
  + MFSA 2013-44 Local privilege escalation through Mozilla Maintenance Service
  + MFSA 2013-43 File input control has access to full path
  + MFSA 2013-42 Privileged access for content level constructor
  + MFSA 2013-41 Miscellaneous memory safety hazards (rv:21.0 / rv:17.0.6)

* Wed Apr 10 2013 Alexey Gladkov <legion@altlinux.ru> 20.0-alt1
- New release (20.0).
- Fixed:
  + MFSA 2013-40 Out-of-bounds array read in CERT_DecodeCertPackage
  + MFSA 2013-39 Memory corruption while rendering grayscale PNG images
  + MFSA 2013-38 Cross-site scripting (XSS) using timed history navigations
  + MFSA 2013-37 Bypass of tab-modal dialog origin disclosure
  + MFSA 2013-36 Bypass of SOW protections allows cloning of protected nodes
  + MFSA 2013-35 WebGL crash with Mesa graphics driver on Linux
  + MFSA 2013-34 Privilege escalation through Mozilla Updater
  + MFSA 2013-33 World read and write access to app_tmp directory on Android
  + MFSA 2013-32 Privilege escalation through Mozilla Maintenance Service
  + MFSA 2013-31 Out-of-bounds write in Cairo library
  + MFSA 2013-30 Miscellaneous memory safety hazards (rv:20.0 / rv:17.0.5)

* Sat Mar 09 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.2-alt1
- New release (19.0.2).
- Fixed:
  + MFSA 2013-29 Use-after-free in HTML Editor

* Fri Mar 01 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.1-alt1
- New release (19.0.1).
- Fixed:
  + MFSA 2013-28 Use-after-free, out of bounds read, and buffer overflow issues found using Address Sanitizer
  + MFSA 2013-27 Phishing on HTTPS connection through malicious proxy
  + MFSA 2013-26 Use-after-free in nsImageLoadingContent
  + MFSA 2013-25 Privacy leak in JavaScript Workers
  + MFSA 2013-24 Web content bypass of COW and SOW security wrappers
  + MFSA 2013-23 Wrapped WebIDL objects can be wrapped again
  + MFSA 2013-22 Out-of-bounds read in image rendering
  + MFSA 2013-21 Miscellaneous memory safety hazards (rv:19.0 / rv:17.0.3)

* Sun Feb 10 2013 Alexey Gladkov <legion@altlinux.ru> 18.0.2-alt1
- New release (18.0.2).

* Mon Jan 28 2013 Alexey Gladkov <legion@altlinux.ru> 18.0.1-alt1
- New release (18.0.1).

* Thu Jan 17 2013 Alexey Gladkov <legion@altlinux.ru> 18.0-alt1
- New release (18.0).
- Fixed:
  + MFSA 2013-20 Mis-issued TURKTRUST certificates
  + MFSA 2013-19 Use-after-free in Javascript Proxy objects
  + MFSA 2013-18 Use-after-free in Vibrate
  + MFSA 2013-17 Use-after-free in ListenerManager
  + MFSA 2013-16 Use-after-free in serializeToStream
  + MFSA 2013-15 Privilege escalation through plugin objects
  + MFSA 2013-14 Chrome Object Wrapper (COW) bypass through changing prototype
  + MFSA 2013-13 Memory corruption in XBL with XML bindings containing SVG
  + MFSA 2013-12 Buffer overflow in Javascript string concatenation
  + MFSA 2013-11 Address space layout leaked in XBL objects
  + MFSA 2013-10 Event manipulation in plugin handler to bypass same-origin policy
  + MFSA 2013-09 Compartment mismatch with quickstubs returned values
  + MFSA 2013-08 AutoWrapperChanger fails to keep objects alive during garbage collection
  + MFSA 2013-07 Crash due to handling of SSL on threads
  + MFSA 2013-06 Touch events are shared across iframes
  + MFSA 2013-05 Use-after-free when displaying table with many columns and column groups
  + MFSA 2013-04 URL spoofing in addressbar during page loads
  + MFSA 2013-03 Buffer Overflow in Canvas
  + MFSA 2013-02 Use-after-free and buffer overflow issues found using Address Sanitizer
  + MFSA 2013-01 Miscellaneous memory safety hazards (rv:18.0/ rv:10.0.12 / rv:17.0.2)
  + MFSA 2012-98 Firefox installer DLL hijacking

* Wed Dec 05 2012 Alexey Gladkov <legion@altlinux.ru> 17.0.1-alt1
- New release (17.0.1).

* Wed Nov 21 2012 Alexey Gladkov <legion@altlinux.ru> 17.0-alt1
- New release (17.0).
- Fixed:
  + MFSA 2012-106 Use-after-free, buffer overflow, and memory corruption issues found using Address Sanitizer
  + MFSA 2012-105 Use-after-free and buffer overflow issues found using Address Sanitizer
  + MFSA 2012-104 CSS and HTML injection through Style Inspector
  + MFSA 2012-103 Frames can shadow top.location
  + MFSA 2012-102 Script entered into Developer Toolbar runs with chrome privileges
  + MFSA 2012-101 Improper character decoding in HZ-GB-2312 charset
  + MFSA 2012-100 Improper security filtering for cross-origin wrappers
  + MFSA 2012-99 XrayWrappers exposes chrome-only properties when not in chrome compartment
  + MFSA 2012-98 Firefox installer DLL hijacking
  + MFSA 2012-97 XMLHttpRequest inherits incorrect principal within sandbox
  + MFSA 2012-96 Memory corruption in str_unescape
  + MFSA 2012-95 Javascript: URLs run in privileged context on New Tab page
  + MFSA 2012-94 Crash when combining SVG text on path with CSS
  + MFSA 2012-93 evalInSanbox location context incorrectly applied
  + MFSA 2012-92 Buffer overflow while rendering GIF images
  + MFSA 2012-91 Miscellaneous memory safety hazards (rv:17.0/ rv:10.0.11)

* Thu Nov 01 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.2-alt1
- New release (16.0.2).
- Fixed:
  + MFSA 2012-90 Fixes for Location object issues

* Mon Oct 22 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.1-alt1
- New release (16.0.1).
- Fixed:
  + MFSA 2012-89 defaultValue security checks not applied
  + MFSA 2012-88 Miscellaneous memory safety hazards (rv:16.0.1)
  + MFSA 2012-87 Use-after-free in the IME State Manager
  + MFSA 2012-86 Heap memory corruption issues found using Address Sanitizer
  + MFSA 2012-85 Use-after-free, buffer overflow, and out of bounds read issues found using Address Sanitizer
  + MFSA 2012-84 Spoofing and script injection through location.hash
  + MFSA 2012-83 Chrome Object Wrapper (COW) does not disallow acces to privileged functions or properties
  + MFSA 2012-82 top object and location property accessible by plugins
  + MFSA 2012-81 GetProperty function can bypass security checks
  + MFSA 2012-80 Crash with invalid cast when using instanceof operator
  + MFSA 2012-79 DOS and crash with full screen and history navigation
  + MFSA 2012-78 Reader Mode pages have chrome privileges
  + MFSA 2012-77 Some DOMWindowUtils methods bypass security checks
  + MFSA 2012-76 Continued access to initial origin after setting document.domain
  + MFSA 2012-75 select element persistance allows for attacks
  + MFSA 2012-74 Miscellaneous memory safety hazards (rv:16.0/ rv:10.0.8)

* Wed Aug 29 2012 Alexey Gladkov <legion@altlinux.ru> 15.0-alt1
- New release (15.0).
- Fixed:
  + MFSA 2012-72 Web console eval capable of executing chrome-privileged code
  + MFSA 2012-71 Insecure use of __android_log_print
  + MFSA 2012-70 Location object security checks bypassed by chrome code
  + MFSA 2012-69 Incorrect site SSL certificate data display
  + MFSA 2012-68 DOMParser loads linked resources in extensions when parsing text/html
  + MFSA 2012-67 Installer will launch incorrect executable following new installation
  + MFSA 2012-66 HTTPMonitor extension allows for remote debugging without explicit activation
  + MFSA 2012-65 Out-of-bounds read in format-number in XSLT
  + MFSA 2012-64 Graphite 2 memory corruption
  + MFSA 2012-63 SVG buffer overflow and use-after-free issues
  + MFSA 2012-62 WebGL use-after-free and memory corruption
  + MFSA 2012-61 Memory corruption with bitmap format images with negative height
  + MFSA 2012-60 Escalation of privilege through about:newtab
  + MFSA 2012-59 Location object can be shadowed using Object.defineProperty
  + MFSA 2012-58 Use-after-free issues found using Address Sanitizer
  + MFSA 2012-57 Miscellaneous memory safety hazards (rv:15.0/ rv:10.0.7)

* Sun Jul 29 2012 Alexey Gladkov <legion@altlinux.ru> 14.0.1-alt1
- New release (14.0.1).
- Fixed:
  + MFSA 2012-56 Code execution through javascript: URLs
  + MFSA 2012-55 feed: URLs with an innerURI inherit security context of page
  + MFSA 2012-53 Content Security Policy 1.0 implementation errors cause data leakage
  + MFSA 2012-52 JSDependentString::undepend string conversion results in memory corruption
  + MFSA 2012-51 X-Frame-Options header ignored when duplicated
  + MFSA 2012-50 Out of bounds read in QCMS
  + MFSA 2012-49 Same-compartment Security Wrappers can be bypassed
  + MFSA 2012-48 use-after-free in nsGlobalWindow::PageHidden
  + MFSA 2012-47 Improper filtering of javascript in HTML feed-view
  + MFSA 2012-46 XSS through data: URLs
  + MFSA 2012-45 Spoofing issue with location
  + MFSA 2012-44 Gecko memory corruption
  + MFSA 2012-43 Incorrect URL displayed in addressbar through drag and drop
  + MFSA 2012-42 Miscellaneous memory safety hazards (rv:14.0/ rv:10.0.6)

* Sun Jul 01 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New release (13.0.1).
- Fixed:
  + MFSA 2012-40 Buffer overflow and use-after-free issues found using Address Sanitizer
  + MFSA 2012-39 NSS parsing errors with zero length items
  + MFSA 2012-38 Use-after-free while replacing/inserting a node in a document
  + MFSA 2012-37 Information disclosure though Windows file shares and shortcut files
  + MFSA 2012-36 Content Security Policy inline-script bypass
  + MFSA 2012-35 Privilege escalation through Mozilla Updater and Windows Updater Service
  + MFSA 2012-34 Miscellaneous memory safety hazards

* Tue May 08 2012 Alexey Gladkov <legion@altlinux.ru> 12.0-alt1
- New release (12.0).
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
  + MFSA 2012-21 Multiple security flaws fixed in FreeType v2.4.9
  + MFSA 2012-20 Miscellaneous memory safety hazards (rv:12.0/ rv:10.0.4)

* Thu Apr 19 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
- New release (11.0).
- Fixed:
  + MFSA 2012-19 Miscellaneous memory safety hazards (rv:11.0/ rv:10.0.3 / rv:1.9.2.28)
  + MFSA 2012-18 window.fullScreen writeable by untrusted content
  + MFSA 2012-17 Crash when accessing keyframe cssText after dynamic modification
  + MFSA 2012-16 Escalation of privilege with Javascript: URL as home page
  + MFSA 2012-15 XSS with multiple Content Security Policy headers
  + MFSA 2012-14 SVG issues found with Address Sanitizer
  + MFSA 2012-13 XSS with Drag and Drop and Javascript: URL
  + MFSA 2012-12 Use-after-free in shlwapi.dll

* Tue Feb 21 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- New release (10.0.2).
- Fixed:
  + MFSA 2012-11 libpng integer overflow
  + MFSA 2012-10 use after free in nsXBLDocumentInfo::ReadPrototypeBindings
  + MFSA 2012-09 Firefox Recovery Key.html is saved with unsafe permission
  + MFSA 2012-08 Crash with malformed embedded XSLT stylesheets
  + MFSA 2012-07 Potential Memory Corruption When Decoding Ogg Vorbis files
  + MFSA 2012-06 Uninitialized memory appended when encoding icon images may cause information disclosure
  + MFSA 2012-05 Frame scripts calling into untrusted objects bypass security checks
  + MFSA 2012-04 Child nodes from nsDOMAttribute still accessible after removal of nodes
  + MFSA 2012-03 <iframe> element exposed across domains via name attribute
  + MFSA 2012-01 Miscellaneous memory safety hazards (rv:10.0/ rv:1.9.2.26)

* Mon Jan 09 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt1
- New release (9.0.1).
- Check default browser (ALT#26195).
- Change location for noarch extensions (ALT#26702).
- Add translation for summary and description (ALT#22789).
- Fixed:
  + MFSA 2011-58 Crash scaling <video> to extreme sizes
  + MFSA 2011-57 Crash when plugin removes itself on Mac OS X
  + MFSA 2011-56 Key detection without JavaScript via SVG animation
  + MFSA 2011-55 nsSVGValue out-of-bounds access
  + MFSA 2011-54 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-53 Miscellaneous memory safety hazards (rv:9.0)

* Mon Nov 14 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New release (8.0).
- Fixed:
  + MFSA 2011-52 Code execution via NoWaiverWrapper
  + MFSA 2011-51 Cross-origin image theft on Mac with integrated Intel GPU
  + MFSA 2011-50 Cross-origin data theft using canvas and Windows D2D
  + MFSA 2011-49 Memory corruption while profiling using Firebug
  + MFSA 2011-48 Miscellaneous memory safety hazards (rv:8.0)
  + MFSA 2011-47 Potential XSS against sites using Shift-JIS

* Wed Oct 19 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt2
- Drop depends for extensions.

* Thu Oct 06 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt1
- New release (7.0.1).
- Fixed:
  + MFSA 2011-45 Inferring Keystrokes from motion data
  + MFSA 2011-44 Use after free reading OGG headers
  + MFSA 2011-43 loadSubScript unwraps XPCNativeWrapper scope parameter
  + MFSA 2011-42 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-41 Potentially exploitable WebGL crashes
  + MFSA 2011-40 Code installation through holding down Enter
  + MFSA 2011-39 Defense against multiple Location headers due to CRLF Injection
  + MFSA 2011-36 Miscellaneous memory safety hazards (rv:7.0 / rv:1.9.2.23)

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.2-alt1
- New release (6.0.2).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.1-alt1
- New release (6.0.1).
- Fixed:
  + MFSA 2011-34 Protection against fraudulent DigiNotar certificates

* Mon Aug 22 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New release (6.0).
- Add Conflict to firefox-settings-desktop (ALT#25473).
- Fixed:
  + MFSA 2011-29 Security issues addressed in Firefox6.

* Wed Jul 13 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt1
- New release (5.0.1).
- Fixed:
  + MFSA 2011-28 Non-whitelisted site can trigger xpinstall
  + MFSA 2011-27 XSS encoding hazard with inline SVG
  + MFSA 2011-26 Multiple WebGL crashes
  + MFSA 2011-25 Stealing of cross-domain images using WebGL textures
  + MFSA 2011-22 Integer overflow and arbitrary code execution in Array.reduceRight()
  + MFSA 2011-21 Memory corruption due to multipart/x-mixed-replace images
  + MFSA 2011-20 Use-after-free vulnerability when viewing XUL document with script disabled
  + MFSA 2011-19 Miscellaneous memory safety hazards (rv:3.0/1.9.2.18)

* Mon May 02 2011 Alexey Gladkov <legion@altlinux.ru> 4.0.1-alt1
- New release (4.0.1).
- Update desktop file (ALT#25530).
- Fixed:
  + MFSA 2011-18 XSLT generate-id() function heap address leak
  + MFSA 2011-17 WebGLES vulnerabilities
  + MFSA 2011-12 Miscellaneous memory safety hazards (rv:2.0.1/ 1.9.2.17/ 1.9.1.19)

* Fri Apr 22 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt3
- Set some settings in Firefox to default values (ALT#22148).

* Tue Apr 19 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt2
- Fix plugins path.
- Fix alternatives for %_bindir/xbrowser.

* Fri Apr 01 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt1
- New release (4.0).
- Remove alternatives for configuration.

* Tue Mar 08 2011 Alexey Gladkov <legion@altlinux.ru> 3.6.15-alt1.20110308
- New release (3.6.15).
- Fixed:
  + MFSA 2011-10 CSRF risk with plugins and 307 redirects
  + MFSA 2011-09 Crash caused by corrupted JPEG image
  + MFSA 2011-08 ParanoidFragmentSink allows javascript: URLs in chrome documents
  + MFSA 2011-07 Memory corruption during text run construction (Windows)
  + MFSA 2011-06 Use-after-free error using Web Workers
  + MFSA 2011-05 Buffer overflow in JavaScript atom map
  + MFSA 2011-04 Buffer overflow in JavaScript upvarMap
  + MFSA 2011-03 Use-after-free error in JSON.stringify
  + MFSA 2011-02 Recursive eval call causes confirm dialogs to evaluate to true
  + MFSA 2011-01 Miscellaneous memory safety hazards (rv:1.9.2.14/ 1.9.1.17)

* Wed Dec 22 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.13-alt1.20101222
- New release (3.6.13).
- Fixed:
  + MFSA 2010-84 XSS hazard in multiple character encodings
  + MFSA 2010-83 Location bar SSL spoofing using network error page
  + MFSA 2010-82 Incomplete fix for CVE-2010-0179
  + MFSA 2010-81 Integer overflow vulnerability in NewIdArray
  + MFSA 2010-80 Use-after-free error with nsDOMAttribute MutationObserver
  + MFSA 2010-79 Java security bypass from LiveConnect loaded via data: URL meta refresh
  + MFSA 2010-78 Add support for OTS font sanitizer
  + MFSA 2010-77 Crash and remote code execution using HTML tags inside a XUL tree
  + MFSA 2010-76 Chrome privilege escalation with window.open and <isindex> element
  + MFSA 2010-75 Buffer overflow while line breaking after document.write with long string
  + MFSA 2010-74 Miscellaneous memory safety hazards (rv:1.9.2.13/ 1.9.1.16)

* Sun Nov 14 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.13-alt1.20101110
- New release (3.6.12).
- Fixed:
  + MFSA 2010-73 Heap buffer overflow mixing document.write and DOM insertion

* Tue Oct 26 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.12-alt1.20101025
- New release (3.6.11).
- Fixed:
  + MFSA 2010-72 Insecure Diffie-Hellman key exchange
  + MFSA 2010-71 Unsafe library loading vulnerabilities
  + MFSA 2010-70 SSL wildcard certificate matching IP addresses
  + MFSA 2010-69 Cross-site information disclosure via modal calls
  + MFSA 2010-68 XSS in gopher parser when parsing hrefs
  + MFSA 2010-67 Dangling pointer vulnerability in LookupGetterOrSetter
  + MFSA 2010-66 Use-after-free error in nsBarProp
  + MFSA 2010-65 Buffer overflow and memory corruption using document.write
  + MFSA 2010-64 Miscellaneous memory safety hazards (rv:1.9.2.11/ 1.9.1.14)

* Tue Sep 21 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.11-alt1.20100920
- New release (3.6.10).

* Sun Sep 12 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.10-alt1.20100909
- New release (3.6.9).
- Fixed:
  + MFSA 2010-63 Information leak via XMLHttpRequest statusText
  + MFSA 2010-62 Copy-and-paste or drag-and-drop into designMode document allows XSS
  + MFSA 2010-61 UTF-7 XSS by overriding document charset using <object> type attribute
  + MFSA 2010-59 SJOW creates scope chains ending in outer object
  + MFSA 2010-58 Crash on Mac using fuzzed font in data: URL
  + MFSA 2010-57 Crash and remote code execution in normalizeDocument
  + MFSA 2010-56 Dangling pointer vulnerability in nsTreeContentView
  + MFSA 2010-55 XUL tree removal crash and remote code execution
  + MFSA 2010-54 Dangling pointer vulnerability in nsTreeSelection
  + MFSA 2010-53 Heap buffer overflow in nsTextFrameUtils::TransformText
  + MFSA 2010-52 Windows XP DLL loading vulnerability
  + MFSA 2010-51 Dangling pointer vulnerability using DOM plugin array
  + MFSA 2010-50 Frameset integer overflow vulnerability
  + MFSA 2010-49 Miscellaneous memory safety hazards (rv:1.9.2.9/ 1.9.1.12)

* Thu Jul 29 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.9-alt1.20100725
- New release (3.6.8).
- Fixed:
  + MFSA 2010-48 Dangling pointer crash regression from plugin parameter array fix
  + MFSA 2010-47 Cross-origin data leakage from script filename in error messages
  + MFSA 2010-46 Cross-domain data theft using CSS
  + MFSA 2010-45 Multiple location bar spoofing vulnerabilities
  + MFSA 2010-44 Characters mapped to U+FFFD in 8 bit encodings cause subsequent character to vanish
  + MFSA 2010-43 Same-origin bypass using canvas context
  + MFSA 2010-42 Cross-origin data disclosure via Web Workers and importScripts
  + MFSA 2010-41 Remote code execution using malformed PNG image
  + MFSA 2010-40 nsTreeSelection dangling pointer remote code execution vulnerability
  + MFSA 2010-39 nsCSSValue::Array index integer overflow
  + MFSA 2010-38 Arbitrary code execution using SJOW and fast native function
  + MFSA 2010-37 Plugin parameter EnsureCachedAttrParamArrays remote code execution vulnerability
  + MFSA 2010-36 Use-after-free error in NodeIterator
  + MFSA 2010-35 DOM attribute cloning remote code execution vulnerability
  + MFSA 2010-34 Miscellaneous memory safety hazards (rv:1.9.2.7/ 1.9.1.11)

* Sun Jun 27 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.6-alt1.20100626
- New release (3.6.6).
- Fixed:
  + MFSA 2010-33 User tracking across sites using Math.random()
  + MFSA 2010-32 Content-Disposition: attachment ignored if Content-Type: multipart also present
  + MFSA 2010-31 focus() behavior can be used to inject or steal keystrokes
  + MFSA 2010-30 Integer Overflow in XSLT Node Sorting
  + MFSA 2010-29 Heap buffer overflow in nsGenericDOMDataNode::SetTextInternal
  + MFSA 2010-28 Freed object reuse across plugin instances
  + MFSA 2010-26 Crashes with evidence of memory corruption (rv:1.9.2.4/ 1.9.1.10)

* Mon Apr 05 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.3-alt1.20100404
- New release (3.6.3).
- Fixed:
  + MFSA 2009-25 Re-use of freed object due to scope confusion

* Mon Mar 29 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.2-alt1.20100328
- New release (3.6.2).
- Fix for Transport Layer Security (ALT#22994).
- Fix addons search (ALT#22878).
- Fix release notes (ALT#22883).
- Fixed:
  + MFSA 2010-15 Asynchronous Auth Prompt attaches to wrong window
  + MFSA 2010-14 Browser chrome defacement via cached XUL stylesheets
  + MFSA 2010-13 Content policy bypass with image preloading
  + MFSA 2010-12 XSS using addEventListener and setTimeout on a wrapped object
  + MFSA 2010-11 Crashes with evidence of memory corruption (rv:1.9.2.2/ 1.9.1.8/ 1.9.0.18)
  + MFSA 2010-10 XSS via plugins and unprotected Location object
  + MFSA 2010-09 Deleted frame reuse in multipart/x-mixed-replace image
  + MFSA 2010-08 WOFF heap corruption due to integer overflow

* Fri Jan 22 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt1
- New release (3.6.0).
- Fix process name (ALT#22731).

* Thu Jan 07 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt0.20100113
- New snapshot (3.6.0 20100113).

* Mon Nov 24 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt0.20091124
- New major branch (3.6.0 b4pre).

* Sun Oct 11 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20091010
- New snapshot (3.5.3 20091010).
- KDE: Update patches (ALT#21509).

* Mon Sep 28 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090918.1
- Rebuild with new browser-plugins-npapi.

* Sun Sep 20 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090918
- New snapshot (3.5.3 20090918).
- Set firefox as default KDE/KDE4 browser (ALT#21509).
- Update desktop file (ALT#21510).
- Update requires (ALT#21533).

* Tue Sep 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090831
- New snapshot (3.5.3 20090831).

* Fri Jul 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.1-alt1
- New release (3.5.1).

* Wed Jul 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt2
- New release (3.5).

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt1.20090601
- New snapshot (3.5 20090601).

* Wed Apr 24 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt1.20090424
- New snapshot (3.5 20090424).

* Sun Jan 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.1-alt1.20090312
- New snapshot (3.1 20090312).

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.4-alt1
- New release (3.0.4).
- Fixed:
  + MFSA 2008-58 Parsing error in E4X default namespace
  + MFSA 2008-57 -moz-binding property bypasses security checks on codebase principals
  + MFSA 2008-56 nsXMLHttpRequest::NotifyEventListeners() same-origin violation
  + MFSA 2008-55 Crash and remote code execution in nsFrameManager
  + MFSA 2008-54 Buffer overflow in http-index-format parser
  + MFSA 2008-53 XSS and JavaScript privilege escalation via session restore
  + MFSA 2008-52 Crashes with evidence of memory corruption (rv:1.9.0.4/1.8.1.18)
  + MFSA 2008-51 file: URIs inherit chrome privileges when opened from chrome
  + MFSA 2008-47 Information stealing via local shortcut files

* Wed Oct 08 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.3-alt1
- New release (3.0.3).
- Firefox set itself as default browser correctly (ALT#17384).
- Reload new plugins.
- Fixed:
  + MFSA 2008-44 resource: traversal vulnerabilities
  + MFSA 2008-43 BOM characters stripped from JavaScript before execution
  + MFSA 2008-42 Crashes with evidence of memory corruption (rv:1.9.0.2/1.8.1.17)
  + MFSA 2008-41 Privilege escalation via XPCnativeWrapper pollution
  + MFSA 2008-40 Forced mouse drag

* Tue Sep 09 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt2
- New bugfix build.
- Update desktop file (ALT#10558).

* Fri Jul 18 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt1
- New version (3.0.1).
- Fixed:
  + MFSA 2008-36 Crash with malformed GIF file on Mac OS X
  + MFSA 2008-35 Command-line URLs launch multiple tabs when Firefox not running
  + MFSA 2008-34 Remote code execution by overflowing CSS reference counter

* Sun Jul 13 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt2.20080704
- New bugfix build.
- Add searchplugins: bugzilla@altlinux, wikipedia-ru, yandex.
- Remove RPATH.

* Fri Jul 04 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080704
- New cvs snapshot 3.0 (20080704).

* Sat May 31 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080530
- New cvs snapshot 20080530.

* Tue May 20 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080519
- New cvs snapshot (3.0 rc1).

* Sun Feb 03 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.b3pre
- New cvs snapshot.

* Thu Dec 20 2007 Alexey Gladkov <legion@altlinux.ru> 3.0.b2-alt1
- New major beta version 3.0.b2

* Wed Nov 28 2007 Alexey Gladkov <legion@altlinux.ru> 3.0.b1-alt1
- New major beta version 3.0.b1

* Sun Feb 25 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.2-alt1
- New bugfix version 2.0.0.2
- Remove version from requires in *.pc.
- Fixed:
    + MFSA 2007-07  Embedded nulls in location.hostname confuse same-domain checks
    + MFSA 2007-06 Mozilla Network Security Services (NSS) SSLv2 buffer overflow
    + MFSA 2007-05 XSS and local file access by opening blocked popups
    + MFSA 2007-04 Spoofing using custom cursor and CSS3 hotspot
    + MFSA 2007-03 Information disclosure through cache collisions
    + MFSA 2007-02 Improvements to help protect against Cross-Site Scripting attacks
    + MFSA 2007-01 Crashes with evidence of memory corruption (rv:1.8.0.10/1.8.1.2)

* Sun Jan 28 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.1-alt1
- New minor version 2.0.0.1
- Fixed:
    + MFSA 2006-76  XSS using outer window's Function object
    + MFSA 2006-75 RSS Feed-preview referrer leak
    + MFSA 2006-73 Mozilla SVG Processing Remote Code Execution
    + MFSA 2006-72 XSS by setting img.src to javascript: URI
    + MFSA 2006-71 LiveConnect crash finalizing JS objects
    + MFSA 2006-70 Privilege escalation using watch point
    + MFSA 2006-69 CSS cursor image buffer overflow (Windows only)
    + MFSA 2006-68 Crashes with evidence of memory corruption (rv:1.8.0.9/1.8.1.1)

* Thu Nov 23 2006 Alexey Gladkov <legion@altlinux.ru> 2.0-alt2
- Add %%pre script.
- Remove version specific paths.

* Sat Oct 28 2006 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1
- New major version 2.0 .
- Don't build libxul.
- Add support for printing via Pango.
- Change printer paper size at A4.
- Check compatibility disabled.
- Patch disabling OS_TEST autoguessing for %%ix86 builds on x86_64 host.

* Fri Sep 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.7-alt1
- New version 1.5.0.7 .
- Fixed:
    + MFSA 2006-64  Crashes with evidence of memory corruption (rv:1.8.0.7)
    + MFSA 2006-62 Popup-blocker cross-site scripting (XSS)
    + MFSA 2006-61 Frame spoofing using document.open()
    + MFSA 2006-60 RSA Signature Forgery
    + MFSA 2006-59 Concurrency-related vulnerability
    + MFSA 2006-58 Auto-Update compromise through DNS and SSL spoofing
    + MFSA 2006-57 JavaScript Regular Expression Heap Corruption

* Wed Aug 30 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt4
- Add libgtkembedmoz.so, firefox-gtkembedmoz.pc .
- Update BuildRequires.

* Wed Aug 16 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt3
- bugfix build.
- Patch to enable intl.locale.matchOS was removed.
- Added default download directory.

* Wed Aug 09 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt2
- bugfix build.
- Added patch to handle #9863 (history #4352).

* Sat Aug 05 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt1
- New version 1.5.0.6 . 
- Fixed:
    + Fixed an issue with playing Windows Media content
    + MFSA 2006-56  chrome: scheme loading remote content
    + MFSA 2006-55 Crashes with evidence of memory corruption (rv:1.8.0.5)
    + MFSA 2006-54 XSS with XPCNativeWrapper(window).Function(...)
    + MFSA 2006-53 UniversalBrowserRead privilege escalation
    + MFSA 2006-52 PAC privilege escalation using Function.prototype.call
    + MFSA 2006-51 Privilege escalation using named-functions and redefined "new Object()"
    + MFSA 2006-50 JavaScript engine vulnerabilities
    + MFSA 2006-48 JavaScript new Function race condition
    + MFSA 2006-47 Native DOM methods can be hijacked across domains
    + MFSA 2006-46 Memory corruption with simultaneous events
    + MFSA 2006-45 Javascript navigator Object Vulnerability
    + MFSA 2006-44 Code execution through deleted frame reference

* Thu Jun 08 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.4-alt1
- New version.
- Fixed:
    + MFSA 2006-43 Privilege escalation using addSelectionListener
    + MFSA 2006-42 Web site XSS using BOM on UTF-8 pages
    + MFSA 2006-41 File stealing by changing input type (variant)
    + MFSA 2006-39 "View Image" local resource linking (Windows)
    + MFSA 2006-38 Buffer overflow in crypto.signText()
    + MFSA 2006-37 Remote compromise via content-defined setter on object prototypes
    + MFSA 2006-36 PLUGINSPAGE privileged JavaScript execution 2
    + MFSA 2006-35 Privilege escalation through XUL persist
    + MFSA 2006-34 XSS viewing javascript: frames or images from context menu
    + MFSA 2006-33 HTTP response smuggling
    + MFSA 2006-32 Fixes for crashes with potential memory corruption
    + MFSA 2006-31 EvalInSandbox escape (Proxy Autoconfig, Greasemonkey)

* Fri May 12 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.3-alt1
- New version.
- Build libxul library.
- Fixed:
    + MFSA 2006-30 Deleted object reference when designMode="on".

* Wed Mar 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.1-alt2
- bugfix build.
- include fix
- plugins directory fix;

* Mon Feb 13 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.1-alt1
- New version 1.5.0.1
- Buildrequires updated for xorg-7.0 
- run-firefox script bugfix:
  * usage update
  * plugins search path (x86_64)
  * unparseable commands handling
- bugfix: #7334, #7682, #8757, #8784, #9017

* Sun Dec 04 2005 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- New version 1.5 .
- Spec cleanup.
- Build with external rpm-build-firefox .
- Build with system NSS and NSPR.
- Unused libraries removed.
- Rpm mascros bugfix.
  * fix for new rpm.
  * change extension installation sheme (again).
- Default preference tunning.
- Startup script rewritten. Now it is single script.
  * command line shortcut added: altfaq:NUM .
- SVG support enabled.
- directory /usr/share/firefox-@version@/extensions was added to extensions search path .
  * this location is controled by the option extensions.dir.extensions .
- Bug: #7682, #7801, #7856, #7949 fixed.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt4
- major bugfix.
- build with official branding.
- x86_64 compatibility addon (patch20, patch21).

* Sun Aug 07 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt3
- release version.
- firsttime script added.
- SVG support disabled.
- Patch #2 bugfix (bug: #7682)

* Sun Jul 24 2005 LAKostis <lakostis at altlinux.ru> 1.0.6-alt2.cvs
- fix -nox patch.
- add gssapi detection and build fixes from mhz@.

* Tue Jul 19 2005 LAKostis <lakostis at altlinux.ru> 1.0.6-alt1.cvs
- new version from aviary branch fixing various bugs:
  + MFSA2005-54
  + Restore API compatibility for extensions and web applications 
    that did not work in Firefox 1.0.5.
  
* Mon Jul 11 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt2.cvs
- new version from aviary branch;

* Wed Jun 22 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt1.cvs
- new version from aviary branch fixing various security bugs;
- fix: #4846, #5101, #7126 (legion).
- if_{with,without} debug - added (legion).
- keyword 'altbug:' added, patch2 updated (legion).
- postin/postun-scripts scripts bugfixes (legion).
- triggers added for trash cleanup (legion).

* Mon Jun 20 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt0.cvs
- new version from aviary branch;
- fix #6595;
- add switches for svg/xprint easy builds.
- update alt-prefs-tuning.patch (disable annoying default browser dialog).

* Sun Jun 12 2005 LAKostis <lakostis at altlinux.ru> 1.0.4-alt1
- new version;
- SA15601 security fix;
- BuildRequires cleanup (remove xorg-x11-libs-static).

* Thu Apr 21 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.3-alt1
- new version;
- requires fix;

* Wed Apr 13 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.2-alt1
- new version;
- RPATH fix;
- NoX patch was rewritten;

* Sun Mar 06 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt2
- rpm macros was updated;

* Fri Feb 25 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt1
- new version;
- patch9 was added (mozilla Bug #123315);
- patch10, patch11 was added (#6151);

* Mon Feb 14 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt7
- plugins path bugfix;
- svg support added;
- x86_64 compatibility added (thx mouse@);

* Tue Feb 01 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt6
- update patch firefox-1.0-20050201-alt-nox.patch 
  * uninstall-global-theme command-line option was added;
  * update-register command-line option was added;
- firefox-1.0-alt-rpm-scripts.tar.bz2 bugfix;

* Thu Jan 27 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt5
- disable svg support becouse svg layout lead to segfault 
  when mozilla compile with gcc3.4 .
- search plugins was moved into the standalone rpm package.

* Wed Jan 19 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt4
- Rebuilt with libstdc++.so.6.

* Wed Jan 05 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt3
- new version;
- browser-plugins-npapi support added;
- new icons default icons(thx shrek@);
- option uninstall-global-extension was fixed;

* Wed Nov 03 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2.rc1
- extension sheme changes;
- postin/preun scripts chenges;

* Mon Oct 18 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2.PR
- new default extensions added;
- protocol 'mailto' external handler added; 
- firefox.macro changed;
- postun script changed;
- icons changed;

* Thu Sep 30 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1.PR
- New version 1.0PR;
- New extension scheme;
- Add:
    * New option 'run-without-x' added (mouse, legion);
    * SVG support added;
    * Certificate (ALT Linux CA Root) added;
    * ALT Linux BTS search plugin added;
    * RPATH added to all binary files;
- bug #4284 fixed;

* Fri May 28 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt4
- Move back some changes at alt3 build.
- Bug #4157 fixed.

* Fri Apr 30 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt3.1
- viewsource protocol was added.

* Thu Apr 29 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt3
- Minimize buildin extensions;
- Disable debug output;
- Disable some options:
  + disable JavaScript debug library;
  + disable LDAP support;
  + disable logging facilities;
- Necko protocols cleanup;

* Tue Feb 24 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt2
- Splash screen added (thx sadist@);
- Search plugins added;
- Remove devel package Conflicts;
- Change rebuild-database.sh script. Script must be run only as root;
- Change locale hack.

* Wed Feb 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt1
- Mozilla Firebird becomes Mozilla Firefox. Mozilla's next 
  generation browser has changed names (again);
- New version;

* Sun Jan 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.7-alt2
- Spec changes.
- run-mozilla.sh script patch.

* Tue Dec 30 2003 Alexey Gladkov <legion@altlinux.ru> 0.7-alt1
- first build for ALT Linux.
- rpm macro created.
- new scheme loading extensions added (thx force@)
