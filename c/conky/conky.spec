%define subst_buildoption() %{expand:-DBUILD_%(echo %{1} |sed 's/./\\U&/g')=%%{?_enable_%{1}:ON}%%{?_disable_%{1}:OFF}}

%define luaver 5.4

%def_enable argb
%def_disable audacious
%def_enable cmus
%def_enable curl
%def_enable docs
%def_enable hddtemp
%def_enable http
%def_enable ibm
%def_enable ical
%def_enable iconv
%def_enable imlib2
%def_enable iostats
%def_enable ipv6
%def_enable irc
%def_enable lua
%def_enable lua_cairo
%def_enable lua_imlib2
%def_enable lua_rsvg
%def_enable math
%def_enable moc
%def_enable mpd
%def_disable mysql
%def_enable ncurses
%def_enable nvidia
%def_enable old_config
%def_enable pulseaudio
%def_enable rss
%def_enable wayland
%def_enable wlan
%def_enable xdamage
%def_enable xdbe
%def_enable xft
%def_enable xinerama
%def_disable xmms2
%def_enable xshape

Name: conky
Version: 1.18.1
Release: alt1

Summary: lightweight graphical system monitor
Summary(ru_RU.UTF-8): Легковесный графический системный монитор
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT
Group: Monitoring
Url: http://conky.sourceforge.net/

VCS: git://github.com/brndnmtthws/conky.git
Source: %name-%version.tar
Source1: conky-dotfiles.tar.bz2
Source99: conky.watch

# git://git.altlinux.org/gears/c/conky.git
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake gcc-c++ rpm-build-vim
BuildRequires: glibc-devel lua%luaver-devel python3-module-yaml libpcre2-devel python3-module-jinja2

%{?_enable_audacious:BuildRequires: libaudacious-devel}
%{?_enable_curl:BuildRequires: libcurl-devel}
%{?_enable_docs:BuildRequires: man-db pandoc}
%{?_enable_ical:BuildRequires: libical-devel}
%{?_enable_imlib2:BuildRequires: imlib2-devel}
%{?_enable_irc:BuildRequires: libircclient-devel}
%{?_enable_http:BuildRequires: libmicrohttpd-devel}
%{?_enable_lua_cairo:BuildRequires: lua%luaver-devel libcairo-devel}
%{?_enable_lua_imlib2:BuildRequires: lua%luaver-devel imlib2-devel}
%{?_enable_lua_rsvg:BuildRequires: lua%luaver-devel librsvg-devel}
%{?_enable_ncurses:BuildRequires: ncurses-devel}
%{?_enable_nvidia:BuildRequires: nvidia-settings-devel}
%{?_enable_pulseaudio:BuildRequires: libpulseaudio-devel}
%{?_enable_rss:BuildRequires: libcurl-devel libxml2-devel}
%{?_enable_wayland:BuildRequires: libpango-devel libwayland-client-devel libwayland-server-devel wayland-protocols}
%{?_enable_wlan:BuildRequires: libwireless-devel}
%{?_enable_xdamage:BuildRequires: libXdamage-devel}
%{?_enable_xft:BuildRequires: libXft-devel}
%{?_enable_xinerama:BuildRequires: libXinerama-devel}

%package -n vim-plugin-conky
BuildArch: noarch
Summary: VIm syntax plugin for conky config file
Group: Editors

%description
Conky is a program which can display arbitrary information (such as
the date, CPU temperature from i2c, MPD info, and anything else you
desire) to the root window in X11.

%description -l ru_RU.UTF-8
Conky - это утилита, позволяющая отображать произвольную информацию
(такую как текущая дата, температура процессора, статус проигрывателя
mpd, и т.д.) в окне графической системы X11.

Данная утилита настраивается в чрезвычайно широких пределах и совсем не
требовательна к ресурсам компьютера.

%description -n vim-plugin-conky
VIm syntax plugin for conky config file.

%prep
%setup
%autopatch -p1
sed -i 's,@LUA_VERSION@,%luaver,' extras/convert.lua

