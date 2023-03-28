#------------------------------------------------------------------------------
#   browser.spec
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#   Prologue information
#------------------------------------------------------------------------------
Summary: Yandex Browser
License: ALT-YANDEX-BROWSER
Name: yandex-browser-stable
Version: 23.1.2.1033
Release: alt1
Group: Networking/WWW
Vendor: YANDEX LLC
Url: http://browser.yandex.ru/

ExclusiveArch: x86_64
Source0: x86_64-linux.tar.gz
Source1: common.tar.gz
Patch0: yandex-browser-stable-proxy-from-environment.patch
Provides: yandex-browser = %{version}
Buildrequires: at-spi2-atk, libalsa, libat-spi2-core, libatk, libcairo, libcups
Buildrequires: libdbus, libdrm, libexpat, libgbm, libgio, libnspr, libnss
Buildrequires: libpango, libX11, libXcomposite, libXdamage, libXext, libXfixes
Buildrequires: libXrandr, libxcb, libxkbcommon
Buildrequires: libwayland-client
Buildrequires: libqt5-core, libqt5-widgets, libqt5-gui
Requires: ca-certificates,ffmpeg-plugin-browser, xdg-utils, fonts-ttf-google-noto-emoji-color
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
%patch0 -p0

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

#partner config
maybe_create_dir() {
  if [ ! -d "$1" ]; then
    mkdir -p "$1"
  fi
}
store_partner_file() {
  if [ -z "$1" ]; then
    local source_file="%{_builddir}/%{name}-%{version}/%{_libdir}/yandex/browser/$2"
  else
    local source_file="%{_builddir}/%{name}-%{version}/%{_libdir}/yandex/browser/$1/$2"
  fi
  local destination_dir="%buildroot%{_localstatedir}/yandex/browser/$1"
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
  local source_dir="%{_builddir}/%{name}-%{version}/%{_libdir}/yandex/browser/$1"
  local destination_dir="%buildroot%{_localstatedir}/yandex/browser/$1"
  maybe_create_dir "${destination_dir}"
  find "${source_dir}" -maxdepth 1 -type f -name "$2" -exec cp -f {} "${destination_dir}" \;
}
store_partner_data() {
  local partner_config="%{_builddir}/%{name}-%{version}/%{_libdir}/yandex/browser/partner_config"
  if [ -f "${partner_config}" ]; then
    remove_partner_storage
    store_partner_file "" "partner_config"
    store_partner_file "" "distrib_info"
    store_partner_file "" "initial_preferences"
    store_partner_file "" "master_preferences"
    store_partner_file "Extensions" "external_extensions.json"
    store_partner_files "resources" "tablo*"
    store_partner_files "resources" "*.png"
    store_partner_files "resources" "*.svg"
    store_partner_files "resources/wallpapers" "*"
  fi
}
store_partner_data

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
* Mon Mar 20 2023 yabro <yabro@altlinux.org> 23.1.2.1033-alt1
 - browser updated to 23.1.2
 - High CVE-2022-4436: Use after free in Blink Media.
 - High CVE-2022-4437: Use after free in Mojo IPC.
 - High CVE-2022-4438: Use after free in Blink Frames.
 - High CVE-2022-4439: Use after free in Aura.
 - Medium CVE-2022-4440: Use after free in Profiles.
 - High CVE-2022-4262: Type Confusion in V8.
 - High CVE-2022-4174: Type Confusion in V8.
 - High CVE-2022-4175: Use after free in Camera Capture.
 - High CVE-2022-4176: Out of bounds write in Lacros Graphics.
 - High CVE-2022-4177: Use after free in Extensions.
 - High CVE-2022-4178: Use after free in Mojo.
 - High CVE-2022-4179: Use after free in Audio.
 - High CVE-2022-4180: Use after free in Mojo.
 - High CVE-2022-4181: Use after free in Forms.
 - Medium CVE-2022-4182: Inappropriate implementation in Fenced Frames.
 - Medium CVE-2022-4183: Insufficient policy enforcement in Popup Blocker.
 - Medium CVE-2022-4184: Insufficient policy enforcement in Autofill.
 - Medium CVE-2022-4185: Inappropriate implementation in Navigation.
 - Medium CVE-2022-4186: Insufficient validation of untrusted input in Downloads.
 - Medium CVE-2022-4187: Insufficient policy enforcement in DevTools.
 - Medium CVE-2022-4188: Insufficient validation of untrusted input in CORS.
 - Medium CVE-2022-4189: Insufficient policy enforcement in DevTools.
 - Medium CVE-2022-4190: Insufficient data validation in Directory.
 - Medium CVE-2022-4191: Use after free in Sign-In.
 - Medium CVE-2022-4192: Use after free in Live Caption.
 - Medium CVE-2022-4193: Insufficient policy enforcement in File System API.
 - Medium CVE-2022-4194: Use after free in Accessibility.
 - Medium CVE-2022-4195: Insufficient policy enforcement in Safe Browsing.
 - High CVE-2022-4135: Heap buffer overflow in GPU.
 - High CVE-2022-3885: Use after free in V8.
 - High CVE-2022-3886: Use after free in Speech Recognition.
 - High CVE-2022-3887: Use after free in Web Workers.
 - High CVE-2022-3888: Use after free in WebCodecs.
 - High CVE-2022-3889: Type Confusion in V8.
 - High CVE-2022-3890: Heap buffer overflow in Crashpad.
 - High CVE-2022-3723: Type Confusion in V8.
 - High CVE-2022-3652: Type Confusion in V8.
 - High CVE-2022-3653: Heap buffer overflow in Vulkan.
 - High CVE-2022-3654: Use after free in Layout.
 - Medium CVE-2022-3655: Heap buffer overflow in Media Galleries.
 - Medium CVE-2022-3656: Insufficient data validation in File System.
 - Medium CVE-2022-3657: Use after free in Extensions.
 - Medium CVE-2022-3658: Use after free in Feedback service on Chrome OS.
 - Medium CVE-2022-3659: Use after free in Accessibility.
 - Medium CVE-2022-3660: Inappropriate implementation in Full screen mode.
 - Low CVE-2022-3661: Insufficient data validation in Extensions.

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
