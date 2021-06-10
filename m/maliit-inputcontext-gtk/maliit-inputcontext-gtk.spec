
Name: maliit-inputcontext-gtk
Version: 0.99.1
Release: alt1

Group: Accessibility
Summary: Maliit Input Method  Context Plugins for GTK
Url: http://www.maliit.org
License: LGPL-2.1-only
%K5init no_altplace

Requires: maliit-inputcontext-gtk2
Requires: maliit-inputcontext-gtk3

Source0: %name-%version.tar

# Automatically added by buildreq on Thu Jun 10 2021 (-bi)
# optimized out: at-spi2-atk cmake-modules debugedit elfutils fontconfig fontconfig-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libctf-nobfd0 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglvnd-devel libgpg-error libharfbuzz-devel libmaliit-glib2 libpango-devel libqt5-core libqt5-gui libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-egl pkg-config python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel rpm-build-python3 sh4 xorg-proto-devel
#BuildRequires: cmake libgtk+2-devel libgtk+3-devel maliit-framework-devel python-modules-encodings python3-dev python3-module-mpl_toolkits qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake libgtk+2-devel libgtk+3-devel maliit-framework-devel
BuildRequires: qt5-base-devel
#qt5-svg-devel qt5-wayland-devel qt5-webengine-devel

%description
Core server and libraries for the Maliit Input Methods Framework

%package -n maliit-inputcontext-qt5
Summary: Maliit Input Context Plugin for Qt
Group: Accessibility
Requires: maliit-framework
%description -n maliit-inputcontext-qt5
%name input context plugin for Qt toolkit support

%package -n maliit-inputcontext-gtk2
Summary: Maliit Input Context Plugin for Gtk+2
Group: Accessibility
Requires: maliit-framework
%description -n maliit-inputcontext-gtk2
%name input context plugin for basic Gtk+ version 2 toolkit support

%package -n maliit-inputcontext-gtk3
Summary: Maliit Input Context Plugin for Gtk+3
Group: Accessibility
Requires: maliit-framework
%description -n maliit-inputcontext-gtk3
%name input context plugin for basic Gtk+ version 3 toolkit support

%prep
%setup -n %name-%version


%build
export PATH=%_qt5_bindir:$PATH
%K5build \
    -DENABLE_X11:BOOL=OFF \
    -DENABLE_GTK2:BOOL=ON \
    -DENABLE_GTK3:BOOL=ON \
    #

%install
%K5install


%files

#%files -n maliit-inputcontext-qt5
#%_qt5_plugindir/inputmethods/*.so

%files -n maliit-inputcontext-gtk2
%_libdir/gtk-2.0/2.10.0/immodules/im-maliit.so*

%files -n maliit-inputcontext-gtk3
%_libdir/gtk-3.0/3.0.0/immodules/im-maliit.so*

%changelog
* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 0.99.1-alt1
- initial build

