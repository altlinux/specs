Name: thunar-archive-plugin
Version: 0.3.0
Release: alt3

Summary: Thunar archive plugin
Summary (ru_RU.UTF8): Дополнение к Thunar позволяющее работать с архивами
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/thunar-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4util-devel libthunar-devel libexo-devel
BuildRequires: libgtk+2-devel intltool libxml2-devel

Requires: thunar

%add_findreq_skiplist %_libexecdir/%name/*.tap

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
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README ChangeLog AUTHORS
%exclude %_libdir/thunarx-*/*.la
%_libdir/thunarx-*/*.so
%_libexecdir/%name/
%_miconsdir/*.png

%changelog
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

