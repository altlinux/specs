%set_verify_elf_method textrel=relaxed
%define v8_ver 3.19
%define rev 223446

%def_disable debug
%def_disable nacl

%if_enabled debug
%define buildtype Debug
%else
%define buildtype Release
%endif

Name:           chromium
Version:        29.0.1547.76
Release:        alt2.r%rev

Summary:        An open source web browser developed by Google
License:        BSD-3-Clause and LGPL-2.1+
Group:          Networking/WWW
Url:            http://code.google.com/p/chromium/

Source0:        %name-%version.tar.gz

Source30:       master_preferences
Source31:       default_bookmarks.html
Source99:       chrome-wrapper
Source100:      %name.sh
Source101:      chromium.desktop
Source102:      chromium-browser.xml
Source104:      chromium-icons.tar
Source200:      %name.default
Provides:       chromium-browser = %version
Obsoletes:      chromium-browser < %version

## Start Patches
# Many changes to the gyp systems so we can use system libraries
# PATCH-FIX-OPENSUSE patches in system zlib library
Patch8:         chromium-codechanges-zlib.patch
# PATCH-FIX-OPENSUSE removes build part for courgette
Patch13:        chromium-no-courgette.patch
# PATCH-FIX-OPENSUSE enables reading of the master preference
Patch14:        chromium-master-prefs-path.patch
# PATCH-FIX-OPENSUSE patches in system glew library
Patch17:        chromium-system-glew.patch
# PATCH-FIX-OPENSUSE disables the requirement for ffmpeg
Patch20:        chromium-6.0.425.0-ffmpeg-no-pkgconfig.patch
# PATCH-FIX-OPENSUSE patches in system speex library
Patch28:        chromium-system-speex.patch
# PATCH-FIX-OPENSUSE patches in the system libvpx library
Patch32:        chromium-7.0.542.0-system-libvpx.patch
# PATCH-FIX-OPENSUSE remove the rpath in the libraries
Patch62:        chromium-norpath.patch
# PATCH-FIX-OPENSUSE patches in the system v8 library
Patch63:        chromium-23.0.1271.64-system-gyp-v8.patch
# PATCH-FIX-OPENSUSE Compile the sandbox with -fPIE settings
Patch66:        chromium-sandbox-pie.patch
# PATCH-FIX-OPENSUSE Compile with the standard gold linker
Patch67:        chromium_use_gold.patch
# ALT: Fix krb5 includes path
Patch69:	chromium-alt-krb5-fix-path.patch
# Set appropriate desktop file name for default browser check
Patch71:	chromium-21.0.1158.0-set-desktop-file-name.patch

# Patches from Debian
Patch80:	nspr.patch
Patch81:	nss.patch
Patch82:	expat.patch
Patch84:	ffmpeg_arm.patch
Patch85:	fix-manpage.patch
Patch87:	cups1.5.patch
Patch88:	arm-no-float-abi.patch
Patch90:	gcc4.7.patch
Patch91:	arm.patch

# Patches from upstream

%add_findreq_skiplist %_libdir/%name/xdg-settings
%add_findreq_skiplist %_libdir/%name/xdg-mime

BuildRequires: /proc

BuildRequires:  bison
BuildRequires:  bzlib-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:	gst-plugins-devel
BuildRequires:  libalsa-devel
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
BuildRequires:  libcups-devel
BuildRequires:  libdbus-glib-devel
BuildRequires:  libelf-devel
BuildRequires:  libevent1.4-devel
BuildRequires:  libexpat-devel
BuildRequires:  libflac-devel
BuildRequires:  libglew-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libhunspell-devel
#BuildRequires:  libicu-devel >= 4.0
BuildRequires:  libkrb5-devel
BuildRequires:  libnspr-devel
BuildRequires:  libnss-devel
BuildRequires:  libpam-devel
BuildRequires:  libpci-devel
BuildRequires:  libpng12-devel
BuildRequires:  libpulseaudio-devel
BuildRequires:  libspeechd-devel >= 0.8
BuildRequires:  libspeex-devel
BuildRequires:  libsqlite3-devel
BuildRequires:  libssl-devel
BuildRequires:  libudev-devel
BuildRequires:  libv8-devel = %v8_ver
BuildRequires:  libvpx-devel
BuildRequires:  libx264-devel
BuildRequires:  libxslt-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libyasm-devel
BuildRequires:  perl-Switch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo) >= 1.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xt)
BuildRequires:  python-devel
BuildRequires:  python-module-PyXML
BuildRequires:  python-modules-compiler
BuildRequires:  python-modules-email
BuildRequires:  python-modules-encodings
BuildRequires:  python-modules-json
BuildRequires:  python-modules-logging
BuildRequires:  subversion
BuildRequires:  wdiff
BuildRequires:  yasm
#BuildRequires:  zlib-devel

