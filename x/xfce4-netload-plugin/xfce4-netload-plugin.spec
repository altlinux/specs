Name: xfce4-netload-plugin
Version: 1.1.0
Release: alt2

Summary: Netload monitor plugin for the XFce panel
Summary(ru_RU.CP1251): Модуль для просмотра загрузки сети на панели XFce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel

BuildRequires: glib2-devel libatk-devel libgtk+2-devel libpango-devel libxml2-devel pkgconfig
BuildRequires: perl-XML-Parser intltool

Requires: xfce4-panel >= 4.8

%description
%name is the netload monitor plugin for the XFce panel.

%description -l ru_RU.CP1251
%name -- это монитор загрузки сети для панели XFce.

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
%doc README AUTHORS
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop
%_datadir/icons/hicolor/*/*/*

%changelog
* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).
- Updated translations from upstream git.

* Fri Jan 13 2012 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Drop obsoleted patch.
- Updated to 1.1.0.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt3
- Rebuild with xfce4-panel-4.9.

* Wed Mar 30 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Adjust the border size to match other plugins.
- Fix build: drop xorg-x11-devel from BR.

* Sun Feb 06 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec updated, tar.bz2 -> tar.
- Drop xfce4-netload-plugin-0.4.0-as-needed.patch
    (fixed in upstream).
- Updated to 1.0.0.

* Wed May 02 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 0.4.0-alt1
- Taken from orphaned
- 0.4.0

* Sun Sep 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3.3-alt2
- fix url

* Tue Aug 23 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Thu Jun 30 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Tue Jan 18 2005 Andrey Astafiev <andrei@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Sun Jan 09 2005 Andrey Astafiev <andrei@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Mon Oct 20 2003 Andrey Astafiev <andrei@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Tue Oct 07 2003 Andrey Astafiev <andrei@altlinux.ru> 0.2.1-alt1
- 0.2.1
- Changed Group tag.

* Tue Sep 16 2003 Andrey Astafiev <andrei@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Sun Sep 13 2003 Andrey Astafiev <andrei@altlinux.ru> 0.2.0pre6-alt0.9
- First version of RPM package for Sisyphus.
