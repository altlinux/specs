# Upstream joined two projects, fbi and ida (framebuffer and Motif-based image
# viewers) into united project named "fbida". But we really not interested in
# packaging ugly motif apps, so we will name our main package just "fbi".
Name: fbi
Version: 2.09
Release: alt1

Summary: Image viewer for Linux framebuffer console
License: GPLv2+
Group: Graphics

Url: http://www.kraxel.org/cgit/fbida/
Source: http://www.kraxel.org/releases/fbida/fbida-%version.tar.gz

# Automatically added by buildreq on Sun Feb 26 2012
BuildRequires: fontconfig-devel libImageMagick-devel libcurl-devel libexif-devel libgif-devel libjpeg-devel liblirc-devel libpng-devel libsane-devel libtiff-devel libwebp-devel

%description
Image viewer for Linux framebuffer console.

%package -n exiftran
Summary: Command line tool to do lossless transformations of JPEG images
Group: Graphics

%description -n exiftran
Command line tool to do lossless transformations of JPEG images, similar to
jpegtran but includes EXIF data.

%prep
%setup -n fbida-%version
# Get rid of build time checks that will bloat buildreq-generated deps.
subst 's/^HAVE_MOTIF.*$//' GNUmakefile

%build
# Must use CFLAGS as env variable, because makefile _adds_ flags to it.
export CFLAGS="%optflags"
%make_build HAVE_MOTIF=no verbose=yes exiftran fbi

%install
%makeinstall_std STRIP="" prefix=%_prefix

%files
%_bindir/fb*
%_man1dir/fb*

%files -n exiftran
%_bindir/exiftran
%_man1dir/exiftran*

%changelog
* Sun Feb 26 2012 Victor Forsiuk <force@altlinux.org> 2.09-alt1
- 2.09

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 2.08-alt1
- 2.08

* Fri Nov 06 2009 Victor Forsyuk <force@altlinux.org> 2.07-alt1
- Initial build.
