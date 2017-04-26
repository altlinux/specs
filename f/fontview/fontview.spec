Name: fontview
Version: 0.2.3
Release: alt1

Summary: Demo app that displays fonts with a free/libre/open-source text rendering stack: FreeType, HarfBuzz and Raqm

License: Apache 2.0
Group: Publishing
Url: https://github.com/googlei18n/fontview

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/googlei18n/fontview/archive/v%version.tar.gz
Source: %name-%version.tar

# manually removed: mariadb-common python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs selinux-policy

# Automatically added by buildreq on Wed Apr 26 2017
# optimized out: at-spi2-atk fontconfig i586-libxcb libat-spi2-core libcairo-gobject libfreetype-devel libgdk-pixbuf libgpg-error libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server pkg-config python-base python-modules python-modules-compiler python3 python3-base
BuildRequires: gcc-c++ libfribidi-devel libharfbuzz-devel libwxGTK3.1-devel

BuildRequires: libucdn-devel
BuildRequires: libraqm-devel >= 0.2.0

%description
Demo app that displays fonts with a free/libre/open-source text rendering stack:
FreeType, HarfBuzz and Raqm.

%prep
%setup

%build
python2.7 build.py

%install
%__install -D build/%name %buildroot%_bindir/%name

%files
%doc README.md LICENSE.md
%_bindir/%name
# TODO
#%_desktopdir/%name.desktop

%changelog
* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- initial build for ALT Sisyphus