#Requires:       libv8 >= %v8_ver

Provides: 		webclient, /usr/bin/xbrowser
BuildPreReq: 	alternatives >= 0.2.0
PreReq(post,preun): alternatives >= 0.2

%description
Chromium is an open-source browser project that aims to build a safer,
faster, and more stable way for all Internet users to experience the web.

%package kde

Summary:        Update to chromium to use KDE's kwallet to store passwords
License:        BSD-3-Clause and LGPL-2.1+
Group:          Networking/WWW
Conflicts:      chromium-gnome
Conflicts:      chromium-desktop-gnome
Provides:       chromium-password = %version
Provides:		chromium-desktop-kde = %version
Obsoletes:		chromium-desktop-kde < %version
Requires:       chromium = %version
Requires:       kde4base-runtime-core

%description kde
By using the update-alternatives the password store for Chromium is
changed to utilize KDE's kwallet. Please be aware that by this change
the old password are no longer accessible and are also not converted
to kwallet.

%package gnome

Summary:        Update to chromium to use Gnome keyring to store passwords
License:        BSD-3-Clause and LGPL-2.1+
Group:          Networking/WWW
Conflicts:      chromium-desktop-kde
Conflicts:      chromium-kde
Provides:       chromium-password = %version
Provides:		chromium-desktop-gnome = %version
Obsoletes:		chromium-desktop-gnome < %version
Requires:       chromium = %version
Requires:       gnome-keyring

%description gnome
By using the update-alternatives the password store for Chromium is
changed to utilize Gnome's Keyring. Please be aware that by this change
the old password are no longer accessible and are also not converted
to Gnome's Keyring.

%prep
%setup -q -n %name

#%%patch62 -p1
%patch63 -p2
%patch8 -p2
%patch13 -p2
%patch14 -p2
%patch17 -p1
#%%patch20 -p1
%patch28 -p2
#%%patch32 -p1
%patch66 -p1
#%%patch67 -p1
%patch69 -p2
%patch71 -p2

%patch80 -p2
%patch81 -p1
%patch82 -p1
#%%patch84 -p1
%patch85 -p1
%patch87 -p1
%patch88 -p1
%patch90 -p1
%patch91 -p1

# Replace anywhere v8 to system package
subst 's,v8/tools/gyp/v8.gyp,build/linux/system.gyp,' `find . -type f -a -name *.gyp*`
sed -i '/v8_shell#host/d' src/chrome/chrome_tests.gypi src/chrome/js_unittest_rules.gypi
grep -Rl '^#include [<"]v8/include' * 2>/dev/null | while read f;do subst 's,^\(#include [<"]\)v8/include/,\1,' "$f";done

echo "svn%rev" > src/build/LASTCHANGE.in

# Make sure that the requires legal files can be found
cp -a src/AUTHORS src/LICENSE .

%build

## create make files

PARSED_OPT_FLAGS=`echo \'%optflags -DUSE_SYSTEM_LIBEVENT -fPIC -fno-ipa-cp -fno-strict-aliasing \' | sed "s/ /',/g" | sed "s/',/', '/g"`
for i in src/build/common.gypi; do
        sed -i "s|'-march=pentium4',||g" $i
%ifnarch x86_64
        sed -i "s|'-mfpmath=sse',||g" $i
%endif
        sed -i "s|'-O<(debug_optimize)',||g" $i
        sed -i "s|'-m32',||g" $i
        sed -i "s|'-fno-exceptions',|$PARSED_OPT_FLAGS|g" $i
        sed -i "s|'-Werror'|'-Wno-error'|g" $i
done


pushd src

