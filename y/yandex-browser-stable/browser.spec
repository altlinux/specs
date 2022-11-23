#------------------------------------------------------------------------------
#   browser.spec
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#   Prologue information
#------------------------------------------------------------------------------
Summary: Yandex Browser
License: ALT-YANDEX-BROWSER
Name: yandex-browser-stable
Version: 22.11.0.2485
Release: alt1
Group: Networking/WWW
Vendor: YANDEX LLC
Url: http://browser.yandex.ru/

ExclusiveArch: x86_64
Source0: x86_64-linux.tar.gz
Source1: common.tar.gz
Provides: yandex-browser = %{version}
Buildrequires: at-spi2-atk, libalsa, libat-spi2-core, libatk, libcairo, libcups
Buildrequires: libdbus, libdrm, libexpat, libgbm, libgio, libnspr, libnss
Buildrequires: libpango, libX11, libXcomposite, libXdamage, libXext, libXfixes
Buildrequires: libXrandr, libxcb, libxkbcommon
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
    echo "%{_builddir} appears to be incorrectly set - aborting"
    exit 1
fi

if [ -z "%{_builddir}/%{name}-%{version}" -o ! \
     -d "%{_builddir}/%{name}-%{version}/%{_libdir}/yandex/browser" ] ; then
    echo "%{_builddir} appears to be incorrectly set - aborting"
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
install -m 644 "%{_builddir}/%{name}-%{version}/%{_libdir}/yandex/browser/partner_config" \
      "%buildroot/%{_libdir}/yandex/browser/partner_config_static"

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

remove_yandex_update_store() {
  local update_store="/var/lib/yandex-browser"
  if [ -d "${update_store}" ]; then
    rm -rf "${update_store}"
    echo "removed ${update_store}"
  fi
}

if [ "$1" -eq "0" ]; then
  remove_yandex_update_store
fi

exit 0
# =============== END preun ===============

%changelog
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
