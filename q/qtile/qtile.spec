%define _unpackaged_files_terminate_build 1

%def_without check

Name: qtile
Version: 0.18.1
Release: alt1

Summary: A full-featured, hackable tiling window manager written and configured in Python
License: MIT
Group: Graphical desktop/Other

#https://github.com/qtile/qtile
Url: http://www.qtile.org/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-cffi
BuildRequires: python3-module-cairocffi
BuildRequires: python3-module-xcffib
BuildRequires: python3-module-setuptools_scm
BuildRequires: libcairo-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libpango-devel
BuildRequires: libXcursor-devel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pygobject3
#BuildRequires: python3-module-bowler
BuildRequires: python3-modules-curses
BuildRequires: libgdk-pixbuf-gir
BuildRequires: libgtk+3-gir
BuildRequires: ImageMagick
BuildRequires: xorg-xephyr
BuildRequires: xorg-xvfb
%endif

%description
%summary

%prep
%setup
%patch0 -p1

%build
./scripts/ffibuild
%python3_build

%install
%python3_install

install -Dm 644 resources/qtile.desktop -t %buildroot%_datadir/xsessions/
install -Dm 644 resources/qtile-wayland.desktop -t %buildroot%_datadir/wayland-sessions/

# FIXME
mv %buildroot%python3_sitelibdir/libqtile/widget/_pulse_audio.abi3.so %buildroot%python3_sitelibdir/libqtile/widget/_pulse_audio.so

%check
%__python3 -m pytest test

%files
%doc LICENSE README.rst libqtile/resources/default_config.py
%_bindir/qtile
%python3_sitelibdir/libqtile
%python3_sitelibdir/*.egg-info
%_datadir/xsessions/qtile.desktop
%_datadir/wayland-sessions/qtile-wayland.desktop

%changelog
* Thu Dec 09 2021 Egor Ignatov <egori@altlinux.org> 0.18.1-alt1
- First build for ALT