./build/gyp_chromium -f make build/all.gyp \
	-Dlinux_sandbox_path=%_libexecdir/chrome_sandbox \
	-Dlinux_sandbox_chrome_path=%_libdir/chromium/chromium \
	-Dbuild_ffmpegsumo=1 \
	-Duse_system_bzip2=1 \
	-Duse_system_ffmpeg=0 \
	-Duse_system_flac=1 \
	-Duse_system_icu=0 \
	-Duse_system_libbz2=1 \
	-Duse_system_libevent=1 \
	-Duse_system_libjpeg=0 \
	-Duse_system_libpng=0 \
	-Duse_system_libwebp=0 \
	-Duse_system_libxml=1 \
	-Duse_system_libxslt=1 \
	-Duse_system_speex=1 \
	-Duse_system_sqlite=0 \
	-Duse_system_v8=1 \
	-Duse_system_vpx=0 \
	-Duse_system_xdg_utils=0 \
	-Duse_system_yasm=1 \
	-Duse_system_zlib=0 \
	-Dremove_webcore_debug_symbols=1 \
	-Dproprietary_codecs=1 \
%if_disabled nacl
    -Ddisable_nacl=1 \
%endif
	-Dlinux_fpic=1 \
%ifnarch x86_64
	-Ddisable_sse2=1 \
%endif
%ifarch x86_64
	-Dtarget_arch=x64 \
%endif
%ifarch arm armh
	-Dtarget_arch=arm \
	-Denable_webrtc=0 \
	-Duse_cups=1 \
%ifarch arm
	-Dv8_use_arm_eabi_hardfloat=false \
	-Darm_float_abi=soft \
	-Darm_thumb=0 \
	-Darmv7=0 \
	-Darm_neon=0 \
%endif
%ifarch armh
	-Dv8_use_arm_eabi_hardfloat=true \
	-Darm_fpu=vfpv3 \
	-Darm_float_abi=hard \
	-Darm_thumb=1 \
	-Darmv7=1 \
	-Darm_neon=0 \
%endif
%endif
	-Dlinux_use_gold_flags=0 \
	-Dlinux_use_gold_binary=0 \
    -Dlinux_link_libpci=1 \
    -Dlinux_link_libspeechd=1 \
    -Dlibspeechd_h_prefix=speech-dispatcher/ \
	-Denable_plugin_installation=0 \
	-Dlinux_use_tcmalloc=0 \
	-Duse_pulseaudio=1 \
	-Djavascript_engine=v8 \
	-Dgoogle_api_key='AIzaSyAIIWz7zaCwYcUSe3ZaRPviXjMjkBP4-xY' \
	-Dgoogle_default_client_id='1018394967181.apps.googleusercontent.com' \
	-Dgoogle_default_client_secret='h_PrTP1ymJu83YTLyz-E25nP'
# Set up Google API keys, see http://www.chromium.org/developers/how-tos/api-keys .
# Note: these are for ALT Linux use ONLY. For your own distribution,
# please get your own set of keys.

# Buld main program
%make_build -r %{?_smp_mflags} chrome V=1 BUILDTYPE=%buildtype

# Build the required SUID_SANDBOX helper
%make_build -r %{?_smp_mflags} chrome_sandbox V=1 BUILDTYPE=%buildtype

# Build the ChromeDriver test suite
%make_build -r %{?_smp_mflags} chromedriver V=1 BUILDTYPE=%buildtype

popd

%install
mkdir -p %buildroot%_libdir/chromium/
%ifarch x86_64
mkdir -p %buildroot%_prefix/lib/
%endif
install -m 755 %SOURCE100 %buildroot%_libdir/chromium/chromium-generic
install -pD -m644 %SOURCE200 %buildroot%_sysconfdir/%name/default
# x86_64 capable systems need this
sed -i "s|/usr/lib/chromium|%_libdir/chromium|g" %buildroot%_libdir/chromium/chromium-generic

#update the password-store settings for each alternative
sed "s|password-store=detect|password-store=kwallet|g" %buildroot%_libdir/chromium/chromium-generic > %buildroot%_libdir/chromium/chromium-kde
sed "s|password-store=detect|password-store=gnome|g" %buildroot%_libdir/chromium/chromium-generic > %buildroot%_libdir/chromium/chromium-gnome
mkdir -p %buildroot%_mandir/man1/

pushd src/out/%buildtype

