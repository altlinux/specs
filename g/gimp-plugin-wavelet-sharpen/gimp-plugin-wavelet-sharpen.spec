%def_enable snapshot
%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

%define _name wavelet-sharpen

Name: gimp-plugin-%_name
Version: 0.1.2
Release: alt4

Summary: GIMP plugin for image sharpening using wavelets
License: GPLv2+
Group: Graphics
Url: http://registry.gimp.org/node/9836

Vcs: https://github.com/gimp-plugins-justice/wavelet-sharpen.git
%if_disabled snapshot
# The gimp registry id dead
Source: http://registry.gimp.org/files/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Patch: %_name-0.1.2-alt-link.patch

Requires: gimp
# Automatically added by buildreq on Wed Oct 15 2008
BuildRequires: libgimp-devel

%description
The wavelet sharpen plugin enhances apparent sharpness of an image by increasing
contrast in high frequency space. The amount of unsharpness of the original
image can be taken into account by adjusting the sharpening radius. As an option
you can choose to sharpen the luminance (YCbCr) channel of the image only.

%prep
%setup -n %_name-%version
%patch
sed -i 's/CFLAGS =/CFLAGS = %optflags -fcommon/' src/Makefile

%build
%make_build

%install
%__subst 's/install /install -pD /' po/Makefile
make -C po install LOCALEDIR=%buildroot%_datadir/locale
install -pD -m755 src/wavelet-sharpen %buildroot%gimpplugindir/plug-ins/%_name

%find_lang gimp20-%_name-plug-in

%files -f gimp20-%_name-plug-in.lang
%gimpplugindir/plug-ins/*

%changelog
* Sat Dec 05 2020 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt4
- rebuilt with -fcommon

* Tue Feb 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt3
- explicitly link against libm

* Thu Oct 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt2
- fixed build

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 0.1.2-alt1
- 0.1.2

* Wed Jan 14 2009 Victor Forsyuk <force@altlinux.org> 0.1.1-alt1
- 0.1.1

* Wed Oct 15 2008 Victor Forsyuk <force@altlinux.org> 0.1-alt1
- Initial build.
