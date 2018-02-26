Name: xfce4-xkb-plugin
Version: 0.5.4.3
Release: alt3

Summary: XKB layout switch plugin for the XFce panel
Summary(ru_RU.UTF-8): Дополнение для панели Xfce для работы с раскладками клавиатуры
License: %bsdstyle
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel
BuildRequires: libSM-devel librsvg-devel libwnck-devel libxklavier-devel perl-XML-Parser xorg-cf-files intltool
# For changes in 2f7b8cf19159af2bf487c9c4074cd4c7f6dea2ba
BuildRequires: libxfconf-devel

Requires: xfce4-panel

%description
%name is the indicator and switcher of keyboard layout for XKB on the
XFce panel.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе дополнение для панели Xfce позволяющее
работать с раскладками клавиатуры.
Возможности:
* выбор вариантов отображения текущей раскладки (флаг/буквенный вариант)
* выбор комбинации клавишь для переключения раскладки
* гибкая настройка управления раскладкой (глобально, для каждого
  приложения или для каждого окна).


%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_libexecdir/xfce4/panel-plugins/*
%dir %_datadir/xfce4/xkb
%dir %_datadir/xfce4/xkb/flags
%_datadir/xfce4/xkb/flags/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Thu Jun 14 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.3-alt3
- Fix group name validation.
- Fix reading xkb settings from xfconf.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.3-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).
- Updated translations from upstream git.

* Fri Feb 03 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.3-alt1
- Updated to 0.5.4.3.

* Fri Jan 20 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.2-alt4
- Never modify xkb configuration if system settings are used.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.2-alt3
- Rebuild with xfce4-panel-4.9.

* Thu Dec 01 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.2-alt2
- Check keyboard-layout settings in the xfconf.
- Disable layout's list if never_modify_config=true.
- Write settings to xfconf too.

* Mon Oct 17 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.2-alt1
- Updated to 0.5.4.2.

* Mon Oct 10 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.1-alt2
- Fix crash with incomplete configuration.

* Tue May 24 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.1-alt1
- Fix build: create m4 directory.
- Updated to 0.5.4.1.

* Fri Apr 29 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.0-alt2
- Fixes from upstream git (mostly memory leaks).

* Thu Apr 21 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.0-alt1
- Fix memory leaks.
- Drop obsoleted patches.
- Updated to 0.5.4.0.

* Thu Mar 24 2011 Sergey Kurakin <kurakin@altlinux.org> 0.5.3.3-alt7
- Fix segfault after configuration with empty keyboard model combobox
  (Closes: #25276)

* Thu Jan 27 2011 Mikhail Efremov <sem@altlinux.org> 0.5.3.3-alt6
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec cleanup.
- tar.gz -> tar.
- Fix License.
- Fix Url.
- Renew patches for libxklavier (from Debian).
- Add fix-various-segfaults.patch (from Debian).
- Drop watch file.

* Mon Jun 14 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt5
- Rebuild with new xclavier.

* Tue Nov 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt4
- Added xkb-config.patch.

* Sun Sep 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt3
 -Russion translation updated.

* Fri Sep 04 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt2
- Added first-run.patch from boyarsh

* Mon Apr 27 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt1
- Version update

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.2-alt1
- new version

* Thu Jan 03 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.3-alt2
- add watch file

* Thu May 03 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.4.3-alt1
- new version

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version for xfce 4.4rc1

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.2-alt2
- Rebuilt with new xfce4-panel.

* Sat Aug 14 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.2-alt1
- First version of RPM package for Sisyphus.