cp -a chrome_sandbox %buildroot%_libexecdir/chrome_sandbox
cp -a *.pak locales xdg-mime %buildroot%_libdir/chromium/
cp -a chromedriver %buildroot%_libdir/chromium/

# Patch xdg-settings to use the chromium version of xdg-mime as that the system one is not KDE4 compatible
sed "s|xdg-mime|%_libdir/chromium/xdg-mime|g" xdg-settings > %{buildroot}%{_libdir}/chromium/xdg-settings

cp -a chrome %buildroot%_libdir/chromium/chromium
cp -a chrome.1 %buildroot%_mandir/man1/chrome.1
cp -a chrome.1 %buildroot%_mandir/man1/chromium.1
cp -a libffmpegsumo.so %buildroot%_libdir/chromium/libffmpegsumo.so

# NaCl
%if_enabled nacl
cp -a nacl_helper %buildroot%_libdir/chromium/
cp -a nacl_helper_bootstrap %buildroot%_libdir/chromium/
cp -a nacl_irt_*.nexe %buildroot%_libdir/chromium/
cp -a libppGoogleNaClPluginChrome.so %buildroot%_libdir/chromium/
%endif
popd

mkdir -p %buildroot%_datadir/icons/
pushd %buildroot%_datadir/icons/
tar -xf %SOURCE104
mv oxygen hicolor
popd

mkdir -p %buildroot%_desktopdir
install -m0644 %SOURCE101 %buildroot%_desktopdir

mkdir -p %buildroot%_datadir/gnome-control-center/default-apps/
cp -a %SOURCE102 %buildroot%_datadir/gnome-control-center/default-apps/

# link to browser plugin path.  Plugin patch doesn't work. Why?
mkdir -p %buildroot%_libdir/browser-plugins
pushd %buildroot%_libdir/%name
ln -s %_libdir/browser-plugins plugins

# Install the master_preferences file
mkdir -p %buildroot%_sysconfdir/%name
install -m 0644 %SOURCE30 %buildroot%_sysconfdir/%name
install -m 0644 %SOURCE31 %buildroot%_sysconfdir/%name

# Set alternative to xbrowser
mkdir -p %buildroot%_altdir
printf '%_bindir/xbrowser\t%_bindir/%name\t50\n' > %buildroot%_altdir/%name
printf '%_bindir/%name\t%_libdir/%name/%name-generic\t10\n' > %buildroot%_altdir/%name-generic
printf '%_bindir/%name\t%_libdir/%name/%name-kde\t15\n' > %buildroot%_altdir/%name-kde
printf '%_bindir/%name\t%_libdir/%name/%name-gnome\t15\n' > %buildroot%_altdir/%name-gnome

%files
%doc AUTHORS LICENSE
%config %_sysconfdir/%name
%dir %_datadir/gnome-control-center
%dir %_datadir/gnome-control-center/default-apps
%config(noreplace) %_sysconfdir/%name/default
%dir %_libdir/chromium/
%attr(4711,root,root) %_libexecdir/chrome_sandbox
%_libdir/chromium/chromium
%_libdir/chromium/chromedriver
%_libdir/chromium/chromium-generic
%_libdir/chromium/libffmpegsumo.so
%_libdir/chromium/plugins/
%_libdir/chromium/locales/
%if_enabled nacl
%_libdir/chromium/nacl_*
%_libdir/chromium/libppGoogleNaClPluginChrome.so
%endif
%attr(755,root,root) %_libdir/chromium/xdg-settings
%attr(755,root,root) %_libdir/chromium/xdg-mime
%_libdir/chromium/*.pak
%_mandir/man1/chrom*
%_datadir/applications/*.desktop
%_datadir/gnome-control-center/default-apps/chromium-browser.xml
%_iconsdir/hicolor/*/apps/chromium-browser.*
%_altdir/%name
%_altdir/%name-generic

%files kde
%attr(755, root, root) %_libdir/chromium/chromium-kde
%_altdir/%name-kde

%files gnome
%attr(755, root, root) %_libdir/chromium/chromium-gnome
%_altdir/%name-gnome

%changelog
* Wed Sep 25 2013 Andrey Cherepanov <cas@altlinux.org> 29.0.1547.76-alt2.r223446
- New version 29.0.1547.76

