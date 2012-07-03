Name: xfce4-clipman-plugin
Version: 1.2.3
Release: alt1

Summary: Clipboard history plugin for the XFce panel
Summary(ru_RU.UTF-8): Менеджер буфера обмена для XFce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Source1: %name-doc.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libexo-devel libxfce4ui-devel libxfconf-devel libxfce4util-devel
BuildRequires: intltool libSM-devel libglade-devel xorg-cf-files libunique-devel libXtst-devel gtk-doc itstool

Requires: xfce4-panel

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
%setup -a1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--disable-static \
	--enable-unique \
	--enable-gen-doc \
	--enable-debug=no
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_bindir/*
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_docdir/%name
%_iconsdir/hicolor/22x22/apps/*
%_iconsdir/hicolor/24x24/apps/*
%_iconsdir/hicolor/scalable/apps/*
%_miconsdir/*
%_niconsdir/*
%_desktopdir/*
%_xdgconfigdir/xfce4/panel/*
%_xdgconfigdir/autostart/*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
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
