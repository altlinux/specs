%define _libexecdir %_prefix/libexec
%def_enable drm
%def_enable randr
%def_enable vidmode
%def_enable gui

Name: redshift
Version: 1.11
Release: alt3

Summary: Redshift adjusts the color temperature of your screen
Summary(ru_RU.UTF-8): Redshift изменяет температуру цвета вашего экрана для снижения утомляемости глаз
Group: Graphical desktop/GNOME
License: GPLv3+
Url: http://jonls.dk/redshift

#VCS:    https://github.com/jonls/redshift.git
#Source: https://github.com/jonls/%name/releases/download/v%version/%name-%version.tar.xz
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: %name-geoclue-provider.patch

Requires: geoclue2
Requires: typelib(Gtk) = 3.0

# use python3
AutoReqProv: nopython
%define __python %nil

%{?_enable_gui:BuildRequires(pre): rpm-build-python3}
BuildRequires(pre): rpm-build-gir
%{?_enable_drm:BuildRequires: libdrm-devel}
%{?_enable_randr:BuildRequires: libxcb-devel}
%{?_enable_vidmode:BuildRequires: libXxf86vm-devel libXrandr-devel}
BuildRequires: libgio-devel geoclue2-devel
BuildRequires: systemd-devel intltool

# libaptindicator is not package in ALT Linux
%add_typelib_req_skiplist typelib(AppIndicator3)

%description
Redshift adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in
front of the screen at night. The color temperature is set according to
the position of the sun. A different color temperature is set during
night and daytime. During twilight and early morning, the color
temperature transitions smoothly from night to daytime temperature to
allow your eyes to slowly adapt.

%description -l ru_RU.UTF-8
Redshift изменяет температуру цвета экрана вашего компьютера. Это может
снизить утомляемость глаз, особенно если вы работаете за компьютером
ночью. Температура цвета устанавливается в зависимости от позиции солнца
на небе (определяется на основе географических координат) и текущего
времени суток. Изменение температуры цвета происходит плавно, давая Вашим
глазам время на адаптацию.

%prep
%setup
%patch -p1
%patch1 -p1
%autoreconf

%build
%configure \
    %{subst_enable drm} \
    %{subst_enable randr} \
    %{subst_enable vidmode} \
    %{subst_enable gui}
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_prefix/lib/systemd/user/%name.service
%_desktopdir/%name.desktop
%_man1dir/%name.1.*

%if_enabled gui
%_bindir/%name-gtk
%_prefix/lib/systemd/user/%name-gtk.service
%python3_sitelibdir_noarch/%{name}_gtk/
%_desktopdir/%name-gtk.desktop
%_iconsdir/hicolor/*/*/*.*
%_datadir/appdata/%name-gtk.appdata.xml
%endif

%doc DESIGN NEWS* README* redshift.conf.sample

%changelog
* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt3
- explicitly required typelib(Gtk) = 3.0 (ALT #34289)

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 15 2016 Yuri N. Sedunov <aris@altlinux.org> 1.11-alt2
- some improvements & cleanups

* Sat Feb 13 2016 Andrey Cherepanov <cas@altlinux.org> 1.11-alt1
- New version

* Wed May 06 2015 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt3
- truly built with geoclue2

* Tue Mar 24 2015 Andrey Cherepanov <cas@altlinux.org> 1.10-alt2
- Build with drm and geoclue2
- Package redshift-gtk.appdata.xml
- Reduce required autoconf version

* Tue Feb 10 2015 Andrey Cherepanov <cas@altlinux.org> 1.10-alt1
- New version

* Tue Apr 29 2014 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1
- New version

* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 1.8-alt1
- New version

* Wed Jul 31 2013 Andrey Cherepanov <cas@altlinux.org> 1.7-alt1
- New version

* Thu Apr 11 2013 Andrey Cherepanov <cas@altlinux.org> 1.6-alt3.2
- Remove requires of deprecated gnome-panel

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt3.1
- Rebuild with Python-2.7

* Sat Nov 12 2010 Anton Chernyshov <ach@altlinux.org> 1.6-alt3
- remove unneeded stuff from spec
- remove linking with .la-files (and create patch for this)

* Mon Oct 18 2010 Anton Chernyshov <ach@altlinux.org> 1.6-alt2
- minor spec modifications
- exclude license from package according to distribution policy
- include man page

* Mon Oct 18 2010 Anton Chernyshov <ach@altlinux.org> 1.6-alt1
- new upstream release
- completely translate this release to Russian language
- added new BuildReq dependencies

* Sat Oct 16 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt3.1
- completely translate program to Russian language

* Thu Oct 14 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt3
- adding some configure settings
- reformed and corrected Russian translation files

* Mon Oct 11 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt2.1
- some minor spec changes

* Tue Oct 7 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt2
- fix up spec-file according to Sisyphus requirements

* Wed Oct 6 2010 Anton Chernyshov <ach@altlinux.org> 1.5-alt1
- create (more or less) generic spec file and initial build...