* Tue Sep 03 2013 Andrey Cherepanov <cas@altlinux.org> 29.0.1547.65-alt1.r220622
- New version 29.0.1547.62
- Security fixes:
  - High CVE-2013-2900: Incomplete path sanitization in file handling.
  - Low CVE-2013-2905: Information leak via overly broad permissions on
    shared memory files.
  - High CVE-2013-2901: Integer overflow in ANGLE.
  - High CVE-2013-2902: Use after free in XSLT.
  - High CVE-2013-2903: Use after free in media element.
  - High CVE-2013-2904: Use after free in document parsing.
- Improved Omnibox suggestions based on the recency of sites you have
  visited
- Ability to reset your profile back to its original state
- Many new apps and extensions APIs
- Lots of stability and performance improvements
- Fix an issue with printing from Google Docs applications
- Fix an issue with Sync

* Wed Jul 31 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 28.0.1500.95-alt2.r213514
- rebuild with versioned v8

* Wed Jul 31 2013 Andrey Cherepanov <cas@altlinux.org> 28.0.1500.95-alt1.r213514
- New version 28.0.1500.95
- Security fixes:
  - Medium CVE-2013-2881: Origin bypass in frame handling.
  - High CVE-2013-2883: Use-after-free in MutationObserver.
  - High CVE-2013-2884: Use-after-free in DOM.
  - High CVE-2013-2885: Use-after-free in input handling.

* Wed Jul 24 2013 Andrey Cherepanov <cas@altlinux.org> 28.0.1500.71-alt1.r209842
- New version 28.0.1500.71
- Security fixes:
  - High CVE-2013-2879: Confusion setting up sign-in and sync.
  - Medium CVE-2013-2868: Incorrect sync of NPAPI extension component.
  - Medium CVE-2013-2869: Out-of-bounds read in JPEG2000 handling.
  - Critical CVE-2013-2870: Use-after-free with network sockets.
  - Medium CVE-2013-2853: Man-in-the-middle attack against HTTP in SSL.
  - High CVE-2013-2871: Use-after-free in input handling.
  - High CVE-2013-2873: Use-after-free in resource loading.
  - Medium CVE-2013-2875: Out-of-bounds-read in SVG.
  - Medium CVE-2013-2876: Extensions permissions confusion with interstitials.
  - Low CVE-2013-2877: Out-of-bounds read in XML parsing.
  - None: Remove the "viewsource" attribute on iframes.
  - Medium CVE-2013-2878: Out-of-bounds read in text handling.
  - High CVE-2013-2880: Various fixes from internal audits, fuzzing and other initiatives

* Wed Jun 05 2013 Andrey Cherepanov <cas@altlinux.org> 27.0.1453.110-alt1.r202711
- New version 27.0.1453.110
- Security fixes:
  - Critical CVE-2013-2863: Memory corruption in SSL socket handling.
  - High CVE-2013-2856: Use-after-free in input handling.
  - High CVE-2013-2857: Use-after-free in image handling.
  - High CVE-2013-2858: Use-after-free in HTML5 Audio.
  - High CVE-2013-2859: Cross-origin namespace pollution.
  - High CVE-2013-2860: Use-after-free with workers accessing database APIs.
  - High CVE-2013-2861: Use-after-free with SVG.
  - High CVE-2013-2862: Memory corruption in Skia GPU handling.
  - High CVE-2013-2864: Bad free in PDF viewer.
  - High CVE-2013-2865: Various fixes from internal audits, fuzzing and other initiatives. 
  - Medium CVE-2013-2855: Memory corruption in dev tools API.

* Thu May 30 2013 Andrey Cherepanov <cas@altlinux.org> 27.0.1453.93-alt1.r200836
- New version 27.0.1453.93
- Security fixes:
  - High CVE-2013-2836: Various fixes from internal audits, fuzzing and
    other initiatives.
  - High CVE-2013-2837: Use-after-free in SVG.
  - High CVE-2013-2839: Bad cast in clipboard handling.
  - High CVE-2013-2840: Use-after-free in media loader.
  - High CVE-2013-2841: Use-after-free in Pepper resource handling.
  - High CVE-2013-2842: Use-after-free in widget handling.
  - High CVE-2013-2843: Use-after-free in speech handling.
  - High CVE-2013-2844: Use-after-free in style resolution.
  - High CVE-2013-2845: Memory safety issues in Web Audio.
  - High CVE-2013-2846: Use-after-free in media loader.
  - High CVE-2013-2847: Use-after-free race condition with workers.
  - Medium CVE-2013-2848: Possible data extraction with XSS Auditor.
  - Low CVE-2013-2849: Possible XSS with drag+drop or copy+paste.
