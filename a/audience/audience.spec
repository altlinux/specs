%define ver_major 0.2
%define gst_api_ver 1.0
%define _name videos
%define rdnn_name io.elementary.%_name

Name: audience
%define xdg_name org.pantheon.%name
Version: %ver_major.5
Release: alt1

Summary: A modern media player
License: GPLv3
Group: Video
Url: https://launchpad.net/audience

#VCS: https://github.com/elementary/videos.git
Source: %_name-%version.tar.gz
#Source: https://launchpad.net/%name/0.4-loki/%version/+download/%name-%version.tar.xz

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav

BuildRequires: cmake gcc-c++ intltool libgranite-devel libclutter-gtk3-devel
BuildRequires: gst-plugins%gst_api_ver-devel libpixman-devel
BuildRequires: libexpat-devel libXdmcp-devel libXxf86vm-devel libharfbuzz-devel
BuildRequires: libpng-devel libXinerama-devel libXcursor-devel
BuildRequires: at-spi2-atk-devel vala libgranite-vala
BuildRequires: gobject-introspection-devel
BuildRequires: libclutter-gst3.0-devel

%description
Audience is a simple, modern media player that makes greater use of
hardware acceleration than most players out there.

%prep
%setup -n %_name-%version
# fix libdir
find ./ -name "CMakeLists.txt" -print0 | xargs -r0 subst 's|lib\/|${LIB_DESTINATION}/|g' --

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang %rdnn_name

%files -f %rdnn_name.lang
%_bindir/%rdnn_name
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/appdata/%rdnn_name.appdata.xml

%changelog
* Fri Jan 12 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt2
- rebuild against libgranite.so.4

* Mon Aug 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Mon Apr 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Wed Jan 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.1.2-alt1
- 0.2.1.2

* Fri Jan 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.1.1-alt1
- 0.2.1.1

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.1.0.2-alt1
- 0.1.0.2

* Sun Jan 05 2014 Igor Zubkov <icesik@altlinux.org> 0.1-alt3.r305
- r305

* Thu Dec 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt2.r302
- Make build more verbose

* Thu Dec 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r302
- r302

* Sun Sep 22 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r296
- build for Sisyphus

