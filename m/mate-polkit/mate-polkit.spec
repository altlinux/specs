%define _libexecdir %_prefix/libexec

Name: mate-polkit
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: Integrates polkit authentication for MATE desktop
License: GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common intltool libappindicator-gtk3-devel libpolkit-devel

%description
Integrates polkit with the MATE Desktop environment

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-accountsservice \
	--enable-appindicator

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README
%_sysconfdir/xdg/autostart/polkit-mate-authentication-agent-1.desktop
%_libexecdir/polkit-mate-authentication-agent-1

%changelog
* Thu Mar 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
