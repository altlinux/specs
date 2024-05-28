%define tested_version 8.3.22.2239

Name:    1c-preinstall
Version: 8.3
Release: alt16

Summary: Set correct environment for 1C:Enterprise platform
License: GPL-2.0
Group:   System/Libraries
URL:     http://1c.ru/
Packager: Pavel Isopenko <pauli@altlinux.org>

BuildArch: noarch

Requires: at-spi2-atk
Requires: bzlib
Requires: glib2
Requires: glibc-core
Requires: glibc-pthread
Requires: libatk
Requires: libat-spi2-core
Requires: libavahi
Requires: libblkid
Requires: libbrotlicommon
Requires: libbrotlidec
Requires: libcairo
Requires: libcairo-gobject
Requires: libcom_err
Requires: libcups
Requires: libdatrie
Requires: libdbus
Requires: libenchant
Requires: libepoxy
Requires: libexpat
Requires: libffi7
Requires: libfontconfig1
Requires: libfreetype
Requires: libfribidi
Requires: libgcc1
Requires: libgcrypt20
Requires: libgdk-pixbuf
Requires: libgio
Requires: libGL
Requires: libglvnd
Requires: libGLX
Requires: libgpg-error
Requires: libgraphite2
Requires: libgst-plugins1.0
Requires: libgstreamer1.0
Requires: libgtk+3
Requires: libharfbuzz
Requires: libharfbuzz-icu
Requires: libICE
Requires: libidn2
Requires: libkeyutils
Requires: libkrb5
Requires: liblzma
Requires: libmount
Requires: liborc
Requires: libpango
Requires: libpcre3
Requires: libpixman
Requires: libpng16
Requires: libpsl
Requires: libselinux
Requires: libSM
Requires: libsoup
Requires: libsqlite3
Requires: libsystemd
Requires: libthai
Requires: libunistring2
Requires: libuuid
Requires: libwayland-client
Requires: libwayland-cursor
Requires: libwayland-egl
Requires: libX11
Requires: libXau
Requires: libxcb
Requires: libXcomposite
Requires: libXcursor
Requires: libXdamage
Requires: libXdmcp
Requires: libXext
Requires: libXfixes
Requires: libXi
Requires: libXinerama
Requires: libxkbcommon
Requires: libxml2
Requires: libXrandr
Requires: libXrender
Requires: libXt
Requires: libXxf86vm
Requires: libzstd
Requires: zlib

Requires: libstdc++6
Requires: fonts-ttf-ms

%description
This metapackage is intend to deploy correct environment for 1C:Enterprise platform installation.

This package also install Microsoft (tm) fonts are needed by 1C:Enterprise.

Tested with 1C:Enterprise platform version %tested_version

%description -l ru_RU.UTF-8
Метапакет предназначен для развёртывания корректного окружения перед установкой платформы 1С:Предприятия.

Также устанавливает шрифты Microsoft (tm), необходимые для отдельных конфигураций.

Проверено с версией платформы 1С:Предприятие %tested_version

%files

%changelog
* Tue May 28 2024 Pavel Isopenko <pauli@altlinux.org> 8.3-alt16
- clarification of dependencies: minus libcrypto1.1 and libssl1.1 (ALT #50479)


* Thu May 16 2024 Pavel Isopenko <pauli@altlinux.org> 8.3-alt15
- Return into Sisyphus

