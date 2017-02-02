%define prerel pre1
%def_disable netpbm

Name: cmyktool
Version: 0.1.6
Release: alt1.%prerel

Summary: CMYK separation utility
License: GPLv3+
Group: Graphics
Url: http://www.blackfiveimaging.co.uk/index.php?article=02Software/05CMYKTool

Source: http://www.blackfiveimaging.co.uk/%name/%name-%version-%prerel.tar.gz
# fc
Patch10: cmyktool-1.16-fc-cxx11.patch
# mga
Patch21: cmyktool-0.1.6-pre1-fix-segfault.patch
# suse
Patch22: cmyktool-0.1.6-pre1-nonvoid-return-hackstream-h.patch
Patch23: cmyktool-0.1.6-pre1-fix_wrong_printf_format_for_size_t.patch

# Automatically added by buildreq on Wed Mar 03 2010
BuildRequires: gcc-c++ libgtk+2-devel libjpeg-devel liblcms-devel libtiff-devel
%{?_enable_netpbm:BuildRequires: libnetpbm-devel}

# External program for devicelink: collink from argyllcms package
Requires: argyllcms
# Make use of gs utility (now in ghostscript-classic subpackage but is is safer
# not to rely on current ghostscript package splittiing, hence path requirement)
Requires: /usr/bin/gs

%description
CMYKTool is a graphical utility that converts images from ICC profile to
another, converts images from RGB to CMYK with a number of configuration options
for the conversion, provides an interface for inspecting image channels,
provides a 'soft proof' mode to preview how an image would look if it was
printed, saves images to JPEG or TIFF (8- or 16-bit) with embedded profiles if
desired. This tool is extremely useful for designers who prepare artwork for
professional printing.

%prep
%setup -n %name-%version-%prerel
%patch10 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_liconsdir/*
%_desktopdir/*

%changelog
* Thu Feb 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1.pre1
- 0.1.6-pre1
- disabled netpbm support

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.1
- Rebuilt with libtiff5

* Tue Jan 04 2011 Victor Forsiuk <force@altlinux.org> 0.1.5-alt1
- 0.1.5

* Tue Aug 17 2010 Victor Forsiuk <force@altlinux.org> 0.1.4a-alt1
- 0.1.4a

* Fri Jun 11 2010 Victor Forsiuk <force@altlinux.org> 0.1.3-alt1
- 0.1.3

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 0.1.2-alt1
- 0.1.2

* Wed Mar 03 2010 Victor Forsiuk <force@altlinux.org> 0.1.1-alt1
- Initial build.
