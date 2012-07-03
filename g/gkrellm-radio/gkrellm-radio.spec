%define plugin radio

Name: gkrellm-%plugin
Version: 2.0.4
Release: alt3
Packager: Roman Savochenko <rom_as at altlinux.ru>

Summary: GKrellM radio tuners control plugin
Summary(ru_RU.UTF-8): Плагин GKrellM для управления радиоприёмником
License: GPL
Group: Monitoring
Url: http://gkrellm.luon.net/gkrellm-radio.phtml

Source: http://gkrellm.luon.net/files/%name-%version.tar.bz2
Source1: 20-radio.rules
Patch0: %name-V4L2.patch

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Tue Nov 11 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel liblirc-devel libpango-devel pkgconfig

%description
This plugin allows your to turn your radio card on/off and tune to
channels.

%description -l ru_RU.UTF-8
Этот плагин GKrellM позволяет включать/выключать радио и переключать
станции.

%prep
%setup -q -n %name
%patch0 -p1
#%patch1 -p1
#%patch2 -p0

%build
%make_build WITH_LIRC=1 enable_nls=1 LOCALEDIR=%_datadir/locale

%install
mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %name
install -m 644 -pD %SOURCE1 %buildroot%_sysconfdir/udev/rules.d/20-radio.rules

%files -f %name.lang
%doc CHANGES README lirc.example
%_libdir/gkrellm2/plugins/%plugin.so
%_sysconfdir/udev/rules.d/*

%changelog
* Sun Jun 19 2011 Roman Savochenko <rom_as@altlinux.ru> 2.0.4-alt3
- V4L2 integration patch is created and included.

* Wed Jan 26 2011 Roman Savochenko <rom_as@altlinux.ru> 2.0.4-alt2
- Udev rule file 20-radio.rules is added to /etc/udev/rules.d/ for link creation from /dev/radio to /dev/radio0 for last kernels for Sisyphus.

* Tue Nov 11 2003 Grigory Batalov <bga@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Sun May 04 2003 Grigory Batalov <bga@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Sun Dec 29 2002 Grigory Batalov <bga@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Dec 09 2002 Grigory Batalov <bga@altlinux.ru> 2.0.1-alt1
- Initial build for ALT Linux
- I18n and ru.po patches