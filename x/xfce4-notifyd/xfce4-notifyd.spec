Name:           xfce4-notifyd
Version:        0.2.2
Release:        alt3.git20120521
Summary:        Simple notification daemon for Xfce
Summary(ru_RU.UTF-8): Менеджер уведомлений для Xfce

Group:          Graphical desktop/XFce
License:        %gpl2only
URL:            http://spuriousinterrupt.org/projects/xfce4-notifyd
Source0:        %name-%version.tar
Packager: XFCE Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4ui-devel libxfconf-devel libxfce4util-devel
BuildPreReq: libdbus-glib-devel libICE-devel libX11-devel libSM-devel
BuildPreReq: desktop-file-utils
# For exo-csource which is needed wnen for --enable-maintainer-mode
BuildPreReq: libexo-devel

# Automatically added by buildreq on Mon Sep 21 2009
BuildRequires: intltool libglade-devel

Requires:       dbus icon-theme-hicolor
Requires:       notify-send
Obsoletes:      notification-daemon-xfce <= 0.3.7

%description
Xfce4-notifyd is a simple, visually-appealing notification daemon for
Xfce that implements the freedesktop.org desktop notifications
specification.
Features:
* Themable using the GTK+ theming mechanism
* Visually appealing: rounded corners, shaped windows
* Supports transparency and fade effects

%description -l ru_RU.UTF-8
Простой менеджер уведомлений для Xfce работающий по спецификациям
freedesktop.org.
Возможности:
* Наличие встроенного механизма тем
* Поддержка скруглений для углов окон
* Поддержка прозрачности и эффекта скрытия

%prep
%setup
sed -i 's/m4_define(\[%{name}_version_tag\], \[git\])/m4_define(\[%{name}_version_tag\], \[\])/' configure.ac.in

%build
%xfce4reconf
%configure \
    --enable-maintainer-mode \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/xfce4-notifyd-config
%_libdir/xfce4/notifyd/
%_desktopdir/*.desktop
%_datadir/dbus-1/services/*
%_liconsdir/*
%_datadir/themes/Default/xfce-notify-4.0/
%_datadir/themes/Smoke/
%_datadir/themes/ZOMG-PONIES!/
%_man1dir/*

%changelog
* Tue May 22 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt3.git20120521
- Updated translations from upstream git.
- Fix BR.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt2.git20120413
- Upstream git snapshot.

* Tue Aug 16 2011 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Drop obsoleted patches.
- Updated to 0.2.2.

* Wed Jun 22 2011 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt3
- Add notify-send requires.
- Update Russian translation (by Artem Zolochevskiy).

* Thu Mar 24 2011 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt2
- Add libxfce4util-devel to BR.
- Renew dbus-service-name.patch.

* Thu Feb 10 2011 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Own %%{_libdir}/xfce4/notifyd/
- Updated to 0.2.1.

* Wed Jan 26 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Spec cleanup, tar.bz2 -> tar.
- Update dbus-service-name.patch from FC.
- Drop xfce4-notifyd-0.1.0-send-second-arg-notification-closed.patch
    (fixed in upstream).
- Updated to 0.2.0.

* Wed Nov 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.1.0-alt2
- First build for Sisyphus.


