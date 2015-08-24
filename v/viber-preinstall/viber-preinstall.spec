Name:    viber-preinstall
Version: 1.0
Release: alt1

Summary: Set correct environment to rebuild official Viber client
License: GPL
Group:   System/Libraries
URL:     http://altlinux.org/Viber
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Requires: rpmrebuild

Requires: ca-certificates
Requires: fontconfig
Requires: glib2
Requires: glibc-core
Requires: glibc-pthread
Requires: libfreetype
Requires: libgcc1
Requires: libGL
Requires: libgst-plugins
Requires: libgstreamer
Requires: libICE
Requires: libSM
Requires: libsqlite3
Requires: libstdc++6
Requires: libX11
Requires: libxcb
Requires: libXcomposite
Requires: libXext
Requires: libXi
Requires: libxml2
Requires: libXrender
Requires: libxslt
Requires: zlib

%description
This metapackage is intend to deploy correct environment for
Viber client installation from http://www.viber.com/ru/products/linux

%files

%changelog
* Mon Aug 24 2015 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

