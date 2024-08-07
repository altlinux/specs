%define _unpackaged_files_terminate_build 1
%set_verify_elf_method relaxed

%ifndef build_parallel_jobs
%global build_parallel_jobs %__nprocs
%endif

%define gst_version   1.0
%define nspr_version  4.35
%define nss_version   3.98
%define rust_version  1.65.0
%define cargo_version 1.65.0
%define llvm_version  17.0

Name: firefox-esr
Version: 128.1.0
Release: alt1

Summary: The Mozilla Firefox project is a redesign of Mozilla's browser
Summary(ru_RU.UTF-8): Интернет-браузер Mozilla Firefox
License: MPL-2.0
Group: Networking/WWW
URL: https://www.mozilla.org/firefox/
# Hang up on build browser/components/about
ExcludeArch: ppc64le

Source0: firefox-source.tar
### Start Patches
Patch001: 0001-FEDORA-build-arm-libopus.patch
Patch002: 0002-MOZILLA-1196777-GTK3-keyboard-input-focus-sticks-on-.patch
Patch003: 0003-bmo-847568-Support-system-harfbuzz.patch
Patch004: 0004-bmo-847568-Support-system-graphite2.patch
Patch005: 0005-bmo-1559213-Support-system-av1.patch
Patch006: 0006-Revert-Bug-1712947-Don-t-pass-neon-flags-to-rustc-wh.patch
Patch007: 0007-ALT-fix-double_t-redefinition.patch
Patch008: 0008-build-Disable-Werror.patch
Patch009: 0009-Add-dbus-cflags.patch
Patch010: 0010-FEDORA-enable-vaapi.patch
### End Patches

Provides: webclient
Provides: firefox-esr-ru = %EVR
Provides: firefox-esr-uk = %EVR
Provides: firefox-esr-kk = %EVR
Provides: firefox-esr-uz = %EVR
Provides: firefox-esr-wayland = %EVR
Requires: mozilla-common
# ALT#30732
Requires: gst-plugins-ugly%gst_version
Requires: libnspr >= %nspr_version
Requires: libnss >= %nss_version
Conflicts: firefox
Obsoletes: firefox-esr-ru < %EVR
Obsoletes: firefox-esr-uk < %EVR
Obsoletes: firefox-esr-kk < %EVR
Obsoletes: firefox-esr-uz < %EVR
Obsoletes: firefox-esr-wayland < %EVR

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
BuildRequires: cbindgen
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
BuildRequires: python3(click)
BuildRequires: python3(curses)
BuildRequires: python3(hamcrest)
BuildRequires: python3(pip)
BuildRequires: python3(setuptools)
BuildRequires: python3(sqlite3)
# Rust requires
BuildRequires: /proc

%description
Mozilla Firefox is an open-source web browser, designed
for standards compliance, performance and portability.

%description -l ru_RU.UTF-8
Mozilla Firefox - это веб-браузер с открытым исходным кодом, разработанный
с учетом соответствия стандартам, производительности и переносимости.

%package config-privacy
Summary:	Firefox configuration with the paranoid privacy settings
Group:		System/Configuration/Networking

Requires: %name
Conflicts: firefox-config-privacy

%description config-privacy
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
ac_add_options --enable-linker=lld
%ifnarch armh
ac_add_options --enable-lto=thin
%endif
%ifarch armh
ac_add_options --disable-webrtc
%endif
%ifarch armh x86_64
ac_add_options --disable-elf-hack
%endif
%ifarch armh
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
%ifarch armh
find toolkit/components/uniffi-js -type f |
	xargs sed -ri.poff 's,_4d51_,_1c79_,g'
%endif

rm -rf -- obj-x86_64-pc-linux-gnu
rm -rf -- third_party/python/setuptools/setuptools*
rm -rf -- third_party/python/click/click*

%build
%add_findprov_lib_path %firefox_prefix

export MOZ_BUILD_APP=browser
export MOZ_CHROME_MULTILOCALE="$(tr '\n' ' ' < .rpm/firefox-l10n.txt)"

MOZ_OPT_FLAGS=()

MOZ_OPT_FLAGS+=( -pipe -O2 )
%ifarch armh
MOZ_OPT_FLAGS+=( -march=armv7-a -mthumb )
%endif

# PIE, full relro
MOZ_OPT_FLAGS+=( -DPIC -fPIC -Wl,-z,relro -Wl,-z,now )

# Add fake RPATH
rpath="/$(printf %%s '%firefox_prefix' |tr '[:print:]' '_')"
MOZ_OPT_FLAGS+=( "-Wl,-rpath,$rpath" )

MOZ_OPT_FLAGS+=( -Wno-unused-command-line-argument )

export CFLAGS="${MOZ_OPT_FLAGS[*]}"
export CXXFLAGS="${MOZ_OPT_FLAGS[*]}"

export MOZ_PARALLEL_BUILD=%build_parallel_jobs
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export RANLIB="llvm-ranlib"
export LLVM_PROFDATA="llvm-profdata"
export ALTWRAP_LLVM_VERSION="%llvm_version"
export RUST_BACKTRACE=1
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2
export SHELL=/bin/sh

# It is necessary to disable the generation of debugging
# information in order to avoid the "LLVM ERROR: out of memory".
%ifarch %ix86
export MOZ_DEBUG_FLAGS="-g0"
%endif
%ifarch armh %ix86
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=0"
%else
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=2"
%endif

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
install -D -m 644 .rpm/firefox-privacy-prefs.js %buildroot/%_sysconfdir/firefox/defaults/pref/all-privacy.js

sed -i \
	-e 's#@VERSION@#%{version}#g' \
	%buildroot/%_sysconfdir/firefox/defaults/pref/all-privacy.js

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
%_bindir/xbrowser	%_bindir/firefox	80
%_bindir/x-www-browser	%_bindir/firefox	80
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
%dir %_sysconfdir/firefox/defaults
%dir %_sysconfdir/firefox/defaults/pref
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

%files config-privacy
%config(noreplace) %_sysconfdir/firefox/defaults/pref/all-privacy.js

%changelog
* Tue Aug 06 2024 Ajrat Makhmutov <rauty@altlinux.org> 128.1.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2024-7518: Fullscreen notification dialog can be obscured by document content
  + CVE-2024-7519: Out of bounds memory access in graphics shared memory handling
  + CVE-2024-7520: Type confusion in WebAssembly
  + CVE-2024-7521: Incomplete WebAssembly exception handing
  + CVE-2024-7522: Out of bounds read in editor component
  + CVE-2024-7524: CSP strict-dynamic bypass using web-compatibility shims
  + CVE-2024-7525: Missing permission check when creating a StreamFilter
  + CVE-2024-7526: Uninitialized memory used by WebGL
  + CVE-2024-7527: Use-after-free in JavaScript garbage collection
  + CVE-2024-7528: Use-after-free in IndexedDB
  + CVE-2024-7529: Document content could partially obscure security prompts
  + CVE-2024-7531: PK11_Encrypt using CKM_CHACHA20 can reveal plaintext on Intel Sandy Bridge machines

* Wed Jul 24 2024 Ajrat Makhmutov <rauty@altlinux.org> 128.0-alt2
- Apply all the changes from regular firefox, the main ones:
  + Enable VAAPI.
  + Merge firefox-esr-wayland to firefox-esr.
  + Enforce window name to associate icon and title with window.
  + Update the url tag.
  + Update the description.

* Mon Jul 15 2024 Ajrat Makhmutov <rauty@altlinux.org> 128.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2024-5702: Use-after-free in networking
  + CVE-2024-5688: Use-after-free in JavaScript object transplant
  + CVE-2024-5690: External protocol handlers leaked by timing attack
  + CVE-2024-5691: Sandboxed iframes were able to bypass sandbox restrictions to open a new window
  + CVE-2024-5692: Bypass of file name restrictions during saving
  + CVE-2024-5693: Cross-Origin Image leak via Offscreen Canvas
  + CVE-2024-5696: Memory Corruption in Text Fragments
  + CVE-2024-5700: Memory safety bugs fixed in Firefox 127, Firefox ESR 115.12, and Thunderbird 115.12
  + CVE-2024-6600: Memory corruption in WebGL API
  + CVE-2024-6601: Race condition in permission assignment
  + CVE-2024-6602: Memory corruption in NSS
  + CVE-2024-6603: Memory corruption in thread creation
  + CVE-2024-6604: Memory safety bugs fixed in Firefox 128, Firefox ESR 115.13, and Thunderbird 115.13

* Sun May 19 2024 Pavel Vasenkov <pav@altlinux.org> 115.11.0-alt1
- New ESR version.
- Security fixes
  + CVE-2024-4367 Arbitrary JavaScript execution in PDF.js
  + CVE-2024-4767 IndexedDB files retained in private browsing mode
  + CVE-2024-4768 Potential permissions request bypass via clickjacking
  + CVE-2024-4769 Cross-origin responses could be distinguished between script and non-script content-types
  + CVE-2024-4770 Use-after-free could occur when printing to PDF
  + CVE-2024-4777 Memory safety bugs fixed in Firefox 126, Firefox ESR 115.11, and Thunderbird 115.11

