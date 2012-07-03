%define gimpver 2.0

Name: gimp-plugin-thinline
Version: 2.0
Release: alt1

Summary: Thin Line plug-in for The GIMP
License: GPLv2+
Group: Graphics

Url: http://registry.gimp.org/plugin?id=2128
# In fact source can be downloaded from URL:
# http://registry.gimp.org/file/thin_line.c?action=download&id=3923
Source: thin_line.c
Source1: stdplugins-intl.h

Requires: gimp >= 2.2

# Automatically added by buildreq on Wed Sep 05 2007
BuildRequires: libgimp-devel

%description
This Gimp plug-in converts the image into 1 pixel line drawing using edge
detectiong or threshold.

%prep
%setup -c -T
install %_sourcedir/thin_line.c .
install -pD %_sourcedir/stdplugins-intl.h ./libgimp/stdplugins-intl.h

%build
export CFLAGS="%optflags -ffast-math -funroll-loops"
gimptool-2.0 --build thin_line.c

%install
export DESTDIR=%buildroot
gimptool-2.0 --install-admin-bin thin_line

%files
%_libdir/gimp/%gimpver/plug-ins/*

%changelog
* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 2.0-alt1
- Initial build.
