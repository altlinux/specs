%define browser_ppapi_plugins_path %_libdir/pepper-plugins
%brp_strip_none %_bindir/*
%brp_strip_none %browser_ppapi_plugins_path/*
%set_verify_elf_method textrel=relaxed
%def_enable include_x86_64
%def_disable flash_props

Name: adobe-flash-player-ppapi
%define bin_name ppapi-plugin-adobe-flash
%define ver_fake   23
%define ver_ix86   23.0.0.162
%define ver_x86_64 23.0.0.162
Release: alt2
Serial: 3

%define ver_real %ver_fake
%ifarch x86_64
%define ver_real %ver_x86_64
%endif
%ifarch %ix86
%define ver_real %ver_ix86
%endif
Version: %ver_fake

Group: Networking/WWW
Summary: Adobe Flash Player
URL: http://www.adobe.com/products/flashplayer/
License: Adobe

ExclusiveArch: %ix86 x86_64

BuildRequires: libstdc++-devel glibc-devel desktop-file-utils

Source: ppapi-plugin-adobe-flash.desktop
#
Source10: flash_player_ppapi-x86_64-%ver_x86_64.tar
Source11: flash_player_ppapi-x86-%ver_ix86.tar

%description
Adobe Flash Player %version (Macromedia Flash)
Fully Supported: Mozilla 1.0+, Netscape 7.x, Firefox 0.8+
Partially Supported: Opera, Konqueror 3.x

See the distribution license in
 http://www.adobe.com/legal/licenses-terms.html

%package -n %bin_name
Version: %ver_real
Group: Networking/WWW
Summary: Adobe Flash Player
Requires: libcurl /usr/bin/xdg-open
#Provides: flash-plugin = %version-%release
#Obsoletes: flash-plugin <= %version
Provides: update-pepperflash = 1.9
Obsoletes: update-pepperflash < 1.9
%description -n %bin_name
Adobe Flash Player %version (Macromedia Flash)
Fully Supported: Mozilla 1.0+, Netscape 7.x, Firefox 0.8+
Partially Supported: Opera, Konqueror 3.x

See the distribution license in
  http://www.adobe.com/legal/licenses-terms.html

%package fake
Version: %ver_fake
Group: Networking/WWW
Summary: fake
%description fake
fake


%prep
%setup -Tqcn flash_player_ppapi_%{version}_linux
%ifarch x86_64
%if_enabled include_x86_64
tar xfv %SOURCE10
%endif
%else
tar xfv %SOURCE11
%endif


%build

%install
mkdir -p -m 0755 %buildroot/%browser_ppapi_plugins_path
%ifarch x86_64
%if_enabled include_x86_64
install -m 0644 libpepflashplayer.so %buildroot/%browser_ppapi_plugins_path
%endif
%else
install -m 0644 libpepflashplayer.so %buildroot/%browser_ppapi_plugins_path
%endif

%if_enabled flash_props
# install flash-player-properties
mkdir -p %buildroot/{%_bindir,%_desktopdir,%_miconsdir,%_niconsdir,%_liconsdir}
install -m0755 ./%_bindir/flash-player-properties %buildroot/%_bindir/
desktop-file-install -m 0644 --dir %buildroot/%_desktopdir \
    --add-category=X-PersonalSettings \
    --remove-key=NotShowIn \
    ./%_desktopdir/flash-player-properties.desktop
for icondir in %_miconsdir %_niconsdir %_liconsdir
do
    install -m 0644 ./$icondir/flash-player-properties.png %buildroot/$icondir/
done
%endif

# menu
mkdir -p -m0755 %buildroot/%_desktopdir
install -m0644 %SOURCE0 %buildroot/%_desktopdir/

%ifarch x86_64
%if_disabled include_x86_64
%post -n %bin_name
echo "At this moment no x86 version of %name"
%endif
%endif

%files -n %bin_name
%if_enabled flash_props
%_bindir/flash-player-properties
%_desktopdir/flash-player-properties.desktop
%_iconsdir/hicolor/*/apps/flash-player-properties.*
%endif
#
%ifarch x86_64
%if_enabled include_x86_64
%browser_ppapi_plugins_path/*
%_desktopdir/ppapi-plugin-adobe-flash.desktop
%endif
%else
%browser_ppapi_plugins_path/*
%_desktopdir/ppapi-plugin-adobe-flash.desktop
%endif

%changelog
* Mon Sep 26 2016 Sergey V Turchin <zerg@altlinux.org> 3:23-alt2
- obsolete update-pepperflash

* Wed Sep 21 2016 Sergey V Turchin <zerg@altlinux.org> 3:23-alt1
- initial build
