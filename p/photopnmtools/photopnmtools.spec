Name: photopnmtools
Version: 1.3
Release: alt1

Summary: Toolset for postprocessing photographic images, based on PPM
License: Artistic
Group: Graphics

Url: http://www.13thmonkey.org/~boris/photopnmtools
Source: %url/photopnmtools-%version.tar.gz
Patch0: photopnmtools-1.3-ppmhsy.patch
Patch1: photopnmtools-1.3-pnmdft.patch

# Automatically added by buildreq on Fri Jul 20 2007
BuildRequires: libnetpbm-devel

%description
PhotoPnMTools is a simple toolkit for processing photographic images using
improved algorithms. It is based on Poskanzer's PPM toolkit. It contains
resizing, sharpening, and contrast/saturation/color balance filters.

%prep
%setup
%patch0 -p1
%patch1 -p1

%__subst 's/-lpnm/-Wl,--no-as-needed -lnetpbm/; s/-O2/%optflags/' Makefile

%build
%make_build

%install
install -d %buildroot%_bindir
# avoid to install source files, their names ends in .c :
install -p -m755 {hsy,pnm,ppm}*[^c] %buildroot%_bindir/

%files
%doc README comparesharpness.pl getexifrotation.pl makephotoalbum.pl 
%_bindir/*

%changelog
* Fri Jul 20 2007 Victor Forsyuk <force@altlinux.org> 1.3-alt1
- Initial build.