* Tue Apr 16 2024 Pavel Vasenkov <pav@altlinux.org> 115.10.0-alt1
- New ESR version.
- Security fixes
  + CVE-2024-3852 GetBoundName in the JIT returned the wrong object
  + CVE-2024-3854 Out-of-bounds-read after mis-optimized switch statement
  + CVE-2024-3857 Incorrect JITting of arguments led to use-after-free during garbage collection
  + CVE-2024-2609 Permission prompt input delay could expire when not in focus
  + CVE-2024-3859 Integer-overflow led to out-of-bounds-read in the OpenType sanitizer
  + CVE-2024-3861 Potential use-after-free due to AlignedBuffer self-move
  + CVE-2024-3863 Download Protections were bypassed by .xrm-ms files on Windows
  + CVE-2024-3302 Denial of Service using HTTP/2 CONTINUATION frames
  + CVE-2024-3864 Memory safety bug fixed in Firefox 125, Firefox ESR 115.10, and Thunderbird 115.10

* Wed Apr 03 2024 Pavel Vasenkov <pav@altlinux.org> 115.9.1-alt1
- New ESR version.
- Security fixes
  + CVE-2024-0743 Crash in NSS TLS method
  + CVE-2024-2605 Windows Error Reporter could be used as a Sandbox escape vector
  + CVE-2024-2607 JIT code failed to save return registers on Armv7-A
  + CVE-2024-2608 Integer overflow could have led to out of bounds write
  + CVE-2024-2616 Improve handling of out-of-memory conditions in ICU
  + CVE-2023-5388 NSS susceptible to timing attack against RSA decryption
  + CVE-2024-2610 Improper handling of html and body tags enabled CSP nonce leakage
  + CVE-2024-2611 Clickjacking vulnerability could have led to a user accidentally granting permissions
  + CVE-2024-2612 Self referencing object could have potentially led to a use-after-free
  + CVE-2024-2614 Memory safety bugs fixed in Firefox 124, Firefox ESR 115.9, and Thunderbird 115.9
  + CVE-2024-29944 Privileged JavaScript Execution via Event Handlers