- Web pages load 5%% faster on average
- New chrome.syncFileSystem API
- Improved ranking of predictions, improved spell correction, and
  numerous fundamental improvements for Omnibox predictions. Please see
  the Help Center for more information on our updated policies.

* Mon May 13 2013 Andrey Cherepanov <cas@altlinux.org> 26.0.1410.57-alt1.r191765
- New version 26.0.1410.57
- Security fixes:
  - High CVE-2013-0927: Unsafe config option loading in Pango.
- Requires new version speech-dispatcher

* Sun Mar 31 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt4.r187217
- Rebuild with libv8-3.15

* Wed Mar 27 2013 Andrey Cherepanov <cas@altlinux.org> 26.0.1410.43-alt1.r189671
- New version 26.0.1410.43
- Security fixes:
  - Medium CVE-2013-0926: Avoid pasting active tags in certain situations.
  - Low CVE-2013-0925: Avoid leaking URLs to extensions without the tabs permissions.
  - Low CVE-2013-0924: Check an extension's permissions API usage again file permissions.
  - Medium CVE-2013-0923: Memory safety issues in the USB Apps API.
  - Low CVE-2013-0922: Avoid HTTP basic auth brute force attempts.
  - High CVE-2013-0921: Ensure isolated web sites run in their own processes.
  - Medium CVE-2013-0920: Use-after-free in extension bookmarks API.
  - Medium CVE-2013-0919: Use-after-free with pop-up windows in extensions.
  - Low CVE-2013-0918: Do not navigate dev tools upon drag and drop.
  - Low CVE-2013-0917: Out-of-bounds read in URL loader.
  - High CVE-2013-0916: Use-after-free in Web Audio.

* Thu Mar 21 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt3.r187217
- Add note that the keys for Google API are only to be used for ALT Linux
- Fix run script if CHROMIUM_ULIMIT is not set in /etc/chromium/default

* Wed Mar 20 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt2.r187217
- Build with access to Google API

* Wed Mar 13 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.172-alt1.r187217
- New version 25.0.1364.172

* Mon Mar 11 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.160-alt1.r186726
- New version 25.0.1364.160
- Security fixes:
  - CVE-2013-0912: Type confusion in WebKit.
- Build with system libpng12 (old version)

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.152-alt1.r185281
- New version 25.0.1364.152
- Security fixes:
  - High CVE-2013-0902: Use-after-free in frame loader.
  - High CVE-2013-0903: Use-after-free in browser navigation handling.
  - High CVE-2013-0904: Memory corruption in Web Audio.
  - High CVE-2013-0905: Use-after-free with SVG animations.
  - High CVE-2013-0906: Memory corruption in Indexed DB.
  - Medium CVE-2013-0907: Race condition in media thread handling.
  - Medium CVE-2013-0908: Incorrect handling of bindings for extension processes.
  - Low CVE-2013-0909: Referer leakage with XSS Auditor.
  - Medium CVE-2013-0910: Mediate renderer -> browser plug-in loads more strictly.
  - High CVE-2013-0911: Possible path traversal in database handling.
- Use builtin libpng

