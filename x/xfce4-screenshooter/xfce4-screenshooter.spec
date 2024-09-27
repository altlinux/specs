#define git_date .git20120414
%define git_date %nil

Name: xfce4-screenshooter
Version: 1.11.1
Release: alt2%git_date

Summary: Screenshot Xfce4 panel plugin
Summary (ru_RU.UTF-8): Дополнение для панели Xfce позволяющее делать снимки экрана
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/apps/screenshooter/start
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/apps/xfce4-screenshooter.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%if_xfce4_wayland_support
%def_enable wayland
%else
%def_disable wayland
%endif

BuildRequires(pre): rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel libexo-gtk3-devel libxfconf-devel
BuildRequires: libX11-devel libXi-devel libXext-devel libXfixes-devel libXtst-devel
%{?_enable_wayland:BuildRequires: wayland-devel libwayland-client-devel wlr-protocols}
BuildRequires: libpango-devel >= 1.44.0

BuildRequires: help2man

Provides:  xfce4-screenshooter-plugin = %version-%release
Obsoletes: xfce4-screenshooter-plugin < %version-%release

%define _unpackaged_files_terminate_build 1

%description
This application allows you to capture the entire screen, the active
window or a selected region.
You can set the delay that elapses before the screenshot is taken
and the action that will be done with the screenshot: save it to a PNG
file, copy it to the clipboard, or open it using another application.

A plugin for the Xfce panel is also available.

%description -l ru_RU.UTF-8
Стандартное приложение Xfce позволяющее делать снимки экрана. Программа
основана на gnome-screenshot и имеет схожие функции. Имеется возможность
управления как мышкой так и с помощью "горячих" клавишь.

Дополнение для панели Xfce так же включено.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-x11 \
	%{subst_enable wayland} \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/applications/*.desktop
%_datadir/metainfo/*.xml
%_bindir/xfce4-screenshoot*
%_libexecdir/xfce4/screenshooter/
%_mandir/man1/xfce4-screenshooter*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Fri Sep 27 2024 Mikhail Efremov <sem@altlinux.org> 1.11.1-alt2
- Enabled wayland support in the Sisyphus only.

* Wed Jul 31 2024 Mikhail Efremov <sem@altlinux.org> 1.11.1-alt1
- Updated to 1.11.1.

* Mon Jul 29 2024 Mikhail Efremov <sem@altlinux.org> 1.11.0-alt1
- Updated to 1.11.0.

* Thu May 30 2024 Mikhail Efremov <sem@altlinux.org> 1.10.6-alt1
- Updated to 1.10.6.

* Mon Feb 05 2024 Mikhail Efremov <sem@altlinux.org> 1.10.5-alt1
- Updated to 1.10.5.

* Mon May 15 2023 Mikhail Efremov <sem@altlinux.org> 1.10.4-alt1
- Updated to 1.10.4.

* Fri Jan 13 2023 Mikhail Efremov <sem@altlinux.org> 1.10.3-alt1
- Updated to 1.10.3.

* Fri Jan 06 2023 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1
- Updated to 1.10.2.

* Thu Dec 22 2022 Mikhail Efremov <sem@altlinux.org> 1.10.1-alt1
- Updated to 1.10.1.

* Wed Nov 16 2022 Mikhail Efremov <sem@altlinux.org> 1.10.0-alt1
- Don't require X display for printing version.
- Updated BR.
- Updated to 1.10.0.

* Fri Aug 12 2022 Mikhail Efremov <sem@altlinux.org> 1.9.11-alt1
- Updated to 1.9.11.

* Mon Mar 07 2022 Mikhail Efremov <sem@altlinux.org> 1.9.10-alt1
- Updated to 1.9.10.

* Mon May 24 2021 Mikhail Efremov <sem@altlinux.org> 1.9.9-alt1
- Added libpango-devel to BR.
- Updated to 1.9.9.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 1.9.8-alt1
- Added Vcs tag.
- Updated Url tag.
- Don't use rpm-build-licenses.
- Updated to 1.9.8.

* Tue Nov 05 2019 Mikhail Efremov <sem@altlinux.org> 1.9.7-alt1
- Updated to 1.9.7.

* Mon Aug 26 2019 Mikhail Efremov <sem@altlinux.org> 1.9.6-alt1
- Updated to 1.9.6.

* Mon Apr 01 2019 Mikhail Efremov <sem@altlinux.org> 1.9.5-alt1
- Updated to 1.9.5.

* Tue Mar 12 2019 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt2
- Fix man page.

* Mon Mar 11 2019 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt1
- Added help2man to BR.
- Updated to 1.9.4.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 1.9.3-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 1.9.3.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.8.2-alt2
- Rebuild with libxfce4util-4.12.

* Mon Jan 26 2015 Mikhail Efremov <sem@altlinux.org> 1.8.2-alt1
- Revert "Don't use xfhelp4.".
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 1.8.2.

* Tue May 22 2012 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt2
- Updated translations from upstream git.
- Fix BR.

* Thu May 03 2012 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1
- Don't use xfhelp4.
- Fix pligin linking.
- Updated to 1.8.1.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt3.git20120414
- Drop additional-category.patch.
- Upstream git snapshot.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt2
- Rebuild with xfce4-panel-4.9.

* Tue Aug 16 2011 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Enable XFIXES extension support.
- Updated to 1.8.0.

* Tue May 03 2011 Mikhail Efremov <sem@altlinux.org> 1.7.9-alt2.git20110429
- Upstream git snapshot.

* Tue Mar 08 2011 Mikhail Efremov <sem@altlinux.org> 1.7.9-alt2.git20110227
- Upstream git snapshot.

* Thu Jan 27 2011 Mikhail Efremov <sem@altlinux.org> 1.7.9-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec cleanup & update.
- Fix License.
- Fix Url.
- tar.bz2 -> tar
- Updated to 1.7.9.

* Tue Dec 15 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.6.0-alt3
- Some repocop warnings is taken into account.

* Thu Jul 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.6.0-alt2
- Fix localization errors in screenshot file names.

* Wed Jun 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.6.0-alt1
- Version update to 1.6.0

* Sat Jun 06 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.99-alt1
- Beta version of Xfce4-screenshooter 1.6

* Sun Apr 26 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.1-alt0.M50.1
- Backport to Desktop 5.0

* Fri Apr 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.1-alt1
Update to version 1.5.1. Name changed to xfce4-screenshooter

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.4.0-alt1
- new version

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.0.0-alt1
- First version of RPM package for Sisyphus.
