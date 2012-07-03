Name: meh
Version: 0.3
Release: alt1

Summary: meh is a small, simple, super fast image viewer using raw XLib

Group: Graphics
License: MIT
Url: http://www.johnhawthorn.com/meh/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://web.uvic.ca/~jhawthor/%name-%version.tar

# Automatically added by buildreq on Fri Apr 13 2012
# optimized out: libX11-devel xorg-xextproto-devel xorg-xproto-devel zlib-devel
BuildRequires: libXext-devel libgif-devel libjpeg-devel libpng-devel

%description
meh is a small, simple, super fast image viewer using raw XLib.
It is similar to feh, but faster and simpler.

meh can use ImageMagick's convert to view almost 200 file formats,
though it is slower for these formats. Built in formats are JPEG, PNG,
BMP, and netpbm.

Features
    Fast
    Tiny
    Fast JPEG, PNG, GIF and BMP support
    Fast netpbm support (.ppm, .pgm, .pbm, .pnm)
    ImageMagick support by calling convert
        All ImageMagick formats (almost 200)
        This allows limited support for PDF's and SVG's
    Scales images to window size
    Preserves aspect ratio (either via EWMH hints or by padding the window)
    XSHM Support
    Minimal dependencies (Xlib, libjpeg, libpng, giflib)


%prep
%setup

%build
%make_build

%install
#makeinstall_std
install %name -D %buildroot%_bindir/%name

%files
%doc AUTHORS BUGS NEWS README THANKS
%_bindir/%name

%changelog
* Fri Apr 13 2012 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