* Fri Feb 22 2013 Andrey Cherepanov <cas@altlinux.org> 25.0.1364.97-alt1.r183676
- New version 25.0.1364.97
- Security fixes:
  - High CVE-2013-0879: Memory corruption with web audio node.
  - High CVE-2013-0880: Use-after-free in database handling.
  - Medium CVE-2013-0881: Bad read in Matroska handling.
  - High CVE-2013-0882: Bad memory access with excessive SVG parameters.
  - Medium CVE-2013-0883: Bad read in Skia.
  - Low CVE-2013-0884: Inappropriate load of NaCl.
  - Medium CVE-2013-0885: Too many API permissions granted to web store.
  - Low CVE-2013-0887: Developer tools process has too many permissions
    and places too much trust in the connected server.
  - Medium CVE-2013-0888: Out-of-bounds read in Skia.
  - Low CVE-2013-0889: Tighten user gesture check for dangerous file
    downloads.
  - High CVE-2013-0890: Memory safety issues across the IPC layer.
  - High CVE-2013-0891: Integer overflow in blob handling.
  - Medium CVE-2013-0892: Lower severity issues across the IPC layer.
  - Medium CVE-2013-0893: Race condition in media handling.
  - High CVE-2013-0894: Buffer overflow in vorbis decoding.
  - High CVE-2013-0895: Incorrect path handling in file copying.
  - High CVE-2013-0896: Memory management issues in plug-in message
    handling.
  - Low CVE-2013-0897: Off-by-one read in PDF.
  - High CVE-2013-0898: Use-after-free in URL handling.
  - Low CVE-2013-0899: Integer overflow in Opus handling.
  - Medium CVE-2013-0900: Race condition in ICU.

* Thu Jan 31 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.57-alt1.r178923
- New version 24.0.1312.57
- Remove revision number from tarball name

* Wed Jan 23 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.56-alt1.r177594
- New version 24.0.1312.56
- Security fixes:
  - High CVE-2013-0839: Use-after-free in canvas font handling.
  - Medium CVE-2013-0840: Missing URL validation when opening new windows.
  - High CVE-2013-0841: Unchecked array index in content blocking.
  - Medium CVE-2013-0842: Problems with NULL characters embedded in paths.

* Mon Jan 14 2013 Andrey Cherepanov <cas@altlinux.org> 24.0.1312.52-alt1.r175374
- New version 24.0.1312.52
- Security fixes:
  - High CVE-2012-5145: Use-after-free in SVG layout.
  - High CVE-2012-5146: Same origin policy bypass with malformed URL.
  - High CVE-2012-5147: Use-after-free in DOM handling.
  - Medium CVE-2012-5148: Missing filename sanitization in hyphenation support.
  - High CVE-2012-5149: Integer overflow in audio IPC handling.
  - High CVE-2012-5150: Use-after-free when seeking video.
  - High CVE-2012-5151: Integer overflow in PDF JavaScript.
  - Medium CVE-2012-5152: Out-of-bounds read when seeking video.
  - High CVE-2012-5156: Use-after-free in PDF fields.
  - Medium CVE-2012-5157: Out-of-bounds reads in PDF image handling.
  - High CVE-2013-0828: Bad cast in PDF root handling.
  - High CVE-2013-0829: Corruption of database metadata leading to incorrect file access.
  - Low CVE-2013-0831: Possible path traversal from extension process.
  - Medium CVE-2013-0832: Use-after-free with printing.
  - Medium CVE-2013-0833: Out-of-bounds read with printing.
  - Medium CVE-2013-0834: Out-of-bounds read with glyph handling.
  - Low CVE-2013-0835: Browser crash with geolocation.
  - Medium CVE-2013-0837: Crash in extension tab handling.
  - Low CVE-2013-0838: Tighten permissions on shared memory segments.
- Fixes:
  - Add new option CHROMIUM_ULIMIT in /etc/chromium/default for increase
    for example maximum number of open file descriptors ("-n 1024"
    is recommended for many opened tabs) if needed.

* Wed Dec 12 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.97-alt1.r171054
- New version 23.0.1271.97
- Security fixes:
  - High CVE-2012-5139: Use-after-free with visibility events.
  - High CVE-2012-5140: Use-after-free in URL loader.
  - Medium CVE-2012-5141: Limit Chromoting client plug-in instantiation.
  - Critical CVE-2012-5142: Crash in history navigation.
  - Medium CVE-2012-5143: Integer overflow in PPAPI image buffers.
  - High CVE-2012-5144: Stack corruption in AAC decoding.
- Fixes:
  - Some texts in a Website Settings popup are trimmed
  - <input> selection renders white text on white bg in apps
  - some plugins stopped working

* Fri Nov 30 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.95-alt1.r169798
- New version 23.0.1271.95
- Security fixes:
  - High CVE-2012-5138: Incorrect file path handling.
  - High CVE-2012-5137: Use-after-free in media source handling.
  - High CVE-2012-5133: Use-after-free in SVG filters.

