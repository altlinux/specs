#define git_date .git20120414
%define git_date %nil

Name: xfce4-screenshooter
Version: 1.8.1
Release: alt2%git_date

Summary: Screenshot XFce4 panel plugin
Summary (ru_RU.UTF-8): Дополнение для панели XFCE позволяющее делать снимки экрана
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/applications/xfce4-screenshooter
Packager: XFCE Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/apps/xfce4-screenshooter
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel libexo-devel
BuildPreReq: gnome-doc-utils xml-utils xsltproc
BuildRequires: intltool libsoup-devel libXext-devel libICE-devel libXfixes-devel libSM-devel

Provides:  xfce4-screenshooter-plugin = %version-%release
Obsoletes: xfce4-screenshooter-plugin < %version-%release

%description
This application allows you to capture the entire screen, the active
window or a selected region.
You can set the delay that elapses before the screenshot is taken
and the action that will be done with the screenshot: save it to a PNG
file, copy it to the clipboard, or open it using another application.

A plugin for the Xfce panel is also available.

%description -l ru_RU.UTF-8
Стандартное приложение XFCE позволяющее делать снимки экрана. Программа
основана на gnome-screenshot и имеет схожие функции. Имеется возможность
управления как мышкой так и с помощью "горячих" клавишь.

Дополнение для панели XFCE так же включено.

%prep
%setup
%patch -p1
# Don't use git tag in version.
#sed -i 's/m4_define(\[xfce4_screenshooter_version_tag\], \[git\])/m4_define(\[xfce4_screenshooter_version_tag\], \[\])/' configure.ac.in

%build
%xfce4reconf
%configure \
    --enable-xsltproc \
    --enable-xml2po \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_datadir/xfce4/doc/*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/applications/*.desktop
%_bindir/xfce4-screenshoot*
%_mandir/man1/xfce4-screenshooter*
%_defaultdocdir/%name

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
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
