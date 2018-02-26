Name: gimp-plugin-normalmap
Version: 1.2.2
Release: alt1

Summary: This is a plugin for GIMP for normal maps creation
License: GPLv2+
Group: Graphics
Url: http://code.google.com/p/gimp-normalmap/
Source: http://gimp-normalmap.googlecode.com/files/gimp-normalmap-1.2.2.tar.bz2

# Automatically added by buildreq on Thu Dec 09 2010
BuildRequires: libgimp-devel libglew-devel libgtkglext-devel

%description
This is a plugin for GIMP.  It allows you to convert images into
RGB normal maps for use in per-pixel lighting applications.
The goal is to completely clone NVIDIA's photoshop plugin,
with a few new useful features.

%prep
%setup -n gimp-normalmap-%version

%build
%make_build CFLAGS="%optflags `pkg-config --cflags gtk+-2.0 gtkglext-1.0 gimp-2.0`"

%install
install -pDm755 normalmap %buildroot%_libdir/gimp/2.0/plug-ins/normalmap

%files
%_libdir/gimp/*/plug-ins/*
%doc README

%changelog
* Thu Dec 09 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Tue Nov 21 2006 Serge Polkovnikov <robin@altlinux.ru> 1.2.1-alt1
- Initial build

