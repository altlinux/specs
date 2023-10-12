#------------------------------------------------------------------------------
#   browser.spec
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#   Prologue information
#------------------------------------------------------------------------------
Summary: Yandex Browser
License: ALT-YANDEX-BROWSER
Name: yandex-browser-stable
Version: 23.9.1.1033
Release: alt1
Group: Networking/WWW
Vendor: YANDEX LLC
Url: http://browser.yandex.ru/

ExclusiveArch: x86_64
Source0: x86_64-linux.tar.gz
Source1: common.tar.gz
Provides: yandex-browser = %{version}
Provides: webclient
Buildrequires: at-spi2-atk, libalsa, libat-spi2-core, libatk, libcairo, libcups
Buildrequires: libdbus, libdrm, libexpat, libgbm, libgio, libnspr, libnss
Buildrequires: libpango, libX11, libXcomposite, libXdamage, libXext, libXfixes
Buildrequires: libXrandr, libxcb, libxkbcommon
Buildrequires: libwayland-client
Buildrequires: libqt5-core, libqt5-widgets, libqt5-gui
Requires: ca-certificates, ffmpeg-plugin-browser, gst-libav, gst-plugins-bad, gst-plugins-base, gst-plugins-good, gstreamer, xdg-utils, fonts-ttf-google-noto-emoji-color
Requires(post): %{_sbindir}/update-alternatives
Requires(preun): %{_sbindir}/update-alternatives


# The prefix is pretty important; RPM uses this to figure out
# how to make a package relocatable

# =============== END Prologue ===============

#------------------------------------------------------------------------------
#   Description
#------------------------------------------------------------------------------
%Description
The web browser from Yandex

Yandex Browser is a browser that combines a minimal design with sophisticated technology to make the web faster, safer, and easier.

#------------------------------------------------------------------------------
#   Prep rule - Prepare sources before build
#------------------------------------------------------------------------------
%prep
%setup -c
%setup -T -D -a 1

#------------------------------------------------------------------------------
#   Build rule - How to make the package
#------------------------------------------------------------------------------
%build

# =============== END build ===============

#------------------------------------------------------------------------------
#       Installation rule - how to install it (note that it
#   gets installed into a temp directory given by %buildroot)
#------------------------------------------------------------------------------
%install
# TODO(palar): remove it when libabt-bindings.so is fixed
%set_verify_elf_method textrel=relaxed
%add_findreq_skiplist %_libdir/yandex/browser/xdg-*

if [ -z "%{_builddir}/%{name}-%{version}" -o ! \
     -d "%{_builddir}/%{name}-%{version}" ] ; then
    exit 1
fi

if [ -z "%{_builddir}/%{name}-%{version}" -o ! \
     -d "%{_builddir}/%{name}-%{version}/%{_libdir}/yandex/browser" ] ; then
    exit 1
fi

install -m 755 -d \
  "%buildroot/usr"
# This is hard coded for now
cp -a "%{_builddir}/%{name}-%{version}/usr/" "%buildroot/"

if [ -d "%{_builddir}/%{name}-%{version}%{_sysconfdir}/" ]; then
  install -m 755 -d \
    "%buildroot%{_sysconfdir}"
  cp -a "%{_builddir}/%{name}-%{version}%{_sysconfdir}/" "%buildroot/"
fi

# install icons
for size in 16 24 32 48 64 128 256; do
  install -Dm644 "%{_builddir}/%{name}-%{version}/%{_libdir}/yandex/browser/product_logo_$size.png" \
    "%buildroot/%_iconsdir/hicolor/${size}x${size}/apps/yandex-browser.png"
done

# Set alternative to xbrowser
mkdir -p -- %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xbrowser       %_bindir/%name  150
%_bindir/x-www-browser  %_bindir/%name  150
EOF

# =============== END install ===============

#------------------------------------------------------------------------------
#   Rule to clean up a build
#------------------------------------------------------------------------------
%clean

