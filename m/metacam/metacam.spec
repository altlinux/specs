Name: metacam
Version: 1.2
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Command line tool to read the EXIF extensions in JPEG files
License: GPLv2+
Group: Graphics

URL: http://www.cheeseplant.org/~daniel/pages/metacam.html
Source: http://www.cheeseplant.org/metacam/downloads/metacam-%version.tar.gz
Patch0: metacam-1.2-gcc43.patch

# Automatically added by buildreq on Tue Oct 28 2008
BuildRequires: gcc-c++

%description
Most digital cameras produce EXIF files, which are JPEG files with extra tags
that contain information about the image.

In contrary to the tools "exif" and "gexif" (and all other libexif-based tools
as "gphoto2") this tool gives a much easier readable summary of camera settings.
But the speciality of this program is that it knows many manufacturer-specific
entries for Nikon, Canon, and Olympus cameras.

%prep
%setup
%patch0 -p0

subst 's/-O. /%optflags /' Makefile

%build
%make_build

%install
install -pD -m755 metacam %buildroot%_bindir/metacam

%files
%_bindir/*
%doc BUGS README* THANKS layout.txt

%changelog
* Tue Oct 28 2008 Victor Forsyuk <force@altlinux.org> 1.2-alt2
- Fix FTBFS with gcc4.3.

* Mon Apr 25 2005 Victor Forsyuk <force@altlinux.ru> 1.2-alt1
- Initial build.
