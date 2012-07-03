%define _plugindir %(gimptool-2.0 --gimpplugindir)/plug-ins
%define _mathmapdir %_datadir/gimp/2.0/mathmap
%define _langdir %_datadir/gtksourceview-2.0/language-specs

Name: gimp-plugin-mathmap
Version: 1.3.5
Release: alt2

Summary: MathMap GIMP Plug-In and Command-Line Tool
License: GPLv2+
Group: Graphics

URL: http://www.complang.tuwien.ac.at/schani/mathmap/
Source: http://www.complang.tuwien.ac.at/schani/mathmap/files/mathmap-%version.tar.gz
Source1: ru.po

Patch0: mathmap-1.3.5-defines-alt.patch
Patch1: mathmap-1.3.4-localefix-alt.patch
Patch2: mathmap-1.3.4-bufoverflowfix-alt.patch

Requires: gimp, gcc

# Automatically added by buildreq on Tue Mar 08 2011
BuildRequires: doxygen gcc-c++ libfftw3-devel libgif-devel libgimp-devel libgsl-devel libgtksourceview-devel libjpeg-devel libpng-devel unzip
#BuildRequires: libquicktime-devel -- ugly buggy, not compiled...

%description
MathMap is a GIMP plug-in which allows distortion of images specified
by mathematical formulae.  For each pixel in the generated image, an
expression is evaluated which should return a pixel value.  The
expression can either refer to a pixel in the source image or can
generate pixels completely independent of the source.

%prep
%setup -n mathmap-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp %SOURCE1 .

%build
%make_build

%install
%makeinstall_std
# blender stuff remained for future
install -m644 generators/blender/blender_template.c generators/blender/blender_opmacros.h %buildroot%_mathmapdir/

%find_lang mathmap

%files -f mathmap.lang

%doc README.filters
%_bindir/mathmap
%_plugindir/mathmap
%_langdir/mathmap.lang
%_mathmapdir

%changelog
* Tue Mar 08 2011 Victor Forsiuk <force@altlinux.org> 1.3.5-alt2
- Refresh BuildRequires.

* Tue Feb 22 2011 Victor Forsiuk <force@altlinux.org> 1.3.5-alt1
- 1.3.5

* Mon Sep 22 2008 Yury Aliaev <mutabor@altlinux.org> 1.3.4-alt2
- buffer overflow fixed

* Fri Sep 19 2008 Yury Aliaev <mutabor@altlinux.org> 1.3.4-alt1
- Update for version 1.3.4
- Russian translation updated

* Thu Jun 19 2008 Yury Aliaev <mutabor@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus
- Russian translation added

* Sat Feb 16 2008 Mark Probst <schani@complang.tuwien.ac.at> 1.3.2
- Update for version 1.3.2

* Sun Jan 13 2008 Mark Probst <schani@complang.tuwien.ac.at> 1.3.1
- Update for version 1.3.1

* Tue Jan 01 2008 Mark Probst <schani@complang.tuwien.ac.at> 1.3.0
- Update for version 1.3.0

* Mon Dec 03 2007 Mark Probst <schani@complang.tuwien.ac.at> 1.2.4
- openSUSE Build Service

* Fri Nov 23 2007 Mark Probst <schani@complang.tuwien.ac.at> 1.2.4
- Update for version 1.2.4

* Fri Nov 09 2007 Mark Probst <schani@complang.tuwien.ac.at> 1.2.3
- Update for version 1.2.3

* Sun Nov 04 2007 Mark Probst <schani@complang.tuwien.ac.at> 1.2.2
- Update for version 1.2.2

* Thu May 04 2007 Mark Probst <schani@complang.tuwien.ac.at> 1.2.0
- Update for version 1.2.0

* Thu Apr 12 2007 Mark Probst <schani@complang.tuwien.ac.at> 1.1.3
- First creation of spec file
