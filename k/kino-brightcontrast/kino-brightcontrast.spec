%define origname plugin-brightness-contrast

Name: kino-brightcontrast
Version: 0.4
Release: alt3

Summary: Brightness & Contrast Kino plugin
License: GPL
Group: Video

Url: http://rad.xtalk.msk.su/files
Source: %url/plugin-brightness-contrast-%version.tar.bz2
Patch: kino-brightcontrast-0.4-alt-libdir.patch
Packager: Michael Shigorin <mike@altlinux.org>

# manually removed: gcc-g77 
# Automatically added by buildreq on Mon Dec 29 2008
BuildRequires: gcc-c++ kino-devel libglade-devel

%description
This is a first version of Kino plugin "Brightness & Contrast".
The implementation of plugin's functionality is based 
on the acticle "Simple raster operations" of sources.ru magazine 
http://www.sources.ru/magazine/0805/paint.html

%prep
%setup -q -n %origname
%patch -p1

%build
./autogen.sh
%configure --libdir=%_libdir/kino-gtk2
%make

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS ChangeLog NEWS README
%_libdir/kino-gtk2/*
%_datadir/brightcontrast/*

# FIXME:
# - the final hack by me isn't upstreamible, but RP does
#   know his way around C so bugreport will suffice

%changelog
* Mon Dec 29 2008 Michael Shigorin <mike@altlinux.org> 0.4-alt3
- fixed build (BR += libglade-devel)

* Sat Mar 10 2007 Michael Shigorin <mike@altlinux.org> 0.4-alt2
- fixed build on x86_64; thanks Eugene Ostapets (eostapets@)

* Thu Dec 28 2006 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- 0.4
- rebuilt against recent libraries and kino

* Sat Sep 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt0.1
- first build for Sisyphus
