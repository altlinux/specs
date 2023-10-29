# Upstream joined two projects, fbi and ida (framebuffer and Motif-based image
# viewers) into united project named "fbida". But we really not interested in
# packaging ugly motif apps, so we will name our main package just "fbi".

%def_enable snapshot

Name: fbi
Version: 2.14
Release: alt2.1

Summary: Image viewer for Linux framebuffer console
License: GPL-2.0-or-later
Group: Graphics
Url: https://www.kraxel.org/cgit/fbida/
Vcs: https://github.com/kraxel/fbida

%if_disabled snapshot
Source: http://www.kraxel.org/releases/fbida/fbida-%version.tar.gz
%else
Source: fbida-%version.tar
%endif
# according to changes in libxkbcommon-1.6
Patch10: fbida-2.14-alt-libxkbcommon-1.6.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
# image format BR
BuildRequires: libjpeg-devel
BuildRequires: libpcd-devel
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(pixman-1)
# fbi & fbpdf BR
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(xkbcommon)
# fbcon BR
BuildRequires: pkgconfig(libtsm)
BuildRequires: pkgconfig(systemd)

%description
Image viewer for Linux framebuffer console.

%package -n fbpdf
Summary: Framebuffer PDF viewer
Group: Graphics

%description -n fbpdf
PDF viewer for Linux framebuffer console.

%package -n exiftran
Summary: Command line tool to do lossless transformations of JPEG images
Group: Graphics

%description -n exiftran
Command line tool to do lossless transformations of JPEG images, similar to
jpegtran but includes EXIF data.

%package -n fbcon
Summary: Framebuffer terminal console
Group: Graphics

%description -n fbcon
Framebuffer terminal console.

%prep
%setup -n fbida-%version
%patch10

echo %version > VERSION

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/fbi
%_man1dir/fbi.1*

%files -n fbpdf
%_bindir/fbpdf

%files -n exiftran
%_bindir/exiftran
%_man1dir/exiftran*

%files -n fbcon
%_bindir/fbcon
%_datadir/wayland-sessions/fbcon.desktop

%changelog
* Sun Oct 29 2023 Yuri N. Sedunov <aris@altlinux.org> 2.14-alt2.1
- fixed build with libxkbcommon-1.6

* Thu Dec 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.14-alt2
- updated to 2.14-1-120-ge1a7db6 (ported to Meson build system)
- new fbpdf and fbcon subpackages

* Wed Oct 11 2017 Yuri N. Sedunov <aris@altlinux.org> 2.14-alt1
- 2.14

* Wed Apr 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.13-alt1
- 2.13

* Mon Jun 06 2016 Yuri N. Sedunov <aris@altlinux.org> 2.12-alt1
- 2.12
- updated buildreqs

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.10-alt1
- 2.10

* Sat Jan 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.09-alt3
- rebuilt against libwebp.so.5

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 2.09-alt2
- rebuilt against libwebp.so.4

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.09-alt1.1
- Rebuilt with libpng15

* Sun Feb 26 2012 Victor Forsiuk <force@altlinux.org> 2.09-alt1
- 2.09

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 2.08-alt1
- 2.08

* Fri Nov 06 2009 Victor Forsyuk <force@altlinux.org> 2.07-alt1
- Initial build.
