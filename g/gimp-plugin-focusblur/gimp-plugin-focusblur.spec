%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
%define shortname focusblur

Name: gimp-plugin-%shortname
Version: 3.2.6
Release: alt3

Summary: Focus Blur plug-in is blurring effect, a kind of called DoF
License: GPLv2+
Group: Graphics

URL: http://registry.gimp.org/node/1444
Source0: http://registry.gimp.org/files/focusblur-%version.tar.bz2
Source1: focusblur-model-inverse.png
Source2: ru.po
# This patch was included in source rpm, but not applied...
Patch0: %name-3.2.2-inversemodel-alt.patch.bz2
# fc
Patch1: gimp-focusblur-plugin-fix-gettext.patch
Patch2: gimp-focusblur-plugin-include-main-glib.patch

Requires: gimp

# Automatically added by buildreq on Thu Feb 17 2011
BuildRequires: intltool libfftw3-devel libgimp-devel

%description
Focus Blur plug-in is blurring effect, a kind of called DoF. This software
makes a out of focus with luminosity and depth, like a sight or lenses.
It can be used with depth map, depth fakes and shine effect. Also it can work
as simple and applicable blur.

%prep
%setup -n %shortname-%version
cp %SOURCE1 pixmaps/
cp -f %SOURCE2 po/
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure LIBS=-lm
%make_build

%install
%makeinstall_std

%find_lang gimp20-%shortname

%files -f gimp20-%shortname.lang
%gimpplugindir/plug-ins/*

%changelog
* Fri Jan 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.2.6-alt3
- fixed build

* Fri Apr 06 2012 Victor Forsiuk <force@altlinux.org> 3.2.6-alt2
- Fix glib include compile problem.

* Tue Feb 22 2011 Victor Forsiuk <force@altlinux.org> 3.2.6-alt1
- 3.2.6

* Wed May 21 2008 Yury Aliaev <mutabor@altlinux.org> 3.2.2-alt1.5
- Sorry! Internationalization files were forgotten in the previous release.
- Russian translation updated.

* Wed May 21 2008 Yury Aliaev <mutabor@altlinux.org> 3.2.2-alt1
- Initial build.
