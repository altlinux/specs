Name: crrcsim
Version: 0.9.12
Release: alt2

Summary: A Model-Airplane Flight Simulation Program
License: GPLv2
Group: Games/Other

Url: http://crrcsim.berlios.de/wiki
# http://download.berlios.de/crrcsim/%%name-%%version.tar.gz
Source0: %name-%version.tar.gz
Source1: CRRCsim.desktop
Patch1: %name-%version-alt-build.patch

BuildRequires: gcc-c++
BuildRequires: libjpeg-devel
BuildRequires: plib-devel
BuildRequires: pkgconfig(glut)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(sdl)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xt)
BuildRequires: desktop-file-utils

%description
Crrcsim is a model-airplane flight simulation program. Using it,
you can learn how to fly model aircraft, test new aircraft
designs, and improve your skills by practicing on your computer.

It rules! The flight model is very realistic. The flight model
parameters are calculated based on a 3D representation of the
aircraft. Stalls are properly modelled as well. Model control
is possible with your own rc transmitter, or any input device
such as joystick, mouse, keyboard ...

%prep
%setup
%patch1 -p2

%build
%configure
%make

%install
%makeinstall_std
mv %buildroot%_defaultdocdir/%name _docs_

%find_lang %name
desktop-file-install --vendor="" \
        --dir=%buildroot%_datadir/applications \
        %SOURCE1

%files -f %name.lang
%doc COPYING
%doc _docs_/*
%_datadir/%name/
%_bindir/crrcsim
%_desktopdir/CRRCsim.desktop
%_man1dir/%name.1*

%changelog
* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.12-alt2
- Fixed build with new toolchain

* Wed Apr 01 2015 Michael Shigorin <mike@altlinux.org> 0.9.12-alt1
- built for ALT Linux (based on rosa's 0.9.12-2 package)
