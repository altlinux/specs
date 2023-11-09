%ifndef _userunitdir
%define _userunitdir %_prefix/lib/systemd/user
%endif

Name: xdg-user-dirs
Version: 0.18
Release: alt2
Summary: Handles user special directories
Group: Graphical desktop/Other
License: GPLv2+ and MIT
Url: http://freedesktop.org/wiki/Software/xdg-user-dirs

Source0: http://user-dirs.freedesktop.org/releases/%name-%version.tar.gz
Source1: xdg-user-dirs.sh
Source2: xdg-user-dirs.control
Source10: xdg-user-dirs.service
Patch1: user-dirs-fix-encoding-0.13-alt.patch
Patch2: xdg-user-dirs-0.14-alt-home.patch
Patch3: user-dirs-update-fix-0.13-alt.patch

BuildRequires: xsltproc docbook-style-xsl

%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%prep
%setup
%patch1 -p2
%patch2 -p1

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot%_x11sysconfdir/profile.d
mkdir -p %buildroot%_controldir/
mkdir -p %buildroot%_controldir/
mkdir -p %buildroot%_userunitdir/
install -p -m 755 %SOURCE1 %buildroot%_x11sysconfdir/profile.d
install -p -m 755 %SOURCE2 %buildroot%_controldir/xdg-user-dirs
install -p -m 0644 %SOURCE10 %buildroot/%_userunitdir/xdg-user-dirs.service
%find_lang %name

%post
%post_control -s disabled xdg-user-dirs
SYSTEMCTL=systemctl
if [ $1 = 1 ] && "$SYSTEMCTL" --version >/dev/null 2>&1; then
    $SYSTEMCTL -q --global enable %name.service >/dev/null 2>&1 || :
fi

%pre
%pre_control xdg-user-dirs

%preun
SYSTEMCTL=systemctl
if [ $1 = 0 ] && "$SYSTEMCTL" --version >/dev/null 2>&1; then
    $SYSTEMCTL -q --global disable %name.service >/dev/null 2>&1 || :
fi

%triggerin -- %name < 0.18-alt2
SYSTEMCTL=systemctl
if "$SYSTEMCTL" --version >/dev/null 2>&1; then
    $SYSTEMCTL -q --global enable %name.service >/dev/null 2>&1 || :
fi

%files -f %name.lang
%doc NEWS AUTHORS README
%_bindir/*
%config(noreplace) %_sysconfdir/xdg/user-dirs.conf
%config(noreplace) %_sysconfdir/xdg/user-dirs.defaults
%_x11sysconfdir/profile.d/*
%_userunitdir/xdg-user-dirs.service
%_controldir/*
%_man1dir/*user-dir*
%_man5dir/*user-dir*

%changelog
* Wed Nov 08 2023 Anton Midyukov <antohami@altlinux.org> 0.18-alt2
- clear Packager
- xdg-user-dirs.service: install to graphical-session-pre.target
- enable xdg-user-dirs.service when first install

* Thu Oct 12 2023 Sergey V Turchin <zerg@altlinux.org> 0.18-alt1
- new version
- add systemd user service

* Thu Oct 21 2021 Andrey Cherepanov <cas@altlinux.org> 0.17-alt2
- Move Picture, Misic, Images subdirectories from Documents directory.

* Wed Oct 09 2019 Sergey V Turchin <zerg@altlinux.org> 0.17-alt1
- new version

* Thu Feb 02 2017 Sergey V Turchin <zerg@altlinux.org> 0.14-alt1.M80P.1
- build for M80P

* Wed Feb 01 2017 Sergey V Turchin <zerg@altlinux.org> 0.14-alt2
- Add option for alternate home directory

* Fri Feb 17 2012 Radik Usupov <radik@altlinux.org> 0.14-alt1
- New version (0.14)

* Fri Feb 18 2011 Radik Usupov <radik@altlinux.org> 0.13-alt4
- The correct update for the directory Documents (thanks dkr@!)

* Tue Feb 15 2011 Radik Usupov <radik@altlinux.org> 0.13-alt3
- Fixed script name (thanks ender@ and shrek@!)

* Sun Feb 13 2011 Radik Usupov <radik@altlinux.org> 0.13-alt2
- changed the default user directories
- changed packager
- use locale instead of utf (thanks thresh@!)
- added xdg-user-dirs.sh script (thanks thresh@!) (Closes: 23975)
- added control (thanks ender@!)

* Mon Jan 10 2011 Radik Usupov <radik@altlinux.org> 0.13-alt1
- new version

* Mon Aug 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10-alt1
- initial release

