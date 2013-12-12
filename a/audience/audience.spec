Name: audience
Version: 0.1
Release: alt2.r302

Summary: A modern media player
License: GPLv3
Group: Video
Url: https://launchpad.net/audience

Source0: %name.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake gcc-c++ libgranite-devel libclutter-gtk3-devel
BuildRequires: gstreamer-devel gst-plugins-devel libpixman-devel
BuildRequires: libexpat-devel libXdmcp-devel libXxf86vm-devel libharfbuzz-devel
BuildRequires: libpng-devel libXinerama-devel libXcursor-devel
BuildRequires: at-spi2-atk-devel vala libgranite-vala

%description
Audience is a simple, modern media player that makes greater use of
hardware acceleration than most players out there.

%prep
%setup -q -n %name

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/audience.desktop
%_datadir/glib-2.0/schemas/org.pantheon.audience.gschema.xml
%_datadir/icons/hicolor/*/apps/audience.svg

%changelog
* Thu Dec 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt2.r302
- Make build more verbose

* Thu Dec 12 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r302
- r302

* Sun Sep 22 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r296
- build for Sisyphus

