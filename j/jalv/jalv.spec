Name: jalv
Version: 1.6.8
Release: alt1

Summary: Simple host for LV2 plugins
License: 0BSD
Group: Sound
Url: https://gitlab.com/drobilla/jalv

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ meson
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(lilv-0)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(serd-0)
BuildRequires: pkgconfig(sord-0)
BuildRequires: pkgconfig(sratom-0)
BuildRequires: pkgconfig(suil-0)
BuildRequires: pkgconfig(zix-0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(Qt5Widgets)

%package gtk3
Summary: GTK-based host for LV2 plugins
Group: Sound
Requires: jalv = %version-%release

%package qt5
Summary: Qt5-based host for LV2 plugins
Group: Sound
Requires: jalv = %version-%release

%define desc\
Jalv (JAck LV2) is a simple host for LV2 plugins. It runs a plugin,\
and exposes the plugin ports to the system, essentially making\
the plugin an application. For more information, see\
http://drobilla.net/software/jalv.

%description %desc

%description gtk3 %desc
This package offers GTK3 based GUI for LV2 plugins.

%description qt5 %desc
This package offers Qt5 based GUI for LV2 plugins.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
sed -r -e '/^Name=/ s,$, (Qt),' -e '/^Exec=/ s,gtk3,qt5,' \
    < %buildroot%_desktopdir/jalv.desktop \
    > %buildroot%_desktopdir/jalv-qt.desktop

%files
%doc AUTHORS COPYING INSTALL* NEWS README*
%_bindir/jalv
%_libdir/jack/jalv.so
%_man1dir/jalv.1*

%files gtk3
%_bindir/jalv.gtk3
%_desktopdir/jalv.desktop
%_man1dir/jalv.gtk3.1*

%files qt5
%_bindir/jalv.qt5
%_desktopdir/jalv-qt.desktop
%_man1dir/jalv.qt5.1*

%changelog
* Wed Mar  6 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.8-alt1
- initial