%build
%cmake \
	-DRELEASE=True \
	-DBUILD_SHARED_LIBS=OFF \
	%{subst_buildoption argb} \
	%{subst_buildoption audacious} \
	%{subst_buildoption cmus} \
	%{subst_buildoption curl} \
	%{subst_buildoption docs} \
	%{subst_buildoption hddtemp} \
	%{subst_buildoption http} \
	%{subst_buildoption ibm } \
	%{subst_buildoption ical} \
	%{subst_buildoption iconv} \
	%{subst_buildoption imlib2} \
	%{subst_buildoption iostats} \
	%{subst_buildoption ipv6} \
	%{subst_buildoption irc} \
	%{subst_buildoption lua_cairo} \
	%{subst_buildoption lua_imlib2} \
	%{subst_buildoption lua_rsvg} \
	%{subst_buildoption math} \
	%{subst_buildoption moc} \
	%{subst_buildoption mpd} \
	%{subst_buildoption mysql} \
	%{subst_buildoption ncurses} \
	%{subst_buildoption nvidia} \
	%{subst_buildoption old_config} \
	%{subst_buildoption pulseaudio} \
	%{subst_buildoption rss} \
	%{subst_buildoption wayland} \
	%{subst_buildoption wlan} \
	%{subst_buildoption xdamage } \
	%{subst_buildoption xdbe } \
	%{subst_buildoption xft} \
	%{subst_buildoption xinerama} \
	%{subst_buildoption xmms2} \
	%{subst_buildoption xshape} \
	#

%cmake_build

%install
install -p -m644 %SOURCE1 ./
%cmakeinstall_std

# install config files
mkdir -p %buildroot%_sysconfdir/conky
install -m644 -p data/conky.conf data/conky_no_x11.conf %buildroot%_sysconfdir/conky

# install config converter
mkdir -p %buildroot/usr/libexec/conky
install -m755 -p extras/convert.lua %buildroot/usr/libexec/conky

# install vim plugins
mkdir -p %buildroot%vim_runtime_dir
cp -a extras/vim/ftdetect %buildroot%vim_runtime_dir
cp -a extras/vim/syntax %buildroot%vim_runtime_dir
mv %buildroot%vim_runtime_dir/syntax/conkyrc.vim{.j2,}

# remove static libs
rm %buildroot%_libdir/libtcp-portmon.a

%files
%doc AUTHORS COPYING LICENSE LICENSE.BSD README.md
%doc conky-dotfiles.tar.bz2

%_bindir/conky
/usr/libexec/conky/convert.lua
%if_enabled lua_cairo || lua_imlib2 || lua_rsvg
%_libdir/conky
%endif
%{?_enable_docs:%_man1dir/conky.1*}

%dir %_sysconfdir/conky
%config %_sysconfdir/conky/conky.conf
%config %_sysconfdir/conky/conky_no_x11.conf

%_desktopdir/conky.desktop
%_iconsdir/hicolor/scalable/apps/conky-logomark-violet.svg

%files -n vim-plugin-conky
%vim_runtime_dir/ftdetect/conkyrc.vim
%vim_runtime_dir/syntax/conkyrc.vim

%changelog
* Sat Feb 25 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.1-alt1
- Updated to 1.18.1.

* Mon Jan 02 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.17.0-alt1
- Updated to 1.17.0.
- Enabled Wayland support.

* Tue Dec 27 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.1-alt1
- Updated to 1.16.1.

* Sat Sep 24 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.13.1.0.7.git54672876-alt1
- Updated to v1.13.1-7-g54672876.

* Sat Jul 16 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.12.2-alt3
- Fixed FTBFS: changed lua-devel to lua5.3-devel in the BR.

* Fri Mar 18 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.12.2-alt2
- Fixed conky.watch.
- Cleaned up gear repo.

* Fri Apr 30 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.12.2-alt1
- Updated to 1.12.2.
- Updated conky.watch.

* Fri Mar 12 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.12.1-alt1
- Updated to 1.12.1.
- Built against libmicrohttpd on %%ix86 and armh.
- Actually fixed conky window crawling (forgot applied patch in the previous
  release).

* Mon Feb 01 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.11.6-alt2
- Fixed FTBFS against libmicrohttpd, do not build against libmicrohttpd on
  %%ix86 and armh.
- Fixed conky window crawling (thx george@).

* Tue Dec 15 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.11.6-alt1
- Updated to 1.11.6.
- Packed converter to new config format.
- Built with support of the various additional options.
- Built VIm syntax plugin.
- Do not build and package HTML documentation.
- Updated watch file.
- Cleaned up spec and fixed license field.

* Wed Nov 14 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.9.0-alt2
- fixed apcupsd support (ALT#32298)

* Wed May 16 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.9.0-alt1.1
- e2k: rebuilt with explicit lua5.1 BR

* Wed Oct 30 2013 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

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
