Name: caffeine
Version: 2.8.2
Release: alt2.1
Summary: Prevent screensaving and powersaving
Group: Graphical desktop/Other
License: GPLv3
Url: https://launchpad.net/%name
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://launchpad.net/%name/%version/+download/caffeine_%version.tar.gz
BuildRequires(pre):  rpm-build-python3
BuildRequires: python3-devel python3 perl-Net-DBus perl-Encode
BuildArch: noarch
Requires: python3-module-xlib
Requires: python3-module-pyxdg
#Requires: python3-module-notify
Requires: python-module-appindicator
#Requires: python3-module-pygnome-gconf

%description
Caffeine is a small daemon that prevents the desktop from becoming idle (and
hence the screen saver and/or blanker from activating) when the active
window is full-screen.

%description -l ru_RU.UTF-8
Caffeine - маленькая служба, которая блокирует активацию скринсейвера и переход
компьютера в ждущий режим, когда активное окно находится в полноэкранном режиме.

%prep
%setup -n caffeine_%version

%build
%python3_build

%install
%python3_install
%find_lang %name-indicator

%files -f %name-indicator.lang
%doc COPYING COPYING.LESSER README
%_sysconfdir/xdg/autostart/%name.desktop
%_bindir/*
%_man1dir/*.1.xz
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*
%_pixmapsdir/*
%python3_sitelibdir/*
%_datadir/%name-indicator/glade/GUI.glade

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Anton Midyukov <antohami@altlinux.org> 2.8.2-alt2
- Fix build.

* Sat Sep 19 2015 Anton Midyukov <antohami@altlinux.org> 2.8.2-alt1
- Initial build for ALT Linux Sisyphus.