# =============== END clean ===============

#------------------------------------------------------------------------------
#   Files listing.
#------------------------------------------------------------------------------
%files
%defattr(-,root,root)
#%doc README

# We cheat and just let RPM figure it out for us; everything we install
# should go under this prefix anyways.
%{_libdir}/yandex/browser
%attr(4711,root,root) %{_libdir}/yandex/browser/yandex_browser-sandbox

%{_sysconfdir}/xdg/autostart/yandex-browser_user_setup.desktop
%{_bindir}/yandex-browser-stable
%{_datadir}/appdata/yandex-browser.appdata.xml
%{_datadir}/applications/yandex-browser.desktop
%{_datadir}/gnome-control-center/default-apps/yandex-browser.xml
%_altdir/%name
%_iconsdir/hicolor/*/apps/*.png
%docdir %{_mandir}/man1
%{_mandir}/man1/yandex-browser.1.xz
%{_mandir}/man1/yandex-browser-stable.1.xz

# =============== END files ===============
#------------------------------------------------------------------------------
#   Post installation script
#------------------------------------------------------------------------------
%post
#partner config
maybe_create_dir() {
  if [ ! -d "$1" ]; then
    mkdir -p "$1"
  fi
}
store_partner_file() {
  if [ -z "$1" ]; then
    local source_file="%{_libdir}/yandex/browser/$2"
  else
    local source_file="%{_libdir}/yandex/browser/$1/$2"
  fi
  local destination_dir="%{_localstatedir}/yandex/browser/$1"
  if [ -f "${source_file}" ]; then
    maybe_create_dir "${destination_dir}"
    cp -f "${source_file}" "${destination_dir}"
  fi
}
remove_partner_storage() {
  local partner_storage_dir="%{_localstatedir}/yandex/browser"
  if [ -d "${partner_storage_dir}" ]; then
    rm -rf "${partner_storage_dir}"
  fi
}
store_partner_files() {
  local source_dir="%{_libdir}/yandex/browser/$1"
  local destination_dir="%{_localstatedir}/yandex/browser/$1"
  maybe_create_dir "${destination_dir}"
  find "${source_dir}" -maxdepth 1 -type f -name "$2" -exec cp -f {} "${destination_dir}" \;
}
store_partner_data() {
  local partner_config="%{_libdir}/yandex/browser/partner_config"
  if [ -f "${partner_config}" ]; then
    remove_partner_storage
    store_partner_file "" "partner_config"
    store_partner_file "" "distrib_info"
    store_partner_file "" "master_preferences"
    store_partner_file "Extensions" "external_extensions.json"
    store_partner_files "resources" "clids*.xml"
    store_partner_files "resources" "tablo*"
    store_partner_files "resources" "*.png"
    store_partner_files "resources" "*.svg"
    store_partner_files "resources/wallpapers" "*"
  fi
}
store_partner_data
exit 0
# =============== END post ===============

#------------------------------------------------------------------------------
#   Pre uninstallation script
#------------------------------------------------------------------------------
%preun

remove_partner_storage() {
  local partner_storage_dir="%{_localstatedir}/yandex/browser"
  if [ -d "${partner_storage_dir}" ]; then
    rm -rf "${partner_storage_dir}"
  fi
}
if [ "$1" -eq "0" ]; then
  remove_partner_storage
fi
exit 0
# =============== END preun ===============

%changelog

* Tue Oct 11 2023 yabro <yabro@altlinux.org> 23.9.1.1033-alt1
- Browser updated to 23.9.1.1033

* Tue Oct 10 2023 yabro <yabro@altlinux.org> 23.9.1.1015-alt1
- Browser updated to 23.9.1.1015
 + Critical CVE-2023-4863: Heap buffer overflow in WebP.
 + High CVE-2023-2312: Use after free in Offline.
 + High CVE-2023-3727: Use after free in WebRTC.
 + High CVE-2023-3730: Use after free in Tab Groups.
 + High CVE-2023-3732: Out of bounds memory access in Mojo.
 + High CVE-2023-4068: Type Confusion in V8.
 + High CVE-2023-4069: Type Confusion in V8.
 + High CVE-2023-4070: Type Confusion in V8.
 + High CVE-2023-4071: Heap buffer overflow in Visuals.
 + High CVE-2023-4072: Out of bounds read and write in WebGL.
 + High CVE-2023-4073: Out of bounds memory access in ANGLE.
 + High CVE-2023-4074: Use after free in Blink Task Scheduling.
 + High CVE-2023-4075: Use after free in Cast.
 + High CVE-2023-4076: Use after free in WebRTC.
 + High CVE-2023-4349: Use after free in Device Trust Connectors.
 + High CVE-2023-4350: Inappropriate implementation in Fullscreen.
 + High CVE-2023-4351: Use after free in Network.
 + High CVE-2023-4352: Type Confusion in V8.
 + High CVE-2023-4353: Heap buffer overflow in ANGLE.
 + High CVE-2023-4354: Heap buffer overflow in Skia.
 + High CVE-2023-4355: Out of bounds memory access in V8.
 + High CVE-2023-4427: Out of bounds memory access in V8.
 + High CVE-2023-4428: Out of bounds memory access in CSS.
 + High CVE-2023-4429: Use after free in Loader.
 + High CVE-2023-4430: Use after free in Vulkan.
 + High CVE-2023-4572: Use after free in MediaStream.
 + High CVE-2023-4761: Out of bounds memory access in FedCM.
 + High CVE-2023-4762: Type Confusion in V8.
 + High CVE-2023-4763: Use after free in Networks.
 + High CVE-2023-4764: Incorrect security UI in BFCache.
 + High CVE-2023-5186: Use after free in Passwords.
 + High CVE-2023-5187: Use after free in Extensions.
 + High CVE-2023-5217: Heap buffer overflow in vp8 encoding in libvpx.
 + High CVE-2023-5346: Type Confusion in V8.
 + Medium CVE-2023-3733: Inappropriate implementation in WebApp Installs.
 + Medium CVE-2023-3734: Inappropriate implementation in Picture In Picture.
 + Medium CVE-2023-3735: Inappropriate implementation in Web API Permission Prompts.
 + Medium CVE-2023-3736: Inappropriate implementation in Custom Tabs.
 + Medium CVE-2023-3737: Inappropriate implementation in Notifications.
 + Medium CVE-2023-3738: Inappropriate implementation in Autofill.
 + Medium CVE-2023-4077: Insufficient data validation in Extensions.
 + Medium CVE-2023-4078: Inappropriate implementation in Extensions.
 + Medium CVE-2023-4356: Use after free in Audio.
 + Medium CVE-2023-4357: Insufficient validation of untrusted input in XML.
 + Medium CVE-2023-4358: Use after free in DNS.
 + Medium CVE-2023-4359: Inappropriate implementation in App Launcher.
 + Medium CVE-2023-4360: Inappropriate implementation in Color.
 + Medium CVE-2023-4361: Inappropriate implementation in Autofill.
 + Medium CVE-2023-4362: Heap buffer overflow in Mojom IDL.
 + Medium CVE-2023-4363: Inappropriate implementation in WebShare.
 + Medium CVE-2023-4364: Inappropriate implementation in Permission Prompts.
 + Medium CVE-2023-4365: Inappropriate implementation in Fullscreen.
 + Medium CVE-2023-4366: Use after free in Extensions.
 + Medium CVE-2023-4367: Insufficient policy enforcement in Extensions API.
 + Medium CVE-2023-4368: Insufficient policy enforcement in Extensions API.
 + Medium CVE-2023-4431: Out of bounds memory access in Fonts.
 + Medium CVE-2023-4900: Inappropriate implementation in Custom Tabs.
 + Medium CVE-2023-4901: Inappropriate implementation in Prompts.
 + Medium CVE-2023-4902: Inappropriate implementation in Input.
 + Medium CVE-2023-4903: Inappropriate implementation in Custom Mobile Tabs.
 + Medium CVE-2023-4904: Insufficient policy enforcement in Downloads.
 + Medium CVE-2023-4905: Inappropriate implementation in Prompts.
 + Low CVE-2023-3740: Insufficient validation of untrusted input in Themes.
 + Low CVE-2023-4906: Insufficient policy enforcement in Autofill.
 + Low CVE-2023-4907: Inappropriate implementation in Intents.
 + Low CVE-2023-4908: Inappropriate implementation in Picture in Picture.
 + Low CVE-2023-4909: Inappropriate implementation in Interstitials.

* Tue Sep 5 2023 yabro <yabro@altlinux.org> 23.7.4.983-alt1
- Browser updated to 23.7.4.983

* Mon Aug 7 2023 yabro <yabro@altlinux.org> 23.7.1.1216-alt1
- Browser updated to 23.7.1.1216
  + Critical CVE-2023-2721: Use after free in Navigation.
  + High CVE-2023-2722: Use after free in Autofill UI.
  + High CVE-2023-2723: Use after free in DevTools.
  + High CVE-2023-2724: Type Confusion in V8.
  + High CVE-2023-2725: Use after free in Guest View.
  + High CVE-2023-2929: Out of bounds write in Swiftshader.
  + High CVE-2023-2930: Use after free in Extensions.
  + High CVE-2023-2931: Use after free in PDF.
  + High CVE-2023-2932: Use after free in PDF.
  + High CVE-2023-2933: Use after free in PDF.
  + High CVE-2023-2934: Out of bounds memory access in Mojo.
  + High CVE-2023-2935: Type Confusion in V8.
  + High CVE-2023-2936: Type Confusion in V8.
  + High CVE-2023-3079: Type Confusion in V8.
  + High CVE-2023-3420: Type Confusion in V8.
  + High CVE-2023-3421: Use after free in Media.
  + High CVE-2023-3422: Use after free in Guest View.
  + High CVE-2023-3598: Out of bounds read and write in ANGLE.
  + Medium CVE-2023-2459: Inappropriate implementation in Prompts.
  + Medium CVE-2023-2460: Insufficient validation of untrusted input in Extensions.
  + Medium CVE-2023-2461: Use after free in OS Inputs.
  + Medium CVE-2023-2462: Inappropriate implementation in Prompts.
  + Medium CVE-2023-2463: Inappropriate implementation in Full Screen Mode.
  + Medium CVE-2023-2464: Inappropriate implementation in PictureInPicture.
  + Medium CVE-2023-2465: Inappropriate implementation in CORS.
  + Medium CVE-2023-2726: Inappropriate implementation in WebApp Installs.
  + Medium CVE-2023-2937: Inappropriate implementation in Picture In Picture.
  + Medium CVE-2023-2938: Inappropriate implementation in Picture In Picture.
  + Medium CVE-2023-2939: Insufficient data validation in Installer.
  + Medium CVE-2023-2940: Inappropriate implementation in Downloads.
  + Low CVE-2023-2466: Inappropriate implementation in Prompts.
  + Low CVE-2023-2467: Inappropriate implementation in Prompts.
  + Low CVE-2023-2468: Inappropriate implementation in PictureInPicture.
  + Low CVE-2023-2941: Inappropriate implementation in Extensions API.

* Wed Jun 21 2023 yabro <yabro@altlinux.org> 23.5.1.793-alt1
- Browser updated to 23.5.1.793
  + Critical CVE-2023-3214: Use after free in Autofill payments
  + High CVE-2023-3215: Use after free in WebRTC
  + High CVE-2023-3216: Type Confusion in V8
  + High CVE-2023-3217: Use after free in WebXR

* Wed Jun 7 2023 yabro <yabro@altlinux.org> 23.5.1.753-alt1
- Browser updated to 23.5.1.753

* Wed May 31 2023 yabro <yabro@altlinux.org> 23.5.1.659-alt1
- Browser updated to 23.5.1.659
  + High CVE-2023-2133: Out of bounds memory access in Service Worker API.
  + High CVE-2023-2134: Out of bounds memory access in Service Worker API.
  + High CVE-2023-2135: Use after free in DevTools.
  + High CVE-2023-2136: Integer overflow in Skia.
  + Medium CVE-2023-2137: Heap buffer overflow in sqlite.
  + High CVE-2023-2033: Type Confusion in V8.
  + High CVE-2023-1810: Heap buffer overflow in Visuals.
  + High CVE-2023-1811: Use after free in Frames.
  + Medium CVE-2023-1812: Out of bounds memory access in DOM Bindings.
  + Medium CVE-2023-1813: Inappropriate implementation in Extensions.
  + Medium CVE-2023-1814: Insufficient validation of untrusted input in Safe Browsing.
  + Medium CVE-2023-1815: Use after free in Networking APIs.
  + Medium CVE-2023-1816: Incorrect security UI in Picture In Picture.
  + Medium CVE-2023-1817: Insufficient policy enforcement in Intents.
  + Medium CVE-2023-1818: Use after free in Vulkan.
  + Medium CVE-2023-1819: Out of bounds read in Accessibility.
  + Medium CVE-2023-1820: Heap buffer overflow in Browser History.
  + Low CVE-2023-1821: Inappropriate implementation in WebShare.
  + Low CVE-2023-1822: Incorrect security UI in Navigation.
  + Low CVE-2023-1823: Inappropriate implementation in FedCM.
  + High CVE-2023-1528: Use after free in Passwords.
  + High CVE-2023-1529: Out of bounds memory access in WebHID.
  + High CVE-2023-1530: Use after free in PDF.
  + High CVE-2023-1531: Use after free in ANGLE.
  + High CVE-2023-1532: Out of bounds read in GPU Video.
  + High CVE-2023-1533: Use after free in WebProtect.
  + High CVE-2023-1534: Out of bounds read in ANGLE.
  + High CVE-2023-1213: Use after free in Swiftshader.
  + High CVE-2023-1214: Type Confusion in V8.
  + High CVE-2023-1215: Type Confusion in CSS.
  + High CVE-2023-1216: Use after free in DevTools.
  + High CVE-2023-1217: Stack buffer overflow in Crash reporting.
  + High CVE-2023-1218: Use after free in WebRTC.
  + High CVE-2023-1219: Heap buffer overflow in Metrics.
  + High CVE-2023-1220: Heap buffer overflow in UMA.
  + Medium CVE-2023-1221: Insufficient policy enforcement in Extensions API.
  + Medium CVE-2023-1222: Heap buffer overflow in Web Audio API.
  + Medium CVE-2023-1223: Insufficient policy enforcement in Autofill.
  + Medium CVE-2023-1224: Insufficient policy enforcement in Web Payments API.
  + Medium CVE-2023-1225: Insufficient policy enforcement in Navigation.
  + Medium CVE-2023-1226: Insufficient policy enforcement in Web Payments API.
  + Medium CVE-2023-1227: Use after free in Core.
  + Medium CVE-2023-1228: Insufficient policy enforcement in Intents.
  + Medium CVE-2023-1229: Inappropriate implementation in Permission prompts.
  + Medium CVE-2023-1230: Inappropriate implementation in WebApp Installs.
  + Medium CVE-2023-1231: Inappropriate implementation in Autofill.
  + Low CVE-2023-1232: Insufficient policy enforcement in Resource Timing.
  + Low CVE-2023-1233: Insufficient policy enforcement in Resource Timing.
  + Low CVE-2023-1234: Inappropriate implementation in Intents.
  + Low CVE-2023-1235: Type Confusion in DevTools.
  + Low CVE-2023-1236: Inappropriate implementation in Internals.

* Tue Apr 25 2023 yabro <yabro@altlinux.org> 23.3.1.946-alt1
- Browser updated to 23.3.1.946
  + Critical CVE-2023-2033: Type confusion in V8

* Mon Apr 17 2023 yabro <yabro@altlinux.org> 23.3.1.929-alt1
- Browser updated to 23.3.1.929
- Fix installation of partner data

* Fri Apr 11 2023 yabro <yabro@altlinux.org> 23.3.1.916-alt1
- Browser updated to 23.3.1
  + Critical CVE-2023-0941: Use after free in Prompts.
  + High CVE-2023-0927: Use after free in Web Payments API.
  + High CVE-2023-0928: Use after free in SwiftShader.
  + High CVE-2023-0929: Use after free in Vulkan.
  + High CVE-2023-0930: Heap buffer overflow in Video.
  + High CVE-2023-0931: Use after free in Video.
  + High CVE-2023-0932: Use after free in WebRTC.
  + Medium CVE-2023-0933: Integer overflow in PDF.
  + High CVE-2023-0696: Type Confusion in V8.
  + High CVE-2023-0697: Inappropriate implementation in Full screen mode.
  + High CVE-2023-0698: Out of bounds read in WebRTC.
  + Medium CVE-2023-0699: Use after free in GPU.
  + Medium CVE-2023-0700: Inappropriate implementation in Download.
  + Medium CVE-2023-0701: Heap buffer overflow in WebUI.
  + Medium CVE-2023-0702: Type Confusion in Data Transfer.
  + Medium CVE-2023-0703: Type Confusion in DevTools.
  + Low CVE-2023-0704: Insufficient policy enforcement in DevTools.
  + Low CVE-2023-0705: Integer overflow in Core.
  + High CVE-2023-0471: Use after free in WebTransport.
  + High CVE-2023-0472: Use after free in WebRTC.
  + Medium CVE-2023-0473: Type Confusion in ServiceWorker API.
  + Medium CVE-2023-0474: Use after free in GuestView.
  + High CVE-2023-0128: Use after free in Overview Mode.
  + High CVE-2023-0129: Heap buffer overflow in Network Service.
  + Medium CVE-2023-0130: Inappropriate implementation in Fullscreen API.
  + Medium CVE-2023-0131: Inappropriate implementation in iframe Sandbox.
  + Medium CVE-2023-0132: Inappropriate implementation in Permission prompts.
  + Medium CVE-2023-0133: Inappropriate implementation in Permission prompts.
  + Medium CVE-2023-0134: Use after free in Cart.
  + Medium CVE-2023-0135: Use after free in Cart.
  + Medium CVE-2023-0136: Inappropriate implementation in Fullscreen API.
  + Medium CVE-2023-0137: Heap buffer overflow in Platform Apps.
  + Low CVE-2023-0138: Heap buffer overflow in libphonenumber.
  + Low CVE-2023-0139: Insufficient validation of untrusted input in Downloads.
  + Low CVE-2023-0140: Inappropriate implementation in File System API.
  + Low CVE-2023-0141: Insufficient policy enforcement in CORS.
- Set provides webclient (closes: #43564)

* Mon Mar 20 2023 yabro <yabro@altlinux.org> 23.1.2.1033-alt1
- browser updated to 23.1.2
  + High CVE-2022-4436: Use after free in Blink Media.
  + High CVE-2022-4437: Use after free in Mojo IPC.
  + High CVE-2022-4438: Use after free in Blink Frames.
  + High CVE-2022-4439: Use after free in Aura.
  + Medium CVE-2022-4440: Use after free in Profiles.
  + High CVE-2022-4262: Type Confusion in V8.
  + High CVE-2022-4174: Type Confusion in V8.
  + High CVE-2022-4175: Use after free in Camera Capture.
  + High CVE-2022-4176: Out of bounds write in Lacros Graphics.
  + High CVE-2022-4177: Use after free in Extensions.
  + High CVE-2022-4178: Use after free in Mojo.
  + High CVE-2022-4179: Use after free in Audio.
  + High CVE-2022-4180: Use after free in Mojo.
  + High CVE-2022-4181: Use after free in Forms.
  + Medium CVE-2022-4182: Inappropriate implementation in Fenced Frames.
  + Medium CVE-2022-4183: Insufficient policy enforcement in Popup Blocker.
  + Medium CVE-2022-4184: Insufficient policy enforcement in Autofill.
  + Medium CVE-2022-4185: Inappropriate implementation in Navigation.
  + Medium CVE-2022-4186: Insufficient validation of untrusted input in Downloads.
  + Medium CVE-2022-4187: Insufficient policy enforcement in DevTools.
  + Medium CVE-2022-4188: Insufficient validation of untrusted input in CORS.
  + Medium CVE-2022-4189: Insufficient policy enforcement in DevTools.
  + Medium CVE-2022-4190: Insufficient data validation in Directory.
  + Medium CVE-2022-4191: Use after free in Sign-In.
  + Medium CVE-2022-4192: Use after free in Live Caption.
  + Medium CVE-2022-4193: Insufficient policy enforcement in File System API.
  + Medium CVE-2022-4194: Use after free in Accessibility.
  + Medium CVE-2022-4195: Insufficient policy enforcement in Safe Browsing.
  + High CVE-2022-4135: Heap buffer overflow in GPU.
  + High CVE-2022-3885: Use after free in V8.
  + High CVE-2022-3886: Use after free in Speech Recognition.
  + High CVE-2022-3887: Use after free in Web Workers.
  + High CVE-2022-3888: Use after free in WebCodecs.
  + High CVE-2022-3889: Type Confusion in V8.
  + High CVE-2022-3890: Heap buffer overflow in Crashpad.
  + High CVE-2022-3723: Type Confusion in V8.
  + High CVE-2022-3652: Type Confusion in V8.
  + High CVE-2022-3653: Heap buffer overflow in Vulkan.
  + High CVE-2022-3654: Use after free in Layout.
  + Medium CVE-2022-3655: Heap buffer overflow in Media Galleries.
  + Medium CVE-2022-3656: Insufficient data validation in File System.
  + Medium CVE-2022-3657: Use after free in Extensions.
  + Medium CVE-2022-3658: Use after free in Feedback service on Chrome OS.
  + Medium CVE-2022-3659: Use after free in Accessibility.
  + Medium CVE-2022-3660: Inappropriate implementation in Full screen mode.
  + Low CVE-2022-3661: Insufficient data validation in Extensions.

* Mon Jan 23 2023 Andrey Cherepanov <cas@altlinux.org> 22.11.0.2485-alt1.1
- NMU: supported proxy settings from environment variables (ALT #44983) 
- NMU: FTBFS fix: required libwayland-client

* Wed Nov 23 2022 Vasiliy Tsukanov <palar@altlinux.org> 22.11.0.2485-alt1
- browser updated to 22.11.0

* Wed Nov 2 2022 Vasiliy Tsukanov <palar@altlinux.org> 22.9.3.920-alt1
- browser updated to 22.9.3

* Mon Sep 5 2022 Vasiliy Tsukanov <palar@altlinux.org> 22.7.3.817-alt3
- removed comment at yandex-browser.appdata.xml (closes: 43673)

* Thu Aug 18 2022 Vasiliy Tsukanov <palar@altlinux.org> 22.7.3.817-alt2
- removed built-in xdg-utils deps from the package
- added font with emoji support dependency

* Thu Aug 11 2022 Vasiliy Tsukanov <palar@altlinux.org> 22.7.3.817-alt1
- initial build for ALT
