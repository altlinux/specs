%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-wavelet-decompose
Version: 0.1.2
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: GIMP tool for decomposing image into layers of wavelet scales
License: GPLv2+
Group: Graphics

Url: http://registry.gimp.org/node/11742
Source: http://registry.gimp.org/files/wavelet-decompose-%version.tar.gz

Requires: gimp >= 2.2
# Automatically added by buildreq on Thu Nov 20 2008
BuildRequires: libgimp-devel

%description
This plugin losslessly decomposes a layer of an image into layers of wavelet
scales. This means that you can edit the image on different detail scales
(frequencies). The trivial recomposition of the image can be done by GIMP's
layer modes so you can see the results of your modifications instantly. Among
the applications are retouching, noise reduction, and enhancing global contrast.

%prep
%setup -n wavelet-decompose-%version

%build
%make_build

%install
%__subst 's/install /install -pD /' po/Makefile
export DESTDIR=%buildroot
%make_install install LOCALEDIR=%buildroot%_datadir/locale

%find_lang gimp20-wavelet-decompose-plug-in

%files -f gimp20-wavelet-decompose-plug-in.lang
%gimpplugindir/plug-ins/*

%changelog
* Wed Jan 14 2009 Victor Forsyuk <force@altlinux.org> 0.1.2-alt1
- 0.1.2

* Thu Nov 20 2008 Victor Forsyuk <force@altlinux.org> 0.1-alt1.beta2
- Initial build.
