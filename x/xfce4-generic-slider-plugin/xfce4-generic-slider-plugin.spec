%define _name xfce4-generic-slider
Name: %_name-plugin
Version: 1.0.0
Release: alt1

Summary: A slider for adjusting the value passed to a command
License: GPL-3.0-only
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-generic-slider/start
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-generic-slider.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4ui-gtk3-devel >= 4.12.0 libxfce4panel-gtk3-devel >= 4.12.0

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
Xfce4-generic-slider is a tool to help Xfce users deal with a variable which
they wish to both GET and SET. The getting side is similar to what
xfce4-genmon-plugin does except the command's numerical output is represented
visually in a slider. Dragging the slider is then used to set the value through
calls to a second command.

%prep
%setup
%patch -p1
ln -s README.md README

%build
%xfce4reconf
%configure \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%doc README.md NEWS
%_libdir/xfce4/panel/plugins/*
%_iconsdir/hicolor/*/apps/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Mon May 29 2023 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Initial build.

