%define ver_major 0.1
%define gst_api_ver 1.0

Name: audience
Version: %ver_major.0.2
Release: alt1

Summary: A modern media player
License: GPLv3
Group: Video
Url: https://launchpad.net/audience

Source: https://launchpad.net/%name/freya/%version/+download/%name-%version.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav

BuildRequires: cmake gcc-c++ libgranite-devel libclutter-gtk3-devel
BuildRequires: gst-plugins%gst_api_ver-devel libpixman-devel
BuildRequires: libexpat-devel libXdmcp-devel libXxf86vm-devel libharfbuzz-devel
BuildRequires: libpng-devel libXinerama-devel libXcursor-devel
BuildRequires: at-spi2-atk-devel vala libgranite-vala
BuildRequires: gobject-introspection-devel

%description
Audience is a simple, modern media player that makes greater use of
hardware acceleration than most players out there.

%prep
%setup
# fix libdir
find ./ -name "CMakeLists.txt" -print0 | xargs -r0 subst 's|lib\/|${LIB_DESTINATION}/|g' --

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/audience.desktop
%_datadir/glib-2.0/schemas/org.pantheon.audience.gschema.xml

%changelog
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

