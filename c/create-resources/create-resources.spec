Name: create-resources
Version: 0.1.3
Release: alt3

Summary: shared resources for use by creative applications
License: GPLv2
Group: Graphics
Packager: Valery Inozemtsev <shrek@altlinux.ru>

BuildArch: noarch
Conflicts: gimp < 2.6.11-alt4

Source: create-%version.tar.bz2
Patch1: sconstruct.patch

# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: ghostscript-classic python-base python-modules python-modules-compiler python-modules-email tetex-core tetex-dvips
#BuildRequires: cvs flex gcc-c++ ghostscript-utils rcs scons swig tetex-latex
BuildRequires: scons

%description
The Create Project provides shared resources for use by creative
applications such as Blender, CinePaint, the GIMP, Inkscape, Scribus,
Audacity and the Open Clip Art Library.

The package includes color swatches files

%prep
%setup -qn create-%version
%patch1 -p0

%build

%install
#mkdir -p %buildroot%_datadir/create
#cp -a swatches %buildroot%_datadir/create/
mkdir -p %buildroot/%_prefix
scons install PREFIX=%buildroot/%_prefix

%files
%doc docs/*.html docs/*.css
%dir %_datadir/create
%_datadir/create/*

%changelog
* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 0.1.3-alt3
- fix build requires

* Fri Feb 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt2
- color swatches files only

* Mon Jan 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt1
- initial release

