%define browser_ppapi_plugins_path %_libdir/pepper-plugins
%define browser_ppapi_plugins_path2 /usr/lib/pepperflashplugin-nonfree
%brp_strip_none %_bindir/*
%brp_strip_none %browser_ppapi_plugins_path/*
%set_verify_elf_method textrel=relaxed
%def_enable include_x86_64
%def_disable flash_props

Name: adobe-flash-player-ppapi
%define bin_name ppapi-plugin-adobe-flash
%define ver_fake   28
%define ver_ix86   28.0.0.126
%define ver_x86_64 28.0.0.126
Release: alt1%ubt
Epoch: 3

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

BuildRequires(pre): rpm-build-ubt
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
Provides: flash-player-ppapi = %version-%release
Obsoletes: flash-player-ppapi <= %version
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
mkdir -p -m 0755 %buildroot/%browser_ppapi_plugins_path2
%ifarch x86_64
%if_enabled include_x86_64
install -m 0644 libpepflashplayer.so %buildroot/%browser_ppapi_plugins_path
ln -s `relative %browser_ppapi_plugins_path/libpepflashplayer.so %browser_ppapi_plugins_path2/libpepflashplayer.so`  %buildroot/%browser_ppapi_plugins_path2/libpepflashplayer.so
%endif
%else
install -m 0644 libpepflashplayer.so %buildroot/%browser_ppapi_plugins_path
ln -s `relative %browser_ppapi_plugins_path/libpepflashplayer.so %browser_ppapi_plugins_path2/libpepflashplayer.so`  %buildroot/%browser_ppapi_plugins_path2/libpepflashplayer.so
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
%dir %browser_ppapi_plugins_path2
%ifarch x86_64
%if_enabled include_x86_64
%browser_ppapi_plugins_path/*
%browser_ppapi_plugins_path2/*
%_desktopdir/ppapi-plugin-adobe-flash.desktop
%endif
%else
%browser_ppapi_plugins_path/*
%browser_ppapi_plugins_path2/*
%_desktopdir/ppapi-plugin-adobe-flash.desktop
%endif

%changelog
* Mon Dec 25 2017 Sergey V Turchin <zerg@altlinux.org> 3:28-alt1%ubt
- new version (ALT#34369)
- security fixes:
  CVE-2017-3114, CVE-2017-3112, CVE-2017-11225, CVE-2017-11215,
  CVE-2017-11213, CVE-2017-11305

* Mon Oct 30 2017 Sergey V Turchin <zerg@altlinux.org> 3:27-alt3%ubt
- new version
- security fixes: CVE-2017-11292

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 3:27-alt2%ubt
- package /usr/lib/pepperflashplugin-nonfree directory

* Thu Sep 21 2017 Sergey V Turchin <zerg@altlinux.org> 3:27-alt1%ubt
- new version
- security fixes: CVE-2017-11281, CVE-2017-11282

* Thu Aug 17 2017 Sergey V Turchin <zerg@altlinux.org> 3:26-alt2%ubt
- new version
- security fixes: CVE-2017-3085, CVE-2017-3106

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 3:26-alt1%ubt
- new version
- security fixes:
  CVE-2017-3075, CVE-2017-3081, CVE-2017-3083, CVE-2017-3084,
  CVE-2017-3076, CVE-2017-3077, CVE-2017-3078, CVE-2017-3079,
  CVE-2017-3082

* Wed May 10 2017 Sergey V Turchin <zerg@altlinux.org> 3:25-alt3%ubt
- new version
- security fixes:
  CVE-2017-3068, CVE-2017-3069, CVE-2017-3070, CVE-2017-3071,
  CVE-2017-3072, CVE-2017-3073, CVE-2017-3074

* Wed Apr 19 2017 Sergey V Turchin <zerg@altlinux.org> 3:25-alt2%ubt
- new version
- security fixes:
  CVE-2017-3058, CVE-2017-3059, CVE-2017-3060, CVE-2017-3061,
  CVE-2017-3062, CVE-2017-3063, CVE-2017-3064

* Mon Mar 20 2017 Sergey V Turchin <zerg@altlinux.org> 3:25-alt1%ubt
- new version
- security fixes:
  CVE-2017-2997, CVE-2017-2998, CVE-2017-2999, CVE-2017-3000,
  CVE-2017-3001, CVE-2017-3002, CVE-2017-3003

* Fri Feb 17 2017 Sergey V Turchin <zerg@altlinux.org> 3:24-alt3
- new version
- security fixes:
  CVE-2017-2982, CVE-2017-2984, CVE-2017-2985, CVE-2017-2986,
  CVE-2017-2987, CVE-2017-2988, CVE-2017-2990, CVE-2017-2991,
  CVE-2017-2992, CVE-2017-2993, CVE-2017-2994, CVE-2017-2995,
  CVE-2017-2996

* Wed Jan 11 2017 Sergey V Turchin <zerg@altlinux.org> 3:24-alt2
- new version
- security fixes:
  CVE-2017-2925, CVE-2017-2926, CVE-2017-2927, CVE-2017-2928,
  CVE-2017-2930, CVE-2017-2931, CVE-2017-2932, CVE-2017-2933,
  CVE-2017-2934, CVE-2017-2935, CVE-2017-2936, CVE-2017-2937,
  CVE-2017-2938

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 3:24-alt1
- new version
- security fixes:
  CVE-2016-7867, CVE-2016-7868, CVE-2016-7869, CVE-2016-7870,
  CVE-2016-7871, CVE-2016-7872, CVE-2016-7873, CVE-2016-7874,
  CVE-2016-7875, CVE-2016-7876, CVE-2016-7877, CVE-2016-7878,
  CVE-2016-7879, CVE-2016-7880, CVE-2016-7881, CVE-2016-7890,
  CVE-2016-7892

* Wed Nov 09 2016 Sergey V Turchin <zerg@altlinux.org> 3:23-alt7
- new version
- security fixes:
  CVE-2016-7857, CVE-2016-7858, CVE-2016-7859, CVE-2016-7860,
  CVE-2016-7861, CVE-2016-7862, CVE-2016-7863, CVE-2016-7864,
  CVE-2016-7865

* Sun Nov 06 2016 Sergey V Turchin <zerg@altlinux.org> 3:23-alt6
- add /usr/lib/pepperflashplugin-nonfree/libpepflashplayer.so symlink (ALT#32721)

* Thu Oct 27 2016 Sergey V Turchin <zerg@altlinux.org> 3:23-alt5
- new version
- security fixes: CVE-2016-7855

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 3:23-alt4
- new version
- security fixes:
  CVE-2016-4273, CVE-2016-4286, CVE-2016-6981, CVE-2016-6982,
  CVE-2016-6983, CVE-2016-6984, CVE-2016-6985, CVE-2016-6986,
  CVE-2016-6987, CVE-2016-6989, CVE-2016-6990, CVE-2016-6992

* Thu Sep 29 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3:23-alt3
- Revered previous change.

* Mon Sep 26 2016 Sergey V Turchin <zerg@altlinux.org> 3:23-alt2
- obsolete update-pepperflash

* Wed Sep 21 2016 Sergey V Turchin <zerg@altlinux.org> 3:23-alt1
- initial build
