%define ver_major 0.4

Name: gnome-video-effects
Version: %ver_major.0
Release: alt1

Summary: A collection of GStreamer video effects
License: GPLv2
Group: Video
Url: http://live.gnome.org/GnomeVideoEffects
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

BuildArch: noarch

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: intltool >= 0.40.0

%description
A collection of GStreamer video effects to be used in different GNOME Modules

%package devel
Summary: Development files for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package provides .pc file needed to build apllications using %name

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%dir %_datadir/gnome-video-effects
%_datadir/gnome-video-effects/*.effect
%doc AUTHORS README NEWS

%files devel
%_datadir/pkgconfig/%name.pc

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu Mar 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Wed Jan 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus
