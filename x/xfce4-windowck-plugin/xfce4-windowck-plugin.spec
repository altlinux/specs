Name: xfce4-windowck-plugin
Version: 0.5.1
Release: alt1

Summary: Put the maximized window title and windows buttons in the panel
License: GPLv3+
Group: Graphical desktop/XFce
Url: https://gitlab.xfce.org/panel-plugins/xfce4-windowck-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-windowck-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel libxfconf-devel
BuildRequires: libwnck3-devel

Requires: xfce4-panel >= 4.14

%define _unpackaged_files_terminate_build 1

%description
Xfce panel plugin which allows to put the maximized window title and windows
buttons on the panel.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=minimum

# makefiles not ready for parallel build
export NPROCS=1
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS NEWS
%_libdir/xfce4/panel/plugins/*.so
%_iconsdir/hicolor/48x48/apps/*.png
%_datadir/xfce4/panel/plugins/*.desktop
%_datadir/themes/Windowck*/

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Wed Nov 02 2022 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Initial build.
