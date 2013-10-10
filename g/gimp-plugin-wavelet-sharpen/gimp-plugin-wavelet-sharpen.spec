%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-wavelet-sharpen
Version: 0.1.2
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: GIMP plugin for image sharpening using wavelets
License: GPLv2+
Group: Graphics

Url: http://registry.gimp.org/node/9836
Source: http://registry.gimp.org/files/wavelet-sharpen-%version.tar.gz

Requires: gimp
# Automatically added by buildreq on Wed Oct 15 2008
BuildRequires: libgimp-devel

%description
The wavelet sharpen plugin enhances apparent sharpness of an image by increasing
contrast in high frequency space. The amount of unsharpness of the original
image can be taken into account by adjusting the sharpening radius. As an option
you can choose to sharpen the luminance (YCbCr) channel of the image only.

%prep
%setup -n wavelet-sharpen-%version

%__subst 's/CFLAGS =/CFLAGS = %optflags/' src/Makefile

%build
%make_build

%install
%__subst 's/install /install -pD /' po/Makefile
make -C po install LOCALEDIR=%buildroot%_datadir/locale
install -pD -m755 src/wavelet-sharpen %buildroot%gimpplugindir/plug-ins/wavelet-sharpen

%find_lang gimp20-wavelet-sharpen-plug-in

%files -f gimp20-wavelet-sharpen-plug-in.lang
%gimpplugindir/plug-ins/*

%changelog
* Thu Oct 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- fixed build

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 0.1.2-alt1
- 0.1.2

* Wed Jan 14 2009 Victor Forsyuk <force@altlinux.org> 0.1.1-alt1
- 0.1.1

* Wed Oct 15 2008 Victor Forsyuk <force@altlinux.org> 0.1-alt1
- Initial build.