* Thu Mar 07 2024 Andrey Cherepanov <cas@altlinux.org> 115.8.0-alt2
- Use maximize icon for CSD restore button missing in some themes (ALT #49606).

* Wed Feb 21 2024 Pavel Vasenkov <pav@altlinux.org> 115.8.0-alt1
- New ESR version.
- Security fixes
  + CVE-2024-1546 Out-of-bounds memory read in networking channels
  + CVE-2024-1547 Alert dialog could have been spoofed on another site
  + CVE-2024-1548 Fullscreen Notification could have been hidden by select element
  + CVE-2024-1549 Custom cursor could obscure the permission dialog
  + CVE-2024-1550 Mouse cursor re-positioned unexpectedly could have led to unintended permission grants
  + CVE-2024-1551 Multipart HTTP Responses would accept the Set-Cookie header in response parts
  + CVE-2024-1552 Incorrect code generation on 32-bit ARM devices
  + CVE-2024-1553 Memory safety bugs fixed in Firefox 123, Firefox ESR 115.8, and Thunderbird 115.8

* Tue Feb 06 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 115.7.0-alt2
- Reverted malicious upstream commit
  https://hg.mozilla.org/integration/autoland/rev/a03a9c72d1db3716adffc6968cfb6eb43c6fcd74
  which forces firefox to autoremove yandex, mail.ru, vk search extensions.
  Note: reverting that (and some similar) commit is a necessary condition to
  make firefox obey the search engine settings specified in policies.json.
  Alas it might be not enough. The problem is that firefox is tightly
  integrated with services provided by Mozilla corporation, such as bookmark
  sync, telemetry, captive portal detection, you name it. Reportedly a similar
  malware has been deployed there, thus yandex search extension (or in fact any
  extension) can be removed remotely (that is, without user consent) if the user
  is signed in into mozilla account, sends telemetry data to mozilla, etc.
  Perhaps it's time to make unmozilla firefox (similarly to ungoogled chromium).
- policies.json: use yandex search by default (Closes: #43516).

* Sun Feb 04 2024 Pavel Vasenkov <pav@altlinux.org> 115.7.0-alt1
- New ESR version.
- Security fixes
  + CVE-2024-0741 Out of bounds write in ANGLE
  + CVE-2024-0742 Failure to update user input timestamp
  + CVE-2024-0746 Crash when listing printers on Linux
  + CVE-2024-0747 Bypass of Content Security Policy when directive unsafe-inline was set
  + CVE-2024-0749 Phishing site popup could show local origin in address bar
  + CVE-2024-0750 Potential permissions request bypass via clickjacking
  + CVE-2024-0751 Privilege escalation through devtools
  + CVE-2024-0753 HSTS policy on subdomain could bypass policy of upper domain
  + CVE-2024-0755 Memory safety bugs fixed in Firefox 122, Firefox ESR 115.7, and Thunderbird 115.7

* Fri Feb 02 2024 Grigory Ustinov <grenka@altlinux.org> 115.6.0-alt2
- Fixed building with python3.12.

* Wed Dec 20 2023 Pavel Vasenkov <pav@altlinux.org> 115.6.0-alt1
- New ESR version.
- Security fixes
  + CVE-2023-6856 Heap-buffer-overflow affecting WebGL DrawElementsInstanced method with Mesa VM driver
  + CVE-2023-6865 Potential exposure of uninitialized data in EncryptingOutputStream
  + CVE-2023-6857 Symlinks may resolve to smaller than expected buffers
  + CVE-2023-6858 Heap buffer overflow in nsTextFragment
  + CVE-2023-6859 Use-after-free in PR_GetIdentitiesLayer
  + CVE-2023-6860 Potential sandbox escape due to VideoBridge lack of texture validation
  + CVE-2023-6867 Clickjacking permission prompts using the popup transition
  + CVE-2023-6861 Heap buffer overflow affected nsWindow::PickerOpen(void) in headless mode
  + CVE-2023-6862 Use-after-free in nsDNSService
  + CVE-2023-6863 Undefined behavior in ShutdownObserver()
  + CVE-2023-6864 Memory safety bugs fixed in Firefox 121, Firefox ESR 115.6, and Thunderbird 115.6

* Thu Nov 23 2023 Pavel Vasenkov <pav@altlinux.org> 115.5.0-alt1
- New ESR version.
- Security fixes
  + CVE-2023-6204 Out-of-bound memory access in WebGL2 blitFramebuffer
  + CVE-2023-6205 Use-after-free in MessagePort::Entangled
  + CVE-2023-6206 Clickjacking permission prompts using the fullscreen transition
  + CVE-2023-6207 Use-after-free in ReadableByteStreamQueueEntry::Buffer
  + CVE-2023-6208 Using Selection API would copy contents into X11 primary selection.
  + CVE-2023-6209 Incorrect parsing of relative URLs starting with "///"
  + CVE-2023-6212 Memory safety bugs fixed in Firefox 120, Firefox ESR 115.5, and Thunderbird 115.5

* Thu Nov 02 2023 Pavel Vasenkov <pav@altlinux.org> 115.4.0-alt1
- New ESR version.
- Security fixes
  + CVE-2023-5721 Queued up rendering could have allowed websites to clickjack
  + CVE-2023-5732 Address bar spoofing via bidirectional characters
  + CVE-2023-5724 Large WebGL draw could have led to a crash
  + CVE-2023-5725 WebExtensions could open arbitrary URLs
  + CVE-2023-5726 Full screen notification obscured by file open dialog on macOS
  + CVE-2023-5727 Download Protections were bypassed by .msix, .msixbundle, .appx, and .appxbundle files on Windows
  + CVE-2023-5728 Improper object tracking during GC in the JavaScript engine could have led to a crash.
  + CVE-2023-5730 Memory safety bugs fixed in Firefox 119, Firefox ESR 115.4, and Thunderbird 115.4.1

* Mon Oct 16 2023 Pavel Vasenkov <pav@altlinux.org> 115.3.1-alt4
- Fix check dependencies error for GLIBC_PRIVATE

* Fri Oct 13 2023 Pavel Vasenkov <pav@altlinux.org> 115.3.1-alt3
- Fix folder location for config-privacy js configuration files (Closes #47960)

* Thu Oct 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 115.3.1-alt2
- Support LoongArch architecture (lp64d ABI).

* Fri Sep 29 2023 Pavel Vasenkov <pav@altlinux.org> 115.3.1-alt1
--
- New ESR version.
- Security fixes
  + CVE-2023-5168 Out-of-bounds write in FilterNodeD2D1
  + CVE-2023-5169 Out-of-bounds write in PathOps
  + CVE-2023-5171 Use-after-free in Ion Compiler
  + CVE-2023-5174 Double-free in process spawning on Windows
  + CVE-2023-5176 Memory safety bugs fixed in Firefox 118, Firefox ESR 115.3, and Thunderbird 115.3
  + CVE-2023-5217 Heap buffer overflow in libvpx

* Wed Sep 20 2023 Pavel Vasenkov <pav@altlinux.org> 115.2.1-alt2
- Restored build for 32bit archs

* Fri Sep 08 2023 Pavel Vasenkov <pav@altlinux.org> 115.2.1-alt1
- New ESR version.
- Security fixes
  + CVE-2023-3600 Use-after-free in workers
  + CVE-2023-4045 Offscreen Canvas could have bypassed cross-origin restrictions
  + CVE-2023-4046 Incorrect value used during WASM compilation
  + CVE-2023-4047 Potential permissions request bypass via clickjacking
  + CVE-2023-4048 Crash in DOMParser due to out-of-memory conditions
  + CVE-2023-4049 Fix potential race conditions when releasing platform objects
  + CVE-2023-4050 Stack buffer overflow in StorageManager
  + CVE-2023-4052 File deletion and privilege escalation through Firefox uninstaller
  + CVE-2023-4054 Lack of warning when opening appref-ms files
  + CVE-2023-4055 Cookie jar overflow caused unexpected cookie jar state
  + CVE-2023-4056 Memory safety bugs fixed in Firefox 116, Firefox ESR 115.1, Firefox ESR 102.14, Thunderbird 115.1, and Thunderbird 102.14
  + CVE-2023-4057 Memory safety bugs fixed in Firefox 116, Firefox ESR 115.1, and Thunderbird 115.1
  + CVE-2023-4573 Memory corruption in IPC CanvasTranslator
  + CVE-2023-4574 Memory corruption in IPC ColorPickerShownCallback
  + CVE-2023-4575 Memory corruption in IPC FilePickerShownCallback
  + CVE-2023-4576 Integer Overflow in RecordedSourceSurfaceCreation
  + CVE-2023-4577 Memory corruption in JIT UpdateRegExpStatics
  + CVE-2023-4051 Full screen notification obscured by file open dialog
  + CVE-2023-4578 Error reporting methods in SpiderMonkey could have triggered an Out of Memory Exception
  + CVE-2023-4053 Full screen notification obscured by external program
  + CVE-2023-4580 Push notifications saved to disk unencrypted
  + CVE-2023-4581 XLL file extensions were downloadable without warnings
  + CVE-2023-4582 Buffer Overflow in WebGL glGetProgramiv
  + CVE-2023-4583 Browsing Context potentially not cleared when closing Private Window
  + CVE-2023-4584 Memory safety bugs fixed in Firefox 117, Firefox ESR 102.15, Firefox ESR 115.2, Thunderbird 102.15, and Thunderbird 115.2
  + CVE-2023-4585 Memory safety bugs fixed in Firefox 117, Firefox ESR 115.2, and Thunderbird 115.2
  + CVE-2023-4863 Heap buffer overflow in libwebp

* Tue Jun 27 2023 Pavel Vasenkov <pav@altlinux.org> 102.12.0-alt2
- Fixes: Unstable name collisions
         Build failure with GCC 13

* Wed Jun 07 2023 Pavel Vasenkov <pav@altlinux.org> 102.12.0-alt1
- New ESR version.
- Security fixes
  + CVE-2023-34414 Click-jacking certificate exceptions through rendering lag
  + CVE-2023-34416 Memory safety bugs fixed in Firefox 114 and Firefox ESR 102.12

* Mon May 15 2023 Pavel Vasenkov <pav@altlinux.org> 102.11.0-alt1
- New ESR version.
- Security fixes
  + CVE-2023-32205 Browser prompts could have been obscured by popups
  + CVE-2023-32206 Crash in RLBox Expat driver
  + CVE-2023-32207 Potential permissions request bypass via clickjacking
  + CVE-2023-32211 Content process crash due to invalid wasm code
  + CVE-2023-32212 Potential spoof due to obscured address bar
  + CVE-2023-32213 Potential memory corruption in FileReader::DoReadData()
  + CVE-2023-32214 Potential DoS via exposed protocol handlers
  + CVE-2023-32215 Memory safety bugs fixed in Firefox 113 and Firefox ESR 102.11

* Wed Apr 19 2023 Pavel Vasenkov <pav@altlinux.org> 102.10.0-alt1
- New ESR version.
- Security fixes
  + CVE-2023-29531 Out-of-bound memory access in WebGL on macOS
  + CVE-2023-29532 Mozilla Maintenance Service Write-lock bypass
  + CVE-2023-29533 Fullscreen notification obscured
  + CVE-2023-1999 Double-free in libwebp
  + CVE-2023-29535 Potential Memory Corruption following Garbage Collector compaction
  + CVE-2023-29536 Invalid free from JavaScript code
  + CVE-2023-29539 Content-Disposition filename truncation leads to Reflected File Download
  + CVE-2023-29541 Files with malicious extensions could have been downloaded unsafely on Linux
  + CVE-2023-29542 Bypass of file download extension restrictions
  + CVE-2023-29545 Windows Save As dialog resolved environment variables
  + CVE-2023-1945 Memory Corruption in Safe Browsing Code
  + CVE-2023-29548 Incorrect optimization result on ARM64
  + CVE-2023-29550 Memory safety bugs fixed in Firefox 112 and Firefox ESR 102.10

* Wed Mar 22 2023 Pavel Vasenkov <pav@altlinux.org> 102.9.0-alt1
- New ESR version.
- Security fixes
  + CVE-2023-25751 Incorrect code generation during JIT compilation
  + CVE-2023-28164 URL being dragged from a removed cross-origin iframe into the same tab triggered navigation
  + CVE-2023-28162 Invalid downcast in Worklets
  + CVE-2023-25752 Potential out-of-bounds when accessing throttled streams
  + CVE-2023-28163 Windows Save As dialog resolved environment variables
  + CVE-2023-28176 Memory safety bugs fixed in Firefox 111 and Firefox ESR 102.9


* Fri Mar 03 2023 Pavel Vasenkov <pav@altlinux.org> 102.8.0-alt1
- New ESR version.
- Security fixes
  + CVE-2023-25728 Content security policy leak in violation reports using iframes
  + CVE-2023-25730 Screen hijack via browser fullscreen mode
  + CVE-2023-0767 Arbitrary memory write via PKCS 12 in NSS
  + CVE-2023-25735 Potential use-after-free from compartment mismatch in SpiderMonkey
  + CVE-2023-25737 Invalid downcast in SVGUtils::SetupStrokeGeometry
  + CVE-2023-25738 Printing on Windows could potentially crash Firefox with some device drivers
  + CVE-2023-25739 Use-after-free in mozilla::dom::ScriptLoadContext::~ScriptLoadContext
  + CVE-2023-25729 Extensions could have opened external schemes without user knowledge
  + CVE-2023-25732 Out of bounds memory write from EncodeInputStream
  + CVE-2023-25734 Opening local .url files could cause unexpected network loads
  + CVE-2023-25742 Web Crypto ImportKey crashes tab
  + CVE-2023-25744 Memory safety bugs fixed in Firefox 110 and Firefox ESR 102.8
  + CVE-2023-25746 Memory safety bugs fixed in Firefox ESR 102.8

* Wed Jan 18 2023 Pavel Vasenkov <pav@altlinux.org> 102.7.0-alt1
- New ESR version.
- Security fixes
  + CVE-2022-46871 libusrsctp library out of date
  + CVE-2023-23598 Arbitrary file read from GTK drag and drop on Linux
  + CVE-2023-23599 Malicious command could be hidden in devtools output on Windows
  + CVE-2023-23601 URL being dragged from cross-origin iframe into same tab triggers navigation
  + CVE-2023-23602 Content Security Policy wasn't being correctly applied to WebSockets in WebWorkers
  + CVE-2022-46877 Fullscreen notification bypass
  + CVE-2023-23603 Calls to <code>console.log</code> allowed bypasing Content Security Policy via format directive
  + CVE-2023-23605 Memory safety bugs fixed in Firefox 109 and Firefox ESR 102.7

* Wed Dec 14 2022 Pavel Vasenkov <pav@altlinux.org> 102.6.0-alt1
- New ESR version.
- Security fixes
  + CVE-2022-46880 Use-after-free in WebGL
  + CVE-2022-46872 Arbitrary file read from a compromised content process
  + CVE-2022-46881 Memory corruption in WebGL
  + CVE-2022-46874 Drag and Dropped Filenames could have been truncated to malicious extensions
  + CVE-2022-46875 Download Protections were bypassed by .atloc and .ftploc files on Mac OS
  + CVE-2022-46882 Use-after-free in WebGL
  + CVE-2022-46878 Memory safety bugs fixed in Firefox 108 and Firefox ESR 102.6

* Fri Dec 09 2022 Pavel Vasenkov <pav@altlinux.org> 102.5.0-alt2
- Build with llvm-version 12 instead llvm-version 13 (Closes: #44436)

* Wed Nov 16 2022 Pavel Vasenkov <pav@altlinux.org> 102.5.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-45403 Service Workers might have learned size of cross-origin media files
  + CVE-2022-45404 Fullscreen notification bypass
  + CVE-2022-45405 Use-after-free in InputStream implementation
  + CVE-2022-45406 Use-after-free of a JavaScript Realm
  + CVE-2022-45408 Fullscreen notification bypass via windowName
  + CVE-2022-45409 Use-after-free in Garbage Collection
  + CVE-2022-45410 ServiceWorker-intercepted requests bypassed SameSite cookie policy
  + CVE-2022-45411 Cross-Site Tracing was possible via non-standard override headers
  + CVE-2022-45412 Symlinks may resolve to partially uninitialized buffers
  + CVE-2022-45416 Keystroke Side-Channel Leakage
  + CVE-2022-45418 Custom mouse cursor could have been drawn over browser UI
  + CVE-2022-45420 Iframe contents could be rendered outside the iframe
  + CVE-2022-45421 Memory safety bugs fixed in Firefox 107 and Firefox ESR 102.5

* Mon Oct 24 2022 Pavel Vasenkov <pav@altlinux.org> 102.4.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-42927 Same-origin policy violation could have leaked cross-origin URLs
  + CVE-2022-42928 Memory Corruption in JS Engine
  + CVE-2022-42929 Denial of Service via window.print
  + CVE-2022-42932 Memory safety bugs fixed in Firefox 106 and Firefox ESR 102.4

* Mon Oct 10 2022 Pavel Vasenkov <pav@altlinux.org> 102.3.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-3266 Out of bounds read when decoding H264
  + CVE-2022-40959 Bypassing FeaturePolicy restrictions on transient pages
  + CVE-2022-40960 Data-race when parsing non-UTF-8 URLs in threads
  + CVE-2022-40958 Bypassing Secure Context restriction for cookies with __Host and __Secure prefix
  + CVE-2022-40956 Content-Security-Policy base-uri bypass
  + CVE-2022-40957 Incoherent instruction cache when building WASM on ARM64
  + CVE-2022-40962 Memory safety bugs fixed in Firefox 105 and Firefox ESR 102.3

* Thu Sep 15 2022 Pavel Vasenkov <pav@altlinux.org> 102.2.0-alt2
- Update language support

* Thu Aug 25 2022 Pavel Vasenkov <pav@altlinux.org> 102.2.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-38472 Address bar spoofing via XSLT error handling
  + CVE-2022-38473 Cross-origin XSLT Documents would have inherited the parent's permissions
  + CVE-2022-38476 Data race and potential use-after-free in PK11_ChangePW
  + CVE-2022-38477 Memory safety bugs fixed in Firefox 104 and Firefox ESR 102.2
  + CVE-2022-38478 Memory safety bugs fixed in Firefox 104, Firefox ESR 102.2, and Firefox ESR 91.13

* Fri Jul 22 2022 Pavel Vasenkov <pav@altlinux.org> 102.1.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-36319 Mouse Position spoofing with CSS transforms
  + CVE-2022-36318 Directory indexes for bundled resources reflected URL parameters
  + CVE-2022-36314 Opening local <code>.lnk</code> files could cause unexpected network loads
  + CVE-2022-2505 Memory safety bugs fixed in Firefox 103 and 102.1

* Wed Jun 29 2022 Pavel Vasenkov <pav@altlinux.org> 91.11.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-34479 A popup window could be resized in a way to overlay the address bar with web content
  + CVE-2022-34470 Use-after-free in nsSHistory
  + CVE-2022-34468 CSP sandbox header without `allow-scripts` can be bypassed via retargeted javascript: URI
  + CVE-2022-34481 Potential integer overflow in ReplaceElementsAt
  + CVE-2022-31744 CSP bypass enabling stylesheet injection
  + CVE-2022-34472 Unavailable PAC file resulted in OCSP requests being blocked
  + CVE-2022-34478 Microsoft protocols can be attacked if a user accepts a prompt
  + CVE-2022-2200 Undesired attributes could be set as part of prototype pollution
  + CVE-2022-34484 Memory safety bugs fixed in Firefox 102 and Firefox ESR 91.11

* Fri Jun 03 2022 Pavel Vasenkov <pav@altlinux.org> 91.10.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-31736 Cross-Origin resource's length leaked
  + CVE-2022-31737 Heap buffer overflow in WebGL
  + CVE-2022-31738 Browser window spoof using fullscreen mode
  + CVE-2022-31739 Attacker-influenced path traversal when saving downloaded files
  + CVE-2022-31740 Register allocation problem in WASM on arm64
  + CVE-2022-31741 Uninitialized variable leads to invalid memory read
  + CVE-2022-31742 Querying a WebAuthn token with a large number of allowCredential entries may have leaked cross-origin information
  + CVE-2022-31747 Memory safety bugs fixed in Firefox 101 and Firefox ESR 91.10

* Sun May 22 2022 Pavel Vasenkov <pav@altlinux.org> 91.9.1-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-1802 Prototype pollution in Top-Level Await implementation
  + CVE-2022-1529 Untrusted input used in JavaScript object indexing, leading to prototype pollution

* Wed May 04 2022 Pavel Vasenkov <pav@altlinux.org> 91.9.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-29914 Fullscreen notification bypass using popups
  + CVE-2022-29909 Bypassing permission prompt in nested browsing contexts
  + CVE-2022-29916 Leaking browser history with CSS variables
  + CVE-2022-29911 iframe Sandbox bypass
  + CVE-2022-29912 Reader mode bypassed SameSite cookies
  + CVE-2022-29917 Memory safety bugs fixed in Firefox 100 and Firefox ESR 91.9

* Wed Apr 06 2022 Pavel Vasenkov <pav@altlinux.org> 91.8.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-1097 Use-after-free in NSSToken objects
  + CVE-2022-28281 Out of bounds write due to unexpected WebAuthN Extensions
  + CVE-2022-1196 Use-after-free after VR Process destruction
  + CVE-2022-28282 Use-after-free in DocumentL10n::TranslateDocument
  + CVE-2022-28285 Incorrect AliasSet used in JIT Codegen
  + CVE-2022-28286 iframe contents could be rendered outside the border
  + CVE-2022-24713 Denial of Service via complex regular expressions
  + CVE-2022-28289 Memory safety bugs fixed in Firefox 99 and Firefox ESR 91.8

* Sun Mar 13 2022 Pavel Vasenkov <pav@altlinux.org> 91.7.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-26383 Browser window spoof using fullscreen mode
  + CVE-2022-26384 iframe allow-scripts sandbox bypass
  + CVE-2022-26387 Time-of-check time-of-use bug when verifying add-on signatures
  + CVE-2022-26381 Use-after-free in text reflows
  + CVE-2022-26386 Temporary files downloaded to /tmp and accessible by other local users

* Mon Mar 07 2022 Pavel Vasenkov <pav@altlinux.org> 91.6.1-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-26485 Use-after-free in XSLT parameter processing
  + CVE-2022-26486 Use-after-free in WebGPU IPC Framework

* Wed Feb 09 2022 Pavel Vasenkov <pav@altlinux.org> 91.6.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-22753 Privilege Escalation to SYSTEM on Windows via Maintenance Service
  + CVE-2022-22754 Extensions could have bypassed permission confirmation during update
  + CVE-2022-22756 Drag and dropping an image could have resulted in the dropped object being an executable
  + CVE-2022-22759 Sandboxed iframes could have executed script if the parent appended elements
  + CVE-2022-22760 Cross-Origin responses could be distinguished between script and non-script content-types
  + CVE-2022-22761 frame-ancestors Content Security Policy directive was not enforced for framed extension pages
  + CVE-2022-22763 Script Execution during invalid object state
  + CVE-2022-22764 Memory safety bugs fixed in Firefox 97 and Firefox ESR 91.6

* Thu Jan 27 2022 Pavel Vasenkov <pav@altlinux.org> 91.5.1-alt1
- New ESR version.

* Tue Jan 11 2022 Andrey Cherepanov <cas@altlinux.org> 91.5.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2022-22746 Calling into reportValidity could have lead to fullscreen window spoof
  + CVE-2022-22743 Browser window spoof using fullscreen mode
  + CVE-2022-22742 Out-of-bounds memory access when inserting text in edit mode
  + CVE-2022-22741 Browser window spoof using fullscreen mode
  + CVE-2022-22740 Use-after-free of ChannelEventQueue::mOwner
  + CVE-2022-22738 Heap-buffer-overflow in blendGaussianBlur
  + CVE-2022-22737 Race condition when playing audio files
  + CVE-2021-4140 Iframe sandbox bypass with XSLT
  + CVE-2022-22748 Spoofed origin on external protocol launch dialog
  + CVE-2022-22745 Leaking cross-origin URLs through securitypolicyviolation event
  + CVE-2022-22744 The 'Copy as curl' feature in DevTools did not fully escape website-controlled data, potentially leading to command injection
  + CVE-2022-22747 Crash when handling empty pkcs7 sequence
  + CVE-2022-22739 Missing throttling on external protocol launch dialog
  + CVE-2022-22751 Memory safety bugs fixed in Firefox 96 and Firefox ESR 91.5

* Fri Dec 17 2021 Andrey Cherepanov <cas@altlinux.org> 91.4.1-alt1
- New ESR version.

* Mon Dec 06 2021 Andrey Cherepanov <cas@altlinux.org> 91.4.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2021-43536 URL leakage when navigating while executing asynchronous function
  + CVE-2021-43537 Heap buffer overflow when using structured clone
  + CVE-2021-43538 Missing fullscreen and pointer lock notification when requesting both
  + CVE-2021-43539 GC rooting failure when calling wasm instance methods
  + CVE-2021-43541 External protocol handler parameters were unescaped
  + CVE-2021-43542 XMLHttpRequest error codes could have leaked the existence of an external protocol handler
  + CVE-2021-43543 Bypass of CSP sandbox directive when embedding
  + CVE-2021-43545 Denial of Service when using the Location API in a loop
  + CVE-2021-43546 Cursor spoofing could overlay user interface when native cursor is zoomed

* Thu Nov 18 2021 Andrey Cherepanov <cas@altlinux.org> 91.3.0-alt2
- Show Home button on toolbar by default (ALT #41360).

* Tue Nov 02 2021 Andrey Cherepanov <cas@altlinux.org> 91.3.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2021-38503 iframe sandbox rules did not apply to XSLT stylesheets
  + CVE-2021-38504 Use-after-free in file picker dialog
  + CVE-2021-38505 Windows 10 Cloud Clipboard may have recorded sensitive user data
  + CVE-2021-38506 Firefox could be coaxed into going into fullscreen mode without notification or warning
  + CVE-2021-38507 Opportunistic Encryption in HTTP2 could be used to bypass the Same-Origin-Policy on services hosted on other ports
  + CVE-2021-38508 Permission Prompt could be overlaid, resulting in user confusion and potential spoofing
  + CVE-2021-38509 Javascript alert box could have been spoofed onto an arbitrary domain
  + CVE-2021-38510 Download Protections were bypassed by .inetloc files on Mac OS

* Tue Oct 05 2021 Andrey Cherepanov <cas@altlinux.org> 91.2.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2021-38496 Use-after-free in MessageTask
  + CVE-2021-38497 Validation message could have been overlaid on another origin
  + CVE-2021-38498 Use-after-free of nsLanguageAtomService object
  + CVE-2021-32810 Data race in crossbeam-deque
  + CVE-2021-38500 Memory safety bugs fixed in Firefox 93, Firefox ESR 78.15, and Firefox ESR 91.2
  + CVE-2021-38501 Memory safety bugs fixed in Firefox 93 and Firefox ESR 91.2

* Tue Sep 07 2021 Andrey Cherepanov <cas@altlinux.org> 91.1.0-alt1
- New ESR version.
- Security fixes:
  + CVE-2021-38492 Navigating to `mk:` URL scheme could load Internet Explorer
  + CVE-2021-38495 Memory safety bugs fixed in Firefox 92 and Firefox ESR 91.1

* Sat Sep 04 2021 Andrey Cherepanov <cas@altlinux.org> 91.0.1-alt1
- New ESR version.
- Security fixes:
  + CVE-2021-29991: Header Splitting possible with HTTP/3 Responses
  + CVE-2021-29981: Live range splitting could have led to conflicting assignments in the JIT
  + CVE-2021-29983: Firefox for Android could get stuck in fullscreen mode
  + CVE-2021-29987: Users could have been tricked into accepting unwanted permissions on Linux
  + CVE-2021-29982: Single bit data leak due to incorrect JIT optimization and type confusion
  + CVE-2021-29990: Memory safety bugs fixed in Firefox 91

* Tue Aug 10 2021 Andrey Cherepanov <cas@altlinux.org> 78.13.0-alt1
- New version (78.13.0).
- Security fixes:
  + CVE-2021-29986 Race condition when resolving DNS names could have led to memory corruption
  + CVE-2021-29988 Memory corruption as a result of incorrect style treatment
  + CVE-2021-29984 Incorrect instruction reordering during JIT optimization
  + CVE-2021-29980 Uninitialized memory in a canvas object could have led to memory corruption
  + CVE-2021-29985 Use-after-free media channels
  + CVE-2021-29989 Memory safety bugs fixed in Firefox 91 and Firefox ESR 78.13

* Mon Jul 12 2021 Andrey Cherepanov <cas@altlinux.org> 78.12.0-alt1
- New version (78.12.0).
- Security fixes:
  + CVE-2021-29970 Use-after-free in accessibility features of a document
  + CVE-2021-30547 Out of bounds write in ANGLE
  + CVE-2021-29976 Memory safety bugs fixed in Firefox 90 and Firefox ESR 78.12

* Tue Jun 01 2021 Andrey Cherepanov <cas@altlinux.org> 78.11.0-alt1
- New version (78.11.0).
- Security fixes:
  + CVE-2021-29964 Out of bounds-read when parsing a `WM_COPYDATA` message
  + CVE-2021-29967 Memory safety bugs fixed in Firefox 89 and Firefox ESR 78.11

* Wed May 05 2021 Andrey Cherepanov <cas@altlinux.org> 78.10.1-alt1
- New version (78.10.1).
- Security fixes:
  + CVE-2021-29951 Mozilla Maintenance Service could have been started or stopped by domain users

* Wed Apr 21 2021 Andrey Cherepanov <cas@altlinux.org> 78.10.0-alt1
- New version (78.10.0).
- Security fixes:
  + CVE-2021-23994 Out of bound write due to lazy initialization
  + CVE-2021-23995 Use-after-free in Responsive Design Mode
  + CVE-2021-23998 Secure Lock icon could have been spoofed
  + CVE-2021-23961 More internal network hosts could have been probed by a malicious webpage
  + CVE-2021-23999 Blob URLs may have been granted additional privileges
  + CVE-2021-24002 Arbitrary FTP command execution on FTP servers using an encoded URL
  + CVE-2021-29945 Incorrect size computation in WebAssembly JIT could lead to null-reads
  + CVE-2021-29946 Port blocking could be bypassed

* Tue Mar 23 2021 Andrey Cherepanov <cas@altlinux.org> 78.9.0-alt1
- New version (78.9.0).
- Security fixes:
  + CVE-2021-23981 Texture upload into an unbound backing buffer resulted in an out-of-bound read
  + CVE-2021-23982 Internal network hosts could have been probed by a malicious webpage
  + CVE-2021-23984 Malicious extensions could have spoofed popup information
  + CVE-2021-23987 Memory safety bugs fixed in Firefox 87 and Firefox ESR 78.9
- Do not build for ppc64le.

* Tue Feb 23 2021 Andrey Cherepanov <cas@altlinux.org> 78.8.0-alt1
- New version (78.8.0).
- Security fixes:
  + CVE-2021-23969 Content Security Policy violation report could have contained the destination of a redirect
  + CVE-2021-23968 Content Security Policy violation report could have contained the destination of a redirect
  + CVE-2021-23973 MediaError message property could have leaked information about cross-origin resources
  + CVE-2021-23978 Memory safety bugs fixed in Firefox 86 and Firefox ESR 78.8

* Fri Feb 12 2021 Andrey Cherepanov <cas@altlinux.org> 78.7.1-alt2
- Rebuild with llvm11.0.

* Fri Feb 05 2021 Andrey Cherepanov <cas@altlinux.org> 78.7.1-alt1
- New version (78.7.1).
- Security fixes:
  + MOZ-2021-0001: Buffer overflow in depth pitch calculations for compressed textures

* Tue Jan 26 2021 Andrey Cherepanov <cas@altlinux.org> 78.7.0-alt1
- New version (78.7.0).
- Security fixes:
  + CVE-2021-23953 Cross-origin information leakage via redirected PDF requests
  + CVE-2021-23954 Type confusion when using logical assignment operators in JavaScript switch statements
  + CVE-2020-26976 HTTPS pages could have been intercepted by a registered service worker when they should not have been
  + CVE-2021-23960 Use-after-poison for incorrectly redeclared JavaScript variables during GC
  + CVE-2021-23964 Memory safety bugs fixed in Firefox 85 and Firefox ESR 78.7

* Wed Jan 06 2021 Andrey Cherepanov <cas@altlinux.org> 78.6.1-alt1
- New version (78.6.1).
- Security fixes:
  + CVE-2020-16044 Use-after-free write when handling a malicious COOKIE-ECHO SCTP chunk

* Mon Dec 14 2020 Andrey Cherepanov <cas@altlinux.org> 78.6.0-alt1
- New version (78.6.0).
- Fixes:
  + CVE-2020-16042 Operations on a BigInt could have caused uninitialized memory to be exposed
  + CVE-2020-26971 Heap buffer overflow in WebGL
  + CVE-2020-26973 CSS Sanitizer performed incorrect sanitization
  + CVE-2020-26974 Incorrect cast of StyleGenericFlexBasis resulted in a heap use-after-free
  + CVE-2020-26978 Internal network hosts could have been probed by a malicious webpage
  + CVE-2020-35111 The proxy.onRequest API did not catch view-source URLs
  + CVE-2020-35112 Opening an extension-less download may have inadvertently launched an executable instead
  + CVE-2020-35113 Memory safety bugs fixed in Firefox 84 and Firefox ESR 78.6

* Thu Dec 03 2020 Andrey Cherepanov <cas@altlinux.org> 78.5.0-alt2
- Fix build against rust-1.48.

* Mon Nov 16 2020 Andrey Cherepanov <cas@altlinux.org> 78.5.0-alt1
- New version (78.5.0).
- Fixes:
  + CVE-2020-26951 Parsing mismatches could confuse and bypass security sanitizer for chrome privileged code
  + CVE-2020-16012 Variable time processing of cross-origin images during drawImage calls
  + CVE-2020-26953 Fullscreen could be enabled without displaying the security UI
  + CVE-2020-26956 XSS through paste (manual and clipboard API)
  + CVE-2020-26958 Requests intercepted through ServiceWorkers lacked MIME type restrictions
  + CVE-2020-26959 Use-after-free in WebRequestService
  + CVE-2020-26960 Potential use-after-free in uses of nsTArray
  + CVE-2020-15999 Heap buffer overflow in freetype
  + CVE-2020-26961 DoH did not filter IPv4 mapped IP Addresses
  + CVE-2020-26965 Software keyboards may have remembered typed passwords
  + CVE-2020-26966 Single-word search queries were also broadcast to local network
  + CVE-2020-26968 Memory safety bugs fixed in Firefox 83 and Firefox ESR 78.5

* Tue Nov 10 2020 Andrey Cherepanov <cas@altlinux.org> 78.4.1-alt1
- New version (78.4.1).
- Fixes:
  + CVE-2020-26950 Write side effects in MCallGetProperty opcode not accounted for

* Mon Oct 26 2020 Andrey Cherepanov <cas@altlinux.org> 78.4.0-alt2
- Build with nss-3.58.0 (thanks legion@).

* Tue Oct 20 2020 Andrey Cherepanov <cas@altlinux.org> 78.4.0-alt1
- New version (78.4.0).
- Fixes:
  + CVE-2020-15969 Use-after-free in usersctp
  + CVE-2020-15683 Memory safety bugs fixed in Firefox 82 and Firefox ESR 78.4

* Thu Oct 01 2020 Andrey Cherepanov <cas@altlinux.org> 78.3.1-alt1
- New version (78.3.1).

* Wed Sep 23 2020 Andrey Cherepanov <cas@altlinux.org> 78.3.0-alt1
- New release (78.3.0).
- Fixes:
  + CVE-2020-15677 Download origin spoofing via redirect
  + CVE-2020-15676 XSS when pasting attacker-controlled data into a contenteditable element
  + CVE-2020-15678 When recursing through layers while scrolling, an iterator may have become invalid, resulting in a potential use-after-free
  + CVE-2020-15673 Memory safety bugs fixed in Firefox 81 and Firefox ESR 78.3

* Mon Sep 14 2020 Andrey Cherepanov <cas@altlinux.org> 78.2.0-alt2
- Allow sideloading app and system unsigned addons.

* Tue Aug 25 2020 Andrey Cherepanov <cas@altlinux.org> 78.2.0-alt1
- New release (78.2.0).
- Fixes:
  + CVE-2020-15663 Downgrade attack on the Mozilla Maintenance Service could have resulted in escalation of privilege
  + CVE-2020-15664 Attacker-induced prompt for extension installation
  + CVE-2020-15670 Memory safety bugs fixed in Firefox 80 and Firefox ESR 78.2

* Fri Aug 14 2020 Andrey Cherepanov <cas@altlinux.org> 78.1.0-alt2
- Remove python2-base from build requirements.

* Tue Jul 28 2020 Andrey Cherepanov <cas@altlinux.org> 78.1.0-alt1
- New release (78.1.0).
- Fixes:
  + CVE-2020-15652 Potential leak of redirect targets when loading scripts in a worker
  + CVE-2020-6514 WebRTC data channel leaks internal address to peer
  + CVE-2020-15655 Extension APIs could be used to bypass Same-Origin Policy
  + CVE-2020-15653 Bypassing iframe sandbox when allowing popups
  + CVE-2020-6463 Use-after-free in ANGLE gl::Texture::onUnbindAsSamplerTexture
  + CVE-2020-15656 Type confusion for special arguments in IonMonkey
  + CVE-2020-15658 Overriding file type when saving to disk
  + CVE-2020-15657 DLL hijacking due to incorrect loading path
  + CVE-2020-15654 Custom cursor can overlay user interface
  + CVE-2020-15659 Memory safety bugs fixed in Firefox 79 and Firefox ESR 78.1

* Sat Jul 18 2020 Andrey Cherepanov <cas@altlinux.org> 78.0.2-alt1
- New ESR version (78.0.2) (based on legion@ spec and patches).
- Package localization files bundled (only kk,ru,uk locales are suppored).

* Mon Jul 13 2020 Alexey Gladkov <legion@altlinux.ru> 78.0.2-alt1
- New release (78.0.2).
- Fixes:
  + MFSA-2020-0003: X-Frame-Options bypass using object or embed tags

* Sat Jul 04 2020 Alexey Gladkov <legion@altlinux.ru> 78.0.1-alt1
- New release (78.0.1).
- Fixes:
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

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 68.9.0-alt1
- New ESR version (68.9.0).
- Fixes:
  + CVE-2020-12399 Timing attack on DSA signatures in NSS library
  + CVE-2020-12405 Use-after-free in SharedWorkerService
  + CVE-2020-12406 JavaScript Type confusion with NativeTypes
  + CVE-2020-12410 Memory safety bugs fixed in Firefox 77 and Firefox ESR 68.9

* Wed May 13 2020 Andrey Cherepanov <cas@altlinux.org> 68.8.0-alt3
- Disable User-Agent patch due to possible infomation leak.

* Wed May 13 2020 Andrey Cherepanov <cas@altlinux.org> 68.8.0-alt2
- Add ALT operating system string to browser User-Agent (ALT #38475).

* Tue May 05 2020 Andrey Cherepanov <cas@altlinux.org> 68.8.0-alt1
- New ESR version (68.8.0).
- Fixes:
  + CVE-2020-12387 Use-after-free during worker shutdown
  + CVE-2020-12388 Sandbox escape with improperly guarded Access Tokens
  + CVE-2020-12389 Sandbox escape with improperly separated process types
  + CVE-2020-6831 Buffer overflow in SCTP chunk input validation
  + CVE-2020-12392 Arbitrary local file access with 'Copy as cURL'
  + CVE-2020-12393 Devtools' 'Copy as cURL' feature did not fully escape website-controlled data, potentially leading to command injection
  + CVE-2020-12395 Memory safety bugs fixed in Firefox 76 and Firefox ESR 68.8

* Mon Apr 06 2020 Andrey Cherepanov <cas@altlinux.org> 68.7.0-alt1
- New ESR version (68.7.0).
- Fixes:
  + CVE-2020-6828 Preference overwrite via crafted Intent from malicious Android application
  + CVE-2020-6827 Custom Tabs in Firefox for Android could have the URI spoofed
  + CVE-2020-6821 Uninitialized memory could be read when using the WebGL copyTexSubImage method
  + CVE-2020-6822 Out of bounds write in GMPDecodeData when processing large images
  + CVE-2020-6825 Memory safety bugs fixed in Firefox 75 and Firefox ESR 68.7

* Sat Apr 04 2020 Andrey Cherepanov <cas@altlinux.org> 68.6.1-alt1
- New ESR version (68.6.1).
- Fixed:
  + CVE-2020-6819 Use-after-free while running the nsDocShell destructor
  + CVE-2020-6820 Use-after-free when handling a ReadableStream

* Tue Mar 10 2020 Andrey Cherepanov <cas@altlinux.org> 68.6.0-alt1
- New ESR version (68.6.0).
- Fix license tag according to SPDX.
- Fixed:
  + CVE-2020-6805 Use-after-free when removing data about origins
  + CVE-2020-6806 BodyStream::OnInputStreamReady was missing protections against state confusion
  + CVE-2020-6807 Use-after-free in cubeb during stream destruction
  + CVE-2020-6811 Devtools' 'Copy as cURL' feature did not fully escape website-controlled data, potentially leading to command injection
  + CVE-2019-20503 Out of bounds reads in sctp_load_addresses_from_init
  + CVE-2020-6812 The names of AirPods with personally identifiable information were exposed to websites with camera or microphone permission
  + CVE-2020-6814 Memory safety bugs fixed in Firefox 74 and Firefox ESR 68.6

* Wed Feb 12 2020 Andrey Cherepanov <cas@altlinux.org> 68.5.0-alt1
- New ESR version (68.5.0).
- Fixed:
  + CVE-2020-6796 Missing bounds check on shared memory read in the parent process
  + CVE-2020-6797 Extensions granted downloads.open permission could open arbitrary applications on Mac OSX
  + CVE-2020-6798 Incorrect parsing of template tag could result in JavaScript injection
  + CVE-2020-6799 Arbitrary code execution when opening pdf links from other applications, when Firefox is configured as default pdf reader
  + CVE-2020-6800 Memory safety bugs fixed in Firefox 73 and Firefox ESR 68.5

* Tue Jan 21 2020 Andrey Cherepanov <cas@altlinux.org> 68.4.2-alt1
- New ESR version (68.4.2).
- Bugs fixed:
  + Fixed various issues opening files with spaces in their path (bug 1601905, bug 1602726).

* Wed Jan 08 2020 Andrey Cherepanov <cas@altlinux.org> 68.4.1-alt1
- New ESR version (68.4.1).
- Fixed:
  + CVE-2019-17015 Memory corruption in parent process during new content process initialization on Windows
  + CVE-2019-17016 Bypass of @namespace CSS sanitization during pasting
  + CVE-2019-17017 Type Confusion in XPCVariant.cpp
  + CVE-2019-17021 Heap address disclosure in parent process during content process initialization on Windows
  + CVE-2019-17022 CSS sanitization does not escape HTML tags
  + CVE-2019-17024 Memory safety bugs fixed in Firefox 72 and Firefox ESR 68.4

* Fri Dec 06 2019 Andrey Cherepanov <cas@altlinux.org> 68.3.0-alt2
- Fix last changelog according to https://www.altlinux.org/Vulnerability_Policy.

* Thu Dec 05 2019 Andrey Cherepanov <cas@altlinux.org> 68.3.0-alt1
- New ESR version (68.3.0).
- Fixed:
  + CVE-2019-17008 Use-after-free in worker destruction
  + CVE-2019-13722 Stack corruption due to incorrect number of arguments in WebRTC code
  + CVE-2019-11745 Out of bounds write in NSS when encrypting with a block cipher
  + CVE-2019-17009 Updater temporary files accessible to unprivileged processes
  + CVE-2019-17010 Use-after-free when performing device orientation checks
  + CVE-2019-17005 Buffer overflow in plain text serializer
  + CVE-2019-17011 Use-after-free when retrieving a document in antitracking
  + CVE-2019-17012 Memory safety bugs fixed in Firefox 71 and Firefox ESR 68.3

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 68.2.0-alt1
- New ESR version (68.2.0).
- Fixed:
  + CVE-2019-15903 Heap overflow in expat library in XML_GetCurrentLineNumber
  + CVE-2019-11757 Use-after-free when creating index updates in IndexedDB
  + CVE-2019-11758 Potentially exploitable crash due to 360 Total Security
  + CVE-2019-11759 Stack buffer overflow in HKDF output
  + CVE-2019-11760 Stack buffer overflow in WebRTC networking
  + CVE-2019-11761 Unintended access to a privileged JSONView object
  + CVE-2019-11762 document.domain-based origin isolation has same-origin-property violation
  + CVE-2019-11763 Incorrect HTML parsing results in XSS bypass technique
  + CVE-2019-11764 Memory safety bugs fixed in Firefox 70 and Firefox ESR 68.2

* Thu Sep 19 2019 Andrey Cherepanov <cas@altlinux.org> 68.1.0-alt2
- Fix open context menu (thanks george@).

* Wed Sep 04 2019 Andrey Cherepanov <cas@altlinux.org> 68.1.0-alt1
- New ESR version (68.1.0).
- Fixed:
  + CVE-2019-11751 Malicious code execution through command line parameters
  + CVE-2019-11746 Use-after-free while manipulating video
  + CVE-2019-11744 XSS by breaking out of title and textarea elements using innerHTML
  + CVE-2019-11742 Same-origin policy violation with SVG filters and canvas to steal cross-origin images
  + CVE-2019-11736 File manipulation and privilege escalation in Mozilla Maintenance Service
  + CVE-2019-11753 Privilege escalation with Mozilla Maintenance Service in custom Firefox installation location
  + CVE-2019-11752 Use-after-free while extracting a key value in IndexedDB
  + CVE-2019-9812 Sandbox escape through Firefox Sync
  + CVE-2019-11743 Cross-origin access to unload event attributes
  + CVE-2019-11748 Persistence of WebRTC permissions in a third party context
  + CVE-2019-11749 Camera information available without prompting using getUserMedia
  + CVE-2019-11750 Type confusion in Spidermonkey
  + CVE-2019-11738 Content security policy bypass through hash-based sources in directives
  + CVE-2019-11747 'Forget about this site' removes sites from pre-loaded HSTS list
  + CVE-2019-11735 Memory safety bugs fixed in Firefox 69 and Firefox ESR 68.1
  + CVE-2019-11740 Memory safety bugs fixed in Firefox 69, Firefox ESR 68.1, and Firefox ESR 60.9
- Build in 8 jobs.

* Thu Aug 15 2019 Andrey Cherepanov <cas@altlinux.org> 68.0.2-alt1
- New ESR version (68.0.2).
- Fixed:
  + CVE-2019-11733 Stored passwords in 'Saved Logins' can be copied without master password entry

* Fri Jul 19 2019 Andrey Cherepanov <cas@altlinux.org> 68.0.1-alt1
- New ESR version (68.0.1).
- Fixed:
  + CVE-2019-9811 Sandbox escape via installation of malicious language pack
  + CVE-2019-11711 Script injection within domain through inner window reuse
  + CVE-2019-11712 Cross-origin POST requests can be made with NPAPI plugins by following 308 redirects
  + CVE-2019-11713 Use-after-free with HTTP/2 cached stream
  + CVE-2019-11729 Empty or malformed p256-ECDH public keys may trigger a segmentation fault
  + CVE-2019-11715 HTML parsing error can contribute to content XSS
  + CVE-2019-11717 Caret character improperly escaped in origins
  + CVE-2019-11719 Out-of-bounds read when importing curve25519 private key
  + CVE-2019-11730 Same-origin policy treats all files in a directory as having the same-origin
  + CVE-2019-11709 Memory safety bugs fixed in Firefox 68 and Firefox ESR 60.8

* Mon Jul 15 2019 Andrey Cherepanov <cas@altlinux.org> 60.8.0-alt2
- Fix Russian description encoding.

* Tue Jul 09 2019 Andrey Cherepanov <cas@altlinux.org> 60.8.0-alt1
- New ESR version (60.8.0).
- Fixed:
  + CVE-2019-9811 Sandbox escape via installation of malicious language pack
  + CVE-2019-11711 Script injection within domain through inner window reuse
  + CVE-2019-11712 Cross-origin POST requests can be made with NPAPI plugins by following 308 redirects
  + CVE-2019-11713 Use-after-free with HTTP/2 cached stream
  + CVE-2019-11729 Empty or malformed p256-ECDH public keys may trigger a segmentation fault
  + CVE-2019-11715 HTML parsing error can contribute to content XSS
  + CVE-2019-11717 Caret character improperly escaped in origins
  + CVE-2019-11719 Out-of-bounds read when importing curve25519 private key
  + CVE-2019-11730 Same-origin policy treats all files in a directory as having the same-origin
  + CVE-2019-11709 Memory safety bugs fixed in Firefox 68 and Firefox ESR 60.8

* Wed Jul 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 60.7.2-alt2
- Added ppc64le support.
- spec: cleaned up rpm-build internal macros.

* Thu Jun 20 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.2-alt1
- New ESR version (60.7.2).
- Fixed:
  + CVE-2019-11708 sandbox escape using Prompt:Open

* Tue Jun 18 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.1-alt1
- New ESR version (60.7.1).
- Fixed:
  + CVE-2019-11707 Type confusion in Array.pop

* Sun Jun 16 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.0-alt2
- Fix build with Rust > 1.33.

* Tue May 21 2019 Andrey Cherepanov <cas@altlinux.org> 60.7.0-alt1
- New ESR version (60.7.0).
- Fixed:
  + CVE-2019-9815 Disable hyperthreading on content JavaScript threads on macOS
  + CVE-2019-9816 Type confusion with object groups and UnboxedObjects
  + CVE-2019-9817 Stealing of cross-domain images using canvas
  + CVE-2019-9818 Use-after-free in crash generation server
  + CVE-2019-9819 Compartment mismatch with fetch API
  + CVE-2019-9820 Use-after-free of ChromeEventHandler by DocShell
  + CVE-2019-11691 Use-after-free in XMLHttpRequest
  + CVE-2019-11692 Use-after-free removing listeners in the event listener manager
  + CVE-2019-11693 Buffer overflow in WebGL bufferdata on Linux
  + CVE-2019-7317 Use-after-free in png_image_free of libpng library
  + CVE-2019-9797 Cross-origin theft of images with createImageBitmap
  + CVE-2018-18511 Cross-origin theft of images with ImageBitmapRenderingContext
  + CVE-2019-11694 Uninitialized memory memory leakage in Windows sandbox
  + CVE-2019-11698 Theft of user history data through drag and drop of hyperlinks to and from bookmarks
  + CVE-2019-5798 Out-of-bounds read in Skia
  + CVE-2019-9800 Memory safety bugs fixed in Firefox 67 and Firefox ESR 60.7

* Sun May 05 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.2-alt1
- New ESR version (60.6.2).
- Hotfix for addon signing cert has not been applied.

* Sat Mar 23 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.1-alt1
- New ESR version (60.6.1).
- Fixed:
  + CVE-2019-9810 IonMonkey MArraySlice has incorrect alias information
  + CVE-2019-9813 Ionmonkey type confusion with __proto__ mutations

* Thu Mar 21 2019 Andrey Cherepanov <cas@altlinux.org> 60.6.0-alt1
- New ESR version (60.6.0).
- Fixed:
  + CVE-2019-9790 Use-after-free when removing in-use DOM elements
  + CVE-2019-9791 Type inference is incorrect for constructors entered through on-stack replacement with IonMonkey
  + CVE-2019-9792 IonMonkey leaks JS_OPTIMIZED_OUT magic value to script
  + CVE-2019-9793 Improper bounds checks when Spectre mitigations are disabled
  + CVE-2019-9794 Command line arguments not discarded during execution
  + CVE-2019-9795 Type-confusion in IonMonkey JIT compiler
  + CVE-2019-9796 Use-after-free with SMIL animation controller
  + CVE-2019-9801 Windows programs that are not 'URL Handlers' are exposed to web content
  + CVE-2018-18506 Proxy Auto-Configuration file can define localhost access to be proxied
  + CVE-2019-9788 Memory safety bugs fixed in Firefox 66 and Firefox ESR 60.6

* Wed Feb 27 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.2-alt1.1
- Rebuild vith libvpx5.

* Sat Feb 23 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.2-alt1
- New ESR version (60.5.2).

* Fri Feb 15 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.1-alt1
- New ESR version (60.5.1).
- Fixed:
  + CVE-2018-18356 Use-after-free in Skia
  + CVE-2019-5785 Integer overflow in Skia
  + CVE-2018-18335 Buffer overflow in Skia with accelerated Canvas 2D

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 60.5.0-alt1
- New ESR version (60.5.0).
- Fixed:
  + CVE-2018-18500 Use-after-free parsing HTML5 stream
  + CVE-2018-18505 Privilege escalation through IPC channel messages
  + CVE-2018-18501 Memory safety bugs fixed in Firefox 65 and Firefox ESR 60.5

* Thu Jan 10 2019 Andrey Cherepanov <cas@altlinux.org> 60.4.0-alt2
- Rebuild with llvm7.0 (ALT #35858).
- Build with gcc on %%ix86.

* Tue Dec 11 2018 Andrey Cherepanov <cas@altlinux.org> 60.4.0-alt1
- New ESR version (60.4.0)
- Fixed:
  + CVE-2018-17466 Buffer overflow and out-of-bounds read in ANGLE library with TextureStorage11
  + CVE-2018-18492 Use-after-free with select element
  + CVE-2018-18493 Buffer overflow in accelerated 2D canvas with Skia
  + CVE-2018-18494 Same-origin policy violation using location attribute and performance.getEntries to steal cross-origin URLs
  + CVE-2018-18498 Integer overflow when calculating buffer sizes for images
  + CVE-2018-12405 Memory safety bugs fixed in Firefox 64 and Firefox ESR 60.4

* Tue Oct 23 2018 Andrey Cherepanov <cas@altlinux.org> 60.3.0-alt1
- New ESR version (60.3.0).
- Fixed:
  + CVE-2018-12391 HTTP Live Stream audio data is accessible cross-origin
  + CVE-2018-12392 Crash with nested event loops
  + CVE-2018-12393 Integer overflow during Unicode conversion while loading JavaScript
  + CVE-2018-12395 WebExtension bypass of domain restrictions through header rewriting
  + CVE-2018-12396 WebExtension content scripts can execute in disallowed contexts
  + CVE-2018-12397 WebExtension can request access to local files without the warning prompt
  + CVE-2018-12389 Memory safety bugs fixed in Firefox ESR 60.3
  + CVE-2018-12390 Memory safety bugs fixed in Firefox 63 and Firefox ESR 60.3

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 60.2.2-alt1
- New ESR version (60.2.2)
- Fixed:
  + CVE-2018-12386 Type confusion in JavaScript
  + CVE-2018-12387 JavaScript JIT compiler inlines Array.prototype.push with multiple arguments

* Mon Sep 24 2018 Andrey Cherepanov <cas@altlinux.org> 60.2.1-alt1
- New ESR version (60.2.1).
- Fixed:
  + CVE-2018-12385 Crash in TransportSecurityInfo due to cached data
  + CVE-2018-12383 Setting a master password post-Firefox 58 does not delete unencrypted previously stored passwords

* Mon Sep 10 2018 Andrey Cherepanov <cas@altlinux.org> 60.2.0-alt1
- New ESR version (60.2.0).
- Fixed:
  + CVE-2018-12377 Use-after-free in refresh driver timers
  + CVE-2018-12378 Use-after-free in IndexedDB
  + CVE-2018-12379 Out-of-bounds write with malicious MAR file
  + CVE-2017-16541 Proxy bypass using automount and autofs
  + CVE-2018-12381 Dragging and dropping Outlook email message results in page navigation
  + CVE-2018-12376 Memory safety bugs fixed in Firefox 62 and Firefox ESR 60.2

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 60.1.0-alt1
- New ESR version (60.1.0).
- Fixed:
  + CVE-2018-12359 Buffer overflow using computed size of canvas element
  + CVE-2018-12360 Use-after-free when using focus()
  + CVE-2018-12361 Integer overflow in SwizzleData
  + CVE-2018-12362 Integer overflow in SSSE3 scaler
  + CVE-2018-5156 Media recorder segmentation fault when track type is changed during capture
  + CVE-2018-12363 Use-after-free when appending DOM nodes
  + CVE-2018-12364 CSRF attacks through 307 redirects and NPAPI plugins
  + CVE-2018-12365 Compromised IPC child process can list local filenames
  + CVE-2018-12371 Integer overflow in Skia library during edge builder allocation
  + CVE-2018-12366 Invalid data handling during QCMS transformations
  + CVE-2018-12367 Timing attack mitigation of PerformanceNavigationTiming
  + CVE-2018-12368 No warning when opening executable SettingContent-ms files
  + CVE-2018-12369 WebExtension security permission checks bypassed by embedded experiments
  + CVE-2018-5187 Memory safety bugs fixed in Firefox 60 and Firefox ESR 60.1
  + CVE-2018-5188 Memory safety bugs fixed in Firefox 60, Firefox ESR 60.1, and Firefox ESR 52.9


* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 60.0.2-alt2
- Fix build for aarch64 (thanks legion@).

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 60.0.2-alt1
- New ESR version (60.0.2).
- Fixed:
  + CVE-2018-6126 Heap buffer overflow rasterizing paths in SVG with Skia

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 60.0.1-alt1
- New ESR version (60.0.1).
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

* Wed May 09 2018 Andrey Cherepanov <cas@altlinux.org> 52.8.0-alt1
- New ESR version (52.8.0).
- Fixes:
  + CVE-2018-5183 Backport critical security fixes in Skia
  + CVE-2018-5154 Use-after-free with SVG animations and clip paths
  + CVE-2018-5155 Use-after-free with SVG animations and text paths
  + CVE-2018-5157 Same-origin bypass of PDF Viewer to view protected PDF files
  + CVE-2018-5158 Malicious PDF can inject JavaScript into PDF Viewer
  + CVE-2018-5159 Integer overflow and out-of-bounds write in Skia
  + CVE-2018-5168 Lightweight themes can be installed without user interaction
  + CVE-2018-5178 Buffer overflow during UTF-8 to Unicode string conversion through legacy extension
  + CVE-2018-5150 Memory safety bugs fixed in Firefox 60 and Firefox ESR 52.8

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.4-alt1
- New ESR version (52.7.4).

* Mon Mar 26 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.3-alt1
- New ESR version (52.7.3)
- Fixes:
  + CVE-2018-5148 Use-after-free in compositor

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.2-alt1
- New ESR version (52.7.2)

* Thu Mar 15 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.1-alt1
- New ESR version (52.7.1)

* Sat Mar 10 2018 Andrey Cherepanov <cas@altlinux.org> 52.7.0-alt1
- New ESR version (52.7.0).
- Fixes:
  + CVE-2018-5127 Buffer overflow manipulating SVG animatedPathSegList
  + CVE-2018-5129 Out-of-bounds write with malformed IPC messages
  + CVE-2018-5130 Mismatched RTP payload type can trigger memory corruption
  + CVE-2018-5131 Fetch API improperly returns cached copies of no-store/no-cache resources
  + CVE-2018-5144 Integer overflow during Unicode conversion
  + CVE-2018-5125 Memory safety bugs fixed in Firefox 59 and Firefox ESR 52.7
  + CVE-2018-5145 Memory safety bugs fixed in Firefox ESR 52.7

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 52.6.0-alt2
- Enable ALSA support (ALT #34608)

* Mon Jan 22 2018 Andrey Cherepanov <cas@altlinux.org> 52.6.0-alt1
- New ESR version (52.6.0)
- Fixes:
  + CVE-2018-5095 Integer overflow in Skia library during edge builder allocation
  + CVE-2018-5096 Use-after-free while editing form elements
  + CVE-2018-5097 Use-after-free when source document is manipulated during XSLT
  + CVE-2018-5098 Use-after-free while manipulating form input elements
  + CVE-2018-5099 Use-after-free with widget listener
  + CVE-2018-5102 Use-after-free in HTML media elements
  + CVE-2018-5103 Use-after-free during mouse event handling
  + CVE-2018-5104 Use-after-free during font face manipulation
  + CVE-2018-5117 URL spoofing with right-to-left text aligned left-to-right
  + CVE-2018-5089 Memory safety bugs fixed in Firefox 58 and Firefox ESR 52.6
- Continue fix of Speculative execution side-channel attack ("Spectre")

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
  + CVE-2017-7806: Use-after-free in layer manager with SVG
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
