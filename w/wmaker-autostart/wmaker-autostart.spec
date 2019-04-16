Name: wmaker-autostart
Version: 0.1
Release: alt1
Summary: Autostart application for WindowMaker
Summary(ru_RU.UTF-8): Автозапуск программ WindowMaker
License: GPL
Group: Graphical desktop/Window Maker
Url: http://git.altlinux.org

BuildArch: noarch
AutoReq: no

%description
Autostart application for WindowMaker

%description -l ru_RU.UTF-8
Автозапуск программ WindowMaker

%package polkit-gnome
Group: Graphical desktop/Window Maker
Summary: autostart polkit-gnome for WindowMaker
Summary(ru_RU.UTF-8): автозапуск polkit-gnome для WindowMaker
Requires: WindowMaker polkit-gnome
AutoReq: no

%description polkit-gnome
autostart polkit-gnome for WindowMaker
%description -l ru_RU.UTF-8 polkit-gnome
автозапуск polkit-gnome для WindowMaker

%install
mkdir -p %buildroot%_datadir/WindowMaker/autostart.d

echo '/usr/libexec/polkit-1/polkit-gnome-authentication-agent-1 &' > \
%buildroot%_datadir/WindowMaker/autostart.d/polkit-gnome

chmod 755 %buildroot%_datadir/WindowMaker/autostart.d/polkit-gnome

%files polkit-gnome
%_datadir/WindowMaker/autostart.d/polkit-gnome

%changelog
* Tue Apr 16 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- initial build
