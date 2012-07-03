Name: conky
Version: 1.8.1
Release: alt3

%def_enable lua
%def_enable ncurses
%def_disable audacious
%def_enable mpd
%def_enable moc
%def_enable nvidia
%def_enable wlan
%def_enable alsa
%def_enable eve
%def_enable rss
%def_enable weather_metar
%def_enable weather_xoap
%def_enable imlib2
%def_enable lua_imlib2
%def_enable lua_cairo

%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

Summary: lightweight graphical system monitor
Summary(ru_RU.UTF-8): Легковесный графический системный монитор
License: GPLv3 with various free software licenses (see COPYING)
Group: Monitoring
URL: http://conky.sourceforge.net/

Source: %name-%version.tar
Source1: conky-dotfiles.tar.bz2

# Automatically added by buildreq on Tue Jul 07 2009
BuildRequires: glib2-devel libXdamage-devel libXext-devel libXft-devel xsltproc zlib-devel

%if_enabled lua
BuildPreReq: liblua5-devel
%endif

%if_enabled ncurses
BuildPreReq: ncurses-devel
%endif

%if_enabled audacious
BuildPreReq: libaudacious-devel
%endif

%if_enabled nvidia
BuildPreReq: nvidia-settings-devel
%endif

%if_enabled wlan
BuildPreReq: libwireless-devel
%endif

%if_enabled alsa
BuildPreReq: libalsa-devel
%endif

%if_enabled eve
BuildPreReq: libcurl-devel
%endif

%if_enabled rss
BuildPreReq: libcurl-devel libxml2-devel
%endif

%if_enabled weather_metar
BuildPreReq: libcurl-devel libxml2-devel
%endif

%if_enabled weather_xoap
BuildPreReq: libcurl-devel libxml2-devel
%endif

%if_enabled imlib2
BuildPreReq: imlib2-devel
%endif

%if_enabled lua_imlib2
BuildPreReq: liblua5-devel tolua++-devel imlib2-devel
%endif

%if_enabled lua_cairo
BuildPreReq: liblua5-devel tolua++-devel libcairo-devel
%endif

%description
Conky is a program which can display arbitrary information (such as
the date, CPU temperature from i2c, MPD info, and anything else you
desire) to the root window in X11.

%description -l ru_RU.UTF-8
Conky - это утилита, позволяющая отображать произвольную информацию
(такую как текущая дата, температура процессора, статус проигрывателя
mpd, и т.д.) в окне графической системы X11.

Данная утилита настраивается в чрезвычайно широких пределах (для
примера, см. снимки экрана на http://conky.sf.net) и совсем не
требовательна к ресурсам компьютера.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-xft \
	%{subst_enable lua} \
	%{subst_enable ncurses} \
	%{subst_enable curl} \
	%{subst_enable audacious} \
	%{subst_enable mpd} \
	%{subst_enable moc} \
	%{subst_enable nvidia} \
	%{subst_enable wlan} \
	%{subst_enable alsa} \
	%{subst_enable eve} \
	%{subst_enable rss} \
	%{subst_enable_to weather_metar weather-metar} \
	%{subst_enable_to weather_xoap weather-xoap} \
	%{subst_enable imlib2} \
	%{subst_enable_to lua_imlib2 lua-imlib2} \
	%{subst_enable_to lua_cairo lua-cairo} \
	--enable-ibm \
	--enable-double-buffer \
	--disable-static

%make_build

%install
install -p -m644 %SOURCE1 ./
%makeinstall_std

%files
%doc COPYING conky-dotfiles.tar.bz2 doc/config_settings.html doc/variables.html doc/docs.html
%if_enabled lua
%doc doc/lua.html
%endif
%_bindir/*
%_man1dir/*
%_libdir/%name
%exclude %_libdir/%name/libimlib2.la
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/%name.conf
%config %_sysconfdir/%name/%{name}_no_x11.conf

%changelog
* Sun Jul 17 2011 Egor Vyscrebentsov <evyscr@altlinux.org> 1.8.1-alt3
- dropped curl/types.h from headers includes
- built with lua-cairo

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.1-alt2
- fix build

* Tue Jan 18 2011 Egor Vyscrebentsov <evyscr@altlinux.org> 1.8.1-alt1
- new version: 1.8.1

* Thu Sep 02 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 1.8.0-alt2
- built with imlib2 and lua-imlib2 (altbug #23926)
- fixed configure weather parameters

* Sun Apr 04 2010 Egor Vyscrebentsov <evyscr@altlinux.org> 1.8.0-alt1
- new version: 1.8.0
- enable most of options (altbug #23274)

* Tue Jul 07 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.7.1.1-alt1
- Version update.

* Tue Dec 18 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 1.4.9-alt1
- new version: 1.4.9
  + number of bugfixes

* Sat Mar 17 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 1.4.5-alt1
- new version: 1.4.5

* Thu Sep 01 2005 Nick S. Grechukh <gns@altlinux.ru> 1.3.0-alt0.1
- initial build for ALTLinux Sisyphus
