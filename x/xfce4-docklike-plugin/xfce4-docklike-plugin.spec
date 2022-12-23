Name:     xfce4-docklike-plugin
Version:  0.4.0
Release:  alt1

Summary:  A Dock-like Taskbar Plugin for XFCE
License:  GPL-3.0
Group:    Other
Url:      https://github.com/nsz32/docklike-plugin

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   docklike-plugin-%version.tar

BuildRequires: gcc-c++
BuildRequires: libxfce4ui-gtk3-devel
BuildRequires: libxfce4panel-gtk3-devel
BuildRequires: xfce4-dev-tools
BuildRequires: libwnck3-devel
BuildRequires: libXi-devel

%description
A modern, docklike, minimalist taskbar for XFCE.

%prep
%setup -n docklike-plugin-%version

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/xfce4/panel/plugins/libdocklike.la
%find_lang %name

%files -f %name.lang
%doc AUTHORS *.md
%_libdir/xfce4/panel/plugins/libdocklike.so
%_datadir/xfce4/panel/plugins/docklike.desktop

%changelog
* Fri Dec 23 2022 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt1
- New version (ALT #44172).

* Mon Jan 24 2022 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1.gitfe9c96c
- Initial build for Sisyphus (ALT #39470).
