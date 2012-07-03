%define gimpver 2.0

Name: gimp-plugin-dcamnoise2
Version: 0.64
Release: alt1

Summary: Gimp plugin for removing noise introduced by digital cameras
License: GPL
Group: Graphics

URL: http://www.hphsite.de/dcamnoise/
Source0: http://www.hphsite.de/dcamnoise/project-files/dcamnoise2-%version.cpp

Requires: gimp2 >= 2.2

# Automatically added by buildreq on Wed Jun 06 2007
BuildRequires: gcc-c++ libgimp-devel

%description
Gimp plugin for removing noise introduced by digital cameras. Very
effective. It is present in image menu, under Filters/Enhance.

%prep
%setup -q -c -T
cp %SOURCE0 .

%build
export CC=g++
export CFLAGS="%optflags -ffast-math -funroll-loops"
gimptool-2.0 --build dcamnoise2-0.64.cpp

%install
export DESTDIR=%buildroot
gimptool-2.0 --install-admin-bin dcamnoise2-0.64

%files
%_libdir/gimp/%gimpver/plug-ins/*

%changelog
* Wed Jun 06 2007 Victor Forsyuk <force@altlinux.org> 0.64-alt1
- Initial build.
