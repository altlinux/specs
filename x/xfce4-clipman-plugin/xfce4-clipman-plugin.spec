Name: xfce4-clipman-plugin
Version: 1.6.3
Release: alt1

Summary: Clipboard history plugin for the Xfce panel
Summary(ru_RU.UTF-8): Менеджер буфера обмена для Xfce
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/%name
Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-clipman-plugin.git
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfconf-devel libxfce4util-devel
BuildRequires: xorg-proto-devel libXtst-devel
BuildRequires: libqrencode-devel
BuildRequires: intltool rpm-build-xdg

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
Clipman is a clipboard manager for Xfce. It keeps the clipboard contents
around while it is usually lost when you close an application.
It is able to handle text and images, and has a feature to execute
actions on specific text selections by matching them against regular
expressions.

%description -l ru_RU.UTF-8
Clipman это менеджер буфера обмена для Xfce. Он сохраняет содержимое
буфера обмена, которое обычно теряется при закрытии приложения. Он
способен обрабатывать как текст так и изображения, а также имеет
функцию, позволяющую выполнять конкретные действия по выбору текста
путем сопоставления их с регулярными выражениями.

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag project_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--disable-static \
	--enable-libqrencode \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README.md NEWS AUTHORS
%_bindir/*
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*
%_miconsdir/*
%_niconsdir/*
%_desktopdir/*
%_xdgconfigdir/xfce4/panel/*
%_xdgconfigdir/autostart/*
%_datadir/metainfo/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Tue Mar 21 2023 Mikhail Efremov <sem@altlinux.org> 1.6.3-alt1
- Updated to 1.6.3.

* Tue Feb 08 2022 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt2
- Patch from upstream git:
  + Fix invalid "Show full history..." menu item behavior.

* Wed May 12 2021 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1
- Updated to 1.6.2.

* Sun Sep 13 2020 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt2.g2fc75f2
- Dropped libexo-devel from BR.
- Updated Vcs tag.
- Upstream git snapshot.

* Sun Apr 05 2020 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt1
- Updated to 1.6.1.

* Mon Mar 30 2020 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Mon Mar 02 2020 Mikhail Efremov <sem@altlinux.org> 1.4.4-alt1
- Fixed configure option.
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Updated Url.
- Updated to 1.4.4.

* Mon Oct 29 2018 Mikhail Efremov <sem@altlinux.org> 1.4.3-alt1
- Updated to 1.4.3.

* Fri Aug 17 2018 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt3
- Fix BR.
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Rebuild with libxfconf-0.so.3.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt2
- Rebuild with libxfce4util-4.12.

* Mon Jun 02 2014 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1
- Updated to 1.2.6.

* Wed Feb 12 2014 Mikhail Efremov <sem@altlinux.org> 1.2.5-alt1
- Bump version in the configure script.
- Fix help url.
- Updated to 1.2.5.

* Mon Feb 03 2014 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Enable QR Code support.
- Updated to 1.2.4.

* Fri Jun 07 2013 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt3
- Really update translations.

* Thu Jun 06 2013 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt2
- Fix build: require gnome-doc-utils.
- Updated from upstream git
    (translations and minor code improvement).

* Fri Apr 13 2012 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt1
- Updated to 1.2.3.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt2
- Rebuild with xfce4-panel-4.9.

* Mon Nov 14 2011 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Patch from upstream:
  + Bug 8106: Use g_return_val_if_fail instead of g_return_if_fail.
- Drop obsoleted patches.
- Updated to 1.2.2.

* Mon Jan 31 2011 Mikhail Efremov <sem@altlinux.org> 1.1.3-alt2
- Fix desktop file path for xfce4-panel >= 4.8.
- Fix possible NULL values (patch from Fedora).
- Fix build with libexo-1.
- Spec updated, tar.bz2 -> tar.

* Fri Dec 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.1.3-alt1
- Version update.

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.5.99.1-alt1
- 0.5.99.1

* Wed Dec 29 2004 Andrey Astafiev <andrei@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Fri Jan 02 2004 Andrey Astafiev <andrei@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Wed Nov 19 2003 Andrey Astafiev <andrei@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Mon Nov 03 2003 Andrey Astafiev <andrei@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Mon Oct 20 2003 Andrey Astafiev <andrei@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