* Thu Nov 08 2012 Andrey Cherepanov <cas@altlinux.org> 23.0.1271.64-alt1.r165196
- New version 23.0.1271.64
- Fixes:
  - High CVE-2012-5116: Use-after-free in SVG filter handling.
  - High CVE-2012-5121: Use-after-free in video layout.
  - High CVE-2012-5124: Memory corruption in texture handling.
  - Critical CVE-2012-5112: SVG use-after-free and IPC arbitrary file
    write.
  - High CVE-2012-2900: Crash in Skia text rendering.
  - Critical CVE-2012-5108: Race condition in audio device handling.
  - High CVE-2012-2896: Integer overflow in WebGL
  - High CVE-2012-2895: Out-of-bounds writes in PDF viewer.
  - High CVE-2012-2894: Crash in graphics context handling.
  - High CVE-2012-2893: Double free in XSL transforms.
  - High CVE-2012-2890: Use-after-free in PDF viewer.
  - High CVE-2012-2889: UXSS in frame handling.
  - High CVE-2012-2888: Use-after-free in SVG text references.
  - High CVE-2012-2887: Use-after-free in onclick handling.
  - High CVE-2012-2886: UXSS in v8 bindings.
  - High CVE-2012-2883: Out-of-bounds write in Skia.
  - High CVE-2012-2882: Wild pointer in OGG container handling.
  - High CVE-2012-2881: DOM tree corruption with plug-ins.
  - High CVE-2012-2878: Use-after-free in plug-in handling.
  - High CVE-2012-2876: Buffer overflow in SSE2 optimizations.
  - High CVE-2012-2874: Out-of-bounds write in Skia.
- Total move to system v8
- Use builtin icu-4.6 and patched zlib (see http://code.google.com/p/chromium/issues/detail?id=143623)

* Wed Oct 03 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt4.r154005
- Set flags for build on ARM
- Rebuild with new version of v8

* Tue Oct 02 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt3.r154005
- Enable video and audio support in HTML5

* Thu Sep 13 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt2.r154005
- Disable debug version and fix problem with Google accounts (ALT 27731)
- Build with system icu libraries
- Open blank initial tab and distribution start page
- Add ALT-specific initial bookmarks

* Fri Sep 07 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.89-alt1.r154005
- New version 21.0.1180.89
- Fixes:
  - Several Pepper Flash fixes (Issue 140577, 144107, 140498, 142479)
  - Microphone issues with tinychat.com (Issue: 143192)
  - Devtools regression with "save as" of edited source (issue: 141180)
  - Mini ninjas shaders fails (Issue: 142705)
  - Page randomly turns red/green gradient boxes (Issue: 110343)
  - Medium CVE-2012-2865: Out-of-bounds read in line breaking.
  - High CVE-2012-2866: Bad cast with run-ins.
  - Low CVE-2012-2867: Browser crash with SPDY.
  - Medium CVE-2012-2868: Race condition with workers and XHR.
  - High CVE-2012-2869: Avoid stale buffer in URL loading.
  - Low CVE-2012-2870: Lower severity memory management issues in XPath.
  - High CVE-2012-2871: Bad cast in XSL transforms.
  - Medium CVE-2012-2872: XSS in SSL interstitial.
- Export patches and flags from Debian
- Disable tcmalloc

* Fri Aug 24 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1180.81-alt1.r151980
- New version 21.0.1180.81
- Disable plugin installation
- Fix tcmalloc because glibc 2.16 removed the undocumented definition of
  'struct siginfo' from <bits/siginfo.h>

* Wed Aug 15 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt5.r139751
- Set appropriate desktop file name for default browser check

* Mon Aug 13 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt4.r139751
- Fix crash when displaying system print dialog on Linux
  (http://code.google.com/p/chromium/issues/detail?id=130095)
- Rename .desktop file and add localization strings

* Fri Aug 10 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt3.r139751
- Add missing file chrome_sandbox

* Thu Aug 09 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt2.r139751
- Rename DE specific packages and set appropriate requirement to wallet subsystem
- Set alternatives to chromium-kde and chromium-gnome
- Add default parameters support in /etc/chromium/default

* Wed Aug 08 2012 Andrey Cherepanov <cas@altlinux.org> 21.0.1158.0-alt1.r139751
- Build for Sisyphus version 21.0.1158.0 (import from SUSE)
- Rename to chromium

