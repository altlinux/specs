Name: parole
Version: 0.2.0.6
Release: alt3

Summary: Media player for the Xfce desktop
License: %gpl2plus
Group: Video

URL: http://goodies.xfce.org/projects/applications/parole
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: XFCE Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfcegui4-devel libxfce4util-devel libexo-devel
BuildRequires: libgtk+2-devel libnotify-devel gst-plugins-devel libtag-devel
BuildRequires: libdbus-glib-devel libdbus-devel
BuildRequires: intltool gtk-doc

%description
Parole is a modern simple media player based on the GStreamer framework
and written to fit well in the Xfce desktop. Parole features playback of
local media files, DVD/CD and live streams. Parole is extensible via
plugins.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libgtk+2-devel
BuildArch: noarch

%description devel
This package contains header files and documentation
for developing plugins for %name.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
    --disable-static \
    --enable-maintainer-mode \
    --enable-libnotify \
    --enable-taglib \
    --enable-gtk-doc \
    --enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS README THANKS
%_bindir/%name
%_libdir/%name-*/
%exclude %_libdir/%name-*/*.la
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/%name/

%files devel
%_includedir/*
%doc %_datadir/gtk-doc/html/*

%changelog
* Mon May 21 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt3
- Fix DSO linking.
- Updated translations from upstream git.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).
- Updated translations from upstream git.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.6-alt1
- Updated to 0.2.0.6.

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.2-alt2
- Package parole-devel as noarch.

* Sun Feb 20 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0.2-alt1
- Fix documentation bulding.
- Initial build (slightly based on FC spec).
