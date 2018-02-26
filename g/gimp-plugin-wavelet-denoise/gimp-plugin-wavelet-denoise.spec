%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-wavelet-denoise
Version: 0.3.1
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: GIMP tool for reducing sensor noise in an image
# GPL v2 only - stated in source
License: GPLv2
Group: Graphics

Url: http://registry.gimp.org/node/4235/
Source: http://registry.gimp.org/files/wavelet-denoise-%version.tar.gz

Requires: gimp >= 2.2
# Automatically added by buildreq on Thu Aug 28 2008
BuildRequires: libgimp-devel

%description
The wavelet denoise plugin is a tool to selectively reduce noise in individual
channels of an image with optional RGB<->YCbCr conversion. It has a user
inteface to adjust the amount of denoising applied. The wavelet nature of the
algorithm makes the processing quite fast.

%prep
%setup -n wavelet-denoise-%version
%__subst 's/do install/do install -pD/' po/Makefile

%build
%make_build

%install
export DESTDIR=%buildroot
%make_install install LOCALEDIR=%buildroot%_datadir/locale

%find_lang gimp20-wavelet-denoise-plug-in

%files -f gimp20-wavelet-denoise-plug-in.lang
%gimpplugindir/plug-ins/*

%changelog
* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 0.3.1-alt1
- 0.3.1

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 0.3-alt1
- 0.3

* Thu Aug 28 2008 Victor Forsyuk <force@altlinux.org> 0.2-alt1
- Initial build.
