%define _unpackaged_files_terminate_build 1

Name: xfce4-calculator-plugin
Version: 0.5.1
Release: alt1

Summary: A calculator plugin for the Xfce panel
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/panel-plugins/xfce4-calculator-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel

Requires: xfce4-panel >= 4.8

%description
Simple command line based calculator for the Xfce panel

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
%doc README AUTHORS NEWS
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Initial build.

