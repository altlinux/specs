Name: xfce4-multiload-nandhp-plugin
Version: 0.3
Release: alt1
License: GPLv2
Summary: System Load Monitor for the Xfce Panel
Summary(ru_RU.UTF-8): Системный монитор нагрузки на систему для панели Xfce
Url: https://github.com/nandhp/multiload-nandhp/
Group: Graphical desktop/XFce
Packager: Anton Midyukov <antohami@altlinux.org>
Source: multiload-nandhp-version-0-3.tar.gz
# Automatically added by buildreq on Sat Sep 05 2015
# optimized out: fontconfig fontconfig-devel glib2-devel gnu-config libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libwayland-client libwayland-server libxfce4util-devel perl-Encode pkg-config xorg-xproto-devel
BuildRequires: intltool libgtop-devel libxfce4panel-devel libxfce4ui-devel

%description
A system load monitor that graphs processor, memory, and swap space use,
plus network and disk activity.

It is a port of the GNOME multiload applet to the Xfce panel.

%description -l ru_RU.UTF-8
Монитор нагрузки на систему с графами: процессор, память и своп, плюс сеть
и дисковая активность.

Это порт апплета GNOME для Xfce панели.

%prep
%setup -n multiload-nandhp-version-0-3

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std
%find_lang multiload-nandhp

%files -f multiload-nandhp.lang
%doc AUTHORS COPYING README.md
%_libdir/xfce4/panel/plugins/libmultiload.so
%_datadir/xfce4/panel/plugins/multiload.desktop

%changelog
* Sat Sep 05 2015 Anton Midyukov <antohami@altlinux.org> 0.3-alt1
- Initial build for ALT Linux Sisyphus.
