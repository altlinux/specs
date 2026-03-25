Name: crrcsim
Version: 0.9.13
Release: alt1

Summary: A Model-Airplane Flight Simulation Program
License: GPLv2
Group: Games/Other

URL:           http://sourceforge.net/apps/mediawiki/crrcsim/
# http://download.berlios.de/crrcsim/%%name-%%version.tar.gz
Source0: %name-%version.tar.gz
Source1: CRRCsim.desktop
#Patch1: %name-0.9.12-alt-build.patch
#Patch2: %name-0.9.12-alt-nonx86.patch

Patch0:        %{name}-0.9.13-support-for-platforms-without-sys-io.h.patch
# aarch64 support added
# upstream report: http://preview.tinyurl.com/cass62h
Patch1:        %{name}-0.9.13-aarch64-support-added.patch
# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1307411
# upstream report: https://sourceforge.net/p/crrcsim/bugs/35/
Patch2:        %{name}-0.9.13-gcc-7-fixes.patch
# hg export -r 1554 >crrcsim-0.9.13-issue-41.patch
# fix fof rhbz#1575624
Patch3:        %{name}-0.9.13-issue-41.patch
# Fix compilation with CGAL >5.x
# upstream report: https://sourceforge.net/p/crrcsim/bugs/44/
Patch4:        %{name}-0.9.13-cgal-header-mode-only.patch


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

#patch1 -p2
#patch2 -p1


%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build

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
* Thu Mar 26 2026 Ilya Mashkin <oddity@altlinux.ru> 0.9.13-alt1
- 0.9.13 (Closes: #58135)
- Update url

* Fri Mar 01 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.9.12-alt3
- NMU: fixed FTBFS on non-x86 architectures (made inputdev_parallel a stub
  on non-x86 architectures).

* Mon Jul 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.12-alt2
- Fixed build with new toolchain

* Wed Apr 01 2015 Michael Shigorin <mike@altlinux.org> 0.9.12-alt1
- built for ALT Linux (based on rosa's 0.9.12-2 package)
