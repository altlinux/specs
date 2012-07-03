%define gimpver 2.0

Name: gimp-plugin-wideangle
Version: 1.0.10
Release: alt1

Summary: Gimp Wideangle Filter
License: GPLv2+
Group: Graphics

Url: http://members.ozemail.com.au/~hodsond/wideangle.html
Source: http://members.ozemail.com.au/~hodsond/wideangle.c

Requires: gimp >= 2.2

# Automatically added by buildreq on Tue Sep 04 2007
BuildRequires: libgimp-devel

%description
The wideangle filter for Gimp is used to correct (or simulate) the distortion
(so called barrel distortion) typically seen on photographs taken with a
wideangle lens.

%prep
%setup -c -T
cp %_sourcedir/wideangle.c .

%build
export CFLAGS="%optflags -ffast-math -funroll-loops"
gimptool-2.0 --build wideangle.c

%install
export DESTDIR=%buildroot
gimptool-2.0 --install-admin-bin wideangle

%files
%_libdir/gimp/%gimpver/plug-ins/*

%changelog
* Tue Sep 04 2007 Victor Forsyuk <force@altlinux.org> 1.0.10-alt1
- Initial build.
