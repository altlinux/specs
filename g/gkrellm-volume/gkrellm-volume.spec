%define plugin volume

Name: gkrellm-%plugin
Version: 2.1.13
Release: alt1.1
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: GKrellM volume control plugin
Summary(ru_RU.KOI8-R): Плагин GKrellM для регулирования громкости
License: GPL
Group: Monitoring
Url: http://gkrellm.luon.net/volume.phtml

Source: http://gkrellm.luon.net/files/%name-%version.tar.bz2
Patch: gkrellm-volume-2.1.11-alt-makefile.patch

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Tue Nov 11 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel pkgconfig libalsa-devel

%description
This GKrellM plugin allows you to control the volume of the mixer devices
supported by your soundcard.

%description -l ru_RU.KOI8-R
Этот плагин GKrellM поможет вам управлять громкостью устройств микшера,
поддерживаемых звуковой картой.

%prep
%setup -q -n %name
%patch -p0

%build
%make_build enable_alsa=1 enable_nls=1 CFLAGS="$RPM_OPT_FLAGS" LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %name

%files -f %name.lang
%doc Changelog README THEMING
%_libdir/gkrellm2/plugins/%plugin.so

%changelog
* Tue Sep 01 2009 L.A. Kostis <lakostis@altlinux.ru> 2.1.13-alt1.1
- NMU: enable alsa.

* Thu Oct 14 2004 Grigory Batalov <bga@altlinux.ru> 2.1.13-alt1
- 2.1.13

* Thu May 20 2004 Grigory Batalov <bga@altlinux.ru> 2.1.11-alt1
- 2.1.11

* Tue Nov 11 2003 Grigory Batalov <bga@altlinux.ru> 2.1.9-alt1
- 2.1.9

* Wed Jul 09 2003 Grigory Batalov <bga@altlinux.ru> 2.1.8-alt1
- 2.1.8
- ru.po updated

* Sun Dec 29 2002 Grigory Batalov <bga@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Mon Oct 28 2002 Grigory Batalov <bga@altlinux.ru> 2.1.4-alt1
- 2.1.4
- New i18n patch made

* Fri May 17 2002 Grigory Batalov <bga@altlinux.ru> 0.8-alt4
- Group changed to GKrellM's one
- Small specfile changes

* Sat Nov 24 2001 Grigory Batalov <bga@altlinux.ru> 0.8-alt3
- More localization fixes

* Wed Nov 21 2001 Grigory Batalov <bga@altlinux.ru> 0.8-alt2
- Fixed localization patch

* Mon Nov 19 2001 Grigory Batalov <bga@altlinux.ru> 0.8-alt1
- Built for ALTLinux
- Russian localization patch
