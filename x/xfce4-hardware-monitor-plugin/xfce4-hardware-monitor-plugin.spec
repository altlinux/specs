Name: xfce4-hardware-monitor-plugin
Version: 1.6.0
Release: alt1

Summary: Display various hardware stats graphically or with text
License: %gpl3plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/xfce4-hardware-monitor-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

# git://git.xfce.org/panel-plugins/xfce4-hardware-monitor-plugin
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: rpm-build-xfce4 xfce4-dev-tools rpm-macros-cmake cmake
BuildRequires: libxfce4panel-devel libxfce4ui-devel
Buildrequires: gcc-c++
BuildRequires: libgtkmm2-devel libgnomecanvasmm-devel libgtop-devel
BuildRequires: libsensors3-devel

%define _unpackaged_files_terminate_build 1

Requires: xfce4-panel >= 4.11

%description
Hardware Monitor is a monitor plugin for the Xfce4 panel. It supports
a variety of monitoring capabilities (CPU usage, network throughput
etc.) and different kinds of viewers (curves, bars, text, flames).

%prep
%setup
%patch -p1

%build
%add_optflags -std=gnu++11
%xfce4reconf
%configure \
		--with-libsensors=yes
%make_build

%install
%makeinstall_std
# glibc supports sr@latin only
mv %buildroot/usr/share/locale/sr@Latn/ %buildroot/usr/share/locale/sr@latin/
%find_lang %name

%files -f %name.lang
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_pixmapsdir/*.png
%_datadir/%name/

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Tue Sep 19 2017 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt2
- Rebuild with libgtop-2.0.so.11.

* Thu Jul 21 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1
- Initial build.

