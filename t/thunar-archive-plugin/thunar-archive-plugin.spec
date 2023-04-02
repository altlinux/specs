Name: thunar-archive-plugin
Version: 0.5.1
Release: alt1

Summary: Thunar archive plugin
Summary (ru_RU.UTF8): Дополнение к Thunar позволяющее работать с архивами
License: LGPLv2+ and GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/xfce/thunar/archive
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs: https://gitlab.xfce.org/thunar-plugins/thunar-archive-plugin.git
Source: %name-%version.tar

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libthunar-devel libexo-gtk3-devel
BuildRequires: libgtk+3-devel intltool libxml2-devel

Requires: thunar

%add_findreq_skiplist %_libexecdir/%name/*.tap

%define _unpackaged_files_terminate_build 1

%description
The thunar-archive-plugin is a plugin for the Thunar File Manager, which
adds archive operations to the file context menus. Using this plugin you
will be able to extract and create archive files from within Thunar
using a single click.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе дополнение к файловому менеджеру Thunar,
позволяющее работать с архивами из контекстного меню. Используя данное
дополнение, вы сможете создавать и распаковывать архивы просто щелкнув
на соотвествующих файлах правой кнопкой мыши и выбрав необходимый пункт
появившегося контекстного меню.

%prep
%setup

%build
%xfce4reconf
%configure \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS NEWS
%exclude %_libdir/thunarx-*/*.la
%_libdir/thunarx-*/*.so
%_libexecdir/%name/
%_miconsdir/*.png

# Seems glibc doesn't support uz@Latn
%exclude %_datadir/locale/uz@Latn/LC_MESSAGES/thunar-archive-plugin.mo

%changelog
* Sun Apr 02 2023 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Updated to 0.5.1.

* Wed May 04 2022 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Added Vcs tag.
- Updated Url.
- Fixed License tag.
- Updated to 0.5.0.

* Tue Aug 21 2018 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Don't package uz@Latn translation.
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.4.0.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Wed Apr 18 2012 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt3
- Updated requires.

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt2
- Own %%_libexecdir/thunar-archive-plugin.

* Thu Feb 10 2011 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Don't use auto requires for *.tap scripts.
- Drop thunar-archive-plugin-file-roller-extract-here.patch
    (fixed in upstream).
- Drop thunar-archive-plugin-asneeded.patch (obsolete).
- Spec updated, tar.bz2 -> tar.
- Updated to 0.3.0.

* Tue Jun 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.2.4-alt3
- Updated russian translation

* Mon May 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.2.4-alt2
- Removed ark depency.
- Added thunar-archive-plugin-file-roller-extract-here.patch

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.4-alt1
- new version

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.2.0-alt1
- First build for Sisyphus.

